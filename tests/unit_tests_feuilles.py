import unittest
from repro2.feuilles import *

class TestVerifierCommandeImpression(unittest.TestCase):
    def test_exemple(self):
        self.assertEqual(verifierCommandeImpression(100, 300), Reponse.ACCEPTER_SANS_ALERTE)
        self.assertEqual(verifierCommandeImpression(100, 140), Reponse.ACCEPTER_ALERTE_ORANGE)
        self.assertEqual(verifierCommandeImpression(100, 100), Reponse.ACCEPTER_ALERTE_ROUGE)
        self.assertEqual(verifierCommandeImpression(100, 90), Reponse.REFUSER)
        self.assertEqual(verifierCommandeImpression(2001, 3000), Reponse.REFUSER)
        with self.assertRaises(ValueError):
            verifierCommandeImpression(0, 100)

if __name__ == '__main__':
    unittest.main()
