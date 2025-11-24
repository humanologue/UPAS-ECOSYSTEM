
# Getting Started with UPAS-IA

## Quick Installation

```bash
# Clone the repository
git clone https://github.com/humanologue/UPAS-IA-FRAMEWORK
cd UPAS-IA-FRAMEWORK

# Install in development mode
pip install -e .

Your First UPAS-IA Session
Basic Usage
python

from upas_ia.core import ProcessLogger

# Initialize the process logger
logger = ProcessLogger()

# Start a research session
logger.start_session(
    research_question="Your research question here",
    discipline="your_discipline"
)

# Log AI interactions as you work
logger.log_interaction(
    "Your question to AI",
    "AI's response", 
    ["context_tag_1", "context_tag_2"]
)

# Generate and examine the process entity
ep_i = logger.generate_ep_i()
print(f"Research: {ep_i['metadata']['research_question']}")
print(f"Interactions recorded: {len(ep_i['interactions'])}")
print(f"Process completeness: {ep_i['confidence_metrics']['process_completeness']:.0%}")

# Save for audit or reproducibility
logger.save_to_file("my_research_process.json")

Using Disciplinary Grammars
python

from upas_ia.core import ProcessLogger
from upas_ia.digs.statistical import StatisticalGrammar

# Initialize with statistical grammar for better classification
grammar = StatisticalGrammar()
logger = ProcessLogger(grammar=grammar)

logger.start_session(
    research_question="Statistical analysis of treatment effects",
    discipline="medical_research"
)

# Interactions will be automatically classified
logger.log_interaction(
    "What test for comparing two groups?",
    "Use independent t-test for normally distributed data",
    ["test_selection"]
)

Running the Demo

Test the framework with the included demo:
bash

python examples/basic_demo.py

This will:

    Start a research session on cognitive training

    Simulate 4 AI interactions

    Generate a process entity (EP_i)

    Save to demo_process.json

    Demonstrate the 40% capture threshold

Project Structure
text

UPAS-IA-FRAMEWORK/
├── src/upas_ia/          # Core framework
│   ├── core.py           # ProcessLogger class
│   └── digs/             # Disciplinary grammars
├── examples/             # Usage examples
├── specs/               # Formal specifications
├── docs/                # Documentation
└── tests/               # Test suite

Next Steps

    Explore the examples in /examples directory

    Review the specifications in /specs for EP_i schema

    Run the demo to see the framework in action

    Integrate into your workflow by importing ProcessLogger

Need Help?

    Check the API Reference for detailed class documentation

    Review the specifications for data formats

    Run the demo to see practical usage