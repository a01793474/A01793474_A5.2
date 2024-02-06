""" Module to read json files with numbers and generate txt file with total of sales """

import sys
import os
import time
import pandas as pd

# pylint: disable=E1101

def check_file(filename):
    """ Function to Validate file exists and is correct extention"""

    if os.path.exists((filename)):

        _, file_extension = os.path.splitext(filename)

        if file_extension != ".json":
            print("File must be json")
            return 'N'

        return 'Y'

    print("File does not exist")
    return 'N'



def create_file(path1,path2):

    """ Function to get total of sales  """

    txtfilename = "SalesResults.txt"

    data1=pd.read_json(path1).rename(columns={"Product": "title"})
    data2=pd.read_json(path2).rename(columns={"Product": "title"})

    result = pd.merge(data1, data2, how="inner",on="title")

    result["Sum"]=result["Quantity"]*result["price"]

    total = result["Sum"].sum(skipna=True,numeric_only=True)

    with open(txtfilename, 'a', encoding='utf-8') as f:
        f.write(f"Sales data from {path1} and {path2}\n")
        f.write(f"Total Sales ${total}\n")
        f.write(f"Execution time = {time.time()-init}\n")
        f.write("\n")
        f.close()

    print(f'Total Sales file {txtfilename} created.')

file_path1 = sys.argv[1]
file_path2 = sys.argv[2]

if check_file(file_path1) == 'Y' and check_file(file_path2) == 'Y':

    init = time.time()
    create_file(file_path1,file_path2)
