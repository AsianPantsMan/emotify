import cv2
from fer import FER
from pprint import pprint

try:
    # Load image
    img_path = "fer_test/test_images/lebomboclat.jpg"
    img = cv2.imread(img_path)

    # Process image and detect emotions
    detector = FER(mtcnn=True)
    all_emotions = detector.detect_emotions(img)
    top_emotion, score = detector.top_emotion(img)

    # Display results
    print("Processing image...")
    print("All Emotions:")
    pprint(all_emotions)
    print("Top Emotion and Score:", top_emotion)
    print("Score:", score)
except:
    print("Image not found")
