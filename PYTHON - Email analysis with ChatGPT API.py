import openai

# Set your OpenAI API key
openai.api_key = "YOUR_API_KEY"

def analyze_email(email_content):
    """
    Analyzes an email's tone, sentiment, and intent using OpenAI's GPT API.

    Args:
        email_content (str): The content of the email to analyze.

    Returns:
        str: Analysis of the email's tone, sentiment, and intent.
    """
    prompt = f"""
    Analyze the following email. Provide insights on:
    1. The overall tone (e.g., formal, casual, neutral, aggressive).
    2. The sentiment (positive, negative, or neutral).
    3. The purpose or intent of the email.

    Email content:
    {email_content}

    Response:
    """
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Use "gpt-4" if available for more detailed analysis
            prompt=prompt,
            max_tokens=200,
            temperature=0.5
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Example usage
if __name__ == "__main__":
    email = """
    Dear Team,

    I hope this email finds you well. I wanted to follow up on the proposal I sent last week.
    Could you please provide your feedback by the end of the day? Let me know if you need
    additional details.

    Best regards,
    John Doe
    """
    
    analysis = analyze_email(email)
    print("Email Analysis:")
    print(analysis)
