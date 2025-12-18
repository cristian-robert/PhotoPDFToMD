#!/usr/bin/env python3
"""
PhotoPDFToMD - Convert photo-based PDFs to Markdown files
Specifically designed for Romanian documents with photo detection
"""

import argparse
import sys
from pathlib import Path
from typing import List, Tuple, Optional
import numpy as np
import cv2
from PIL import Image
from pdf2image import convert_from_path
import pytesseract


class PDFToMarkdownConverter:
    """Convert PDF files to Markdown, skipping photo pages"""
    
    def __init__(self, language: str = "ron", photo_threshold: float = 0.15):
        """
        Initialize the converter
        
        Args:
            language: Tesseract language code (ron for Romanian)
            photo_threshold: Threshold for photo detection (0-1). Lower = more sensitive
        """
        self.language = language
        self.photo_threshold = photo_threshold
    
    def is_photo_page(self, image: Image.Image) -> bool:
        """
        Detect if a page is primarily a photo (vs text document)
        
        Uses edge detection and text detection to determine if page contains
        mainly photographic content
        
        Args:
            image: PIL Image of the page
            
        Returns:
            True if page appears to be a photo, False otherwise
        """
        # Convert PIL Image to OpenCV format
        img_array = np.array(image)
        if len(img_array.shape) == 3:
            gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
        else:
            gray = img_array
        
        # Try to detect text using OCR confidence
        try:
            # Get OCR data with confidence scores
            ocr_data = pytesseract.image_to_data(
                image,
                lang=self.language,
                output_type=pytesseract.Output.DICT
            )
            
            # Calculate text detection metrics
            confidences = [int(conf) for conf in ocr_data['conf'] if conf != '-1']
            text_blocks = [text for text in ocr_data['text'] if text.strip()]
            
            # Check if we have meaningful text
            if not text_blocks or len(text_blocks) < 5:
                return True  # Likely a photo if very little text detected
            
            # Calculate average confidence
            if confidences:
                avg_confidence = sum(confidences) / len(confidences)
                # Low confidence suggests photo rather than clear text
                if avg_confidence < 30:
                    return True
            
            # Calculate text density
            total_text_length = sum(len(text) for text in text_blocks)
            if total_text_length < 50:  # Very little text content
                return True
                
        except Exception as e:
            print(f"Warning: Error during text detection: {e}", file=sys.stderr)
            # If OCR fails, fall back to edge detection
            pass
        
        # Additional check: edge detection for photo characteristics
        edges = cv2.Canny(gray, 50, 150)
        edge_density = np.sum(edges > 0) / edges.size
        
        # High edge density with complex patterns suggests photo
        if edge_density > 0.3:
            return True
        
        return False
    
    def process_page(self, image: Image.Image, page_num: int) -> Optional[str]:
        """
        Process a single page and extract text
        
        Args:
            image: PIL Image of the page
            page_num: Page number for logging
            
        Returns:
            Extracted text as markdown, or None if page is a photo
        """
        # Check if page is a photo
        if self.is_photo_page(image):
            print(f"Page {page_num}: Skipped (detected as photo)")
            return None
        
        # Extract text using OCR
        print(f"Page {page_num}: Processing text...")
        try:
            text = pytesseract.image_to_string(
                image,
                lang=self.language,
                config='--psm 6'  # Assume uniform block of text
            )
            
            # Clean up the text
            text = text.strip()
            
            if not text:
                print(f"Page {page_num}: No text found")
                return None
            
            return text
            
        except Exception as e:
            print(f"Page {page_num}: Error during OCR - {e}", file=sys.stderr)
            return None
    
    def convert_pdf_to_markdown(
        self,
        pdf_path: str,
        output_path: str,
        start_page: Optional[int] = None,
        end_page: Optional[int] = None,
        dpi: int = 300
    ) -> None:
        """
        Convert a PDF file to Markdown
        
        Args:
            pdf_path: Path to input PDF file
            output_path: Path to output Markdown file
            start_page: First page to process (1-indexed), None for first page
            end_page: Last page to process (1-indexed), None for last page
            dpi: DPI for PDF rendering (higher = better quality but slower)
        """
        pdf_path = Path(pdf_path)
        if not pdf_path.exists():
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")
        
        print(f"Converting PDF: {pdf_path}")
        print(f"Output will be saved to: {output_path}")
        
        # Convert PDF pages to images
        print("Loading PDF pages...")
        try:
            # Determine page range
            first_page = start_page if start_page else None
            last_page = end_page if end_page else None
            
            images = convert_from_path(
                pdf_path,
                dpi=dpi,
                first_page=first_page,
                last_page=last_page
            )
            
            total_pages = len(images)
            actual_start = start_page if start_page else 1
            actual_end = end_page if end_page else (actual_start + total_pages - 1)
            
            print(f"Processing pages {actual_start} to {actual_end} ({total_pages} pages)")
            
        except Exception as e:
            raise RuntimeError(f"Failed to load PDF: {e}")
        
        # Process each page
        markdown_content = []
        markdown_content.append(f"# {pdf_path.stem}\n")
        markdown_content.append(f"*Converted from PDF pages {actual_start}-{actual_end}*\n\n")
        
        processed_count = 0
        skipped_count = 0
        
        for idx, image in enumerate(images, start=actual_start):
            result = self.process_page(image, idx)
            
            if result:
                markdown_content.append(f"## Page {idx}\n\n")
                markdown_content.append(result)
                markdown_content.append("\n\n---\n\n")
                processed_count += 1
            else:
                skipped_count += 1
        
        # Write output
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(''.join(markdown_content))
        
        print(f"\nConversion complete!")
        print(f"  Processed: {processed_count} pages")
        print(f"  Skipped: {skipped_count} pages (photos)")
        print(f"  Output: {output_path}")


