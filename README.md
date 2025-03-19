# GitHub Non-Followers Finder

A Python-based desktop application that helps you find and manage users you follow on GitHub who do not follow you back. This application is built using **Tkinter** for the GUI and integrates with the GitHub API to fetch and display the required information.

---

## Features
- **Non-Followers Finder**: Find users you follow on GitHub who do not follow you back.
- **Manage Followers**: View your followers and the users you are following.
- **Unfollow Users**: Directly unfollow users who do not follow you back.
- **GitHub Integration**: Uses GitHub Personal Access Tokens (PAT) for secure access to the GitHub API.
- **Dark Theme**: A modern dark-themed interface for better usability.
- **Interactive Table**: Displays user lists with the ability to open GitHub profiles directly in your browser.

---

## Prerequisites
1. **GitHub Personal Access Token (PAT)**:
   You need a GitHub PAT to use this application. To generate one:
   - Go to GitHub and log in to your account.
   - Click on your profile picture -> `Settings` -> `Developer settings` -> `Personal access tokens`.
   - Click "Generate new token" and select the following scopes:
     - `repo`
     - `user`
     - `read:user`
     - `follow`
   - Generate the token and copy it. _Save the token securely as it will only be shown once._

2. **Python Installation**:
   Make sure Python 3.x is installed on your system. You can download it from [python.org](https://www.python.org/).

---

## How to Use
1. **Clone or Download the Repository**:
   - Clone the repository or download it as a ZIP and extract it.

2. **Run the Program**:
   - If you're using the Python script (`.py`):
     - Install the required dependencies:
       ```bash
       pip install requests
       ```
       ```bash
       pip install tkinter
       ```
     - Run the script:
       ```bash
       python gitfol.py
       ```
   - If you're using the executable (`.exe`):
     - Double-click the `.exe` file to launch the program. No Python installation is required.

3. **Using the Application**:
   - Enter your GitHub **username** and **Personal Access Token** in the respective fields.
   - Click:
     - **Find Non-Followers**: To view users you follow but who don't follow you back.
     - **Show Followers**: To display a list of your GitHub followers.
     - **Show Following**: To display users you are following.
   - Select a user from the list to unfollow or click their username to open their profile in a web browser.

---

## Screenshots
![image](https://github.com/user-attachments/assets/d25c6e34-14e6-4c7b-a1b0-cd0e68fd372b)


---

## Reporting Issues and Collaborating
### **Report a Bug**
If you encounter any issues or bugs while using the application:
1. Navigate to the "Issues" section of this repository.
2. Click **New Issue** and provide details such as:
   - Steps to reproduce the issue.
   - Screenshots or error messages.
   - Environment details (OS, Python version, etc.).

### **Suggest a Feature**
Have an idea to improve the application? Share your suggestions by creating a **New Issue** in the "Issues" section with a clear description of your feature request.

### **Contribute**
We welcome contributions! If you'd like to collaborate, follow these steps:
1. Fork the repository.
2. Make your changes on a new branch.
3. Ensure your code is clean and follows best practices.
4. Submit a pull request with a detailed description of the changes.

---

## How to Convert Python Script to Executable (.exe)
If you'd like to distribute the application as an executable, follow these steps:
1. Install **PyInstaller**:
   ```bash
   pip install pyinstaller
   ```
2. Create the `.exe` file:
   ```bash
   pyinstaller --onefile gitfol.py
   ```
3. The generated executable will be available in the `dist` directory.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

### Github.com/RezaGooner
