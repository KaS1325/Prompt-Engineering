# Prompting Principles

# Principle 1: Write clear and specific instructions
# Principle 2: Give the model time to “think”


# Tactics

# Tactic 1: Use delimiters to clearly indicate distinct parts of the input
# Delimiters can be anything like: ```, """, < >, <tag> </tag>, :


def simulate_response(prompt):
    # Simulate model behavior for common tasks
    simulated_outputs = {
        "Summarize the following text:": "This is a simulated summary of the text provided.",
        "Translate to French:": "Translation (simulated): Voici votre texte traduit.",
        "Sentiment analysis of:": "Simulated sentiment: Positive."
    }
    
    for key in simulated_outputs:
        if prompt.startswith(key):
            return simulated_outputs[key]
    
    return "Simulated response: Unable to interpret the prompt."

# Example Prompts
prompts = [
    "Summarize the following text: The quick brown fox jumps over the lazy dog.",
    "Translate to French: I am learning Python programming.",
    "Sentiment analysis of: I absolutely love this product!"
]

# Generate Simulated Responses
for prompt in prompts:
    print(f"Prompt: {prompt}")
    print(f"Response: {simulate_response(prompt)}")
    print("-" * 40)
