import pandas as pd
import json

def clean_text_columns(df):
    """Remove extra spaces and standardize text columns"""
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].str.strip().str.title()
    return df

def load_json_safe(file_path):
    """Safely load JSON with error handling"""
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File {file_path} not found")
        return {}
