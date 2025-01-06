
# SubstanceBatchTools

Python library for Adobe Substance batching executables.

## Overview

**SubstanceBatchTools** is a Python library that streamlines batch processing for Adobe Substance tools. It provides modules for cooking `.sbs` files into `.sbsar` files and rendering `.sbsar` files into images using Adobe's `sbscooker` and `sbsrender` executables.

## Modules

### `Cooker`
- Handles batch processing of `.sbs` files to generate `.sbsar` files.
- Key features:
  - Exclude specific `.sbs` files using a filename filter.
  - Configurable options for the `sbscooker` executable (e.g., compression, output paths).

### `Render`
- Handles batch rendering of `.sbsar` files to images.
- Key features:
  - Exclude specific `.sbsar` files using a filename filter.
  - Organizes rendered images into subdirectories named after the `.sbsar` files (without the extension).
  - Configurable options for the `sbsrender` executable (e.g., output format, bit depth, colorspace).

## Combined Script: `CookAndRender`

The `CookAndRender.py` script combines the functionality of `Cooker` and `Render` modules to create a seamless pipeline for cooking and rendering Substance files.

### Workflow
1. **Cooking**:
   - Converts `.sbs` files into `.sbsar` files using the `Cooker` module.
   - Skips files specified in the exclude list.
   - Saves `.sbsar` files to the specified output directory.
2. **Rendering**:
   - Converts `.sbsar` files into images using the `Render` module.
   - Saves images in subdirectories named after the `.sbsar` files.
   - Skips files specified in the exclude list.

## Installation

1. Ensure Python 3.x is installed.
2. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
3. Install dependencies if required (e.g., logging).

## Usage

1. Update paths in `CookAndRender.py` for input and output directories and executable locations.
2. Customize options in the `cook_options` and `render_options` lists as needed.
3. Run the script:
   ```bash
   python CookAndRender.py
   ```

## Example Configuration

### Cooking Options
```python
cook_options = [
    "--enable-icons",
    "--compression-mode", "1",
    "--expose-output-size", "1",
    "--full", "1"
]
```

### Rendering Options
```python
render_options = [
    "--output-format", "png",
    "--output-bit-depth", "16",
    "--output-colorspace", "sRGB",
    "--png-format-compression", "best_compression"
]
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.
