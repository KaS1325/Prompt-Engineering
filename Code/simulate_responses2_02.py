# Simulate the OpenAI API completion function
def get_completion(prompt):
    # Adjust the simulated response to match the summarization goal
    if "Summarize the text" in prompt:
        return (
            "Longer and clear prompts guide models effectively, "
            "reducing irrelevant or incorrect responses."
        )
    return "Simulated response: Unable to process the prompt."

# Original text
text = r"""
You should express what you want a model to do by \
providing instructions that are as clear and \
specific as you can possibly make them. \
This will guide the model towards the desired output, \
and reduce the chances of receiving irrelevant \
or incorrect responses. Don't confuse writing a \
clear prompt with writing a short prompt. \
In many cases, longer prompts provide more clarity \
and context for the model, which can lead to \
more detailed and relevant outputs.
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


