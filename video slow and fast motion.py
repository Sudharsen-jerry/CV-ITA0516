import cv2

def play_video(video_path, speed):
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Check if the video file was successfully opened
    if not cap.isOpened():
        print("Error: Could not open video file.")
        return

    # Read the first frame from the video
    ret, frame = cap.read()

    # Get the frame dimensions
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (frame_width, frame_height))

    while ret:
        # Display the frame
        cv2.imshow('Video', frame)

        # Write the frame to the output video
        out.write(frame)

        # Check if the user pressed the 'q' key to exit
        if cv2.waitKey(int(1000 / speed)) & 0xFF == ord('q'):
            break

        # Read the next frame
        ret, frame = cap.read()

    # Release the VideoCapture and VideoWriter objects
    cap.release()
    out.release()

    # Close all OpenCV windows
    cv2.destroyAllWindows()

# Example usage:
# Play the video in slow motion (speed=0.5)
play_video('C:\\Users\\ADMIN\\Desktop\\Computer vision\\bunny.mp4', speed=0.5)

# Play the video in normal speed (speed=1)
play_video('C:\\Users\\ADMIN\\Desktop\\Computer vision\\bunny.mp4', speed=2)

# Play the video in fast motion (speed=2)
# play_video('path/to/your/video.mp4', speed=2)
