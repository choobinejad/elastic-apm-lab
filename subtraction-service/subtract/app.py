from flask import Flask
from flask import request, jsonify, abort
from elasticapm.contrib.flask import ElasticAPM


with open('/run/secrets/apm-secret-token', 'r') as f:
    APM_SECRET_TOKEN = f.read()
with open('/run/secrets/apm-server-url', 'r') as f:
    APM_SERVER_URL = f.read()

app = Flask(__name__)

app.config['ELASTIC_APM'] = {
  'SERVICE_NAME': 'subtraction-service',
  'SECRET_TOKEN': APM_SECRET_TOKEN,
  'SERVER_URL': APM_SERVER_URL
}

apm = ElasticAPM(app)


@app.route("/subtract")
def subtract():
    try:
        n1 = float(request.args.get('n1'))
        n2 = float(request.args.get('n2'))
    except ValueError:
        msg = 'Math needs numbers.'
        apm.capture_exception()
        app.logger.error(msg, exc_info=True)
        abort(500)

    result = dict(result=n1-n2)
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
