import unittest
from main import filter_list_of_dict
from main import string_to_dictionary


class TestDataAnalysis(unittest.TestCase):
    def test_string_to_dictionary(self):
        keys = ['data', 'time', 'seed', 'tag']
        line = '2007-05,15:45,1413561,anri'

        result = string_to_dictionary(keys, line)
        expect = {'data': '2007-05', 'time': '15:45', 'seed': '1413561', 'tag': 'anri'}

        self.assertEqual(expect, result)

    def test_filter(self):
        list_of_dict = [{'arbuz': '1', 'ogurets': '2'},
                        {'arbuz': '2', 'ogurets': '2'},
                        {'arbuz': '2', 'ogurets': '1'}]
        key = 'arbuz'
        value = '1'

        result = filter_list_of_dict(list_of_dict, key, value)
        expect = [{'arbuz': '1', 'ogurets': '2'}]

        self.assertEqual(expect, result)


if __name__ == '__main__':
    unittest.main()
