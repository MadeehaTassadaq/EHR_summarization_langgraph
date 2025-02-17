# EHR_summarization_langgraph# EHR Summarization Agent App

## Overview
The **EHR Summarization Agent App** is a multi-agent system designed to extract and summarize patient information from Electronic Health Records (EHR). Built with **LangGraph** and **Streamlit**, the app structures and organizes patient data into a readable format, allowing healthcare professionals to access crucial medical insights efficiently. The extracted data is also saved in a **PDF file** for documentation purposes.

## Features
- **Multi-Agent System**: Uses structured agents to extract and summarize patient data.
- **Demographic Data Extraction**: Captures patient information such as name, age, gender, and contact details.
- **Past Medical History Extraction**: Retrieves historical medical conditions and treatments.
- **Past Surgical History Extraction**: Extracts past surgical procedures.
- **Diagnosis Agent**: Summarizes key diagnostic information.
- **Summarization Agent**: Generates a concise summary of the extracted EHR data.
- **PDF Generation**: Saves the summarized data into a structured PDF document.
- **Streamlit Web App**: Provides a user-friendly interface for data input and visualization.

## Tech Stack
- **Python**
- **LangGraph** (for multi-agent orchestration)
- **Streamlit** (for web UI)
- **Hugging Face Models** (for NLP-based extraction and summarization)
- **PDF Generation Libraries** (e.g., `reportlab`, `pdfkit`)

## Installation
1. Clone the repository:
   ```bash
   git clone [(https://github.com/MadeehaTassadaq/EHR_summarization_langgraph.git)]
   cd ehr-summarization-agent
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
2. Upload EHR data or enter details manually.
3. The system extracts and summarizes the patient information.
4. Download the generated PDF report.

## Folder Structure
```
EHR-Summarization-Agent/
│-- app.py  # Main Streamlit app
│-- agents/
│   ├── demographic_extraction.py
│   ├── medical_history_extraction.py
│   ├── surgical_history_extraction.py
│   ├── diagnosis_agent.py
│   ├── summarization_agent.py
│-- utils/
│   ├── pdf_generator.py  # Utility functions for PDF creation
│-- requirements.txt  # Dependencies
│-- README.md  # Project Documentation
```

## Future Enhancements
- Integration with **FHIR APIs** for real-time EHR data extraction.
- Adding **voice-based** patient history input.
- Implementing **LlamaIndex** for advanced search and retrieval.
- Incorporating **explainable AI (XAI)** for transparency in decision-making.

## License
This project is licensed under the MIT License.

## Contact
For any queries or collaborations, reach out to **Dr. Madeeha** on [LinkedIn]([(https://www.linkedin.com/in/dr-madeeha-tassadaq-3104aa290/)])).

---
### 🚀 Transforming Healthcare with AI! 🚀

