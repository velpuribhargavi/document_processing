## Automated Document Processing, Categorization & Report Generation System

## Project Overview

A Python-based automation system that processes multiple document formats, extracts text, categorizes documents using keyword-based rules, generates summaries, and produces comprehensive PDF reports. This system mimics corporate automation workflows for document management.

------------------------------------------------------------------------
## Project Structure
PROJECT_DOC/
│
├── env/
├── input_documents/
├── logs/
├── output/
├── utils/
│   ├── create_test_files.py
│   └── main.py
------------------------------------------------------------------------

## Features
Multi-format document processing (PDF, DOCX, TXT, XLSX)

Rule-based document categorization into HR, Finance, Operations, Legal, or Unknown

Automated summary generation with keyword extraction

Date and amount detection from document content

Statistical analysis (word count, character count)

------------------------------------------------------------------------
## System Requirements
Python 3.7 or higher

4GB RAM minimum

500MB free disk space

------------------------------------------------------------------------
## Installation

Install dependencies:

pip install pdfplumber python-docx openpyxl reportlab

Run the System:

python main.py

Packages:
pdfplumber - PDF processing

python-docx - Word document handling

openpyxl - Excel file processing

reportlab - PDF report generation
After running:

Summaries: output/summaries/

Categories: output/categories/

PDF Reports: output/reports/

Logs: logs/document_processor.log

--------------------------------------------------------------------------

