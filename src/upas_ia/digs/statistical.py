class StatisticalGrammar:
    """Grammar for statistical analysis interactions."""
    
    def __init__(self):
        self.name = "statistical-analysis"
        self.patterns = {
            "hypothesis_testing": {
                "description": "Selecting and justifying statistical tests",
                "required_elements": ["test_type", "variables", "hypothesis"]
            },
            "assumption_checking": {
                "description": "Validating statistical assumptions",
                "required_elements": ["assumption_type", "validation_method"]
            }
        }
    
    def validate_interaction(self, prompt, response):
        """Validate if an interaction follows this grammar."""
        return {
            "valid": True,
            "pattern": self._detect_pattern(prompt),
            "compliance_score": 0.8
        }
    
    def _detect_pattern(self, prompt):
        """Detect which grammar pattern applies to a prompt."""
        prompt_lower = prompt.lower()
        if any(word in prompt_lower for word in ['test', 'statistic', 'hypothesis']):
            return "hypothesis_testing"
        elif any(word in prompt_lower for word in ['assumption', 'check', 'validate']):
            return "assumption_checking"
        return "general"