from health_utils import health
from flask_restful import Resource

class HealthEndPoint(Resource):
    def post(self):
        return health();

    def get(self):
        return health();
