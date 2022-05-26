
import os
import csv
import datetime

# create the lists that will contain re-formatted data
emp_id = []
f_name = []
l_name = []
dob = []
ssn = []
state = []

with open('employee_data.csv') as csvfile:
    """
    In csv module, csv.DictReader class behave like a regular reader but maps the information rad into a dictionary
    So each iteration of the loop produces a dictionary from string to strings
    Keys = names of the columns and Values = data of corresponding columns
    """
    raw_data = csv.DictReader(csvfile)
    
    # loop through each row, grap, reformat and store them in the new created lists
    for row in raw_data:
        # grab the id and store it
        emp_id.append(row['Emp ID']) # or row['Emp ID']

        # spplit and store the first and last name in seaprate lists
        f_name.append(row['Name'].split(" ")[0])
        l_name.append(row['Name'].split(" ")[1])
        
        #dob
        reformat_dob = datetime.datetime.strptime(row["DOB"], "%Y-%m-%d")
        reformat_dob = reformat_dob.strftime("%m/%d/%Y")

        dob.append(reformat_dob)

        #SSN
        ssn.append('***-**-' + row['SSN'].split('-')[2])

        #state
        state.append(row['State'])

new_data = zip(emp_id, f_name, l_name, dob, ssn, state)

output = os.path.join('output_file.csv')
with open(output, 'w') as csvwrite:
    clean_file = csv.writer(csvwrite, delimiter = ",")
    clean_file.writerow(['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State'])
    clean_file.writerows(new_data)