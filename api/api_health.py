import os

from datetime import datetime
from flask_restful import Resource

class HealthEndPoint(Resource):
    def get(self):
        vdate = datetime.now()
        return {
            'status': 'ok',
            'time': vdate.isoformat(),
            'alive': True,
            'name': os.environ['IMALIVE_NODE_NAME']
        }
