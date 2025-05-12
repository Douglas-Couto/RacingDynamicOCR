# utils/color_analysis.py
import cv2
import numpy as np
import os
import pandas as pd

def analyze_colors_in_folder(frames_folder, show_images=True):
    """
    Analyze green and red pixel percentages in each frame.
    Returns a DataFrame with IMGNAME, RED, GREEN.
    """
    lower_green = np.array([29, 89, 70])
    upper_green = np.array([60, 255, 255])
    lower_red1 = np.array([0, 50, 20])
    upper_red1 = np.array([5, 255, 255])
    lower_red2 = np.array([160, 50, 20])
    upper_red2 = np.array([180, 255, 255])

    results = []

    image_files = sorted([f for f in os.listdir(frames_folder) if f.endswith('.jpg')])

    for image_name in image_files:
        img_path = os.path.join(frames_folder, image_name)
        img = cv2.imread(img_path)
        if img is None:
            continue

        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        mask_green = cv2.inRange(hsv, lower_green, upper_green)
        mask_red1 = cv2.inRange(hsv, lower_red1, upper_red1)
        mask_red2 = cv2.inRange(hsv, lower_red2, upper_red2)
        mask_red = cv2.bitwise_or(mask_red1, mask_red2)

        green_pct = cv2.countNonZero(mask_green) / (img.size / 10)
        red_pct = cv2.countNonZero(mask_red) / (img.size / 10)

        if show_images:
            out_green = cv2.bitwise_and(img, img, mask=mask_green)
            out_red = cv2.bitwise_and(img, img, mask=mask_red)
            cv2.imshow("Original / Red / Green", np.hstack([img, out_red, out_green]))
            cv2.waitKey(1)  # Show briefly

        results.append({
            'IMGNAME': image_name,
            'RED': round(red_pct, 3),
            'GREEN': round(green_pct, 3)
        })

    cv2.destroyAllWindows()
    return pd.DataFrame(results)