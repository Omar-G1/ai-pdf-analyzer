import datetime

def add_gdpr_features(text):
    german_summary = text.replace("summary", "Zusammenfassung")                   #replace summary with Zusammenfassung

    disclaimer = "\n\n DATENSCHUTZ: Diese Daten werden nach 24 Stunden automatisch gelöscht gemäß DSGVO."  #add disclaimer

    timestamp = datetime.datetime.now().strftime("%d.%m.%Y %H:%M Uhr")     #add timestamp

    return f"[Verarbeitet am: {timestamp}]\n{german_summary}{disclaimer}"             #return text with timestamp and disclaimer

if __name__ == "__main__":
    from ai_summarizer import summarize_text
    from pdf_reader import extract_text_from_pdf
    
    text = extract_text_from_pdf("sample_german_document.pdf")
    summary = summarize_text(text)
    final_output = add_gdpr_features(summary)
    print(final_output)
