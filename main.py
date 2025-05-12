# main.py
import os
import pandas as pd
from utils.video_to_frames import extract_frames
from utils.ocr_processor import run_ocr_on_folder
from utils.color_analysis import analyze_colors_in_folder

# Base folders
INPUT_FOLDER = "input_videos"
FRAME_FOLDER = "frames"
OCR_OUTPUT_FOLDER = "ocr_text"
ANALYSIS_OUTPUT_FOLDER = "analysis"


def main():
    # Find all video files in input_videos
    video_files = [f for f in os.listdir(INPUT_FOLDER) if f.lower().endswith(('.mp4', '.wmv'))]

    if not video_files:
        print("No videos found in 'input_videos' folder.")
        return

    for video_file in video_files:
        print(f"\nProcessing video: {video_file}")
        video_path = os.path.join(INPUT_FOLDER, video_file)
        video_name = os.path.splitext(video_file)[0]

        # 1. Extract frames
        extract_frames(video_path, FRAME_FOLDER)
        frame_path = os.path.join(FRAME_FOLDER, video_name)

        # 2. Run OCR
        ocr_txt_path = os.path.join(OCR_OUTPUT_FOLDER, f"{video_name}.txt")
        df_ocr = run_ocr_on_folder(frame_path, ocr_txt_path)

        # 3. Ask if we should run color analysis
        run_color = input(f"Run color analysis for {video_name}? (y/n): ").strip().lower() == 'y'

        if run_color:
            df_color = analyze_colors_in_folder(frame_path)
            df_result = pd.merge(df_ocr, df_color, on='IMGNAME', how='outer')
        else:
            df_result = df_ocr

        # 4. Save final Excel
        os.makedirs(ANALYSIS_OUTPUT_FOLDER, exist_ok=True)
        output_path = os.path.join(ANALYSIS_OUTPUT_FOLDER, f"{video_name}_results.xlsx")
        #df_result.to_excel(output_path, index=False)
        print(f"Saved result to {output_path}")


if __name__ == "__main__":
    main()
