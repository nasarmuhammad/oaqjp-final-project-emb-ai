"""Unit tests for the Watson NLP EmotionDetection package."""

import unittest

from EmotionDetection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """Test detection of the five supported emotions."""

    def test_joy(self):
        """Verify that a happy statement produces joy."""
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_anger(self):
        """Verify that an angry statement produces anger."""
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result["dominant_emotion"], "anger")

    def test_disgust(self):
        """Verify that a disgusting statement produces disgust."""
        result = emotion_detector(
            "I feel disgusted just hearing about this"
        )
        self.assertEqual(result["dominant_emotion"], "disgust")

    def test_sadness(self):
        """Verify that a sad statement produces sadness."""
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result["dominant_emotion"], "sadness")

    def test_fear(self):
        """Verify that a fearful statement produces fear."""
        result = emotion_detector(
            "I am really afraid that this will happen"
        )
        self.assertEqual(result["dominant_emotion"], "fear")


if __name__ == "__main__":
    unittest.main()
