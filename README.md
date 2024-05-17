# 📧 Daily Email Reporter

Welcome to the **Daily Email Reporter** repository! This project contains a Python script to automate sending daily email reports. 📅

## 📖 Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## 📝 Introduction

This script allows you to send automated daily email reports. It uses Python's `smtplib` for email sending, `email` for managing email components, and `schedule` for scheduling the email to be sent at a specific time every day.

## ✨ Features

- Automated daily email sending 📅
- Configurable email body and recipient 📧
- Easy to set up and use 🛠️
- Supports environment variables for secure credential management 🔒

## 🛠️ Requirements

- Python 3.6+
- An email account (Gmail, Yahoo, etc.)
- Internet connection

## 📦 Installation

1. **Clone the Repository**

    ```sh
    git clone https://github.com/Rishit-katiyar/daily-email-reporter.git
    cd daily-email-reporter
    ```

2. **Create a Virtual Environment (Optional but Recommended)**

    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**

    ```sh
    pip install schedule
    ```

## ⚙️ Configuration

1. **Set Up Environment Variables**

    It's recommended to use environment variables to store your email credentials securely.

    - On Linux/macOS:

        ```sh
        export EMAIL_ADDRESS='your_email@example.com'
        export EMAIL_PASSWORD='your_password'
        ```

    - On Windows:

        ```sh
        set EMAIL_ADDRESS=your_email@example.com
        set EMAIL_PASSWORD=your_password
        ```

2. **Update SMTP Configuration**

    Edit the `daily_report.py` script to configure the SMTP server settings and recipient email:

    ```python
    SMTP_SERVER = 'smtp.example.com'  # e.g., 'smtp.gmail.com' for Gmail
    SMTP_PORT = 587  # For TLS/STARTTLS, use 465 for SSL
    RECIPIENT_EMAIL = 'recipient@example.com'
    ```

## 🚀 Usage

1. **Run the Script**

    ```sh
    python daily_report.py
    ```

    The script will start running and will send an email daily at 8 AM. Make sure to keep the script running for it to send the email at the scheduled time.

2. **Automate Script Execution**

    - **Linux/macOS**: Use `cron` to run the script at startup.

        ```sh
        crontab -e
        ```

        Add the following line to the crontab file:

        ```sh
        @reboot /usr/bin/python3 /path/to/your/daily_report.py
        ```

    - **Windows**: Use Task Scheduler to create a new task that runs the script at startup.

        1. Open Task Scheduler.
        2. Create a new task.
        3. Set the trigger to "At startup".
        4. Set the action to "Start a program" and select the Python interpreter and script path.

## 📜 License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.
