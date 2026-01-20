class DocumentClassifier:
    def __init__(self):
        self.hr_keywords = ['resume', 'hire', 'employee', 'salary', 'interview', 'training', 'hr', 'human resources']
        self.finance_keywords = ['invoice', 'budget', 'financial', 'revenue', 'expense', 'tax', 'audit', 'accounting', 'payment']
        self.operations_keywords = ['inventory', 'supply chain', 'logistics', 'production', 'manufacturing', 'shipping', 'delivery']
        self.legal_keywords = ['contract', 'agreement', 'compliance', 'law', 'legal', 'clause', 'terms', 'confidential']
    
    def classify(self, text):
        text_lower = text.lower()
        
        hr_score = sum(1 for keyword in self.hr_keywords if keyword in text_lower)
        finance_score = sum(1 for keyword in self.finance_keywords if keyword in text_lower)
        operations_score = sum(1 for keyword in self.operations_keywords if keyword in text_lower)
        legal_score = sum(1 for keyword in self.legal_keywords if keyword in text_lower)
        
        scores = {
            'HR': hr_score,
            'Finance': finance_score,
            'Operations': operations_score,
            'Legal': legal_score
        }
        
        max_category = max(scores, key=scores.get)
        
        if scores[max_category] == 0:
            return 'Unknown'
        
        return max_category