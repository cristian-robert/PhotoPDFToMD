# Quick Start Guide

Get started with PhotoPDFToMD in 5 minutes!

## Step 1: Install System Dependencies

### Ubuntu/Debian
```bash
sudo apt-get update
sudo apt-get install -y tesseract-ocr tesseract-ocr-ron poppler-utils
```

### macOS
```bash
brew install tesseract tesseract-lang poppler
```

## Step 2: Install Python Dependencies

```bash
pip install -r requirements.txt
```

## Step 3: Verify Installation

```bash
python3 test_setup.py
```

You should see all green checkmarks ✓

## Step 4: Convert Your First PDF

```bash
python3 pdf_to_md.py your-document.pdf output.md
```

That's it! Your converted Markdown file will be at `output.md`

## Common Use Cases

### Convert specific pages (e.g., pages 5-10)
```bash
python3 pdf_to_md.py document.pdf output.md --start-page 5 --end-page 10
```

### Convert with higher quality
```bash
python3 pdf_to_md.py document.pdf output.md --dpi 400
```

### Convert from a specific page to the end
```bash
python3 pdf_to_md.py document.pdf output.md --start-page 10
```

## Need Help?

- See full documentation in [README.md](README.md)
- View all options: `python3 pdf_to_md.py --help`
- Check [CONTRIBUTING.md](CONTRIBUTING.md) for troubleshooting tips

## What Happens During Conversion?

1. **PDF is loaded** and converted to high-resolution images
2. **Each page is analyzed** to detect if it's a photo or text
3. **Photo pages are skipped** automatically
4. **Text is extracted** from text pages using Romanian OCR
5. **Markdown file is generated** with all extracted text

## Expected Output

The generated Markdown file will have this structure:

```markdown
# your-document
*Converted from PDF pages 1-10*

## Page 1

[Extracted text from page 1...]

---

## Page 3

[Extracted text from page 3...]
(Page 2 was skipped as it was a photo)

---
```

## Tips

- Start with low page ranges to test: `--start-page 1 --end-page 3`
- If too many pages are skipped, adjust sensitivity: `--photo-threshold 0.20`
- For better OCR quality on scanned documents, use higher DPI: `--dpi 400`
- The tool works best with clear, high-quality PDF scans

Enjoy using PhotoPDFToMD! 🚀
