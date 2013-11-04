from flask import *
from twilio.rest import TwilioRestClient
import os 

debug = False

app = Flask(__name__)

account_sid = os.environ['ACCOUNT_SID'] 
# will get these numbers from Heroku, already config'd
auth_token = os.environ['AUTH_TOKEN']
twilionumber = os.environ['TWILIO']
mynumber = os.environ['ME']

@app.route('/', methods=['GET'])
def index():
	return account_sid+", "+auth_token
	# render_template("template.html")

@app.route('/', methods=['POST'])
def handle_form():
	sendtonumber = request.forms.get('From')
	client = TwilioRestClient(account_sid, auth_token)
 
	message = client.sms.messages.create(body="sent from python!", to=sendtonumber, from_=twilionumber)
	return render_template("template.html", message=message.sid)

if __name__ == "__main__":
	app.run(debug=debug)



	# base_url = url_for("index", _external=True)
	# if request.form.get('content', None):