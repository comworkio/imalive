from flask_restful import Resource

from metrics_utils import disk_usage

class DiskEndPoint(Resource):
    def get(self):
        return disk_usage()
