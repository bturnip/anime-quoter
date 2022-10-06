''' test driver for anime_quote.py '''
import unittest
import anime_quote as aq

class TestAnimeQuote(unittest.TestCase):
    ''' unit test cases '''

    def test01_get_anime_quote(self):
        ''' test 01: confirm that a dict is returned '''
        self.assertIs(type(aq.get_anime_quote()), dict)

    def test02_get_anime_quote(self):
        ''' test 02: keys of dict are ['anime', 'character', 'quote']'''
        expected_keys = ['anime', 'character', 'quote']
        received_keys =  list(aq.get_anime_quote().keys())

        for i,k in enumerate(expected_keys):
            expected = k
            received = received_keys[i]
            self.assertEqual(expected,received,)
            #print(f'+++ i:{i} k:{k}')
            #print(f'+++ i:{i} r:{received_keys[i]}')

    def test03_get_anime_quote(self):
        ''' test 03: simpler version of test02 '''
        expected_keys = ['anime', 'character', 'quote']
        received_keys = list(aq.get_anime_quote().keys())

        self.assertEqual(expected_keys,received_keys)


if __name__ == '__main__':
    unittest.main()
