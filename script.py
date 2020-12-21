##Imports
import pandas as pd 
import numpy as np 
import os
import subprocess


##Define function
def call_batch_file():
    ##Define path to check existance of and batch file to execute if True
    path_exists = r'C:\Users\Chris\scripts\github\05_if_exists_call_bat_file\source\file_to_be_moved.txt'
    batch_file = r'C:\Users\Chris\scripts\github\move.bat'

    ##Check if file exists and call .bat file if True
    if os.path.exists(path_exists):
        print(f"File exists: executing {batch_file}")
        subprocess.call([batch_file])
        print("File moved successfuly")
    else:
        print("File does not exist")

##Call function       
call_batch_file()