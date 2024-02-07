from unittest import TestCase
from utils.health import health as get_health

class TestHealth(TestCase):
    def init(self, *args, **kwargs):
        super(TestHealth, self).__init__(*args, **kwargs)

    def test_get_health(self):
        ## Given

        #When
        result = get_health()

        ## Then
        self.assertIsNotNone(result)
        
    def test_post_health(self):
        #When
        result = get_health()

        ## Then
        self.assertIsNotNone(result)
