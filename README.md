# PhotoPDFToMD

A Python project that transforms photo-based PDFs to Markdown (.md) files with intelligent photo detection and OCR optimized for Romanian documents.

## Features

- **Romanian OCR**: Uses Tesseract OCR with Romanian language support (`ron`) for accurate text extraction
- **Photo Detection**: Automatically detects and skips pages that contain primarily photos (not text)
- **Page Range Selection**: Process specific page intervals with `--start-page` and `--end-page` arguments
- **High Quality**: Configurable DPI for optimal text recognition
- **Batch Processing**: Convert multiple pages in a single run

## Requirements

- Python 3.8 or higher
- Tesseract OCR with Romanian language data
- poppler-utils (for PDF processing)

## Installation

### 1. Install System Dependencies

#### Ubuntu/Debian:
```bash
sudo apt-get update
sudo apt-get install -y tesseract-ocr tesseract-ocr-ron poppler-utils
```

#### macOS:
```bash
brew install tesseract tesseract-lang poppler
```

#### Windows:
- Install [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki)
- Download Romanian language data from [tessdata](https://github.com/tesseract-ocr/tessdata)
- Install [poppler](https://github.com/oschwartz10612/poppler-windows/releases/)

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

Convert an entire PDF to Markdown:
```bash
python pdf_to_md.py input.pdf output.md
```

### Process Specific Pages

Convert pages 5 to 10:
```bash
python pdf_to_md.py input.pdf output.md --start-page 5 --end-page 10
```

Convert from page 3 to the end:
```bash
python pdf_to_md.py input.pdf output.md --start-page 3
```

Convert only up to page 20:
```bash
python pdf_to_md.py input.pdf output.md --end-page 20
```

### Advanced Options

**Higher quality OCR:**
```bash
python pdf_to_md.py input.pdf output.md --dpi 400
```

**Different language (e.g., English):**
```bash
python pdf_to_md.py input.pdf output.md --language eng
```

**Adjust photo detection sensitivity:**
```bash
# More sensitive (skip more pages as photos)
python pdf_to_md.py input.pdf output.md --photo-threshold 0.10

# Less sensitive (process more pages as text)
python pdf_to_md.py input.pdf output.md --photo-threshold 0.20
```

### Help

View all available options:
```bash
python pdf_to_md.py --help
```

## How It Works

1. **PDF Loading**: Converts PDF pages to high-resolution images using pdf2image
2. **Photo Detection**: Each page is analyzed using:
   - OCR confidence scores
   - Text block detection
   - Edge detection algorithms
   - Text density calculation
3. **Text Extraction**: Pages with text content are processed with Tesseract OCR using Romanian language models
4. **Markdown Generation**: Extracted text is formatted as Markdown with page separators

## Photo Detection Algorithm

The tool uses multiple heuristics to determine if a page is primarily a photo:
- Low OCR confidence scores (< 30%)
- Minimal text blocks (< 5 blocks)
- Low text density (< 50 characters)
- High edge density (> 30%)

This ensures that photo pages are skipped while text pages are accurately processed.

## Output Format

The generated Markdown file includes:
- Document title (based on PDF filename)
- Page range information
- Individual page sections with headers
- Page separators for easy navigation

Example output:
```markdown
# Document_Name
*Converted from PDF pages 1-10*

## Page 1

[Extracted text from page 1...]

---

## Page 2

[Extracted text from page 2...]

---
```

## Troubleshooting

### "Tesseract not found" error
Make sure Tesseract is installed and in your system PATH.

### Romanian language not available
Install the Romanian language data: `sudo apt-get install tesseract-ocr-ron`

### Poor OCR quality
- Increase DPI: `--dpi 400` or `--dpi 600`
- Ensure the PDF is not too low resolution
- Check that Romanian language data is properly installed

### Too many pages being skipped
Adjust the photo threshold: `--photo-threshold 0.20` (less sensitive)

## License

This project is provided as-is for educational and personal use.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests. 
