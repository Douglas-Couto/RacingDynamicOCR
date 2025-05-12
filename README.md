# 🏁 Dynamic Racing OCR

**Dynamic Racing OCR** is a Python-based tool that extracts telemetry-style data (speed, lap time, throttle) from onboard racing videos using frame-by-frame OCR and user-defined regions.

## 🚀 Features

- Converts videos into individual frames
- Mouse-based selection of OCR regions
- Prompts for label names (e.g., Speed, LapTime)
- Saves results in both `.txt` and `.xlsx` formats
- Output is organized by label and frame, ready for merging

## 📦 Requirements

Install the required packages:

```
pip install opencv-python pillow pytesseract pandas
```

Also install [Tesseract-OCR for Windows](https://github.com/UB-Mannheim/tesseract/wiki)  
and ensure it's installed at:

```
C:\Program Files\Tesseract-OCR\tesseract.exe
```

If installed elsewhere, update the path in `ocr_processor.py`.

## 📂 Folder Structure

```
/input_videos/              # Drop videos here
/frames/{video_name}/       # Extracted frames per video
/ocr_text/{label}/          # Output folder per field (e.g., Speed)
/ocr_text/{label}/
├── {label}_results.txt     # Raw CSV-style OCR output
└── {label}_results.xlsx    # Excel file (one row per frame)
```

## ▶️ How to Run (Step-by-Step)

1. Place a video file in the `/input_videos/` folder
2. Run the program:
   ```
   python main.py
   ```
3. Select the frame number to use as reference
4. Use your mouse to draw the crop region
5. Enter a label name for the data (e.g., "Speed")
6. OCR runs on all frames using the selected region
7. Results are saved to:
   ```
   /ocr_text/{label}/{label}_results.xlsx
   ```

## 📊 Output Example

Each row in the result corresponds to a frame:

```
IMGNAME, TEXT
frame000.jpg, 178
frame001.jpg, 180
frame002.jpg, 
```

Multiple labeled outputs can be joined using `IMGNAME` as the key.

Example:

| IMGNAME     | SPEED | LAPTIME |
|-------------|--------|----------|
| frame000.jpg | 178    | 0:00.45  |
| frame001.jpg | 180    | 0:00.48  |
