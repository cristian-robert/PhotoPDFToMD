#!/usr/bin/env python3
"""
Setup script for PhotoPDFToMD
Allows installation as a package
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

setup(
    name="photopdftomd",
    version="1.0.0",
    description="Convert photo-based PDFs to Markdown with Romanian OCR support",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Cristian Robert",
    url="https://github.com/cristian-robert/PhotoPDFToMD",
    py_modules=["pdf_to_md"],
    python_requires=">=3.8",
    install_requires=[
        "pdf2image>=1.17.0",
        "Pillow>=10.4.0",
        "pytesseract>=0.3.13",
        "numpy>=1.26.4",
        "opencv-python>=4.10.0.84",
    ],
    entry_points={
        "console_scripts": [
            "pdf-to-md=pdf_to_md:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Text Processing :: Markup :: Markdown",
        "Topic :: Multimedia :: Graphics :: Capture :: Scanners",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    keywords="pdf markdown ocr romanian tesseract photo-detection",
)
