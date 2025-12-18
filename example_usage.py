#!/usr/bin/env python3
"""
Example usage of the PDF to Markdown converter
This demonstrates how to use the converter programmatically
"""

from pdf_to_md import PDFToMarkdownConverter


def example_basic_conversion():
    """Basic conversion example"""
    print("Example 1: Basic Conversion")
    print("-" * 40)
    
    converter = PDFToMarkdownConverter(language='ron')
    
    # Convert entire PDF
    converter.convert_pdf_to_markdown(
        pdf_path='input.pdf',
        output_path='output.md'
    )
    
    print()


def example_page_range():
    """Convert specific page range"""
    print("Example 2: Page Range Conversion")
    print("-" * 40)
    
    converter = PDFToMarkdownConverter(language='ron')
    
    # Convert pages 5-10
    converter.convert_pdf_to_markdown(
        pdf_path='input.pdf',
        output_path='output_pages_5_10.md',
        start_page=5,
        end_page=10
    )
    
    print()


def example_high_quality():
    """High quality conversion with custom settings"""
    print("Example 3: High Quality Conversion")
    print("-" * 40)
    
    # Create converter with custom photo threshold
    converter = PDFToMarkdownConverter(
        language='ron',
        photo_threshold=0.12  # More sensitive photo detection
    )
    
    # Convert with higher DPI for better quality
    converter.convert_pdf_to_markdown(
        pdf_path='input.pdf',
        output_path='output_hq.md',
        dpi=400
    )
    
    print()


def example_from_middle():
    """Convert from a specific page to the end"""
    print("Example 4: Convert From Middle to End")
    print("-" * 40)
    
    converter = PDFToMarkdownConverter(language='ron')
    
    # Convert from page 10 to the end
    converter.convert_pdf_to_markdown(
        pdf_path='input.pdf',
        output_path='output_from_10.md',
        start_page=10
    )
    
    print()


if __name__ == '__main__':
    print("=" * 60)
    print("PhotoPDFToMD - Usage Examples")
    print("=" * 60)
    print()
    
    print("These are example code snippets.")
    print("Modify the PDF paths to match your files.")
    print()
    
    # Uncomment the example you want to run:
    
    # example_basic_conversion()
    # example_page_range()
    # example_high_quality()
    # example_from_middle()
    
    print("To run these examples, uncomment the function calls above.")
    print("Or use the CLI: python pdf_to_md.py input.pdf output.md")
