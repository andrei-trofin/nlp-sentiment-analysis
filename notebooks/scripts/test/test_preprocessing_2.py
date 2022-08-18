import unittest
from preprocessing_2 import preprocess_text


class TestPreprocessingFunctions2(unittest.TestCase):
    def test_preprocess_text(self):
        # Given
        text = "i wanna have a day like this full of fatmo and modicum and some veremo"

        # When
        new_text = preprocess_text(text)

        # Then
        self.assertEqual("i wanna have a this full of and and some", new_text)
