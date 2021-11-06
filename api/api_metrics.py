from flask_restful import Resource

from metrics_utils import all_metrics

class MetricsEndPoint(Resource):
    def get(self):
        return all_metrics()
