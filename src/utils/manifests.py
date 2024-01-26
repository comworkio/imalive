import os
import json

def get_manifest():
    try:
        with open(os.environ['MANIFEST_FILE_PATH']) as manifest_file:
            manifest = json.load(manifest_file)
            manifest['status'] = 'success'
            return manifest
    except IOError as err:
        return {
            'status': 'error', 
            'reason': err
        }
