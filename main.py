import pandas as pd

# Load the Excel file
df = pd.read_excel("Review_text_data.xlsx")

# Define the triage logic using rule-based classification
def triage_review(review_text):
    review_text_lower = review_text.lower()
    
    # Detect sentiment and related attributes
    if any(word in review_text_lower for word in ['bad', 'terrible', 'awful', 'slow', 'rude']):
        sentiment = 'Negative'
        priority = 'High'
        suggested_action = 'Escalate to manager and contact customer'
        first_reply = 'We’re very sorry to hear about your experience. Our team will look into this and get back to you shortly.'
        tags = ['Service', 'Food Quality'] if 'food' in review_text_lower or 'service' in review_text_lower else ['Service']
    
    elif any(word in review_text_lower for word in ['great', 'excellent', 'amazing', 'delicious']):
        sentiment = 'Positive'
        priority = 'Low'
        suggested_action = 'Share compliment with staff'
        first_reply = 'Thank you so much for your kind words! We’re thrilled to hear you had a great experience.'
        tags = ['Food Quality', 'Ambiance']
    
    else:
        sentiment = 'Neutral'
        priority = 'Normal'
        suggested_action = 'Log for future analysis'
        first_reply = 'Thank you for your feedback. We appreciate your thoughts and are always looking to improve.'
        tags = ['General']

    return pd.Series({
        'Sentiment': sentiment,
        'Tags': ', '.join(tags),
        'Priority': priority,
        'Suggested_Action': suggested_action,
        'First_Reply': first_reply
    })

# Apply triage function to each review
triage_results = df['Review'].apply(triage_review)

# Combine original data with triage output
output_df = pd.concat([df, triage_results], axis=1)

# Save results to a new Excel file
output_df.to_excel("review_triage_output.xlsx", index=False)

print("Triage completed. Results saved to 'review_triage_output.xlsx'.")
