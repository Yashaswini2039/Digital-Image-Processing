import cv2
import os

# Read the video
video = cv2.VideoCapture('C:/Users/Asus/OneDrive/Documents/CEVI/images/video.mp4')

# Get the number of frames in the video
num_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

# Create a directory to store the frames
frames_dir = 'frames'
if not os.path.exists(frames_dir):
    os.mkdir(frames_dir)

# Iterate through the frames and save them to the frames_dir directory
for i in range(num_frames):
    ret, frame = video.read()
    if not ret:
        break
    cv2.imwrite(os.path.join(frames_dir, 'frame_{}.jpg'.format(i)), frame)

# Close the video