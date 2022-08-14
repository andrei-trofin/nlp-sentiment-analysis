import re

from chardet.universaldetector import UniversalDetector
from contractions import contractions_dict
from unicodedata import normalize
from emot.emo_unicode import EMOTICONS_EMO
from spacy.lang.en import STOP_WORDS

LC_EMOTIONS_DICT = {
    k.lower(): " " + "_".join(v.lower().replace(",", " ").replace("or", "").split()) + " "
    for k, v in EMOTICONS_EMO.items() if k != "oO"}

"""
Initial data verification
"""


def get_file_encoding(file_path):
    """
    Function that outputs the most probable encoding for a file at a file path.
    :param file_path: The path of the file that needs encoding check.
    :return: The file encoding that the library is most confident that it is correct and the confidence.
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
    :return: The average word length from the text.
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
    :return: The number of hashtags in the text.
    """
    return len([word for word in text.split() if len(word) > 1 and word.startswith("#")])


def get_upper_case_count(text):
    """
    Function which return the number of uppercase words with more than 3 characters in a text.
    :param text: The text to search through.
    :return: The number of uppercase words with a length bigger than 3 in the text.
    """
    return len([word for word in text.split() if len(word) > 3 and word.isupper()])


def expand_contractions(text):
    """
    Function which expands the words in a text given a static dictionary.
    The assumption is that the text is in lowercase.
    :param text: The text to modify.
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
    :return: The number of emails in the text.
    """
    mail_regex = r'([a-zA-Z0-9+._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)'
    return len(re.findall(mail_regex, text))


def remove_emails(text):
    """
    Remove the emails from text.
    :param text: The text to modify.
    :return: The text without any email that was initially in.
    """
    mail_regex = r'([a-zA-Z0-9+._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)'

    return re.sub(mail_regex, '', text)


def get_url_count(text):
    """
    Get the number of URLs in the text.
    :param text: The text to search through.
    :return: The number of URLs in the text.
    """
    url_regex = r'(http|ftp|https):\/\/([\w\-_]+(?:(?:\.[\w\-_]+)+))([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?'

    return len(re.findall(url_regex, text))


def remove_urls(text):
    """
    Remove the URLs from text.
    :param text: The text to modify.
    :return: The text without any URL that was initially in.
    """
    url_regex = r'(http|ftp|https):\/\/([\w\-_]+(?:(?:\.[\w\-_]+)+))([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?'

    return re.sub(url_regex, '', text)


def remove_retweet(text):
    """
    Function which removes the rt part of the message if it is a retweet.
    :param text: The text to modify.
    :return: The text without the retweet key.
    """
    retweet_regex = r'( |^)rt( @)'
    retweet_keep_regex = r'\1\2'

    return re.sub(retweet_regex, retweet_keep_regex, text)


def get_mention_count(text):
    """
    Get the number of mentions in the text.
    :param text: The text to search through.
    :return: The number of mentions in the text
    """
    mention_regex = r'[ \.,\\\/;]@\w+[ \.,\\\/;]'

    return len(re.findall(mention_regex, text))


def remove_mentions(text):
    """
    Function which removes the mentions from the message.
    :param text: The text to modify
    :return: The text without the mentions.
    """
    mention_regex = r'([ \.,\\\/;])@\w+([ \.,\\\/;])'
    mention_keep_regex = r'\1\2'

    return re.sub(mention_regex, mention_keep_regex, text)


def is_reply(text):
    """
    Functions which returns whether a tweet is a reply to someone or not
    :param text: The text to search through.
    :return: 1 if the tweet is a reply, 0 if not.
    """
    mention_regex = r'^@\w+[ \.,\\\/;]'

    return len(re.findall(mention_regex, text))


def remove_reply_target(text):
    """
    Function which removes the reply target from the message.
    :param text: The text to modify.
    :return: The text without the reply target.
    """
    mention_regex = r'^@\w+([ \.,\\\/;])'
    mention_keep_regex = r'\1'

    return re.sub(mention_regex, mention_keep_regex, text)


def remove_accents(text):
    """
    Function which removes the accents on words from the message.
    :param text: The text to modify.
    :return: The text without the accents on words.
    """

    return normalize('NFKD', text).encode('ascii', 'ignore').decode('ascii', 'ignore')


def replace_emoticons(text):
    """
    Function which replaces the emoticons in text with their meaning
    :param text: The text to modify.
    :return: The text with emoticons converted to words.
    """
    for em in LC_EMOTIONS_DICT:
        emoticon_words = LC_EMOTIONS_DICT[em]
        text = re.sub(re.escape(em), emoticon_words, text)

    return text


def remove_special_characters(text):
    """
    Function which removes all the special characters, besides - and _ from text.
    :param text: The text to modify.
    :return: Text without any special characters besides - and _. Special characters are replaced by space.
    """
    special_chars_regex = r'[^A-Za-z0-9 \-\_]+'
    return re.sub(special_chars_regex, ' ', text)


def remove_single_characters(text):
    """
    Function which removes all the single characters from text.
    :param text: The text to modify.
    :return: Text containing words with a length >= 2.
    """
    return " ".join([word for word in text.split() if len(word) > 1])


def preprocess_text(text, stemmer):
    new_text = text.lower()
    new_text = expand_contractions(new_text)
    new_text = remove_emails(new_text)
    new_text = remove_urls(new_text)
    new_text = remove_retweet(new_text)
    new_text = remove_mentions(new_text)
    new_text = remove_reply_target(new_text)
    new_text = remove_accents(new_text)
    new_text = replace_emoticons(new_text)
    new_text = remove_special_characters(new_text)
    new_text = remove_single_characters(new_text)
    new_text = " ".join([word for word in new_text.split() if word not in STOP_WORDS])
    new_text = " ".join([stemmer.stem(word) for word in new_text.split()])

    return new_text
