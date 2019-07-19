import json
from http.server import HTTPServer, BaseHTTPRequestHandler
import requests

#url = 'https://api.myjson.com/bins/8cvw5' #Greennn
url = 'https://api.myjson.com/bins/10pz5h' #yellow
#url = 'https://api.myjson.com/bins/1ey8id' #green

#slack settings
webhook_url = 'https://hooks.slack.com/services/xhxhx/xhxhxhx/ksshskhksksk'
slack_data = {'text': "*Warning:* Kibana service has crashed and container terminate is in progress"}

port = 8000

def check_further(data):
        status_lst = []
        for i in data["status"]["statuses"]:
                if i["state"] != "green":
                        return False
                        print('i["id"] has critical service with following')

def check_service():
	resp = requests.get(url=url)
	try:
		resp.raise_for_status()
	except requests.exceptions.RequestException as exp: 
		print (exp)
		return False
	data = resp.json()
	if data["status"]["overall"]["state"] == "green":
		return True
		print("Yay! Healthy cluster")
	else:
		check_further(data)


def slack_msg():

	response = requests.post(
    	webhook_url, data=json.dumps(slack_data),
    	headers={'Content-Type': 'application/json'}
	)
	if response.status_code != 200:
    		raise ValueError(
        		'Request to slack returned an error %s, the response is:\n%s'
        		% (response.status_code, response.text)
    		)	

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

	def do_GET(self):
		if check_service():
			self.send_response(200)
			self.end_headers()
			self.wfile.write(b'Yay! Healthy cluster.')
		else:
			self.send_response(500)
			self.end_headers()
			self.wfile.write(b'Damn! Unhealthy cluster.')
			slack_msg()


httpd = HTTPServer(('localhost', port), SimpleHTTPRequestHandler)
httpd.serve_forever()
