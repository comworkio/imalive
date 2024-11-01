import re

from unittest import TestCase
from utils.manifests import get_manifest_as_dict

class TestManifest(TestCase):
    def init(self, *args, **kwargs):
        super(TestManifest, self).__init__(*args, **kwargs)
        
    def test_get_manifest(self):
        ## Given

        #When
        result = get_manifest_as_dict()

        ## Then
        self.assertIsNotNone(result)
