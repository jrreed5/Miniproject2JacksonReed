# INF601 - Advanced Programming in Python
# Jackson Reed
# Mini Project 2

# Proper import of packages used
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Load the data into a Pandas dataframe
data = pd.read_csv('dataset/Airplane_Crashes_and_Fatalities_Since_1908.csv')

# Group the data by 'Operator' and sum the 'Fatalities' within each group
FatalitiesSum = data.groupby('Operator')['Fatalities'].sum().reset_index()

# Sort the dataframe by 'Fatalities' column in descending order and select the top 20 rows
top_10 = FatalitiesSum.sort_values(by='Fatalities', ascending=False).head(20)

# I feel like I should add that this data is 100 percent accurate,
# Aeroflot actually has over 8,000 fatalities which shocked me.

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(top_10['Operator'], top_10['Fatalities'], color='maroon')
plt.xlabel('Location')
plt.ylabel('Fatalities')
plt.title('20 Highest Fatality Air Operators to Date')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Save the image
try:
    Path("images").mkdir()
except FileExistsError:
    pass

# Save the graph as a PNG file in a folder called 'charts'
plt.savefig('images/top_10_airports_fatalities.png')

# Show the plot
plt.show()
