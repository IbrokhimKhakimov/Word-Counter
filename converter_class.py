# Regex library is used to find the patterns inside text
import re
# CSV library is used to make csv files
import csv
# Counter class from collections library is used to count the word count
from collections import Counter


class Converter:
    def __init__(self, text):
        self._text = text
        self._word_count = None

    def process_text(self):
        # Processing the text
        #   reading finding the patterns, and putting them into a list
        #   counting them using Counter class, it takes list of words and outputs the dictionary of words with the counting numbers
        pattern = r"\w+"
        words = re.findall(pattern, self._text.lower())
        self._word_count = Counter(words)

    def sorted_word_count(self, by="frequency_desc"):
        """
        Sorting the word count dictionary.

        Sorting options:
        - 'frequency_desc': by frequency in descending order (default)
        - 'frequency_asc': by frequency in ascending order
        - 'alpha_asc': by words alphabetically in ascending order
        - 'alpha_desc': by words alphabetically in descending order
        """
        if self._word_count is None:
            self.process_text()

        if by == "frequency_asc":
            # Sorting by frequency in ascending order
            return dict(sorted(self._word_count.items(), key=lambda x: x[1]))
        elif by == "alpha_asc":
            # Sorting by word in alphabetical order (ascending)
            return dict(sorted(self._word_count.items(), key=lambda x: x[0]))
        elif by == "alpha_desc":
            # Sorting by word in alphabetical order (descending)
            return dict(sorted(self._word_count.items(), key=lambda x: x[0], reverse=True))
        else:
            # Default: Sorting by frequency in descending order
            return dict(sorted(self._word_count.items(), key=lambda x: x[1], reverse=True))

    # Function that creates the csv file
    def save_to_csv(self, file_name="word_count.csv", sort_by="frequency_desc"):
        sorted_words = self.sorted_word_count(by=sort_by)
        with open(file_name, "w", newline="") as word_count_file:
            writer = csv.DictWriter(
                word_count_file, fieldnames=["Word", "Count"])
            writer.writeheader()
            for word, count in sorted_words.items():
                writer.writerow({"Word": word, "Count": count})
