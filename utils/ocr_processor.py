

# utils/ocr_processor.py
from PIL import Image
import pytesseract as pt
import os
import pandas as pd
import cv2

def run_ocr_on_folder(frames_folder, base_output_dir="ocr_text"):
    """
    Runs OCR on a selected region of the first frame in the folder.
    User selects ROI with the mouse, provides a label, and the same region is applied to all frames.
    Saves text results to a labeled folder and returns a DataFrame with IMGNAME, TEXT.
    """
    pt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    df_rows = []

    image_files = sorted(
        [f for f in os.listdir(frames_folder) if f.endswith('.jpg')],
        key=lambda x: int(''.join(filter(str.isdigit, x)))
    )
    if not image_files:
        print("No images found in folder.")
        return pd.DataFrame()

        # Let user choose which frame to use for region selection
    print(f"Found {len(image_files)} frames.")
    frame_index = int(input(f"Enter frame number to use for crop selection (0 to {len(image_files)-1}): "))
    frame_index = max(0, min(frame_index, len(image_files)-1))  # clamp to valid range
    first_img_path = os.path.join(frames_folder, image_files[frame_index])
    img = cv2.imread(first_img_path)
    roi = cv2.selectROI("Select OCR Region", img, fromCenter=False, showCrosshair=True)
    cv2.destroyWindow("Select OCR Region")

    x, y, w, h = roi
    crop_box = (x, y, x + w, y + h)
    label = input("Enter a label for this region (e.g., 'Speed', 'LapTime'): ").strip()

    # Create labeled output folder
    output_folder = os.path.join(base_output_dir, label)
    os.makedirs(output_folder, exist_ok=True)
    output_txt_path = os.path.join(output_folder, f"{label}_results.txt")
    txt_file = open(output_txt_path, "w", encoding='utf-8')

    for image_name in image_files:
        img_path = os.path.join(frames_folder, image_name)
        pil_img = Image.open(img_path)
        cropped_img = pil_img.crop(crop_box)

        text = pt.image_to_string(cropped_img).strip()

        txt_file.write(f"{image_name},{text}\n")
        df_rows.append({
            'IMGNAME': image_name,
            'TEXT': text
        })

    txt_file.close()

    df = pd.DataFrame(df_rows)
    df.to_excel(os.path.join(output_folder, f"{label}_results.xlsx"), index=False)
    return df
