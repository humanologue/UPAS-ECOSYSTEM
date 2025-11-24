#!/usr/bin/env python3
"""
Basic demonstration of UPAS-IA Framework
"""

from upas_ia.core import ProcessLogger
from upas_ia.digs.statistical import StatisticalGrammar

def main():
    print("UPAS-IA Framework Demo")
    print("=" * 50)
    
    # Initialize with statistical grammar
    grammar = StatisticalGrammar()
    logger = ProcessLogger(grammar=grammar)
    
    # Start research session
    question = "Does meditation improve focus and productivity?"
    print(f"🔬 {logger.start_session(question, 'psychology')}")
    print()
    
    # Simulate AI interactions
    interactions = [
        ("What research design should I use for this study?",
         "A pre-post test design with control group would be appropriate."),
        
        ("Which statistical test for comparing pre-post scores?",
         "Use paired t-test for normally distributed data within groups."),
        
        ("How to check normality assumption?",
         "Shapiro-Wilk test or visual inspection of Q-Q plots."),
        
        ("What sample size do I need?",
         "For medium effect size (d=0.5) with 80% power, aim for 34 participants per group.")
    ]
    
    for i, (prompt, response) in enumerate(interactions, 1):
        result = logger.log_interaction(prompt, response, ["research_design", "statistics"])
        print(f"💬 Interaction {i}: {result}")
    
    # Generate and display process entity
    ep_i = logger.generate_ep_i()
    
    print(f"\n📊 Process Entity Generated:")
    print(f"   EP ID: {ep_i['ep_id']}")
    print(f"   Research: {ep_i['metadata']['research_question']}")
    print(f"   Discipline: {ep_i['metadata']['discipline']}")
    print(f"   Interactions: {len(ep_i['interactions'])}")
    print(f"   Completeness: {ep_i['confidence_metrics']['process_completeness']:.0%}")
    
    # Save to file
    result = logger.save_to_file("demo_process.json")
    print(f"\n💾 {result}")
    print("\n✅ Demo completed successfully!")

if __name__ == "__main__":
    main()