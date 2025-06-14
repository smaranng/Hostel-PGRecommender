import pandas as pd

# Load the data from the Excel file
df = pd.read_excel("hostel_comments.xlsx")

# Shuffle the rows using pandas
df_shuffled = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Save the shuffled DataFrame back to Excel
df_shuffled.to_excel("hostel_comments_shuffled.xlsx", index=False)
