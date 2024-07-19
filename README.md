# python-challenge
# Pybank & PyPoll

Two different scripts written in Python that are designed to read a csv file, use its contents to conduct some calcualtions and analysis, and then output those results to the terminal as well as write them to a text file.

## Description

While spreadsheet programs such as Excel are excellent tools for analyzing datasets, there are cases where the data files are far too large for these programs to effectively handle and use for analysis.  It is these instances that programming languages such as Python can be a powerful option for handling large data files.  This repository contains two Python scripts, PybBnk and PyPoll, that demonstrate how Python can be used to handle big data, conduct calculations, and reveal potential insights.

**PyBank**, is a Python script that analyzes a financial dataset in the form of a .csv file ('budget_data.csv') and outputs the following:
* Total number of months in the dataset
* Net total amount of 'Profit/Losses' over the entire period of the dataset
* Average monnth-to-month in 'Profit/Losses' over the entire period of the dataset
* The month with the greatest increase in profits and its amount
* The month wit hthe greatest decrease in profits and its amount

These metrics are printed to the terminal and also written into a .txt file ('analysis_results.txt).

**PyPoll** is a Python script that analyzes a dataset of poll data in a .csv file ('election_data.csv') and calculates the following:
* Total number of votes cast
* A list of candidates who received votes
* The percentage of votes each candidate won
* Total number of votes each candidate won
* Winner of the election based on the popular vote

Similar to PyBank, these metrics are printed to the terminal and also written into a .txt file ('election_results.txt).

### Dependencies
The latest version of Python must be installed in order to run both scripts.

PyBank assumes the .csv file it is assigned to read is organized and formatted as follows 
* Data occupies columns with the headings 'Date', 'Profit/Losses'

PyPoll assumes the .csv file it is assigned to read is organized and formatted as follows 
* Data occupies columns with the headings 'Voted ID', 'County', and 'Candidate'


## Authors

Daniel Pineda

## Acknowledgments
PyBank and PyPoll were created as an assignment for the University of California, Irvine Data Analytics Bootcamp - June 2024 Cohort under the instruction and guidance of Melissa Engle (Instructor) and Mitchell Stone (TA).
The practical exercises and coding examples demonstrated through the bootcamp helped inform and inspire the code for this project.

In addition, the following resources were used for further reference (sections of code within each file noted in parentheses):
* [How to skip the headers when processing a csv file using Python? - Stack Overflow](https://stackoverflow.com/questions/14257373/how-to-skip-the-headers-when-processing-a-csv-file-using-python) - referenced for how to skip the header row within a read .csv file (pybank.py - line 29, pypoll.py - line 20)
* [Precision Handling in Python - GeeksforGeeks](https://www.geeksforgeeks.org/precision-handling-python) - referenced for how to leverage the round() function (pybank.py - line 64, pypoll.py - line 36)
* [How to write a text file with no any delimiter in python? - Stack Overflow](https://stackoverflow.com/questions/21173446/how-to-write-a-text-file-with-no-any-delimiter-in-python) - referenced for how to use the .write() function vs .writerow() function (pybank.py - lines 95-111, pypoll.py - lines 96-115)
* [Python | Increment value in dictionary](https://www.geeksforgeeks.org/python-increment-value-in-dictionary) - referenced for how to incrementally increase a particular key's numeric value in a dictionary (pypoll.py - line 31)
* [Python tips - How to easily convert a list to a string for display | Decalage](https://www.decalage.info/en/python/print_list) - referenced for how to use .join to display/add a list to a string (pypoll.py - line 85)
