from uuid import uuid4
from flask import Flask
from flask import request, render_template
from elasticapm.contrib.flask import ElasticAPM


with open('/run/secrets/apm-secret-token', 'r') as f:
    APM_SECRET_TOKEN = f.read()
with open('/run/secrets/apm-server-url', 'r') as f:
    APM_SERVER_URL = f.read()


app = Flask(__name__)
app.config['ELASTIC_APM'] = {
    'SERVICE_NAME': 'math-service',
    'SECRET_TOKEN': APM_SECRET_TOKEN,
    'SERVER_URL': APM_SERVER_URL
}
app.config['SECRET_KEY'] = str(uuid4())
apm = ElasticAPM(app)


@app.route('/', methods=['GET', 'POST'])
def login():
    error = 100
    problem = request.form['problem']
    return render_template('index.html', error=error)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
