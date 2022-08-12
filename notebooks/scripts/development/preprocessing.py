import re

import pandas as pd
from chardet.universaldetector import UniversalDetector
from contractions import contractions_dict

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
    :param text: The text to search through.
    :return: the average word length from the text
    """
    words = text.split()
    total_word_len = 0
    for word in words:
        total_word_len += len(word)

    return total_word_len/len(words)


def get_hashtags_count(text):
    """
    Function which returns the number of hashtags in a text. It will not count single #, it has to be followed by other
    characters.
    :param text: The text to search through.
    :return: the number of hashtags in the text
    """
    return len([word for word in text.split() if len(word) > 1 and word.startswith("#")])


def get_mentions_count(text):
    """
    Function which returns the number of mentions in a text. It will not count single @, it has to be followed by other
    characters.
    :param text: The text to search through.
    :return: the number of mentions in the text
    """
    return len([word for word in text.split() if len(word) > 1 and word.startswith("@")])


def get_upper_case_count(text):
    """
    Function which return the number of uppercase words with more than 3 characters in a text.
    :param text: The text to search through.
    :return: the number of uppercase words with a length bigger than 3 in the text
    """
    return len([word for word in text.split() if len(word) > 3 and word.isupper()])


def expand_contractions(text):
    """
    Function which expands the words in a text given a static dictionary.
    The assumption is that the text is in lowercase.
    :param text: The text to search through.
    :return:
    """
    my_contractions_dict = {k.lower(): v.lower() for k, v in contractions_dict.items()}
    # Add some contractions that are not in the library
    my_contractions_dict.update({' u ': ' you ', ' n ': ' and ', " 'n ": ' and ', ' w ': ' with ', ' w/ ': ' with ',
                                 ' ur ': ' your ', ' nah ': ' no '})
    if type(text) is str:
        for key in my_contractions_dict.keys():
            value = my_contractions_dict[key]
            text = text.replace(key, value)
    return text


def get_email_count(text):
    """
    Get the number of emails in the text.
    :param text: The text to search through.
    :return: The number of email mentions in the text
    """
    mail_regex = r'([a-zA-Z0-9+._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)'
    return len(re.findall(mail_regex, text))


def remove_emails(text):
    """
    Remove the emails from text
    :param text: The text to search through.
    :return: The text without any email that was initially in.
    """
    mail_regex = r'([a-zA-Z0-9+._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)'

    return re.sub(mail_regex, '', text)