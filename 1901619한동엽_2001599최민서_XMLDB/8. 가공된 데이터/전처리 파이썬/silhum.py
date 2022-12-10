import csv
import re
import pandas as pd


one=open('새 폴더\\1.txt','w',encoding='utf-8')
two=open('새 폴더\\2.txt','r',encoding='utf-8')
finalresult=open('새 폴더\\finalresult.csv','w',encoding='utf-8')
finalresult.write("id,legalName,category,RoadNameAddress,AdministrativeNeighborhood,isThisKunsancredit")
for i in two:
    if two.readline()=='5':
        one.write(two)





#df.loc[df['category'].str.contains("종합소매|팬시|주방|인테리어|정밀기기|의류|의복|귀금속|페인트|액세서리|가전제품|철물|음/식료품소매|애견"), 'category'] = '소매업'
#df.to_csv('새 폴더\\finalresult1.csv',encoding='utf-8')

"""
value.replace(/\([^)]*\)/, "")

"""