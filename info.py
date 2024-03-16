import pandas as pd
import re

file_path = '/Users/brucnoa2185/Documents/out-copy.xlsx'
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

output_file_path = '/Users/brucnoa2185/Documents/modelnumberoutput.xlsx'
df.to_excel(output_file_path, index=False, engine='openpyxl')

print('saved successfully!')