# Homework Writer (Python)

This is a tiny CLI tool I made after realizing it takes forever to format and write daily class homework messages manually.

The script asks for each subject's homework, then prints a ready-to-send WhatsApp-style message in one go.

## Idea

Writing homework updates every day was repetitive and time-consuming.
So this project automates the boring part:

- Ask for homework subject by subject
- Skip empty subjects automatically
- Generate one clean, formatted homework message

## Implementation

The project has 2 Python files:

- `functions.py`
	- Contains one input function per subject (`maths`, `phy`, `chem`, etc.)
	- Each function returns a formatted line like `*Maths*: Do exercise 4`
	- Also includes `date()` and `additional()` helpers
- `homework-writer.py`
	- Imports all functions
	- Calls them in sequence
	- Builds a `results` list
	- Filters out empty responses
	- Prints final message using `"\n".join(results)`

## Setup

1. Install Python 3.8+ (if not already installed).
2. Clone the repository.
3. Open terminal in the project folder.

```bash
python homework-writer.py
```

## Example Output

```text
*Homework*
11-05-2026
*Maths*: Ex 6.2 Q1-5
*Physics*: Learn chapter 3 definitions
*English*: Write summary of poem
```

## Why This Exists

Simple reason: save time every day and avoid re-typing the same message format.

If you are a student/class monitor and send daily homework updates, this should help a lot.
