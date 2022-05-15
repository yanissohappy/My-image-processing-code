from io import StringIO
import csv, codecs, glob, os 
import xlsxwriter
import glob
import csv
import numpy as np
import pandas as pd

### merge many excel into a xlsx file with many sheets

csvfiles = glob.glob('*.csv')
        
workbook = xlsxwriter.Workbook('joined.xlsx')
# counter = 0
_fold_dict = {}
count = 1
for csv_file in csvfiles:
    # fold_num = csv_file.split("(")[-1][4]
    sheet_name = 'result_by_patient(fold ' + str(count) + ')'
    _fold_dict[sheet_name] = []
    worksheet = workbook.add_worksheet(sheet_name)
    count += 1
    with open(csv_file, 'rt', encoding='utf8') as f:
        reader = csv.reader(f)
        for r, row in enumerate(reader):
            # print(row)
            # if len(row) == 1: # title
                # continue
            _fold_dict[sheet_name].append(row)
            for c, col in enumerate(row):
                try:
                    col = float(col)
                    worksheet.write(r, c, col)
                except:
                    worksheet.write(r, c, col)
    
    # _fold_dict[sheet_name] = np.array(_fold_dict[sheet_name])
    # print(_fold_dict[sheet_name].shape)
                
sheet_name = 'avg'
worksheet = workbook.add_worksheet(sheet_name)
workbook.close()


#### 5-fold Average ####
# https://stackoverflow.com/questions/55302897/using-pandas-to-average-data-across-excel-sheets-with-matching-column-data
# df1 = pd.read_excel('joined.xlsx', sheet_name='fold_1')
# df2 = pd.read_excel('joined.xlsx', sheet_name='fold_2')
# df3 = pd.read_excel('joined.xlsx', sheet_name='fold_3')
# df4 = pd.read_excel('joined.xlsx', sheet_name='fold_4')
# df5 = pd.read_excel('joined.xlsx', sheet_name='fold_5')

# df_all = pd.concat([df1, df2, df3, df4, df5], ignore_index=True)

# print(df1)

# print(df_all.dir.mean().reset_index())