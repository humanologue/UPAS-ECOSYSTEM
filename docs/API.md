```markdown
# API Reference

## Core Classes

### ProcessLogger

The main class for capturing AI-assisted research processes.

#### Methods

**`__init__(grammar=None)`**
- `grammar`: Optional disciplinary grammar for interaction classification

**`start_session(research_question, discipline="general")`**
Starts a new research session.
- `research_question`: Primary research question
- `discipline`: Research discipline (e.g., "psychology", "biology")

**`log_interaction(prompt, response, context=None)`**
Logs an AI interaction.
- `prompt`: User's question or prompt to AI
- `response`: AI's response
- `context`: Optional list of context tags

**`generate_ep_i()`**
Generates a Process Entity from logged data.
- Returns: EP_i dictionary with metadata and interactions

**`save_to_file(filename="process_entity.json")`**
Saves the process entity to a JSON file.
- `filename`: Output filename

#### Attributes

- `interactions`: List of logged AI interactions
- `metadata`: Session metadata including research question
- `grammar`: Active disciplinary grammar

### StatisticalGrammar

Grammar for statistical analysis interactions.

#### Methods

**`validate_interaction(prompt, response)`**
Validates if interaction follows statistical grammar patterns.

**`_detect_pattern(prompt)`**
Internal method for pattern detection.

## Data Structures

### Process Entity (EP_i)

```json
{
  "ep_id": "ep_4_20251124_191217",
  "timestamp": "2024-11-24T19:12:17.123456",
  "metadata": {
    "research_question": "Research question",
    "discipline": "discipline_name",
    "start_time": "2024-11-24T19:12:15.123456"
  },
  "interactions": [
    {
      "timestamp": "2024-11-24T19:12:15.123456",
      "prompt": "User question",
      "response": "AI response",
      "context": ["tag1", "tag2"]
    }
  ],
  "confidence_metrics": {
    "interaction_count": 4,
    "process_completeness": 0.4
  }
}

Interaction Object
json

{
  "timestamp": "ISO-8601 timestamp",
  "prompt": "User input to AI system",
  "response": "AI system response",
  "context": ["optional", "context", "tags"]
}

Usage Examples
Basic Logging
python

from upas_ia.core import ProcessLogger

logger = ProcessLogger()
logger.start_session("My research question")
logger.log_interaction("Question?", "Answer.")
ep_i = logger.generate_ep_i()

With Grammar
python

from upas_ia.core import ProcessLogger
from upas_ia.digs.statistical import StatisticalGrammar

grammar = StatisticalGrammar()
logger = ProcessLogger(grammar=grammar)
logger.start_session("Statistical analysis", "statistics")

File Operations
python

logger.save_to_file("research.json")
# File can be loaded with:
import json
with open("research.json") as f:
    ep_i = json.load(f)