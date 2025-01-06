import Cooker
import Render
import logging
import os


def ImagesFromSbsFile():
    # Define input and output directories for cooking
    work_files_dir = os.environ.get("WorkFiles", "")
    cook_input_dir = os.path.join(work_files_dir, "LayeredMaterials")
    cook_output_dir = cook_input_dir

    # Define input and output directories for rendering
    render_input_dir = cook_output_dir  # Use cooked files as input for rendering
    render_output_dir = cook_output_dir

    # Filenames to exclude (case-sensitive)
    excluded_filenames = ["MaskSelector", "Plastic", "Steel"]
    excluded_sbs_filenames = [f"{name}.sbs" for name in excluded_filenames]
    excluded_sbsar_filenames = [f"{name}.sbsar" for name in excluded_filenames]

    # Additional options for cooking and rendering
    cook_options = [
        "--enable-icons",
        "--compression-mode", "0",
        "--expose-output-size", "1",
        "--full", "0"
    ]
    render_options = [
        "--output-format", "png",
        "--output-bit-depth", "16",
        "--output-colorspace", "sRGB",
        "--png-format-compression", "best_compression",
        "--set-value", "$outputsize@11,11"  # Example for specifying output size as 2048x2048 (2^11)
    ]

    try:
        # Validate and cook .sbs files to .sbsar
        Cooker.validate_sbscooker_path(Cooker.SBSCookerPath)
        Cooker.batch_process_sbs_files(cook_input_dir, cook_output_dir, excluded_sbs_filenames, cook_options)

        # Validate and render .sbsar files to images
        Render.validate_sbsrender_path(Render.SBSRenderPath)
        output_dirs = Render.batch_render_sbsar_files(render_input_dir, render_output_dir, excluded_sbsar_filenames, render_options)
    except Exception as e:
        logging.error(f"An error occurred during CookAndRender: {e}")

    return output_dirs

if __name__ == "__main__":
    ImagesFromSbsFile()