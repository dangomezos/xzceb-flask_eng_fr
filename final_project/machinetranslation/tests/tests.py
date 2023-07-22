
### Tests ###

import unittest
from translator import english_to_french, french_to_english

class e2f_Test(unittest.TestCase):
    def test_englishToFrench(self):
        frenchText = english_to_french('Hello')
        self.assertEqual(frenchText, 'Bonjour')
        frenchText = english_to_french('Good Bye')
        self.assertEqual(frenchText, 'au revoir')
    
    def test_frenchToEnglish(self):
        englishText = french_to_english('Bonjour')
        self.assertEqual(englishText, 'Hello')
        englishText = french_to_english('au revoir')
        self.assertEqual(englishText, 'goodbye')


if __name__ == '__main__':
    unittest.main()
