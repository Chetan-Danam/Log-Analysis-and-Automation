# Log Analyzer and Automated Alerts

This Python-based log analysis tool helps you automatically parse log files, detect suspicious activity (errors, warnings, exceptions), and send email alerts when anomalies are found.

## Features:
- **Log Parsing**: Reads log files line by line.
- **Keyword Detection**: Searches for predefined keywords (e.g., "error", "warning", "critical").
- **Alerting**: Sends an email alert when suspicious activity is detected.
- **Customizable**: Easily modify the list of keywords and log file path.

## Requirements:
- Python 3.x
- `smtplib` (for email alerts)
- Basic knowledge of email settings (SMTP credentials)
  
## Installation:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/log-analyzer.git
    ```

2. **Navigate to the project directory:**
    ```bash
    cd log-analyzer
    ```

3. **Install any dependencies (if needed):**
    ```bash
    pip install -r requirements.txt
    ```

    > **Note**: `smtplib` is part of the standard Python library, so no additional installation is required for this.

## Configuration:

1. **Email Configuration:**
   - In the `log_analyzer.py` file, update the following email configuration with your Gmail account details:
     ```python
     SMTP_SERVER = "smtp.gmail.com"
     SMTP_PORT = 587
     SENDER_EMAIL = "youremail@gmail.com"
     SENDER_PASSWORD = "yourpassword"
     ALERT_RECIPIENT = "recipientemail@example.com"
     ```

2. **Log File Path:**
   - Update the `LOG_FILE_PATH` variable in the script with the full path to the log file you want to analyze:
     ```python
     LOG_FILE_PATH = "/path/to/your/logfile.log"
     ```

3. **Keyword List:**
   - Modify the `ERROR_KEYWORDS` list if you want to track different error types:
     ```python
     ERROR_KEYWORDS = ["error", "failed", "critical", "exception", "warning"]
     ```

## Usage:

1. **Run the script:**
   - After configuring the script with your email and log file path, run the following command:
     ```bash
     python log_analyzer.py
     ```

2. **Output:**
   - If suspicious activity is found in the logs, the script will:
     - Print a summary of the detected errors.
     - Send an email alert to the configured recipient.

### Example Output:

