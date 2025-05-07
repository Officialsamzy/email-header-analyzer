from flask import Flask, render_template, request
import email
from email import policy
from email.parser import BytesParser

app = Flask(__name__)

def analyze_headers(raw_headers):
    findings = []
    if "spf=fail" in raw_headers.lower():
        findings.append("SPF failed")
    if "dkim=fail" in raw_headers.lower():
        findings.append("DKIM failed")
    if "dmarc=fail" in raw_headers.lower():
        findings.append("DMARC failed")
    if "reply-to" in raw_headers.lower() and "from" in raw_headers.lower():
        findings.append("Check if 'Reply-To' is different from 'From'")
    return findings if findings else ["No obvious issues found."]

@app.route("/", methods=["GET", "POST"])
def index():
    result = []
    if request.method == "POST":
        headers = request.form["headers"]
        result = analyze_headers(headers)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
