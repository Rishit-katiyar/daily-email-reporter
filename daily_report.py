import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time
import os

# Email configuration
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
SMTP_SERVER = 'smtp.example.com'  # e.g., 'smtp.gmail.com' for Gmail
SMTP_PORT = 587

# Recipient configuration
RECIPIENT_EMAIL = 'recipient@example.com'

# Function to send email
def send_email():
    try:
        # Set up the server
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = RECIPIENT_EMAIL
        msg['Subject'] = 'Daily Report'
        
        # Email body
        body = 'This is your daily report.'
        msg.attach(MIMEText(body, 'plain'))
        
        # Send the email
        server.send_message(msg)
        print('Email sent successfully')
        
        # Quit the server
        server.quit()
    except Exception as e:
        print(f'Failed to send email: {e}')

# Schedule the email to be sent every day at 8 AM
schedule.every().day.at("08:00").do(send_email)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(60)
