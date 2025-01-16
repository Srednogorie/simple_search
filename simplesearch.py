import os
import re
import sys

from collections import defaultdict


class SimpleSearch:
    def __init__(self, directory):
        self.directory = directory
        self.index = defaultdict(list)
        self.text_files = []

    def _read_files(self):
        '''
        Very simple matching pattern which can be improved further:
            -- Handle contractions and hyphenated words.
            -- Custom configurable stop words.
        '''
        self.text_files = [
            f for f in os.listdir(self.directory) if f.endswith('.txt')
        ]
        for file in self.text_files:
            file_path = os.path.join(self.directory, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read().lower()
                words = list(set(re.findall(r'\b\w+\b', text)))
                for word in words:
                    self.index[word].append(file)

    def search(self, query):
        '''
        Removing duplicates from the query to avoid double counting.
        '''
        query_words = list(set(re.findall(r'\b\w+\b', query.lower())))
        if not query_words:
            print("No valid search terms.")
            return

        words_found = {}
        for word in query_words:
            for file in self.index.get(word, []):
                if file in words_found:
                    words_found[file][0] += 1
                    words_found[file][1].append(word)
                else:
                    words_found[file] = [1, [word]]

        result = {}
        for file, score in words_found.items():
            percent_total_found = (score[0] / len(query_words)) * 100
            result[file] = (percent_total_found, score[1])
        self.build_report(result)

    def build_report(self, result):
        '''
        Filling the report with 0% records for files not found in the result.
        Sorting based on the percent of words found in the file.
        '''
        if not result:
            print("No matches found.")
        else:
            report = {}
            for fine_name in self.text_files:
                if fine_name in result:
                    report[fine_name] = result[fine_name]
                else:
                    report[fine_name] = (0, [])
            sorted_report = sorted(
                report.items(), key=lambda x: x[1], reverse=True
            )
            self.print_report(sorted_report)

    def print_report(self, sorted_report):
        for entry in sorted_report:
            print(f"File name: {entry[0]}")
            print(f"    -- Percent found in the file: {entry[1][0]}%")
            print(f"    -- Words found: {entry[1][1]}")

    def interactive_search(self):
        '''
        Don't like running _read_files here but doing it the init makes it
        difficult to test. If it wasn't a console application we probably would
        do other stuff in a similar entry method.
        '''
        self._read_files()
        print("search> ", end="", flush=True)
        while True:
            query = input()
            if query.strip() == ":q":
                break
            self.search(query)
            print("search> ", end="", flush=True)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python simplesearch.py <pathToDirectoryContainingFiles>")
    else:
        search_engine = SimpleSearch(sys.argv[1])
        search_engine.interactive_search()
