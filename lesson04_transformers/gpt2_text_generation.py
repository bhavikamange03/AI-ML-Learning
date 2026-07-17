# Use the Hugging Face transformers library to load a small GPT-2 model and generate text from a prompt such as:
# "Artificial Intelligence is"
# Observe how changing the temperature changes the output.

# Install: pip3 install transformers torch

from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

prompt = "Artificial Intelligence is"

temperatures = [0.2, 0.5, 1.0, 1.5]

for temp in temperatures:
    print("=" * 70)
    print(f"Temperature: {temp}")
    print("=" * 70)

    result = generator(
        prompt,
        max_new_tokens=50,
        do_sample=True,
        temperature=temp
    )

    print(result[0]["generated_text"])
    print()

