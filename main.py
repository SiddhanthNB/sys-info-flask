import platform,socket,re,uuid,psutil
from flask import request, Flask, jsonify

app = Flask(__name__)

@app.route("/get_my_info", methods=["GET"])
def get_my_info():
    try:
        info={}
        info['platform']=platform.system()
        info['platform-release']=platform.release()
        info['platform-version']=platform.version()
        info['architecture']=platform.machine()
        info['hostname']=socket.gethostname()
        info['ip-address']=request.remote_addr
        info['mac-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
        info['processor']=platform.processor()
        info['ram']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
        # return json.dumps(info)
        return jsonify(info), 200
    except Exception as e:
        return jsonify({'ERROR': "Couldn't process request."})

# @app.route("/get_my_ip", methods=["GET"])
# def get_my_ip():
#     return jsonify({'ip': request.remote_addr}), 200

# json.loads(getSystemInfo())

if __name__ == "__main__":
    app.run(debug=True)