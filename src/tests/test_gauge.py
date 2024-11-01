import re

from unittest import TestCase
from utils.gauge import _numeric_value_pattern

class TestGauge(TestCase):
    def init(self, *args, **kwargs):
        super(TestGauge, self).__init__(*args, **kwargs)

    def test_gauge_regexp_integer(self):
        ## Given
        value = 1

        #When
        result = re.search(_numeric_value_pattern, "{}".format(value))

        ## Then
        self.assertTrue(result)

    def test_gauge_regexp_float(self):
        ## Given
        value = 1.1

        #When
        result = re.search(_numeric_value_pattern, "{}".format(value))

        ## Then
        self.assertTrue(result)

    def test_gauge_regexp_float2(self):
        ## Given
        value = 1.15

        #When
        result = re.search(_numeric_value_pattern, "{}".format(value))

        ## Then
        self.assertTrue(result)

    def test_gauge_regexp_string(self):
        ## Given
        value = "yo"

        #When
        result = re.search(_numeric_value_pattern, "{}".format(value))

        ## Then
        self.assertFalse(result)
