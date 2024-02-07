from fastapi import FastAPI
from unittest import TestCase

class TestApp(TestCase):
    def __init__(self, *args, **kwargs):
        super(TestApp, self).__init__(*args, **kwargs)
        TestApp.get_app()

    @staticmethod
    def get_app():
        global app
        app = FastAPI(docs_url = "/docs")
        return app
