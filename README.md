# AI DECODED: FROM MODELS TO HUGGING FACE

## 1. Project Overview

This project demonstrates how to download and run an open-source Artificial Intelligence model from Hugging Face using Python.

For this project, I selected **FLAN-T5 Small (`google/flan-t5-small`)**, a Text-to-Text model developed by Google.

The model was downloaded and executed locally using the Hugging Face Transformers library. Different text-to-text tasks were tested to observe how the model responds to different types of prompts.

---

## 2. Model Details

### Model Name

**google/flan-t5-small**

### Domain

**Text-to-Text**

### Hugging Face Source

https://huggingface.co/google/flan-t5-small

### Model Type

FLAN-T5 is an instruction-tuned version of the T5 (Text-To-Text Transfer Transformer) architecture. It can be used for different natural language processing tasks by providing suitable text prompts.

The model can perform tasks such as:

* Translation
* Summarization
* Question answering
* Classification
* Text generation
* Text transformation

---

## 3. What Problem Is the Model Designed to Solve?

FLAN-T5 is designed to handle different natural language processing tasks using a text-to-text approach.

Instead of having a separate model for every task, the task can be described using a text prompt. The model then generates a text response.

For example:

```text
translate English to French: Hello
```

The model attempts to generate the French translation as its output.

This makes the model useful for experimenting with multiple NLP tasks using a single model.

---

## 4. Why Did I Choose This Model?

I selected `google/flan-t5-small` for the following reasons:

1. It is an open-source model available on Hugging Face.
2. It belongs to the Text-to-Text domain required for this assignment.
3. It can be used for multiple NLP tasks.
4. The Small version is relatively lightweight and suitable for running on a local computer.
5. It can be easily loaded using the Python Transformers library.
6. It provides a good introduction to how Hugging Face models can be used in practical applications.

---

## 5. Real-World Application

One possible real-world application of FLAN-T5 is **automated text processing**.

For example, it can be used as part of an application that summarizes long text, classifies user feedback, translates short sentences, or answers questions.

A customer-support system could use a text-to-text model to classify customer messages or generate short responses.

---

## 6. Technologies Used

* **Python**
* **PyTorch**
* **Hugging Face Transformers**
* **SentencePiece**
* **FLAN-T5 Small**

---

## 7. Project Structure

```text
AI-Decoded-From-Models-to-Hugging-Face/
│
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

### `main.py`

Contains the Python implementation used to:

* Load the tokenizer
* Load the FLAN-T5 model
* Select CPU or GPU
* Generate model outputs
* Run different experiments
* Accept interactive user prompts

### `requirements.txt`

Contains the Python libraries required to run the project.

---

## 8. Installation and Setup

### Step 1: Clone the repository

Clone this repository to your computer.

```bash
git clone # AI DECODED: FROM MODELS TO HUGGING FACE

## 1. Project Overview

This project demonstrates how to download and run an open-source Artificial Intelligence model from Hugging Face using Python.

For this project, I selected **FLAN-T5 Small (`google/flan-t5-small`)**, a Text-to-Text model developed by Google.

The model was downloaded and executed locally using the Hugging Face Transformers library. Different text-to-text tasks were tested to observe how the model responds to different types of prompts.

---

## 2. Model Details

### Model Name

**google/flan-t5-small**

### Domain

**Text-to-Text**

### Hugging Face Source

https://huggingface.co/google/flan-t5-small

### Model Type

FLAN-T5 is an instruction-tuned version of the T5 (Text-To-Text Transfer Transformer) architecture. It can be used for different natural language processing tasks by providing suitable text prompts.

The model can perform tasks such as:

* Translation
* Summarization
* Question answering
* Classification
* Text generation
* Text transformation

---

## 3. What Problem Is the Model Designed to Solve?

FLAN-T5 is designed to handle different natural language processing tasks using a text-to-text approach.

Instead of having a separate model for every task, the task can be described using a text prompt. The model then generates a text response.

For example:

```text
translate English to French: Hello
```

The model attempts to generate the French translation as its output.

This makes the model useful for experimenting with multiple NLP tasks using a single model.

---

## 4. Why Did I Choose This Model?

I selected `google/flan-t5-small` for the following reasons:

