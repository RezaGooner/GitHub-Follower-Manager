import requests
import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser

# Function to display token help instructions
def show_token_help():
    help_text = """
To create a GitHub Personal Access Token:
1. Go to GitHub and log in to your account.
2. Click on your profile picture in the top-right corner and select 'Settings'.
3. In the left sidebar, click on 'Developer settings'.
4. Click on 'Personal access tokens' and then 'Generate new token'.
5. Select the following scopes:
   - `repo`: Access to repositories.
   - `user`: Access to user information.
   - `read:user`: Read user profile data.
   - `follow`: Access to follow/unfollow users.
6. Click 'Generate token' and copy the token. Keep it safe, as it will only be shown once.
"""
    messagebox.showinfo("How to Get a GitHub Token", help_text)

# Function to fetch the list of followers
def get_github_followers(username, token):
    followers_url = f"https://api.github.com/users/{username}/followers"
    headers = {"Authorization": f"token {token}"}
    response = requests.get(followers_url, headers=headers)
    if response.status_code == 200:
        return [user['login'] for user in response.json()]
    else:
        messagebox.showerror("Error", f"Error fetching followers: {response.status_code}")
        return []

# Function to fetch the list of users being followed
def get_github_following(username, token):
    following_url = f"https://api.github.com/users/{username}/following"
    headers = {"Authorization": f"token {token}"}
    response = requests.get(following_url, headers=headers)
    if response.status_code == 200:
        return [user['login'] for user in response.json()]
    else:
        messagebox.showerror("Error", f"Error fetching following: {response.status_code}")
        return []

# Function to unfollow a user
def unfollow_user():
    target_user = entry_selected_user.get()
    if not target_user:
        messagebox.showwarning("Input Error", "Please select a user to unfollow.")
        return

    username = entry_username.get()
    token = entry_token.get()

    if not username or not token:
        messagebox.showwarning("Input Error", "Please enter both GitHub username and token.")
        return

    unfollow_url = f"https://api.github.com/user/following/{target_user}"
    headers = {"Authorization": f"token {token}"}
    response = requests.delete(unfollow_url, headers=headers)
    if response.status_code == 204:
        messagebox.showinfo("Success", f"Unfollowed {target_user} successfully!")
        find_non_followers()  # Refresh the list after unfollowing
    else:
        messagebox.showerror("Error", f"Failed to unfollow {target_user}: {response.status_code}")

# Function to open a user's profile in the browser
def open_user_profile(username):
    webbrowser.open(f"https://github.com/{username}")

# Main function to find users you follow but who don't follow you back
def find_non_followers():
    username = entry_username.get()
    token = entry_token.get()

    if not username or not token:
        messagebox.showwarning("Input Error", "Please enter both GitHub username and token.")
        return

    global followers, following
    followers = set(get_github_followers(username, token))
    following = set(get_github_following(username, token))

    non_followers = following - followers

    # Clear the table before adding new data
    for row in tree.get_children():
        tree.delete(row)

    if non_followers:
        for user in non_followers:
            # Add each user to the table
            tree.insert("", "end", values=(user,))
    else:
        tree.insert("", "end", values=("All users you follow also follow you back.",))

# Function to display the list of followers
def show_followers():
    username = entry_username.get()
    token = entry_token.get()

    if not username or not token:
        messagebox.showwarning("Input Error", "Please enter both GitHub username and token.")
        return

    followers_list = get_github_followers(username, token)
    # Clear the table before adding new data
    for row in tree.get_children():
        tree.delete(row)

    if followers_list:
        for user in followers_list:
            tree.insert("", "end", values=(user,))
    else:
        tree.insert("", "end", values=("No followers found.",))

# Function to display the list of users being followed
def show_following():
    username = entry_username.get()
    token = entry_token.get()

    if not username or not token:
        messagebox.showwarning("Input Error", "Please enter both GitHub username and token.")
        return

    following_list = get_github_following(username, token)
    # Clear the table before adding new data
    for row in tree.get_children():
        tree.delete(row)

    if following_list:
        for user in following_list:
            tree.insert("", "end", values=(user,))
    else:
        tree.insert("", "end", values=("You are not following anyone.",))

# Function to populate the selected user field when a user is selected
def on_user_select(event):
    selected_item = tree.selection()
    if selected_item:
        user = tree.item(selected_item)["values"][0]
        entry_selected_user.delete(0, tk.END)
        entry_selected_user.insert(0, user)

# Create the main window
root = tk.Tk()
root.title("GitHub Non-Followers Finder")

# Set dark theme
root.tk_setPalette(background='#2d2d2d', foreground='#ffffff', activeBackground='#3e3e3e', activeForeground='#ffffff')

# Label and entry for GitHub username
label_username = tk.Label(root, text="GitHub Username:")
label_username.grid(row=0, column=0, padx=10, pady=10)
entry_username = tk.Entry(root, width=30, bg='#3e3e3e', fg='#ffffff', insertbackground='white')
entry_username.grid(row=0, column=1, padx=10, pady=10)

# Label and entry for GitHub token
label_token = tk.Label(root, text="GitHub Token:")
label_token.grid(row=1, column=0, padx=10, pady=10)
entry_token = tk.Entry(root, width=30, show="*", bg='#3e3e3e', fg='#ffffff', insertbackground='white')
entry_token.grid(row=1, column=1, padx=10, pady=10)

# Help button for token instructions
help_button = tk.Button(root, text="?", command=show_token_help, bg='#3e3e3e', fg='#ffffff', width=2)
help_button.grid(row=1, column=2, padx=5, pady=10)

# Buttons
button_find = tk.Button(root, text="Find Non-Followers", command=find_non_followers, bg='#3e3e3e', fg='#ffffff')
button_find.grid(row=2, column=0, pady=10)

button_show_followers = tk.Button(root, text="Show Followers", command=show_followers, bg='#3e3e3e', fg='#ffffff')
button_show_followers.grid(row=2, column=1, pady=10)

button_show_following = tk.Button(root, text="Show Following", command=show_following, bg='#3e3e3e', fg='#ffffff')
button_show_following.grid(row=2, column=2, pady=10)

# Create a table using Treeview
columns = ("Username",)
tree = ttk.Treeview(root, columns=columns, show="headings", selectmode="browse")
tree.heading("Username", text="Username")
tree.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

# Add a scrollbar
scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.grid(row=3, column=3, sticky="ns")

# Configure table colors
style = ttk.Style()
style.theme_use("default")
style.configure("Treeview", background="#2d2d2d", foreground="#ffffff", fieldbackground="#2d2d2d")
style.map("Treeview", background=[("selected", "#3e3e3e")])

# Selected user field and unfollow button
label_selected_user = tk.Label(root, text="Selected User:")
label_selected_user.grid(row=4, column=0, padx=10, pady=10)
entry_selected_user = tk.Entry(root, width=30, bg='#3e3e3e', fg='#ffffff', insertbackground='white')
entry_selected_user.grid(row=4, column=1, padx=10, pady=10)

button_unfollow = tk.Button(root, text="Unfollow", command=unfollow_user, bg='#3e3e3e', fg='#ffffff')
button_unfollow.grid(row=4, column=2, padx=10, pady=10)

# Bind the user selection event to the on_user_select function
tree.bind("<<TreeviewSelect>>", on_user_select)

# Run the main window
root.mainloop()

#Github.com/RezaGooner
