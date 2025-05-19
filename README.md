# TEXT SUMMARIZATION TOOL

*COMPANY* : CODTECH IT SOLUTIONS

*NAME* : ARVA ARAVINDA SAI

*INTERN ID*: CODF219

*DOMAIN*:ARTIFICIAL INTELLIGENCE

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTHOSH


# TEXT SUMMARIZER                                                               
  A simple and elegant Streamlit web app that transforms lengthy text into concise summaries using file upload or manual input.
  Choose between a quick highlight-style summary or a deeper, context-aware summary approach.

# FEATURES:
-  Upload support for **PDF**, **DOCX**, and **TXT** files
-  Manual text input option
-  Two summarization modes:
       - **Basic Summary** – First few important sentences
       - **Deep Thinking** – Longest and most meaningful sentences
-   Word count display for original and summary text
-   Clean, minimal UI styled with CSS
-  "Clear" button to reset inputs easily
---

# APP PREVIEW:

![OUTPUT 1](https://github.com/user-attachments/assets/dbd4dc49-2eef-477d-b055-08c8cd4054d0)

# WORKING:
![OUTPUT 2](https://github.com/user-attachments/assets/c59ef065-dc9f-4d74-88af-0eae5c935aff)
![OUTPUT 3](https://github.com/user-attachments/assets/a8a96141-eb40-4ea2-ad94-6199ef500bdc)

---

# HOW TO RUN LOCALLY:
1. Clone this repo

   git clone https://github.com/Aravinda-Sai10/Text-Summarizer.git
   cd Text-Summarizer

2. Create a virtual environment:
   
   python -m venv venv
   # Activate
   venv\Scripts\activate   # Windows
   source venv/bin/activate  # macOS/Linux
   
3. Install dependencies:
   
   pip install -r requirements.txt

4. Run the Streamlit app:
   
   streamlit run app.py

---

# FILE STRUCTURE:

text-summarizer/
│
├── app.py                  # Main Streamlit app
├── style.css               # Custom styling
├── requirements.txt        # Required Python packages
├── README.md               # documentation
└── screenshots/
    └── app_preview.png     # App interface image
    
---
# USES:

- **Academic Work**:Quickly summarize research papers, notes, or long articles.
- **Learning**: Understand key ideas from textbooks or PDFs without reading everything.
- **Business**: Condense long reports, proposals, or meeting transcripts into clear summaries.
- **Content Creation**: Extract main points from drafts or reference materials.
- **File Review**: Summarize uploaded DOCX, TXT, or PDF files in one click.
- **Daily Productivity**: Save time by reading summarized content instead of full documents.

# FUTURE ENHANCEMENTS:

-  Hugging Face transformer-based summarizer
-  Download summary as text
-  Multilingual support
-  Summary history panel
-  Mobile responsiveness

---

⭐ If you like this project, consider giving it a star on GitHub!
