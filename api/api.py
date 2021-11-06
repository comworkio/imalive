from flask import Flask
from flask_restful import Api
from multiprocessing import Process

from heartbit import heartbit
from api_health import HealthEndPoint
from api_manifest import ManifestEndPoint
from api_metrics import MetricsEndPoint

app = Flask(__name__)
api = Api(app)

async_process = Process( 
    target=heartbit,
    daemon=True
)
async_process.start()

health_check_routes = ['/', '/health', '/health/', '/v1', '/v1/', '/v1/health', '/v1/health/']
manifest_routes = ['/manifest', '/manifest/', '/v1/manifest', '/v1/manifest/']
disk_routes = ['/metrics', '/metrics/', '/v1/metrics', '/v1/metrics/']

api.add_resource(HealthEndPoint, *health_check_routes)
api.add_resource(ManifestEndPoint, *manifest_routes)
api.add_resource(MetricsEndPoint, *disk_routes)

if __name__ == '__main__':
    app.run()
