from unittest import TestCase
from preprocessing import get_avg_word_len, get_hashtags_count, \
    get_mentions_count, get_upper_case_count, expand_contractions, get_email_count, remove_emails


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
        count1 = get_hashtags_count(text1)
        count2 = get_hashtags_count(text2)

        # Then
        self.assertEqual(count1, 4)
        self.assertEqual(count2, 4)

    def test_get_number_of_mentions(self):
        # Given
        text1 = "this is @great I feel so cool @blessed #yay #wooho #whoops @mee @@@"
        text2 = "@mine #cool @hashtag #queen slay wow @ damn "

        # When
        count1 = get_mentions_count(text1)
        count2 = get_mentions_count(text2)

        # Then
        self.assertEqual(count1, 4)
        self.assertEqual(count2, 2)

    def test_get_number_of_uppercase_words(self):
        # Given
        text = "HOLD ON I have received this message from James SRL and it's AMAZING!"

        # When
        count = get_upper_case_count(text)

        # Then
        self.assertEqual(count, 2)

    def test_expand_contractions(self):
        # Given
        text = "I'll be right back w/ u I can't wait to see you. I shan't forget"
        text = text.lower()

        # When
        expansion = expand_contractions(text)

        # Then
        self.assertEqual(expansion, "i will be right back with you i cannot wait to see you. i shall not forget")

    def test_get_email_count(self):
        # Given
        text = "I wanna check with jo@bee.com and michael@wawawawa.brough and perhaps jimmy-1212@me.com and " \
               "?+-231aa@ha.do wahoo@me?com"

        # When
        count = get_email_count(text)

        # Then
        self.assertEqual(4, count)

    def test_remove_emails(self):
        # Given
        text = "I wanna check with jo@bee.com and michael@wawawawa.brough and perhaps jimmy-1212@me.com and " \
               "?+-231aa@ha.do wahoo@me?com"

        # When
        new_text = remove_emails(text)

        # Then
        self.assertEqual("I wanna check with  and  and perhaps  and  wahoo@me?com", new_text)
