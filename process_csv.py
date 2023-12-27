import csv

def read_csv_file(file_path):
    with open(file_path, 'r', newline='') as csvfile:
        # Create a CSV reader object
        csv_reader = csv.reader(csvfile)
        
        # Read the rows and extract columns
        column1, column2, column3 = [], [], []
        for row in csv_reader:
            # Assuming three columns, adjust indices as needed
            col1, col2, col3 = row[0], row[1], row[2]
            
            # Append values to respective lists
            column1.append(col1)
            column2.append(col2)
            column3.append(col3)
        
        return column1, column2, column3

# Replace 'your_file.csv' with the path to your CSV file
csv_file_path = '/workspaces/insta-followers-extract/instfollowers - version1.csv'

# Call the function to read the CSV file and get three lists for each column
col1_list, col2_list, col3_list = read_csv_file(csv_file_path)

# Print the results
#print("Column 1:", col1_list)
#print("Column 2:", col2_list)
#print("Column 3:", col3_list)
col1_list = [value for value in col1_list if value not in col3_list]
print(col1_list)