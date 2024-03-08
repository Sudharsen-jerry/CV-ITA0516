import cv2

def play_video_in_reverse(video_path):
    # Open the video file
    video = cv2.VideoCapture(video_path)

    # Read the frames and store them in a list
    frames = []
    while True:
        ret, frame = video.read()
        if not ret:
            break
        frames.append(frame)

    # Release the video capture object
    video.release()

    # Play the frames in reverse order
    for frame in reversed(frames):
        cv2.imshow('Video in Reverse', frame)
        if cv2.waitKey(30) & 0xFF == ord('q'):  # Press 'q' to exit
            break

    # Close all OpenCV windows
    cv2.destroyAllWindows()

# Example usage:
# Provide the path to the input video
play_video_in_reverse('C:\\Users\\ADMIN\\Desktop\\Computer vision\\bunny.mp4')
