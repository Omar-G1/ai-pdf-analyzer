import streamlit as st
from pdf_reader import extract_text_from_pdf
from ai_summarizer import summarize_text
from german_compliance import add_gdpr_features

st.title("PDF Summarizer")
uploaded_file = st.file_uploader(" Lade eine PDF-Datei hoch (Upload PDF)", type="pdf")
if uploaded_file:
    # Save temporarily to process
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Process the PDF
    with st.spinner("🔍 Analysiere Dokument..."):
        text = extract_text_from_pdf("temp.pdf")
        summary = summarize_text(text)
        final_output = add_gdpr_features(summary)
    # Show results
    st.subheader("📝 Zusammenfassung:")
    st.write(final_output)

 # GDPR compliance button
    if st.button("🗑️ Daten sofort löschen (Delete Data Now)"):
        import os
        if os.path.exists("temp.pdf"):
            os.remove("temp.pdf")
        st.success("✅ Daten wurden gelöscht!")
