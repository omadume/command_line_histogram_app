import unittest
from unittest.mock import patch
import argparse
import task

class TestTask(unittest.TestCase):
    @patch('argparse.ArgumentParser.parse_args',
           return_value=argparse.Namespace(number='10'))
    def test_with_name_argument(self, mock_parse_args):
        with patch('builtins.print') as mock_print:
            task.main()
            self.assertTrue(any('*' in call_args[0] for call_args, _ in mock_print.call_args_list)) # Test that there was any histogram output

    @patch('argparse.ArgumentParser.parse_args',
           return_value=argparse.Namespace(number=None))
    def test_without_number_argument(self, mock_parse_args):
        with patch('builtins.print') as mock_print:
            task.main()
            mock_print.assert_called_with('No argument provided.\nUse -h or --help for full usage options.')

if __name__ == '__main__':
    unittest.main()
