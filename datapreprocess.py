# import pandas as pd

# # Read the CSV file
# df = pd.read_csv('Volve production data.csv')

# # Extract the desired columns
# selected_columns = df[['AVG_DOWNHOLE_PRESSURE', 'AVG_DOWNHOLE_TEMPERATURE', 'AVG_DP_TUBING', 'BORE_OIL_VOL']]

# # Save the extracted data to a new CSV file
# selected_columns.to_csv('Volve.csv', index=False)
import pandas as pd

# Read the CSV file
df = pd.read_csv('Volve.csv')

# Convert 'BORE_OIL_VOL' column to integers, handling NaN values
df['BORE_OIL_VOL'] = pd.to_numeric(df['BORE_OIL_VOL'], errors='coerce')

# Drop rows with NaN values in 'BORE_OIL_VOL'
df = df.dropna(subset=['BORE_OIL_VOL'])

# Convert 'BORE_OIL_VOL' to integers
df['BORE_OIL_VOL'] = df['BORE_OIL_VOL'].astype(int)

# Extract the desired columns
selected_columns = df[['AVG_DOWNHOLE_PRESSURE', 'AVG_DOWNHOLE_TEMPERATURE', 'AVG_DP_TUBING', 'BORE_OIL_VOL']]

# Save the extracted data to a new CSV file
selected_columns.to_csv('Volve.csv', index=False)
