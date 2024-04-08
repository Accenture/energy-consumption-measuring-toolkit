import pandas as pd
import matplotlib.pyplot as plt
import mplcursors  # Import mplcursors for interactive labels

# Load data from a CSV file
data = pd.read_csv('Python_Energy_Consumption_New.csv')

# Extract the relevant columns
energy_consumed = data['Actual']
time_taken = data['TotalTime(Sec)']

# Get all the headers as a list
headers = data.columns.tolist()

# Create a scatter plot for each record
fig, ax = plt.subplots(figsize=(10, 6))
sc = ax.scatter(energy_consumed, time_taken, marker='o', color='blue', alpha=0.7)

# Set the labels for X and Y axes
ax.set_xlabel('Energy Consumed')
ax.set_ylabel('Time Taken')


# Set the title
ax.set_title('Energy Consumed vs. Time Taken')

# Create a function to generate the label text with all header values
def generate_label_text(index):
    record = data.iloc[index]
    label = 'Details ------\n'
    for header in headers:
        label += f'{header}: {record[header]}\n'
    return label

# Add interactive labels with hyperlinks to all header values
labels = [generate_label_text(index) for index in range(len(data))]
cursor = mplcursors.cursor(sc, hover=True)
cursor.connect("add", lambda sel: sel.annotation.set_text(labels[sel.target.index]))

# Show the plot
plt.grid(True)
plt.tight_layout()
plt.show()
plt.tight_layout()