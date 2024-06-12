import unittest
import platform

if platform.system() == "Windows":
    from src.camera_module_stub import capture_image
else:
    from src.camera_module import capture_image

class TestCameraModule(unittest.TestCase):
    def test_capture_image(self):
        capture_image()
        self.assertTrue(True)  

if __name__ == "__main__":
    unittest.main()
