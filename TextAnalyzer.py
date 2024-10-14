import pandas as pd
from collections import Counter

class TextAnalyzer:
    def __init__(self, text):
        self.text = text.upper() 

    def get_letter_frequencies(self):
        letter_counts = Counter(char for char in self.text if char.isalpha())
        total_letters = sum(letter_counts.values())

        letter_freq = {letter: round((count / total_letters) * 100, 2) for letter, count in letter_counts.items()}

        df = pd.DataFrame({
            'Letter': letter_counts.keys(),
            'Count': letter_counts.values(),
            'Frequency': letter_freq.values(),
            'Matching_letter': [''] * len(letter_counts)
        })

        df = df.sort_values(by='Frequency', ascending=False)

        return df

    def replace_letters(self, df):
        replacement_map = {row['Letter']: row['Matching_letter'] for _, row in df.iterrows() if row['Matching_letter']}
        new_text = ""

        for char in self.text:
            if char in replacement_map:
                new_text += replacement_map[char].lower()
            else:
                new_text += char
        return new_text

    def count_digraphs(self):
        digraph_counts = {}

        for i in range(len(self.text) - 1):
            digraph = self.text[i:i + 2]
            if digraph.isalpha():
                if digraph in digraph_counts:
                    digraph_counts[digraph] += 1
                else:
                    digraph_counts[digraph] = 1

        sorted_digraphs = sorted(digraph_counts.items(), key=lambda item: item[1], reverse=True)
        top_digraphs = dict(sorted_digraphs[:12])

        return top_digraphs

    def count_trigraphs(self):
        trigraph_count = {}

        for i in range(len(self.text) - 2):
            trigraph = self.text[i:i + 3]
            if trigraph.isalpha():
                if trigraph in trigraph_count:
                    trigraph_count[trigraph] += 1
                else:
                    trigraph_count[trigraph] = 1

        sorted_trigraphs = sorted(trigraph_count.items(), key=lambda item: item[1], reverse=True)
        top_trigraphs = dict(sorted_trigraphs[:13])

        return top_trigraphs

    def count_doubles(self):
        double_count = {}

        for i in range(len(self.text) - 1):
            if self.text[i] == self.text[i + 1]:
                double = self.text[i:i + 2]
                if double in double_count:
                    double_count[double] += 1
                else:
                    double_count[double] = 1

        sorted_doubles = sorted(double_count.items(), key=lambda item: item[1], reverse=True)
        top_doubles = dict(sorted_doubles[:7])

        return top_doubles
