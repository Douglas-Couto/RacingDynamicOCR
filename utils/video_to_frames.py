# utils/video_to_frames.py
import cv2
import os

def extract_frames(video_path, base_output_dir):
    video_name = os.path.splitext(os.path.basename(video_path))[0]  # e.g., TaycanS
    output_dir = os.path.join(base_output_dir, video_name)
    os.makedirs(output_dir, exist_ok=True)

    vidcap = cv2.VideoCapture(video_path)
    success, image = vidcap.read()
    count = 0

    while success:
        frame_name = f"frame{count:03d}.jpg"
        cv2.imwrite(os.path.join(output_dir, frame_name), image)
        print(f"Saved {frame_name} to {output_dir}")

        success, image = vidcap.read()
        count += 1

    vidcap.release()
    print(f"Finished extracting {count} frames to {output_dir}")