1. It is an open-source model available on Hugging Face.
2. It belongs to the Text-to-Text domain required for this assignment.
3. It can be used for multiple NLP tasks.
4. The Small version is relatively lightweight and suitable for running on a local computer.
5. It can be easily loaded using the Python Transformers library.
6. It provides a good introduction to how Hugging Face models can be used in practical applications.

---

## 5. Real-World Application

One possible real-world application of FLAN-T5 is **automated text processing**.

For example, it can be used as part of an application that summarizes long text, classifies user feedback, translates short sentences, or answers questions.

A customer-support system could use a text-to-text model to classify customer messages or generate short responses.

---

## 6. Technologies Used

* **Python**
* **PyTorch**
* **Hugging Face Transformers**
* **SentencePiece**
* **FLAN-T5 Small**

---

## 7. Project Structure

```text
AI-Decoded-From-Models-to-Hugging-Face/
│
├── main.py
├── README.md
├── requirements.txt

```

### `main.py`

Contains the Python implementation used to:

* Load the tokenizer
* Load the FLAN-T5 model
* Select CPU or GPU
* Generate model outputs
* Run different experiments
* Accept interactive user prompts

### `requirements.txt`

Contains the Python libraries required to run the project.

---

## 8. Installation and Setup

### Step 1: Clone the repository

Clone this repository to your computer.

```bash
git clone https://github.com/sarmi1503s-cloud/AI-Decoded-From-Models-to-Hugging-Face.git
```

Then move into the project folder:

```bash
cd AI-Decoded-From-Models-to-Hugging-Face
```

### Step 2: Create a virtual environment

```bash
python -m venv venv
```

### Step 3: Activate the virtual environment

On Windows PowerShell:

```bash
venv\Scripts\activate
```

### Step 4: Install the required libraries

```bash
pip install -r requirements.txt
```

The project uses PyTorch and Hugging Face Transformers to load and run the model.

---

## 9. How to Run the Project

After activating the virtual environment, run:

```bash
python main.py
```

The program downloads/loads the model and then runs the predefined experiments.

After the experiments, an interactive mode allows the user to enter custom prompts.

Type:

```text
exit
```

to stop the program.

---

## 10. Experiments Performed

Five different text-to-text experiments were performed.

### Experiment 1: Translation

**Input:**

```text
translate English to French: Hello
```

**Observed Output:**

```text
Bonjour, j'ai l'ai l'ai l'ai l'ai l'ai l'ai l'ai l'ai l'ai l'ai l'
```

**Observation:**

The model attempted to translate the sentence, but the generated output contained repeated words and was not a correct translation.

---

### Experiment 2: Summarization

**Input:**

```text
summarize: Python is a programming language used to create websites, software, automate tasks, analyze data, and develop artificial intelligence.
```

**Observed Output:**

```text
python is a programming language used to create websites, software, automate tasks, analyze data, and develop artificial intelligence.
```

**Observation:**

The model returned almost the same content as the input instead of producing a shorter summary.

---

### Experiment 3: Sentiment Classification

**Input:**

```text
classify the sentiment as positive or negative: I love this product.
```

**Observed Output:**

```text
positive
```

**Observation:**

The model correctly identified the sentiment as positive.

---

### Experiment 4: Simple Explanation

**Input:**

```text
Explain artificial intelligence in one short sentence.
```

**Observed Output:**

```text
Artificial intelligence is an artificial intelligence.
```

**Observation:**

The model generated a repetitive answer and did not provide a meaningful explanation.

---

### Experiment 5: Question Answering

**Input:**

```text
Question: What is the largest planet in our solar system? Answer:
```

**Observed Output:**

```text
venus
```

**Expected Answer:**

```text
Jupiter
```

**Observation:**

The model produced an incorrect answer. This demonstrates that the model should not always be assumed to provide factually correct information.

---

## 11. Interactive Mode

The program also provides an interactive mode where users can enter their own prompts.

### Example Input

```text
how are you
```

### Observed Output

```text
as a child
```

This demonstrates that the model accepts user-provided prompts and generates a response, although the response may not always be meaningful or relevant.

---

## 12. Observations and Findings

During the experiments, the model successfully loaded and generated outputs for all the tested prompts.

