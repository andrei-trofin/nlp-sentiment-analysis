import pandas as pd
from chardet.universaldetector import UniversalDetector

"""
Initial data verification
"""


def get_file_encoding(file_path):
    """
    Function that outputs the most probable encoding for a file at a file path.
    :param file_path: the path of the file that needs encoding check
    :return: the file encoding that the library is most confident that it is correct and the confidence
    """
    detector = UniversalDetector()
    with open(file_path, "rb") as file:
        for line in file.readlines():
            detector.feed(line)
            if detector.done:
                break
        detector.close()

    return detector.result


"""
Data preprocessing functions
"""


def get_avg_word_len(text):
    """
    Function which returns the average word length within a paragraph.
    :param text: the actual text
    :return: the average word length from the text
    """
    words = text.split()
    total_word_len = 0
    for word in words:
        total_word_len += len(word)

    return total_word_len/len(words)


def get_number_of_hashtags(text):
    """
    Function which return the number of hashtags in a text. It will not count single #, it has to be followed by other
    characters.
    :param text: the actual text
    :return: the number of hashtags in the text
    """
    return len([word for word in text.split() if len(word) > 1 and word.startswith("#")])


def get_number_of_mentions(text):
    """
    Function which return the number of mentions in a text. It will not count single @, it has to be followed by other
    characters.
    :param text: the actual text
    :return: the number of mentions in the text
    """
    return len([word for word in text.split() if len(word) > 1 and word.startswith("@")])


