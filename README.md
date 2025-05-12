# RacingDynamicOCR
Extract speed, lap time, and telemetry data from onboard racing videos using frame-by-frame OCR. Select regions with your mouse, label them (e.g. Speed), and get clean Excel outputs for data merging and analysis.
# 🏁 Dynamic Racing OCR

**Dynamic Racing OCR** is a Python-based tool that extracts telemetry-style data (speed, lap time, throttle) from onboard racing videos using frame-by-frame OCR and user-defined regions of interest.

## 🚀 Features

- Converts videos into individual frames
- Interactive mouse-based region selection
- Prompts for label names (e.g., Speed, LapTime)
- Saves results in both `.txt` and `.xlsx` formats
- Allows merging of multiple outputs based on frame names

## 📦 Requirements

Install required Python packages:

\`\`\`bash
pip install opencv-python pillow pytesseract pandas
\`\`\`

Also install [Tesseract-OCR for Windows](https://github.com/UB-Mannheim/tesseract/wiki)  
and ensure it's installed at:

\`\`\`
C:\Program Files\Tesseract-OCR\tesseract.exe
\`\`\`

If installed elsewhere, update the path in `ocr_processor.py`.

## 📂 Folder Structure

\`\`\`
\\/input_videos/              # Drop videos here
\\/frames/{video_name}/       # Auto-generated frames
\\/ocr_text/{label}/          # Output per label
    ├── {label}_results.txt
    └── {label}_results.xlsx
\`\`\`

## ▶️ How to Run

\`\`\`bash
python main.py
\`\`\`

1. Drop a video file into `/input_videos/`
2. Select which frame to use for cropping
3. Draw a region with your mouse (e.g., speed or time box)
4. Enter a label name when prompted
5. Results will be saved in `/ocr_text/{label}/`

## 📊 How to Use the Output

- TXT and Excel files are generated for each label
- Each row corresponds to one frame (e.g., `frame025.jpg`)
- You can merge multiple `.xlsx` files by `IMGNAME` to create full logs

Example:

| IMGNAME     | SPEED | LAPTIME |
|-------------|--------|----------|
| frame000.jpg | 178    | 0:00.45  |
| frame001.jpg | 181    | 0:00.48  |

---
