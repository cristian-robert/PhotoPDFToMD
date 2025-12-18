# Contributing to PhotoPDFToMD

Thank you for your interest in contributing to PhotoPDFToMD!

## Development Setup

1. Clone the repository:
```bash
git clone https://github.com/cristian-robert/PhotoPDFToMD.git
cd PhotoPDFToMD
```

2. Install system dependencies:
```bash
# Ubuntu/Debian
sudo apt-get install tesseract-ocr tesseract-ocr-ron poppler-utils

# macOS
brew install tesseract tesseract-lang poppler
```

3. Install Python dependencies:
```bash
pip install -r requirements.txt
```

4. Verify setup:
```bash
python3 test_setup.py
```

## Project Structure

```
PhotoPDFToMD/
├── pdf_to_md.py         # Main converter script
├── requirements.txt     # Python dependencies
├── test_setup.py        # Setup verification script
├── example_usage.py     # Usage examples
├── README.md            # User documentation
├── CONTRIBUTING.md      # This file
└── .gitignore          # Git ignore rules
```

## Code Style

- Follow PEP 8 guidelines
- Use type hints where appropriate
- Add docstrings to all public methods
- Keep functions focused and concise
- Use meaningful variable names

## Testing

Before submitting changes:

1. Run syntax check:
```bash
python3 -m py_compile pdf_to_md.py
```

2. Test with sample PDFs:
```bash
python3 pdf_to_md.py sample.pdf output.md
```

3. Verify all command-line arguments work:
```bash
python3 pdf_to_md.py sample.pdf output.md --start-page 1 --end-page 5
python3 pdf_to_md.py sample.pdf output.md --dpi 400
python3 pdf_to_md.py sample.pdf output.md --language eng
```

## Areas for Contribution

### High Priority
- Add unit tests with pytest
- Support for additional languages
- Improve photo detection accuracy
- Better handling of complex layouts (tables, columns)

### Medium Priority
- Progress bar for long conversions
- Batch processing of multiple PDFs
- GUI interface
- Docker container for easy deployment

### Low Priority
- Support for image export (extracted text areas)
- PDF metadata preservation
- Custom Markdown formatting options

## Submitting Changes

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make your changes
4. Test thoroughly
5. Commit with clear messages: `git commit -m "Add feature: description"`
6. Push to your fork: `git push origin feature/your-feature`
7. Open a Pull Request

## Photo Detection Algorithm

The current algorithm uses multiple heuristics:
1. OCR confidence scoring
2. Text block counting
3. Text density calculation
4. Edge detection analysis

These thresholds can be adjusted via class constants in `PDFToMarkdownConverter`:
- `MIN_TEXT_BLOCKS`: Minimum text blocks to consider as text page
- `MIN_OCR_CONFIDENCE`: Minimum average OCR confidence score
- `MIN_TEXT_LENGTH`: Minimum total text length
- `EDGE_DENSITY_THRESHOLD`: Maximum edge density for text pages

## Debugging Tips

Enable verbose output by modifying the converter:
```python
# Add debug prints in is_photo_page()
print(f"Text blocks: {len(text_blocks)}")
print(f"Avg confidence: {avg_confidence}")
print(f"Text length: {total_text_length}")
print(f"Edge density: {edge_density}")
```

## Questions or Issues?

- Open an issue on GitHub
- Check existing issues for solutions
- Review the README for common troubleshooting

## License

By contributing, you agree that your contributions will be licensed under the same terms as the project.
