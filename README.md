# Smart Resume Matcher

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![AI](https://img.shields.io/badge/AI-BERT_Transformers-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

### Overview
**Smart Resume Matcher** is an intelligent hiring assistant that goes beyond simple keyword matching. It uses **Deep Learning (BERT models)** to understand the *semantic meaning* of resumes and job descriptions, ranking candidates based on true relevance rather than just buzzwords.

> *Unlike traditional ATS (Applicant Tracking Systems) that fail if you write "ML" instead of "Machine Learning", this system understands that they are the same concept.*

---

### Key Features
 ** PDF Parsing Pipeline:** Automatically extracts text from PDF resumes using a modular loader (`pypdf`).
 ** Semantic Vectorization:** Converts text into high-dimensional vectors (384 dimensions) using the `all-MiniLM-L6-v2` Transformer model.
 ** Cosine Similarity Engine:** Mathematically calculates the angle between the Job Description vector and Resume vectors to determine relevance.
 ** Automated Analytics:** Generates **Bar Charts** for visual comparison and exports rankings to **CSV** for HR teams.

---

### Tech Stack
| Component | Technology | Description |
| :--- | :--- | :--- |
| **Language** | Python 3.x | Core Logic |
| **ML Model** | `sentence-transformers` | HuggingFace BERT for Embeddings |
| **Math** | `scikit-learn` & `numpy` | Cosine Similarity & Matrix Operations |
| **Data Processing** | `pandas` | DataFrames & CSV Export |
| **Visualization** | `matplotlib` & `seaborn` | Statistical Graphics |
| **File I/O** | `pypdf` | PDF Text Extraction |

---

###  Project Structure
```bash
Smart-Resume-Matcher/
├── 📂 resumes/              # Drop your PDF resumes here or you can upload in app
├── 📄 analytics.py          # Module for Plotting & CSV Export
├── 📄 pdf_loader.py         # Module for PDF extraction
├── 📄 smart_resume_matcher.ipynb  # MAIN NOTEBOOK (Run this)
├── 📄 main.py               # (Optional) Standalone script version
├── 📄 requirements.txt      # Dependencies
└── 📄 README.md             # Documentation
```

### Quick Start
**1. Clone the Repository**
```bash
git clone https://github.com/Kambammohankalyan/Smart-Resume-Matcher.git
cd Smart-Resume-Matcher
```
**2. Install Dependencies**
```bash
pip install -r requirements.txt
```
**3. Add Data**
  1. Create a folder named resumes (if not exists).
  2. Paste your PDF resumes into the resumes/ folder.


**4. Run the Application**
  1. run streamlit app then upload the resume file.
  2. The system will scan the folder.
  3. It will rank candidates against the Job Description.
  4. It will save a CSV report and display a visualization.


### How It Works (The Math)
1. **Tokenization:** The text is broken down into tokens (words/sub-words).
2. **Vector Embedding:** The BERT model transforms these tokens into a dense vector:
   $\mathbf{v} \in \mathbb{R}^{384}$
3. **Similarity Score:** We calculate the **Cosine Similarity** between the Job Vector ($\mathbf{A}$) and Resume Vector ($\mathbf{B}$):

$$
\text{similarity} = \cos(\theta) = \frac{\mathbf{A} \cdot \mathbf{B}}{\|\mathbf{A}\| \|\mathbf{B}\|}
$$

* **1.0:** Perfect Match (Same meaning)
* **0.0:** No correlation
