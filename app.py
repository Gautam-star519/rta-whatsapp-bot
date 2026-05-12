from flask import Flask, request
from database import init_db, lookup
app = Flask(__name__)
init_db()

def process_message(text):
    lower = text.strip().lower()
    if lower == 'help':
        return "Commands: dividend <company>, mgt7 <company>, drn <code>, help"
    if lower.startswith('dividend '):
        company = text[9:].strip()
        return lookup('dividend_status','company','status',company) or f"No dividend status found for {company}."
    if lower.startswith('mgt7 '):
        company = text[5:].strip()
        return lookup('mgt7_status','company','status',company) or f"No MGT-7 status found for {company}."
    if lower.startswith('drn '):
        code = text[4:].strip()
        return lookup('drn_codes','code','meaning',code) or f"No DRN meaning found for code {code}."
    return "Unknown command. Type help."

@app.route('/')
def home():
    return 'RTA WhatsApp Bot is running.'

@app.route('/test')
def test():
    return process_message(request.args.get('msg', 'help'))

@app.route('/webhook', methods=['GET'])
def verify():
    return request.args.get('hub.challenge', '')

@app.route('/webhook', methods=['POST'])
def webhook():
    return 'EVENT_RECEIVED', 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)