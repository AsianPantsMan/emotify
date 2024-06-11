from fer import FER
from fer import Video

try:
    # Load video
    vid_path = "fer_test/test_videos/ye.mp4"
    vid = Video(vid_path)

    # Process video and detect emotions
    detector = FER(mtcnn=True)
    raw_data = vid.analyze(detector, display=True)

    # Convert raw data to data frame
    df = vid.to_pandas(raw_data)

    # Display data frame
    print(df)
except:
    print("Video not found")