However, the quality of the generated responses was inconsistent.

The main observations were:

* The model successfully performed sentiment classification for the tested example.
* Translation produced repetitive output.
* Summarization did not significantly shorten the input.
* The explanation task produced a repetitive response.
* The question-answering task produced an incorrect answer.
* Interactive prompts were successfully accepted and processed.
* The model was executed locally using the CPU.

These results show that successful model execution does not necessarily mean that every generated answer will be accurate or useful.

---

## 13. Challenges Faced

### Challenge 1: Installing Required Libraries

Initially, the project produced a `ModuleNotFoundError` for PyTorch.

**Solution:**

PyTorch and the required Hugging Face libraries were installed inside the Python virtual environment.

---

### Challenge 2: Slow Model Download

A larger FLAN-T5 model was considered, but downloading and loading the larger model took significantly longer.

**Solution:**

The project continued with `google/flan-t5-small`, which was more suitable for local experimentation and still satisfied the assignment requirements.

---

### Challenge 3: Incorrect or Repetitive Outputs

Some prompts produced incorrect, repetitive, or low-quality responses.

For example, the question-answering experiment returned `venus` instead of `Jupiter`.

**Solution:**

Different prompts were tested and the outputs were recorded honestly. The inconsistent results were treated as an important observation about the limitations of the small model rather than modifying the results.

---

### Challenge 4: Running on CPU

The model was executed using the CPU because a GPU was not available for the experiment.

**Solution:**

The program automatically checks whether a CUDA-compatible GPU is available. If not, it uses the CPU.

---

## 14. Limitations

The experiment demonstrated that `google/flan-t5-small` can generate text for different tasks, but it also has limitations.

The model may:

* Generate incorrect factual answers.
* Produce repetitive text.
* Fail to follow some instructions accurately.
* Produce weak summaries.
* Give irrelevant responses to open-ended prompts.

Therefore, generated results should be checked before being used in real-world applications.

---

## 15. Conclusion

This project provided practical experience with downloading and running an open-source Hugging Face model using Python.

The `google/flan-t5-small` model was successfully loaded using the Transformers library and tested with multiple text-to-text tasks.

The experiments demonstrated both the capabilities and limitations of an AI language model. While the model successfully handled some tasks, other tasks produced incorrect or repetitive outputs.

The project helped demonstrate that working with AI models involves not only running the model but also designing suitable prompts, analyzing outputs, identifying limitations, and evaluating the reliability of generated results.

Overall, this project provided a practical introduction to using Hugging Face models in Python and understanding their real-world behavior.

---

## 16. References

* Hugging Face FLAN-T5 Small Model:
  https://huggingface.co/google/flan-t5-small

* Hugging Face Transformers Documentation:
  https://huggingface.co/docs/transformers/

* PyTorch:
  https://pytorch.org/

