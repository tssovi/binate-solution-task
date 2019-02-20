import shutil, tempfile
import unittest
from function import ReadFile


class TestLink(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory
        self.test_img_path = tempfile.mkdtemp()

    def tearDown(self):
        # Remove the directory after the test
        shutil.rmtree(self.test_img_path)

    F1 = {'valid': 1, 'invalid': 0}
    F2 = {'valid': 0, 'invalid': 1}

    def test_valid_link(self):
        self.assertEqual(ReadFile('textfile/test_valid_url.txt', self.test_img_path), self.F1, "Should be same")

    def test_invalid_link(self):
        self.assertEqual(ReadFile('textfile/test_invalid_url.txt', self.test_img_path), self.F2, "Should be same")

if __name__ == '__main__':
    unittest.main()

