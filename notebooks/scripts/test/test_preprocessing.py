from unittest import TestCase
from preprocessing import get_avg_word_len, get_hashtags_count, get_upper_case_count, \
    expand_contractions, get_email_count, remove_emails, get_url_count, remove_urls, remove_retweet, get_mention_count,\
    remove_mentions, is_reply, remove_reply_target, remove_accents, remove_special_characters, remove_extra_spaces


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

    def test_get_url_count(self):
        # Given
        text = "@switchfoot http://twitpic.com/2y1zl - awww, t... httv://www.me.com ftp://ro.know.me/"

        # When
        count = get_url_count(text)

        # Then
        self.assertEqual(2, count)

    def test_remove_urls(self):
        # Given
        text = "@switchfoot http://twitpic.com/2y1zl - awww, t... httv://www.me.com ftp://ro.know.me/"

        # When
        new_text = remove_urls(text)

        # Then
        self.assertEqual("@switchfoot  - awww, t... httv://www.me.com ", new_text)

    def test_remove_retweet(self):
        # Given
        text = "rt @bro come here and tell me rt now where you at I wanna know if art is good or not. rt @romeo ha"

        # When
        new_text = remove_retweet(text)

        # Then
        self.assertEqual(" @bro come here and tell me rt now where you at I wanna know if art is good or not."
                         "  @romeo ha", new_text)

    def test_get_mention_count(self):
        # Given
        text = "@switchfoot let's talk to @james and @michale and @bee222 to see me @ the pub @@@"

        # When
        count = get_mention_count(text)

        # Then
        self.assertEqual(3, count)

    def test_remove_mentions(self):
        # Given
        text = "@switchfoot let's talk to @james and @michale and @bee222 to see me @ the pub @@@"

        # When
        count = remove_mentions(text)

        # Then
        self.assertEqual("@switchfoot let's talk to  and  and  to see me @ the pub @@@", count)

    def test_is_reply(self):
        # Given
        text1 = "@switchfoot let's talk to @james and @michale and @bee222 to see me @ the pub @@@"
        text2 = "bamabam @me hey yo hey"

        # When
        is_reply_flag1 = is_reply(text1)
        is_reply_flag2 = is_reply(text2)

        # Then
        self.assertEqual(1, is_reply_flag1)
        self.assertEqual(0, is_reply_flag2)

    def test_remove_reply_target(self):
        # Given
        text = "@switchfoot let's talk to @james and @michale and @bee222 to see me @ the pub @@@"

        # When
        count = remove_reply_target(text)

        # Then
        self.assertEqual(" let's talk to @james and @michale and @bee222 to see me @ the pub @@@", count)

    def test_remove_accents(self):
        # Given
        text = "dà, è, ì, ò, ù, á, é, í, ó, ú, ý, â, ê, î, ô, û, ã, ñ, õ, ä, ë, ï, ö, ü, ÿ, å, ç"

        # When
        count = remove_accents(text)

        # Then
        self.assertEqual("da, e, i, o, u, a, e, i, o, u, y, a, e, i, o, u, a, n, o, a, e, i, o, u, y, a, c", count)

    def test_remove_special_characters(self):
        # Given
        text = "So cool dude ... hope u can be.so.nice and you+me=great h@h@h@ see ya @@@@ wanna-be"

        # When
        new_text = remove_special_characters(text)

        # Then
        self.assertEqual("So cool dude   hope u can be so nice and you me great h h h  see ya   wanna-be", new_text)

    def test_remove_extra_spaces(self):
        # Given
        text = "So cool dude   hope u can be so nice and you me great h h h  see ya   wanna-be"

        # When
        new_text = remove_extra_spaces(text)

        # Then
        self.assertEqual("So cool dude hope u can be so nice and you me great h h h see ya wanna-be", new_text)
