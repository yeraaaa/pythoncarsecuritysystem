import unittest
import platform

if platform.system() == "Windows":
    from src.ignition_module_stub import start_engine, stop_engine
else:
    from src.ignition_module import start_engine, stop_engine

class TestIgnitionModule(unittest.TestCase):
    def test_start_engine(self):
        start_engine()
        self.assertTrue(True)  

    def test_stop_engine(self):
        stop_engine()
        self.assertTrue(True)  

if __name__ == "__main__":
    unittest.main()
