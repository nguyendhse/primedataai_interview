import unittest

from string_tokenize import Tokenizer


class TestStringTokenize(unittest.TestCase):

    def setUp(self):
        self.string_tokenize = Tokenizer()

    def test_format_string_correct(self):
        template = 'Hi {name}, welcome to {company}!. How\'re you {name}.'
        params = {"name": "Nguyen", "company": "PrimeData"}

        actual = self.string_tokenize.format_string(template, params)

        self.assertEqual("Hi Nguyen, welcome to PrimeData!. How\'re you Nguyen.", actual)

    def test_format_string_correct_2(self):
        template = 'Hi {name}, welcome to {company}!. How\'re you {name}. Say {say}'
        params = {"name": "Nguyen", "company": "PrimeData", "say": "Hello, world"}

        actual = self.string_tokenize.format_string(template, params)

        self.assertEqual("Hi Nguyen, welcome to PrimeData!. How\'re you Nguyen. Say Hello, world", actual)

    def test_format_string_fail_and_raise_error_1(self):
        template = 'Hi {name}{name}, welcome to {company}!. How\'re you {name}.'
        params = {"name": "Nguyen", "company": "PrimeData"}
        try:
            self.string_tokenize.format_string(template, params)
        except ValueError as err:
            self.assertEqual('Insufficient number of params', str(err))

    def test_format_string_fail_and_raise_error_2(self):
        template = 'Hi {name}, welcome to {company}!. How\'re you {name}. Say {say1234}'
        params = {"name": "Nguyen", "company": "PrimeData", "say": "Hello, world"}

        with self.assertRaises(ValueError):
            self.string_tokenize.format_string(template, params)
