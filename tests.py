from collections import defaultdict
import unittest
from unittest import mock
from unittest.mock import mock_open
from simplesearch import SimpleSearch


class TestSimpleSearch(unittest.TestCase):

    @mock.patch.object(SimpleSearch, "_read_files")
    def test_engine_initialized(self, mock_read_files):
        self.search_engine = SimpleSearch("./test-dir")

        self.assertEqual(self.search_engine.directory, "./test-dir")
        self.assertEqual(self.search_engine.index, defaultdict(list))
        self.assertEqual(self.search_engine.text_files, [])
        mock_read_files.assert_not_called()

    @mock.patch(
        "builtins.open",
        new_callable=mock_open,
        read_data="dummy string to test",
    )
    @mock.patch("simplesearch.os.path.join")
    @mock.patch("simplesearch.os.listdir")
    def test_read_files(self, mock_listdir, mock_join, mock_open):
        mock_listdir.return_value = ["example_file.txt", "another_file.txt"]
        mock_join.return_value = None

        self.search_engine = SimpleSearch("./test-dir")
        self.search_engine._read_files()

        self.assertEqual(
            self.search_engine.text_files,
            ["example_file.txt", "another_file.txt"]
        )
        self.assertEqual(
            dict(self.search_engine.index),
            {
                'string': ['example_file.txt', 'another_file.txt'],
                'dummy': ['example_file.txt', 'another_file.txt'],
                'to': ['example_file.txt', 'another_file.txt'],
                'test': ['example_file.txt', 'another_file.txt']
            }
        )

    @mock.patch.object(SimpleSearch, "build_report")
    def test_single_word_search(self, mock_build_report):
        self.search_engine = SimpleSearch("./test-dir")
        self.search_engine.index = {
            'dummy': ['example_file.txt']
        }
        self.search_engine.search("dummy")

        mock_build_report.assert_called_once_with(
            {'example_file.txt': (100.0, ['dummy'])}
        )

    @mock.patch.object(SimpleSearch, "build_report")
    def test_multiple_word_search(self, mock_build_report):
        self.search_engine = SimpleSearch("./test-dir")
        self.search_engine.index = {
            'multiple': ['another_file.txt'],
            'dummy': ['example_file.txt']
        }
        self.search_engine.search("multiple dummy")

        mock_build_report.assert_called_once_with(
            {
                'another_file.txt': (50.0, ['multiple']),
                'example_file.txt': (50.0, ['dummy'])
            }
        )

    @mock.patch.object(SimpleSearch, "build_report")
    def test_no_match(self, mock_build_report):
        self.search_engine = SimpleSearch("./test-dir")
        self.search_engine.index = {
            'multiple': ['another_file.txt'],
            'dummy': ['example_file.txt']
        }
        self.search_engine.search("different words")

        mock_build_report.assert_called_once_with({})

    @mock.patch.object(SimpleSearch, "build_report")
    def test_empty_search(self, mock_build_report):
        self.search_engine = SimpleSearch("./test-dir")
        self.search_engine.index = {
            'multiple': ['another_file.txt'],
            'dummy': ['example_file.txt']
        }
        self.search_engine.search("")

        mock_build_report.assert_not_called()

    @mock.patch.object(SimpleSearch, "print_report")
    def test_build_report__single_file(self, mock_print_report):
        self.search_engine = SimpleSearch("./test-dir")
        self.search_engine.text_files = [
            "example_file.txt", "another_file.txt"
        ]

        self.search_engine.build_report(
            {'example_file.txt': (100.0, ['dummy'])}
        )

        mock_print_report.assert_called_once_with(
            [
                ('example_file.txt', (100.0, ['dummy'])),
                ('another_file.txt', (0, []))
            ]
        )

    @mock.patch.object(SimpleSearch, "print_report")
    def test_build_report__multiple_file(self, mock_print_report):
        self.search_engine = SimpleSearch("./test-dir")
        self.search_engine.text_files = [
            "example_file.txt", "another_file.txt"
        ]
        self.search_engine.build_report(
            {
                'another_file.txt': (50.0, ['multiple']),
                'example_file.txt': (50.0, ['dummy'])
            }
        )

        mock_print_report.assert_called_once_with(
            [
                ('another_file.txt', (50.0, ['multiple'])),
                ('example_file.txt', (50.0, ['dummy']))
            ]
        )
