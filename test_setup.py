#!/usr/bin/env python3
"""
Test script to verify that all dependencies are correctly installed
"""

import sys


def test_imports():
    """Test that all required modules can be imported"""
    print("Testing imports...")
    
    try:
        import pdf2image
        print("  ✓ pdf2image")
    except ImportError as e:
        print(f"  ✗ pdf2image: {e}")
        return False
    
    try:
        import PIL
        print("  ✓ PIL (Pillow)")
    except ImportError as e:
        print(f"  ✗ PIL (Pillow): {e}")
        return False
    
    try:
        import pytesseract
        print("  ✓ pytesseract")
    except ImportError as e:
        print(f"  ✗ pytesseract: {e}")
        return False
    
    try:
        import numpy
        print("  ✓ numpy")
    except ImportError as e:
        print(f"  ✗ numpy: {e}")
        return False
    
    try:
        import cv2
        print("  ✓ opencv-python")
    except ImportError as e:
        print(f"  ✗ opencv-python: {e}")
        return False
    
    return True


def test_tesseract():
    """Test that Tesseract is installed and accessible"""
    print("\nTesting Tesseract OCR...")
    
    try:
        import pytesseract
        version = pytesseract.get_tesseract_version()
        print(f"  ✓ Tesseract version: {version}")
    except Exception as e:
        print(f"  ✗ Tesseract not found: {e}")
        print("  Please install Tesseract OCR:")
        print("    Ubuntu/Debian: sudo apt-get install tesseract-ocr")
        print("    macOS: brew install tesseract")
        return False
    
    return True


def test_romanian_language():
    """Test that Romanian language data is available"""
    print("\nTesting Romanian language support...")
    
    try:
        import pytesseract
        languages = pytesseract.get_languages()
        
        if 'ron' in languages:
            print("  ✓ Romanian (ron) language data found")
            return True
        else:
            print("  ✗ Romanian language data not found")
            print(f"  Available languages: {', '.join(languages)}")
            print("  Please install Romanian language data:")
            print("    Ubuntu/Debian: sudo apt-get install tesseract-ocr-ron")
            return False
    except Exception as e:
        print(f"  ✗ Error checking languages: {e}")
        return False


def test_poppler():
    """Test that poppler is installed (required for pdf2image)"""
    print("\nTesting poppler-utils...")
    
    import subprocess
    
    try:
        result = subprocess.run(
            ['pdftoppm', '-v'],
            capture_output=True,
            text=True
        )
        print("  ✓ poppler-utils installed")
        return True
    except FileNotFoundError:
        print("  ✗ poppler-utils not found")
        print("  Please install poppler:")
        print("    Ubuntu/Debian: sudo apt-get install poppler-utils")
        print("    macOS: brew install poppler")
        return False


def main():
    """Run all tests"""
    print("=" * 60)
    print("PhotoPDFToMD - Setup Verification")
    print("=" * 60)
    
    results = []
    
    results.append(("Python imports", test_imports()))
    results.append(("Tesseract OCR", test_tesseract()))
    results.append(("Romanian language", test_romanian_language()))
    results.append(("Poppler utils", test_poppler()))
    
    print("\n" + "=" * 60)
    print("Summary:")
    print("=" * 60)
    
    all_passed = True
    for test_name, passed in results:
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"  {status}: {test_name}")
        if not passed:
            all_passed = False
    
    print("=" * 60)
    
    if all_passed:
        print("\n✓ All tests passed! You're ready to use PhotoPDFToMD.")
        return 0
    else:
        print("\n✗ Some tests failed. Please install missing dependencies.")
        return 1


if __name__ == '__main__':
    sys.exit(main())
