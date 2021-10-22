import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
# try:
#     from PIL import image
# except ImportError:
#     import image 
import pytesseract

def mergeInv():
    path = "GridCSVs"
    file_list = glob.glob(path + "/*.xlsx")
    count = len(file_list)
    
    excl_list = []
    excl_merged = pd.DataFrame()
    for i in range(0, int(count/2)):
        excl_list.append(pd.read_excel("GridCSVs/Data_Extraction0"+str(i+1)+".xlsx"))
        excl_list.append(pd.read_excel("GridCSVs/output"+str(i+1)+ ".xlsx"))
    

    
    

    for excl_file in excl_list:
        excl_merged = excl_merged.append(excl_file, ignore_index=True)
    excl_merged.to_excel("mergedInvoice/A.xlsx", index=False)

# mergeInv()

