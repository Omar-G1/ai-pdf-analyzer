def summarize_text(text):
    """
    Summarizes the provided text.
    Currently a placeholder that returns the first 500 characters.
    """
    if not text:
        return "No text to summarize."
    
    # Placeholder logic
    summary = f"**Summary (Preview):**\n{text[:500]}..."
    if len(text) > 500:
        summary += "\n\n*(Full AI summarization requires an API key or model)*"
    return summary