import csv
import re
import pandas as pd

kunsan=pd.read_csv('새 폴더\\finalresult.csv',encoding='utf-8')
print(kunsan.columns)
kunsan.drop_duplicates(subset=['legalName'])

kunsan.to_csv('새 폴더\\finalresult1.csv',encoding='utf-8')