```

Then move into the project folder:

```bash
cd AI-Decoded-From-Models-to-Hugging-Face
```

### Step 2: Create a virtual environment

```bash
python -m venv venv
```

### Step 3: Activate the virtual environment

On Windows PowerShell:

```bash
venv\Scripts\activate
```

### Step 4: Install the required libraries

```bash
pip install -r requirements.txt
```

The project uses PyTorch and Hugging Face Transformers to load and run the model.

---

## 9. How to Run the Project

After activating the virtual environment, run:

```bash
python main.py
```

The program downloads/loads the model and then runs the predefined experiments.

After the experiments, an interactive mode allows the user to enter custom prompts.

Type:

```text
exit
```

to stop the program.

---

## 10. Experiments Performed

Five different text-to-text experiments were performed.

### Experiment 1: Translation

**Input:**

```text
translate English to French: Hello
```

**Observed Output:**

```text
Bonjour, j'ai l'ai l'ai l'ai l'ai l'ai l'ai l'ai l'ai l'ai l'ai l'
```

**Observation:**

The model attempted to translate the sentence, but the generated output contained repeated words and was not a correct translation.

---

### Experiment 2: Summarization

**Input:**

```text
summarize: Python is a programming language used to create websites, software, automate tasks, analyze data, and develop artificial intelligence.
```

**Observed Output:**

```text
python is a programming language used to create websites, software, automate tasks, analyze data, and develop artificial intelligence.
```

**Observation:**

The model returned almost the same content as the input instead of producing a shorter summary.

---

### Experiment 3: Sentiment Classification

**Input:**

```text
classify the sentiment as positive or negative: I love this product.
```

**Observed Output:**

```text
positive
```

**Observation:**

The model correctly identified the sentiment as positive.

---

### Experiment 4: Simple Explanation

**Input:**

```text
Explain artificial intelligence in one short sentence.
```

**Observed Output:**

```text
Artificial intelligence is an artificial intelligence.
```

**Observation:**

The model generated a repetitive answer and did not provide a meaningful explanation.

---

### Experiment 5: Question Answering

**Input:**

```text
Question: What is the largest planet in our solar system? Answer:
```

**Observed Output:**

```text
venus
```

**Expected Answer:**

```text
Jupiter
```

**Observation:**

The model produced an incorrect answer. This demonstrates that the model should not always be assumed to provide factually correct information.

---

## 11. Interactive Mode

The program also provides an interactive mode where users can enter their own prompts.

### Example Input

```text
how are you
```

### Observed Output

```text
as a child
```

This demonstrates that the model accepts user-provided prompts and generates a response, although the response may not always be meaningful or relevant.

---

## 12. Observations and Findings

During the experiments, the model successfully loaded and generated outputs for all the tested prompts.

However, the quality of the generated responses was inconsistent.

The main observations were:

* The model successfully performed sentiment classification for the tested example.
* Translation produced repetitive output.
* Summarization did not significantly shorten the input.
* The explanation task produced a repetitive response.
* The question-answering task produced an incorrect answer.
* Interactive prompts were successfully accepted and processed.
* The model was executed locally using the CPU.

These results show that successful model execution does not necessarily mean that every generated answer will be accurate or useful.

---

## 13. Challenges Faced

### Challenge 1: Installing Required Libraries

Initially, the project produced a `ModuleNotFoundError` for PyTorch.

**Solution:**

PyTorch and the required Hugging Face libraries were installed inside the Python virtual environment.

---

### Challenge 2: Slow Model Download

A larger FLAN-T5 model was considered, but downloading and loading the larger model took significantly longer.

**Solution:**

The project continued with `google/flan-t5-small`, which was more suitable for local experimentation and still satisfied the assignment requirements.

---

### Challenge 3: Incorrect or Repetitive Outputs

Some prompts produced incorrect, repetitive, or low-quality responses.

For example, the question-answering experiment returned `venus` instead of `Jupiter`.

**Solution:**

Different prompts were tested and the outputs were recorded honestly. The inconsistent results were treated as an important observation about the limitations of the small model rather than modifying the results.

---

### Challenge 4: Running on CPU

The model was executed using the CPU because a GPU was not available for the experiment.

**Solution:**

The program automatically checks whether a CUDA-compatible GPU is available. If not, it uses the CPU.

---

## 14. Limitations

The experiment demonstrated that `google/flan-t5-small` can generate text for different tasks, but it also has limitations.

The model may:

* Generate incorrect factual answers.
* Produce repetitive text.
* Fail to follow some instructions accurately.
* Produce weak summaries.
* Give irrelevant responses to open-ended prompts.

Therefore, generated results should be checked before being used in real-world applications.

---

## 15. Conclusion

This project provided practical experience with downloading and running an open-source Hugging Face model using Python.

The `google/flan-t5-small` model was successfully loaded using the Transformers library and tested with multiple text-to-text tasks.

The experiments demonstrated both the capabilities and limitations of an AI language model. While the model successfully handled some tasks, other tasks produced incorrect or repetitive outputs.

The project helped demonstrate that working with AI models involves not only running the model but also designing suitable prompts, analyzing outputs, identifying limitations, and evaluating the reliability of generated results.

Overall, this project provided a practical introduction to using Hugging Face models in Python and understanding their real-world behavior.

---

## 16. References

* Hugging Face FLAN-T5 Small Model:
  https://huggingface.co/google/flan-t5-small

* Hugging Face Transformers Documentation:
  https://huggingface.co/docs/transformers/

* PyTorch:
  https://pytorch.org/
