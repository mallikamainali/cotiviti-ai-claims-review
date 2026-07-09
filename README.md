# Cotiviti AI Claims Review Assistant

## Overview

This project is a proof of concept developed for the Cotiviti assessment. The application demonstrates how Retrieval-Augmented Generation (RAG) can be used with agentic AI to support clinical claims review and payment integrity workflows. The system retrieves relevant clinical guidelines, evaluates whether a patient's documentation satisfies those guidelines, and provides a transparent recommendation to either approve the claim or flag it for human review.

## Features

- Retrieve diagnosis-specific clinical guidelines
- Analyze clinical documentation
- Identify missing required findings
- Recommend:
  - Approve
  - Flag for Review
- Explain why the recommendation was made

## Technologies

- Python
- Streamlit
- JSON Knowledge Base

## Project Structure

```
cotiviti-ai-claims-review/
│
├── app.py
├── requirements.txt
│
├── data/
│   ├── guidelines.json
│   └── sample_cases.json
│
├── utils/
│   ├── retrieve.py
│   └── reviewer.py
├── Clinical Decision Making and Pattern Recognition in Healthcare.mp4
├── Clinical Decision Making and Pattern Recognition in Healthcare.pptx
├── Clinical Decision Making and Pattern Recognition in Healthcare - Report.docx
└── README.md

```

## Installation

Clone the repository.

```bash
git clone https://github.com/mallikamainali/cotiviti-ai-claims-review.git

cd cotiviti-ai-claims-review
```

Install the required packages.

```bash
pip install -r requirements.txt
```

Run the application.

```bash
streamlit run app.py
```

## Example

### Input

Diagnosis Code

```
I21.3
```

Clinical Note

```
67-year-old male with chest pain.
ECG shows STEMI.
Troponin elevated.
Coronary angioplasty performed.
```

### Output

Recommendation

```
APPROVE
```

Explanation

```
The documentation contains all required findings to support the billed procedure.
```

## How It Works

This proof of concept follows a simple workflow:

1. The user enters a clinical note and diagnosis code.
2. The application retrieves the appropriate clinical guideline.
3. The note is compared against the required clinical findings.
4. The application determines whether documentation is complete.
5. A recommendation and explanation are displayed.

## Disclaimer

This application is a proof of concept developed for educational and demonstration purposes only. It is not intended for clinical use, medical decision-making, or real healthcare reimbursement decisions.
