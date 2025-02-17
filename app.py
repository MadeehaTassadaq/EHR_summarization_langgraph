import streamlit as st
from agents  import (
    demographic_agent, diagnosis_agent, encounter_progress_notes_agent,
    family_history_agent, immunization_agent, pmh_agent,
    psh_agent, social_history_agent, vitals_agent, summary_agent
)  
from agents  import app 
from fpdf import FPDF
import PyPDF2
from IPython.display import Image,display

st.set_page_config(page_title="EHR Summarization App", page_icon="📄")

st.title("EHR Summarization Application using Multi-Agent LangGraph")
html_temp = """
    <div style="background-color:yellow;padding:9px">
    <h3 style="color:black;text-align:center;">
    Summarization of Electronic Health Record (EHR) of Patient with Multi-agent Langgraph</h3>
    </div>
    """
st.markdown(html_temp,unsafe_allow_html=True)

st.markdown("""

        <style>
            .stFileUploader label {
                font-size: 40px; /* Adjust font size as needed */
            }

        </style>

    """, unsafe_allow_html=True)

# ✅ Step 1: Upload PDF File
file_uploader = st.file_uploader("Upload the Patient EHR PDF", type=["pdf"])

if file_uploader:
    pdf_reader = PyPDF2.PdfReader(file_uploader)
    extracted_text = " ".join([page.extract_text() for page in pdf_reader.pages])

    if not extracted_text:
        st.error("⚠️ No text could be extracted from the PDF. Please check the file.")
    else:
        st.success("✅ Successfully extracted text from PDF.")

    # ✅ Step 3: Process EHR Data using LangGraph
    if st.button("Summarize EHR"):
        inputs = {"messages": [extracted_text]}
        outputs = app.stream(inputs)

        results = []
        for output in outputs:
            for key, value in output.items():
                results.append(f"**{key}**:\n{value['messages'][0]}\n")

        summary = "\n".join(results)
        
        from IPython.display import Image, display

        try:
            display(Image(app.get_graph().draw_mermaid_png()))
        except Exception:
    # This requires some extra dependencies and is optional
         pass
        # ✅ Step 4: Display the Summary
        st.success("Summary Generated Successfully!")
        st.text_area("📄 EHR Summary", summary, height=400)

        # ✅ Step 5: Save Summary as PDF
        def save_summary_as_pdf(summary_text):
            pdf = FPDF()
            pdf.set_auto_page_break(auto=True, margin=15)
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(190, 10, summary_text)
            pdf.output("Patient_EHR_Summary.pdf")

        save_summary_as_pdf(summary)

        # ✅ Step 6: Provide Download Button for Summary PDF
        st.download_button(
            label="📥 Download Summary PDF",
            data=open("Patient_EHR_Summary.pdf", "rb").read(),
            file_name="Patient_EHR_Summary.pdf",
            mime="application/pdf",
        )
