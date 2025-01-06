import os
import subprocess
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Path to the sbscooker executable
SBSCookerPath = r"C:\Program Files\Adobe\Adobe Substance 3D Designer\sbscooker.exe"

# Function to validate the executable path
def validate_sbscooker_path(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"sbscooker executable not found at {path}")
    logging.info("sbscooker path validated.")

# Batch processing function
def batch_process_sbs_files(input_dir, output_dir, exclude_files=None, options=None):
    """
    Batch process .sbs files using sbscooker with filename filtering.

    :param input_dir: Directory containing input .sbs files.
    :param output_dir: Directory to save cooked files.
    :param exclude_files: List of filenames (without path) to exclude from processing.
    :param options: Additional command-line options for sbscooker.
    """
    input_dir = Path(input_dir)
    output_dir = Path(output_dir)

    # Ensure input and output directories exist
    if not input_dir.is_dir():
        raise NotADirectoryError(f"Input directory does not exist: {input_dir}")
    output_dir.mkdir(parents=True, exist_ok=True)

    logging.info(f"Starting batch processing. Input: {input_dir}, Output: {output_dir}")

    # Default options if none provided
    if options is None:
        options = []

    # Default to empty exclude list if not provided
    if exclude_files is None:
        exclude_files = []

    # Process each .sbs file in the input directory
    for sbs_file in input_dir.glob("*.sbs"):
        if sbs_file.name in exclude_files:
            logging.info(f"Skipping excluded file: {sbs_file.name}")
            continue

        logging.info(f"Processing {sbs_file.name}...")
        try:
            output_name = output_dir / f"{sbs_file.stem}.sbsar"
            command = [
                SBSCookerPath,
                "--inputs", str(sbs_file),
                "--output-path", str(output_dir),
                "--output-name", output_name.stem,
            ] + options
            subprocess.run(command, check=True)
            logging.info(f"Successfully processed {sbs_file.name} -> {output_name}")
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to process {sbs_file.name}. Error: {e}")
        except Exception as e:
            logging.error(f"Unexpected error while processing {sbs_file.name}: {e}")
