def add_gdpr_features(text):
    """
    Adds GDPR compliance disclaimer/features to the text.
    """
    compliance_note = "\n\n---\n**GDPR Compliance Notice:**\nThis document has been processed locally. No personal data was permanently stored."
    return text + compliance_note
