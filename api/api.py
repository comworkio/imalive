from flask import Flask
from flask_restful import Api
from multiprocessing import Process

from heartbit import heartbit
from api_health import HealthEndPoint

app = Flask(__name__)
api = Api(app)

async_process = Process( 
    target=heartbit,
    daemon=True
)
async_process.start()

health_check_routes = ['/', '/health', '/health/', '/v1', '/v1/', '/v1/health', '/v1/health/']

api.add_resource(HealthEndPoint, *health_check_routes)

if __name__ == '__main__':
    app.run()
