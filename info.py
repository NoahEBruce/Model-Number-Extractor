import pandas as pd
import re

file_path = 'your file path'
sheet_name = 'Sheet1'

df = pd.read_excel(file_path, sheet_name=sheet_name)

def extract_numbers(s):
    if pd.isna(s):
        return None
    if not isinstance(s, str):
        s=str(s)
    numbers = re.findall(r'\d+', s)
    return ''.join(numbers) if numbers else None

df['Model Number'] = df['Models'].apply(lambda x: extract_numbers(x))

output_file_path = 'your file path'
df.to_excel(output_file_path, index=False, engine='openpyxl')

print('saved successfully!')
