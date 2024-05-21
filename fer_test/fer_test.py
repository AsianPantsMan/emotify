import cv2
from fer import FER
from pprint import pprint

# Load image
img_path = "fer_test/test_images/ye.jpg"
img = cv2.imread(img_path)

# Process image and detect emotions
if img is None:
    print("Image not found")
else:
    print("Processing image...")

    detector = FER()
    all_emotions = detector.detect_emotions(img)
    top_emotion, score = detector.top_emotion(img)

    print("All Emotions:")
    pprint(all_emotions)
    print("Top Emotion:", top_emotion)
    print("Score:", score)
