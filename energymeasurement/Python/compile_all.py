import sys
import os
from subprocess import Popen, PIPE, call
import pandas as pd
import matplotlib.pyplot as plt
import mplcursors  # Import mplcursors for interactive labels

path = '.'
action = 'compile'

def file_exists(file_path):
    if not file_path:
        return False
    else:
        return os.path.isfile(file_path)

def main():
    for root, dirs, files in os.walk(path):
       
        
        # Check if the directory name is 'binary-trees'
        if os.path.basename(root) == 'binary-trees':
            # print('Executing code in folder ' + root)
            makefile = os.path.join(root, "Makefile")
            if file_exists(makefile):
                cmd = 'cd ' + root + '; make ' + action
                # cmd = 'ls -la'
                pipes = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE, text=True)
                std_out, std_err = pipes.communicate()

                if (action == 'compile') or (action == 'run'):
                    if pipes.returncode != 0:
                        # an error happened!
                        err_msg = "%s. Code: %s" % (std_err.strip(), pipes.returncode)
                        print('[E] Error on ' + root + ': ')
                        print(err_msg)
                    elif len(std_err):
                        # return code is 0 (no error), but we may want to
                        # do something with the info on std_err
                        # i.e. logger.warning(std_err)
                        print('[OK]')
                    else:
                        print('[OK]')
                if action == 'measure':
                    call(['sleep', '1'])
                    print('Measuring energy for ' + root)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        act = sys.argv[1]
        if (act == 'compile') or (act == 'run') or (act == 'clean') or (act == 'measure') or (act == 'visualize'):
            print('Performing "' + act + '" action...')
            action = act
            if(act == 'visualize'):
               # Load data from a CSV file
               data = pd.read_csv('Python_Energy_Consumption.csv')

               # Extract the relevant columns
               #energy_consumed = data['Actual']
               energy_consumed = data['Actual'].str.rstrip('J').astype(float)
               time_taken = data['TotalTime(Sec)']

               # Get all the headers as a list
               headers = data.columns.tolist()

               # Create a scatter plot for each record
               fig, ax = plt.subplots(figsize=(10, 6))
               sc = ax.scatter(energy_consumed, time_taken, marker='o', color='blue', alpha=0.7)

               # Set the labels for X and Y axes
               ax.set_xlabel('Energy Consumed (Joules)')
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
  
        else:
            print('Error: Unrecognized action "' + act + '"')
            sys.exit(1)
    else:
        print('Performing "compile" action...')
        action = 'compile'

    main()