def main():
    """Main entry point for the CLI"""
    parser = argparse.ArgumentParser(
        description="Convert photo-based PDFs to Markdown files (Romanian OCR)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Convert entire PDF
  python pdf_to_md.py input.pdf output.md
  
  # Convert specific page range
  python pdf_to_md.py input.pdf output.md --start-page 5 --end-page 10
  
  # Convert with higher quality
  python pdf_to_md.py input.pdf output.md --dpi 400
  
  # Use different language (default is Romanian)
  python pdf_to_md.py input.pdf output.md --language eng
        """
    )
    
    parser.add_argument(
        'input_pdf',
        help='Path to input PDF file'
    )
    
    parser.add_argument(
        'output_md',
        help='Path to output Markdown file'
    )
    
    parser.add_argument(
        '--start-page',
        type=int,
        default=None,
        help='First page to process (1-indexed, default: first page)'
    )
    
    parser.add_argument(
        '--end-page',
        type=int,
        default=None,
        help='Last page to process (1-indexed, default: last page)'
    )
    
    parser.add_argument(
        '--dpi',
        type=int,
        default=300,
        help='DPI for PDF rendering (default: 300, higher = better quality)'
    )
    
    parser.add_argument(
        '--language',
        type=str,
        default='ron',
        help='Tesseract language code (default: ron for Romanian)'
    )
    
    parser.add_argument(
        '--photo-threshold',
        type=float,
        default=0.15,
        help='Photo detection threshold 0-1 (default: 0.15, lower = more sensitive)'
    )
    
    args = parser.parse_args()
    
    # Validate arguments
    if args.start_page and args.start_page < 1:
        parser.error("--start-page must be >= 1")
    
    if args.end_page and args.end_page < 1:
        parser.error("--end-page must be >= 1")
    
    if args.start_page and args.end_page and args.start_page > args.end_page:
        parser.error("--start-page must be <= --end-page")
    
    if args.dpi < 72 or args.dpi > 600:
        parser.error("--dpi must be between 72 and 600")
    
    # Create converter and process
    try:
        converter = PDFToMarkdownConverter(
            language=args.language,
            photo_threshold=args.photo_threshold
        )
        
        converter.convert_pdf_to_markdown(
            pdf_path=args.input_pdf,
            output_path=args.output_md,
            start_page=args.start_page,
            end_page=args.end_page,
            dpi=args.dpi
        )
        
        return 0
        
    except KeyboardInterrupt:
        print("\nConversion interrupted by user")
        return 130
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
