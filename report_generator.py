import re
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
import os

class ReportGenerator:
    def __init__(self):
        self.styles = getSampleStyleSheet()
    
    def extract_dates(self, text):
        date_patterns = [
            r'\d{1,2}/\d{1,2}/\d{2,4}',
            r'\d{1,2}-\d{1,2}-\d{2,4}',
            r'\d{4}-\d{1,2}-\d{1,2}',
            r'(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{1,2},? \d{4}'
        ]
        dates = []
        for pattern in date_patterns:
            dates.extend(re.findall(pattern, text, re.IGNORECASE))
        return list(set(dates))[:5]
    
    def extract_amounts(self, text):
        amount_patterns = [
            r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?',
            r'\d{1,3}(?:,\d{3})*(?:\.\d{2})?\s*(?:USD|EUR|GBP)',
            r'\d+(?:\.\d+)?\s*(?:million|billion|thousand)',
        ]
        amounts = []
        for pattern in amount_patterns:
            amounts.extend(re.findall(pattern, text, re.IGNORECASE))
        return list(set(amounts))[:5]
    
    def extract_keywords(self, text, max_keywords=10):
        words = re.findall(r'\b[a-zA-Z]{4,}\b', text.lower())
        word_freq = {}
        for word in words:
            if word not in ['this', 'that', 'with', 'from', 'have', 'which']:
                word_freq[word] = word_freq.get(word, 0) + 1
        
        sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
        return [word for word, freq in sorted_words[:max_keywords]]
    
    def generate_summary(self, text):
        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if len(s.strip()) > 20]
        
        if len(sentences) >= 4:
            summary = sentences[0] + ". " + sentences[1] + ". " + sentences[2] + ". " + sentences[3] + "."
        elif len(sentences) > 0:
            summary = ". ".join(sentences) + "."
        else:
            summary = "Document content is insufficient for summary generation."
        
        return summary[:500]
    
    def create_pdf_report(self, filename, text, category, summary, output_path):
        doc = SimpleDocTemplate(output_path, pagesize=letter)
        story = []
        
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=self.styles['Heading1'],
            fontSize=16,
            spaceAfter=30
        )
        
        story.append(Paragraph(f"Document Analysis Report", title_style))
        story.append(Spacer(1, 12))
        
        story.append(Paragraph(f"<b>File Name:</b> {filename}", self.styles["Normal"]))
        story.append(Paragraph(f"<b>Category:</b> {category}", self.styles["Normal"]))
        story.append(Paragraph(f"<b>Processing Date:</b> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", self.styles["Normal"]))
        story.append(Spacer(1, 20))
        
        story.append(Paragraph("<b>Document Summary:</b>", self.styles["Heading2"]))
        story.append(Paragraph(summary, self.styles["Normal"]))
        story.append(Spacer(1, 20))
        
        word_count = len(text.split())
        char_count = len(text)
        
        story.append(Paragraph("<b>Document Statistics:</b>", self.styles["Heading2"]))
        stats_data = [
            ["Word Count", str(word_count)],
            ["Character Count", str(char_count)],
            ["Lines", str(len(text.split('\n')))],
            ["Processing Time", datetime.now().strftime("%H:%M:%S")]
        ]
        stats_table = Table(stats_data, colWidths=[200, 200])
        stats_table.setStyle(TableStyle([
            ('GRID', (0,0), (-1,-1), 1, colors.black),
            ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
        ]))
        story.append(stats_table)
        story.append(Spacer(1, 20))
        
        keywords = self.extract_keywords(text)
        dates = self.extract_dates(text)
        amounts = self.extract_amounts(text)
        
        story.append(Paragraph("<b>Extracted Keywords:</b>", self.styles["Heading2"]))
        story.append(Paragraph(", ".join(keywords[:15]), self.styles["Normal"]))
        story.append(Spacer(1, 20))
        
        if dates:
            story.append(Paragraph("<b>Dates Found:</b>", self.styles["Heading2"]))
            story.append(Paragraph(", ".join(dates), self.styles["Normal"]))
            story.append(Spacer(1, 20))
        
        if amounts:
            story.append(Paragraph("<b>Amounts Found:</b>", self.styles["Heading2"]))
            story.append(Paragraph(", ".join(amounts), self.styles["Normal"]))
        
        doc.build(story)
    
    def save_text_file(self, content, output_path):
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)