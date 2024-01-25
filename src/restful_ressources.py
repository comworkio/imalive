from routes import api_health as health
from routes import api_manifest as manifest
from routes import api_metrics as metrics

health_check_routes = ['', '/v1', '/health', '/v1/health']
manifest_routes = ['/manifest', '/v1/manifest']
disk_routes = ['/metrics', '/v1/metrics']

def import_ressources(app):
    for route in health_check_routes:
        app.include_router(health.router, tags=["Health"], prefix=route)
    
    for route in manifest_routes:
        app.include_router(manifest.router, tags=["Manifest"], prefix=route)
    
    for route in disk_routes:
        app.include_router(metrics.router, tags=["Metrics"], prefix=route)