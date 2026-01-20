import logging
import os
from datetime import datetime

class DocumentLogger:
    def __init__(self, log_dir="logs"):
        self.log_dir = log_dir
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        
        log_file = os.path.join(log_dir, f"document_processing_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def log_info(self, message):
        self.logger.info(message)
    
    def log_error(self, message):
        self.logger.error(message)
    
    def log_document_processed(self, filename, category, status="SUCCESS"):
        self.logger.info(f"Processed: {filename} | Category: {category} | Status: {status}")