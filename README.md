# Email Header Analyzer

A simple Flask web app to analyze raw email headers for signs of phishing or spoofing.

## Features
- Detect SPF, DKIM, and DMARC failures
- Check for suspicious 'Reply-To' vs 'From'
- Web-based form input

## Tech Stack
- Python
- Flask
- HTML

## How to Run
```bash
git clone https://github.com/yourusername/email-header-analyzer.git
cd email-header-analyzer
python -m venv venv
source venv/bin/activate  # Or venv\Scripts\activate on Windows
pip install -r requirements.txt
python app.py
