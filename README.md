## Getting Started
1. You'll need a recent version of docker engine and compose. Mine are installed as
part of the Docker Desktop for Mac bundle (v2.0.0.3, includes engine=18.09.2, compose=1.23.2). 

1. If swarm isn't running, `docker swarm init`

1. Add your secrets. If you don't have APM credentials, head over to cloud.elastic.co and spin
up a cluster.  
`printf "<your apm secret token>" | docker secret create apm-secret-token -`  
`printf "<your apm server url>" | docker secret create apm-server-url -`

1. Get the code: `git clone <this repo>`

1. Build and deploy the stack: `sh deploy.sh`

1. You'll now have four math services running, and a math UI. Each service accepts two URL
parameters, `n1` and `n2`, and the response will contain the sum, difference, product, or quotient.
  - http://localhost:5000
  - http://localhost:5001/add?n1=`number`&n2=`number`
  - http://localhost:5002/subtract?n1=`number`&n2=`number`
  - http://localhost:5003/multiply?n1=`number`&n2=`number`
  - http://localhost:5004/divide?n1=`number`&n2=`number`
