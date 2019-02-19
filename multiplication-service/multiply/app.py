from flask import Flask
from flask import request, jsonify, abort
from elasticapm.contrib.flask import ElasticAPM
import requests


with open('/run/secrets/apm-secret-token', 'r') as f:
    APM_SECRET_TOKEN = f.read()
with open('/run/secrets/apm-server-url', 'r') as f:
    APM_SERVER_URL = f.read()

app = Flask(__name__)

app.config['ELASTIC_APM'] = {
  'SERVICE_NAME': 'multiplication-service',
  'SECRET_TOKEN': APM_SECRET_TOKEN,
  'SERVER_URL': APM_SERVER_URL
}

apm = ElasticAPM(app)


@app.route("/multiply")
def multiply():
    try:
        n1 = float(request.args.get('n1'))
        n2 = float(request.args.get('n2'))
    except ValueError:
        msg = 'Math needs numbers.'
        apm.capture_exception()
        app.logger.error(msg, exc_info=True)
        abort(500)

    if n2 == int(n2):
        result = n1
        for i in range(int(n2)-1):
            result = requests.get('http://addition-service:5001/add?n1={}&n2={}'.format(result, n1)).json()['result']
    else:
        result = n1*n2
    return jsonify(dict(result=result))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
