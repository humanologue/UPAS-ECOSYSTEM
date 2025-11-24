import json
from datetime import datetime

class ProcessLogger:
    """Core logger for capturing AI-assisted research processes."""
    
    def __init__(self, grammar=None):
        self.grammar = grammar
        self.interactions = []
        self.metadata = {}
    
    def start_session(self, research_question, discipline="general"):
        """Start a new research session."""
        self.metadata = {
            "research_question": research_question,
            "discipline": discipline,
            "start_time": datetime.now().isoformat()
        }
        self.interactions = []
        return f"Session started: {research_question}"
    
    def log_interaction(self, prompt, response, context=None):
        """Log an AI interaction."""
        interaction = {
            "timestamp": datetime.now().isoformat(),
            "prompt": prompt,
            "response": response,
            "context": context or []
        }
        self.interactions.append(interaction)
        return f"Logged interaction {len(self.interactions)}"
    
    def generate_ep_i(self):
        """Generate a Process Entity from logged data."""
        return {
            "ep_id": f"ep_{len(self.interactions)}_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            "metadata": self.metadata,
            "interactions": self.interactions,
            "confidence_metrics": {
                "interaction_count": len(self.interactions),
                "process_completeness": min(len(self.interactions) / 10, 1.0),
                "timestamp": datetime.now().isoformat()
            }
        }
    
    def save_to_file(self, filename="process_entity.json"):
        """Save the process entity to a JSON file."""
        ep_i = self.generate_ep_i()
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(ep_i, f, indent=2, ensure_ascii=False)
        return f"Process entity saved to {filename}"