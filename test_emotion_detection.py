from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    """
    Test for the emotion detector function
    """
    def test_emotion_detector(self):
        # Test the joy emotion
        self.assertEqual(emotion_detector("I am glad this happened")["dominant_emotion"], "joy")

        # Test the anger emotion
        self.assertEqual(emotion_detector("I am really mad about this")["dominant_emotion"], "anger")

        # Test the disgust emotion
        self.assertEqual(emotion_detector("I feel disgusted just hearing about this")["dominant_emotion"], "disgust")

        # Test the sadness emotion
        self.assertEqual(emotion_detector("I am so sad about this")["dominant_emotion"], "sadness")

        # Test the fear emotion
        self.assertEqual(emotion_detector("I am really afraid that this will happen")["dominant_emotion"], "fear")

# Call the unit tests. 
unittest.main()

