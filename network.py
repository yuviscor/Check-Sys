import socket
import requests

def check_localhost():

    localhost = socket.gethostbyname('localhost')
    request = requests.get("http://www.google.com")

    response = request.status_code

    if(str(localhost)=="127.0.0.1" and response ==200):

        print("NETWROK IS RESPONDING AND LOCAL HOST IS CONFIGURED")
    else:
        print("CHECK CONNECTION OR INSTALL A LOCAL HOST")

check_localhost()