import unittest
from repro2.code import *

class TestCodeCommandeConforme(unittest.TestCase):
    def test_exemple(self):
        self.assertEqual(codeCommandeConforme("#22ABg12"),True)
        self.assertEqual(codeCommandeConforme("$22ABg12"),False)
        self.assertEqual(codeCommandeConforme("#2AAbg12"),False)
        self.assertEqual(codeCommandeConforme("#22ABg1+"),False)
        with self.assertRaises(ErreurTropCourt):
            codeCommandeConforme("#22")
        with self.assertRaises(ErreurTropLong):
            codeCommandeConforme("#22ABg12963")

if __name__ == '__main__':
    unittest.main()
