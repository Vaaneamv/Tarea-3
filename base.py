from flask import Flask
from flask_restful import Resource, Api, reqparse
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import json

# Inicializaciones de Flask
app = Flask(__name__)
api = Api(app)

# Parsers para el Endpoint
parser = reqparse.RequestParser()
parser.add_argument('paciente')

# Cassandra
auth_provider = PlainTextAuthProvider(username='cassandra', password='cassandra')
cluster = Cluster(['172.22.0.4'],port=9042, auth_provider=auth_provider)

# Endpoint /paciente [POST]
class Paciente(Resource):
    def post(self):
        args = parser.parse_args()
        if (args['paciente'] != None):
            session = cluster.connect('pacientes',wait_for_all_pools=True)
            rows = session.execute('SELECT * FROM paciente')
            for row in rows:
                print(row)
            return {'rows': 'allok'}, 201
        else:
            return {'status': 'error'}, 500
api.add_resource(Paciente, '/paciente')

if __name__ == "__main__":
    app.run(debug=True)

