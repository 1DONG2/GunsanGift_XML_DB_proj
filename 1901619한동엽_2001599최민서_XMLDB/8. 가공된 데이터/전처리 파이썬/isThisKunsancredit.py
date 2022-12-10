import csv
import re
import pandas as pd

kunsancredit=pd.read_csv('새 폴더\\test2-csv.csv',encoding='utf-8')
kunsanstore=pd.read_csv('새 폴더\\gunsanStore-csv.csv',encoding='utf-8')
finalresult=pd.read_csv('새 폴더\\finalresult.csv',encoding='utf-8')
#df.astype({"telephone":"object"})
print(finalresult.columns,"\n")
print(kunsanstore.columns)
print(kunsancredit.columns)


finalresult.loc[kunsanstore['legalName'].str.contains(kunsancredit['legalName']), 'legalName'] = kunsanstore['legalName']




#df.loc[df['category'].str.contains("종합소매|팬시|주방|인테리어|정밀기기|의류|의복|귀금속|페인트|액세서리|가전제품|철물|음/식료품소매|애견"), 'category'] = '소매업'
#df.to_csv('새 폴더\\finalresult1.csv',encoding='utf-8')

"""
value.replace(/\([^)]*\)/, "")

"""