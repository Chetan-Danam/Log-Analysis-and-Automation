import os
import re
import smtplib
from email.mime.text import MIMEText
from collections import Counter

# Define email configuration (for alerts)
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "youremail@gmail.com"
SENDER_PASSWORD = "yourpassword"
ALERT_RECIPIENT = "recipientemail@example.com"

# Define log file path (can be customized)
LOG_FILE_PATH = "/path/to/your/logfile.log"

# Keywords to detect (customizable)
ERROR_KEYWORDS = ["error", "failed", "critical", "exception", "warning"]

# Function to analyze logs for the defined error keywords
def analyze_logs(file_path):
    if not os.path.exists(file_path):
        print(f"Log file {file_path} not found.")
        return

    with open(file_path, "r") as log_file:
        logs = log_file.readlines()

    # List to store found suspicious lines
    suspicious_lines = []
    keyword_count = Counter()

    for line in logs:
        for keyword in ERROR_KEYWORDS:
            if re.search(rf"\b{keyword}\b", line, re.IGNORECASE):
                suspicious_lines.append(line.strip())
                keyword_count[keyword] += 1

    return suspicious_lines, keyword_count

# Function to send an alert email if suspicious activity is detected
def send_alert_email(suspicious_lines, keyword_count):
    subject = "Log Analysis Alert: Suspicious Activity Detected"
    body = f"The following suspicious activity was detected in the logs:\n\n"
    body += "Detected Keywords:\n"
    for keyword, count in keyword_count.items():
        body += f"{keyword}: {count}\n"
    
    body += "\nSuspicious log entries:\n"
    for line in suspicious_lines:
        body += f"{line}\n"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = ALERT_RECIPIENT

    # Send the email
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, ALERT_RECIPIENT, msg.as_string())
        server.quit()
        print(f"Alert email sent to {ALERT_RECIPIENT}")
    except Exception as e:
        print(f"Failed to send email alert: {e}")

# Function to generate the analysis report
def generate_report(suspicious_lines, keyword_count):
    if suspicious_lines:
        print("\nSuspicious Activity Detected:")
        for line in suspicious_lines:
            print(f"- {line}")
        print("\nKeyword Frequency Analysis:")
        for keyword, count in keyword_count.items():
            print(f"{keyword}: {count}")
    else:
        print("No suspicious activity detected.")

# Main function to automate log analysis
def main():
    suspicious_lines, keyword_count = analyze_logs(LOG_FILE_PATH)
    
    if suspicious_lines:
        # Print and send email alert
        generate_report(suspicious_lines, keyword_count)
        send_alert_email(suspicious_lines, keyword_count)
    else:
        print("No suspicious activity found in the logs.")

if __name__ == "__main__":
    main()
