from flask import Flask, render_template,redirect,url_for
import shutil
import psutil
import requests
import socket
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def main():
    return render_template("main_page.html")


    
@app.route('/check',methods=['GET','POST'])
def check():
    def disk_usage(disk):
        du = shutil.disk_usage(disk)
        free = du.free
        total = du.total
        check = free/total*100
        return check > 10

    def cpu_percent():

        usage = psutil.cpu_percent(1)
        return usage < 50

    if not disk_usage("/") or not cpu_percent():
        message = "Error cool down or remove some space"

        return render_template("main_page.html", message=message)
    else:
        message = "DISK IS FREE AND CPU USAGE IS BELOW 60%"
        return render_template("main_page.html", message=message)
    

    


@app.route('/check_network', methods=['GET','POST'])
def check_network():
    localhost = socket.gethostbyname('localhost')
    
    request = requests.get("http://www.google.com")

    response = request.status_code

    if(str(localhost)=="127.0.0.1" and response ==200):

        message = "NETWROK IS RESPONDING AND LOCAL HOST IS CONFIGURED"
        return render_template("main_page.html",message = message)

    else:
        message="CHECK CONNECTION OR INSTALL A LOCAL HOST"
        return render_template("main_page.html",message = message)


    

app.run(port=5000,debug =True)



