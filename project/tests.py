import unittest

from translator import englishToFrench,frenchToEnglish

class Test1(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench('0'), '0') # test when 2 is given as input the output is 4.
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')  # test when 3.0 is given as input the output is 9.0.

class Test2(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchToEnglish('0'), '0') # test when 2 is given as input the output is 4.
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello') # test when -3.1 is given as input the output is -6.2.

unittest.main()
