# Simulate the OpenAI API completion function
def get_completion(prompt):
    # Adjust the simulated response to match the summarization goal
    if "Summarize the text" in prompt:
        return (
            "Bioinformatics integrates biology, computer science, and mathematics to analyze biological data and plays a crucial role in genomics, personalized medicine, and understanding genetic variations."
        )
    return "Simulated response: Unable to process the prompt."

# Original text
text = r"""
Bioinformatics is an interdisciplinary field that combines computer science, biology, and mathematics to analyze and interpret biological data. 
With the advent of high-throughput technologies, such as next-generation sequencing, bioinformatics has become essential for processing and understanding the massive amounts of data generated in genomics, proteomics, and transcriptomics. 
Applications of bioinformatics include genome assembly, identification of gene functions, and the study of evolutionary relationships. 
Furthermore, bioinformatics plays a crucial role in personalized medicine by identifying genetic variations that influence disease susceptibility and drug response..
"""

# Original prompt
prompt = r"""
Summarize the text delimited by triple backticks \
into a single sentence.
```{text}```
"""

# Call the simulated function and print the response
response = get_completion(prompt)
print(response)
