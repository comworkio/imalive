import os

from flask_restful import Resource

class HealthEndPoint(Resource):
    def get(self):
        return {
            'status': 'ok',
            'alive': True,
            'name': os.environ['IMALIVE_NODE_NAME']
        }
