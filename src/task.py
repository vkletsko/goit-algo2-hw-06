import requests
import re
import matplotlib.pyplot as plt
from collections import Counter
from functools import reduce


def download_text(url):
    response = requests.get(url)
    return response.text


def map_func(text):
    words = re.findall(r'\w+', text.lower())
    return words


def reduce_func(word_lists):
    word_count = Counter()
    for word_list in word_lists:
        word_count.update(word_list)
    return word_count


def visualize_top_words(word_count, top_n=10):
    top_words = word_count.most_common(top_n)
    words, counts = zip(*top_words)

    plt.figure(figsize=(10, 6))
    plt.barh(words, counts, color='skyblue')
    plt.xlabel('Frequency')
    plt.ylabel('Words')
    plt.title(f'Top {top_n} Words by Frequency')
    plt.show()


if __name__ == "__main__":
    url = "https://gutenberg.net.au/ebooks01/0100291.txt"
    text = download_text(url)
    mapped_words = map_func(text)
    word_count = reduce_func([mapped_words])
    visualize_top_words(word_count, top_n=10)