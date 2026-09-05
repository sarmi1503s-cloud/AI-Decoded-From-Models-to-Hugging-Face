import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

MODEL_NAME = "google/flan-t5-small"


def load_model():
    """Load the tokenizer and FLAN-T5 model."""

    print("Loading model:", MODEL_NAME)

    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

    # Use GPU if available, otherwise use CPU
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    model = model.to(device)
    model.eval()

    print("Using device:", device)

    return tokenizer, model, device


def generate_output(prompt, tokenizer, model, device):
    """Generate text from the model for a given prompt."""

    # Convert the prompt into tokens
    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=512
    )

    # Move the input to the same device as the model
    inputs = {
        key: value.to(device)
        for key, value in inputs.items()
    }

    # Generate the model's response
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=50,
            num_beams=4
        )

    # Convert the generated tokens back into text
    result = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True
    )

    return result


def run_experiments(tokenizer, model, device):
    """Run different text-to-text experiments."""

    experiments = [
        ("Translation", "translate English to French: Hello"),

        (
            "Summarization",
            "summarize: Python is a programming language "
            "used to create websites, software, automate tasks, "
            "analyze data, and develop artificial intelligence."
        ),

        (
            "Sentiment Classification",
            "classify the sentiment as positive or negative: "
            "I love this product."
        ),

        (
            "Simple Explanation",
            "Explain artificial intelligence in one short sentence."
        ),

        (
            "Question Answering",
            "Question: What is the largest planet in our solar system? "
            "Answer:"
        )
    ]

    print("\n" + "=" * 70)
    print("FLAN-T5 TEXT-TO-TEXT EXPERIMENTS")
    print("=" * 70)

    for task, prompt in experiments:
        print("\nTask:", task)
        print("Input:", prompt)

        output = generate_output(
            prompt,
            tokenizer,
            model,
            device
        )

        print("Output:", output)


def interactive_mode(tokenizer, model, device):
    """Allow the user to enter custom prompts."""

    print("\n" + "=" * 70)
    print("INTERACTIVE MODE")
    print("=" * 70)

    print("Enter your own text-to-text prompts.")
    print("Type 'exit' to stop the program.")

    while True:
        prompt = input("\nEnter prompt: ").strip()

        if prompt.lower() == "exit":
            print("Program ended.")
            break

        if not prompt:
            print("Please enter a prompt.")
            continue

        output = generate_output(
            prompt,
            tokenizer,
            model,
            device
        )

        print("Output:", output)


def main():
    # Load the model and tokenizer
    tokenizer, model, device = load_model()

    # Run the sample experiments
    run_experiments(tokenizer, model, device)

    # Allow the user to enter custom prompts
    interactive_mode(tokenizer, model, device)


if __name__ == "__main__":
    main()