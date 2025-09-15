import pandas as pd
import re

def clean_text(text: str) -> str:
    
    if not isinstance(text, str):
        return ""
    text = text.lower()  
    text = re.sub(r'<br\s*/?>', ' ', text)  # Remove HTML line breaks
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    text = re.sub(r'\s+', ' ', text).strip()  # Remove extra whitespace
    return text

def process_data(df: pd.DataFrame) -> pd.DataFrame:
    
    print("-> Starting data processing...")
    # The IMDB dataset has 'review' and 'sentiment' columns.
    df_processed = df[['review', 'sentiment']].copy()
    df_processed['cleaned_text'] = df_processed['review'].apply(clean_text)
    print("✅ Data processing complete.")
    return df_processed