import platform,socket,re,uuid,psutil
from flask import request, Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
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

if __name__ == "__main__":
    app.run(debug=True)
