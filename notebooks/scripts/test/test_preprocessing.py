from unittest import TestCase
from preprocessing import get_avg_word_len, get_number_of_hashtags, get_number_of_mentions


class TestPreprocessingFunctions(TestCase):
    def test_get_avg_word_len(self):
        # Given
        text1 = "It is a wonderful night let's play"
        text2 = "Wow    NICE"

        # When
        count1 = get_avg_word_len(text1)
        count2 = get_avg_word_len(text2)

        # Then
        self.assertEqual(count1, 4)
        self.assertEqual(count2, 3.5)

    def test_get_number_of_hashtags(self):
        # Given
        text1 = "this is great I feel so cool #blessed #yay #wooho #whoops @mee"
        text2 = "#mine #cool #hashtag #queen slay wow # damn"

        # When
        count1 = get_number_of_hashtags(text1)
        count2 = get_number_of_hashtags(text2)

        # Then
        self.assertEqual(count1, 4)
        self.assertEqual(count2, 4)

    def test_get_number_of_mentions(self):
        # Given
        text1 = "this is @great I feel so cool @blessed #yay #wooho #whoops @mee @@@"
        text2 = "@mine #cool @hashtag #queen slay wow @ damn "

        # When
        count1 = get_number_of_mentions(text1)
        count2 = get_number_of_mentions(text2)

        # Then
        self.assertEqual(count1, 4)
        self.assertEqual(count2, 2)
