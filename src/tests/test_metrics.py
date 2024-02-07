from unittest import TestCase
from utils.metrics import disk_usage, virtual_memory, swap_memory, cpu

class TestMetrics(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_disk_usage(self):
        ## Given

        # When
        result = disk_usage()

        ## Then
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)
        self.assertIn("total", result)
        self.assertIn("used", result)
        self.assertIn("free", result)

    def test_virtual_memory(self):
        ## Given

        # When
        result = virtual_memory()

        ## Then
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)
        self.assertIn("total", result)
        self.assertIn("available", result)

    def test_swap_memory(self):
        ## Given

        # When
        result = swap_memory()

        ## Then
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)
        self.assertIn("total", result)
        self.assertIn("used", result)
        self.assertIn("free", result)
        self.assertIn("percent", result)

    def test_cpu(self):
        ## Given

        # When
        result = cpu()

        ## Then
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)
        self.assertIn("percent", result)
        self.assertIn("count", result)
        self.assertIn("times", result)
