import os
import glob
from datetime import datetime
from utils.file_reader import FileReader
from utils.classifier import DocumentClassifier
from utils.report_generator import ReportGenerator
from utils.logger import DocumentLogger

class DocumentAutomationSystem:
    def __init__(self):
        self.file_reader = FileReader()
        self.classifier = DocumentClassifier()
        self.report_gen = ReportGenerator()
        self.logger = DocumentLogger()
        
        self.input_folder = "input_documents"
        self.output_base = "output"
        self.summary_folder = os.path.join(self.output_base, "summaries")
        self.category_folder = os.path.join(self.output_base, "categories")
        self.report_folder = os.path.join(self.output_base, "reports")
        
        self.create_folders()
    
    def create_folders(self):
        folders = [
            self.input_folder,
            self.summary_folder,
            self.category_folder,
            self.report_folder
        ]
        
        for folder in folders:
            if not os.path.exists(folder):
                os.makedirs(folder)
    
    def get_input_files(self):
        extensions = ['*.txt', '*.pdf', '*.docx', '*.xlsx']
        files = []
        
        for ext in extensions:
            files.extend(glob.glob(os.path.join(self.input_folder, ext)))
        
        return files
    
    def process_document(self, file_path):
        try:
            filename = os.path.basename(file_path)
            base_name = os.path.splitext(filename)[0]
            
            self.logger.log_info(f"Processing: {filename}")
            
            text = self.file_reader.read_file(file_path)
            
            if not text or len(text.strip()) < 10:
                self.logger.log_error(f"Empty or invalid content in: {filename}")
                return False
            
            category = self.classifier.classify(text)
            summary = self.report_gen.generate_summary(text)
            
            word_count = len(text.split())
            char_count = len(text)
            keywords = self.report_gen.extract_keywords(text)
            dates = self.report_gen.extract_dates(text)
            amounts = self.report_gen.extract_amounts(text)
            
            summary_content = f"Filename: {filename}\n"
            summary_content += f"Category: {category}\n"
            summary_content += f"Word Count: {word_count}\n"
            summary_content += f"Character Count: {char_count}\n"
            summary_content += f"Processing Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
            summary_content += f"\nSummary:\n{summary}\n"
            summary_content += f"\nTop Keywords: {', '.join(keywords[:10])}\n"
            if dates:
                summary_content += f"\nDates Found: {', '.join(dates)}\n"
            if amounts:
                summary_content += f"\nAmounts Found: {', '.join(amounts)}\n"
            
            summary_file = os.path.join(self.summary_folder, f"{base_name}_summary.txt")
            self.report_gen.save_text_file(summary_content, summary_file)
            
            category_file = os.path.join(self.category_folder, f"{base_name}_category.txt")
            self.report_gen.save_text_file(f"Filename: {filename}\nCategory: {category}", category_file)
            
            pdf_file = os.path.join(self.report_folder, f"{base_name}_report.pdf")
            self.report_gen.create_pdf_report(filename, text, category, summary, pdf_file)
            
            self.logger.log_document_processed(filename, category)
            
            print(f"✓ Processed: {filename}")
            print(f"  Category: {category}")
            print(f"  Summary saved: {summary_file}")
            print(f"  PDF report: {pdf_file}")
            print("-" * 50)
            
            return True
            
        except Exception as e:
            self.logger.log_error(f"Error processing {filename}: {str(e)}")
            print(f"✗ Error processing {filename}: {str(e)}")
            return False
    
    def run(self):
        print("=" * 60)
        print("DOCUMENT AUTOMATION SYSTEM")
        print("=" * 60)
        print(f"Input folder: {self.input_folder}")
        print(f"Output folder: {self.output_base}")
        print("-" * 60)
        
        files = self.get_input_files()
        
        if not files:
            print("No documents found in input_documents folder.")
            print("Supported formats: .txt, .pdf, .docx, .xlsx")
            return
        
        print(f"Found {len(files)} document(s) to process")
        print("-" * 60)
        
        processed_count = 0
        error_count = 0
        
        for file_path in files:
            if self.process_document(file_path):
                processed_count += 1
            else:
                error_count += 1
        
        print("=" * 60)
        print("PROCESSING COMPLETE")
        print(f"Total documents: {len(files)}")
        print(f"Successfully processed: {processed_count}")
        print(f"Errors: {error_count}")
        print(f"Log file: logs/document_processing_*.log")
        print("=" * 60)

if __name__ == "__main__":
    system = DocumentAutomationSystem()
    system.run()