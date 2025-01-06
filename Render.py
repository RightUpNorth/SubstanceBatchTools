import os
import subprocess
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Path to the sbsrender executable
SBSRenderPath = r"C:\Program Files\Adobe\Adobe Substance 3D Designer\sbsrender.exe"

# Function to validate the executable path
def validate_sbsrender_path(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"sbsrender executable not found at {path}")
    logging.info("sbsrender path validated.")

# Batch rendering function
def batch_render_sbsar_files(input_dir, output_dir, exclude_files=None, options=None):
    """
    Batch render .sbsar files using sbsrender with filename filtering.

    :param input_dir: Directory containing input .sbsar files.
    :param output_dir: Base directory to save rendered images.
    :param exclude_files: List of filenames (without path) to exclude from processing.
    :param options: Additional command-line options for sbsrender.
    """
    input_dir = Path(input_dir)
    base_output_dir = Path(output_dir)
    output_dirs = []
    # Ensure input directory exists
    if not input_dir.is_dir():
        raise NotADirectoryError(f"Input directory does not exist: {input_dir}")
    base_output_dir.mkdir(parents=True, exist_ok=True)

    logging.info(f"Starting batch rendering. Input: {input_dir}, Output Base Directory: {base_output_dir}")

    # Default options if none provided
    if options is None:
        options = []

    # Default to empty exclude list if not provided
    if exclude_files is None:
        exclude_files = []

    # Process each .sbsar file in the input directory
    for sbsar_file in input_dir.glob("*.sbsar"):
        if sbsar_file.name in exclude_files:
            logging.info(f"Skipping excluded file: {sbsar_file.name}")
            continue

        logging.info(f"Rendering {sbsar_file.name}...")

        # Append sbsar file name (without extension) as a subdirectory
        specific_output_dir = base_output_dir / sbsar_file.stem
        specific_output_dir.mkdir(parents=True, exist_ok=True)

        output_dirs.append(specific_output_dir)

        try:
            command = [
                SBSRenderPath,
                "render",
                "--input", str(sbsar_file),
                "--output-path", str(specific_output_dir),
            ] + options
            subprocess.run(command, check=True)
            logging.info(f"Successfully rendered {sbsar_file.name} to {specific_output_dir}")
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to render {sbsar_file.name}. Error: {e}")
        except Exception as e:
            logging.error(f"Unexpected error while rendering {sbsar_file.name}: {e}")

    return output_dirs