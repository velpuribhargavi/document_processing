import os

def create_test_files():
    input_dir = "input_documents"
    
    if not os.path.exists(input_dir):
        os.makedirs(input_dir)
    
    files = {
        "test_report.txt": """Financial Analysis Report - Q4 2025
This report contains financial data for the fourth quarter of 2025.
Total revenue for the quarter was $2,500,000 with expenses of $1,800,000.
Net profit amounted to $700,000 after accounting for taxes.
The fiscal year ends on December 31, 2025.
Budget for next quarter is set at $3,000,000.
Payment of bonuses scheduled for January 15, 2026.
Audit completion date: February 28, 2026.""",
        
        "test_resume.pdf": """EMPLOYEE RESUME AND PROFILE
Name: John Smith
Position: Senior Manager
Department: Human Resources
Hire Date: March 15, 2023
Salary: $85,000 per year
Training Completed: Leadership Development, Compliance Training
Performance Review Date: December 10, 2025
Benefits: Health insurance, 401k matching, paid vacation
Upcoming Training: Advanced Management Skills - January 2026
Contract renewal date: March 15, 2026.""",
        
        "hr_policy.docx": """HUMAN RESOURCES POLICY DOCUMENT
This document outlines company HR policies effective January 1, 2026.
Employee leave policy allows 15 vacation days per year.
Salary reviews occur annually on employment anniversary.
Training budget per employee: $2,000 annually.
Employee benefits include health coverage worth $12,000 per year.
Recruitment process requires three interview rounds.
Onboarding process takes two weeks for new hires.
Termination procedures follow legal guidelines.""",
        
        "test_invoice.docx": """INVOICE #INV-2025-789
Date: November 30, 2025
Due Date: December 30, 2025
Client: ABC Corporation
Services: Consulting for Q4 2025
Amount: $25,000
Tax: $1,500
Total Due: $26,500
Payment Terms: Net 30
Late fee: 2% per month after due date
Contact: accounts@company.com""",
        
        "test_data.xlsx": """OPERATIONS INVENTORY REPORT
Item,Quantity,Value,Reorder Level
Product A,1500,$45,000,500
Product B,2300,$92,000,800
Product C,1800,$72,000,600
Shipping Cost: $15,000 per month
Warehouse Capacity: 10,000 units
Delivery Time: 2-3 business days
Supplier: Global Logistics Inc.
Order Date: December 15, 2025
Delivery Date: December 20, 2025"""
    }
    
    for filename, content in files.items():
        filepath = os.path.join(input_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Created: {filepath}")
    
    print("\nTest files created successfully!")
    print("Now run: python main.py")

if __name__ == "__main__":
    create_test_files()