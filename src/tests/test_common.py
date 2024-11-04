import re

from unittest import TestCase

from utils.common import sanitize_header_name

class TestCommon(TestCase):
    def init(self, *args, **kwargs):
        super(TestCommon, self).__init__(*args, **kwargs)

    def test_sanitize_header_name_accept(self):
        ## Given
        header = "accept"

        #When
        result = sanitize_header_name(header)

        ## Then
        self.assertEqual("Accept", result)

    def test_sanitize_header_name_contenttype(self):
        ## Given
        header = "content-type"

        #When
        result = sanitize_header_name(header)

        ## Then
        self.assertEqual("Content-Type", result)
