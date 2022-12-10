import csv
import re
import pandas as pd
df=pd.read_csv('새 폴더\\test2-csv.csv',encoding='utf-8')
#df.astype({"telephone":"object"})
df.astype("string",errors = 'ignore')
print(df.dtypes)


df.loc[df['LegalStatusNeighborhood'].str.contains("옥구|옥정|상평|이곡|수산|오곡|선제|어은"), 'AdministrativeNeighborhood'] = '옥구읍' #행정동이 없는 csv파일에 행정동을 추가할 때 사용함
df.loc[df['LegalStatusNeighborhood'].str.contains("옥산|남내|당북|쌍봉|금성"), 'AdministrativeNeighborhood'] = '옥산면'
df.loc[df['LegalStatusNeighborhood'].str.contains("회현|월연|금광|대정|고사|세장|학당|원우|증석"), 'AdministrativeNeighborhood'] = '회현면'
df.loc[df['LegalStatusNeighborhood'].str.contains("임피|옥정|상평|이곡|수산|오곡|선제|어은"), 'AdministrativeNeighborhood'] = '임피면'
df.loc[df['LegalStatusNeighborhood'].str.contains("서수|축동|관원|마룡|화등|금암리"), 'AdministrativeNeighborhood'] = '서수면'
df.loc[df['LegalStatusNeighborhood'].str.contains("대야|산월|보덕|지경|복교|광교|접산|죽산리"), 'AdministrativeNeighborhood'] = '대야면'
df.loc[df['LegalStatusNeighborhood'].str.contains("아동|운회|아산|통사|발산|옥석리"), 'AdministrativeNeighborhood'] = '개정면'
df.loc[df['LegalStatusNeighborhood'].str.contains("성산|성덕|둔덕|고봉|도암|여방|대명|산곡|창오리"), 'AdministrativeNeighborhood'] = '성산면'
df.loc[df['LegalStatusNeighborhood'].str.contains("나포|장상|옥곤|부곡|주곡|서포리"), 'AdministrativeNeighborhood'] = '나포면'
df.loc[df['LegalStatusNeighborhood'].str.contains("옥도|개야도|연도|어청도|선유도|무녀도|신시도|야미도|장자도|관리도|말도|비안도"), 'AdministrativeNeighborhood'] = '옥도면'
df.loc[df['LegalStatusNeighborhood'].str.contains("옥서|옥봉|선연리"), 'AdministrativeNeighborhood'] = '옥서면'
df.loc[df['LegalStatusNeighborhood'].str.contains("해망|신흥|금동"), 'AdministrativeNeighborhood'] = '해신동'
df.loc[df['LegalStatusNeighborhood'].str.contains("장미|월명|신창|중앙로1|영화|장미|선양|둔율|창성|명산|송창|개복"), 'AdministrativeNeighborhood'] = '월명동'
df.loc[df['LegalStatusNeighborhood'].str.contains("오룡|금광|삼학"), 'AdministrativeNeighborhood'] = '삼학동'
df.loc[df['LegalStatusNeighborhood'].str.contains("신풍|송풍|문화"), 'AdministrativeNeighborhood'] = '신풍동'
df.loc[df['LegalStatusNeighborhood'].str.contains("중앙로2|영|신영|죽성|평화|중|금암동"), 'AdministrativeNeighborhood'] = '중앙동'
df.loc[df['LegalStatusNeighborhood'].str.contains("중앙로3|대명|장재|미원|동흥남|서흥남동"), 'AdministrativeNeighborhood'] = '흥남동'
df.loc[df['LegalStatusNeighborhood'].str.contains("조촌|경장"), 'AdministrativeNeighborhood'] = '조촌동'
df.loc[df['LegalStatusNeighborhood'].str.contains("경암동"), 'AdministrativeNeighborhood'] = '경암동'
df.loc[df['LegalStatusNeighborhood'].str.contains("구암|내흥"), 'AdministrativeNeighborhood'] = '구암동'
df.loc[df['LegalStatusNeighborhood'].str.contains("개정|사정"), 'AdministrativeNeighborhood'] = '개정동'
df.loc[df['LegalStatusNeighborhood'].str.contains("수송|미장|지곡"), 'AdministrativeNeighborhood'] = '수송동'
df.loc[df['LegalStatusNeighborhood'].str.contains("나운1|나운 1"), 'AdministrativeNeighborhood'] = '나운 1동'
df.loc[df['LegalStatusNeighborhood'].str.contains("나운|개사"), 'AdministrativeNeighborhood'] = '나운동'
df.loc[df['LegalStatusNeighborhood'].str.contains("나운2|나운 2|나운5길"), 'AdministrativeNeighborhood'] = '나운 2동'
df.loc[df['LegalStatusNeighborhood'].str.contains("나운3|나운 3|미룡|신관"), 'AdministrativeNeighborhood'] = '나운 3동'
df.loc[df['LegalStatusNeighborhood'].str.contains("소룡|오식도|비응도"), 'AdministrativeNeighborhood'] = '소룡동'
df.loc[df['LegalStatusNeighborhood'].str.contains("산북|내초"), 'AdministrativeNeighborhood'] = '미성동'


print(df[df['AdministrativeNeighborhood'].isnull()])

df.to_csv('새 폴더\\firstmodified.csv',encoding='utf-8')

"""
value.replace(/\([^)]*\)/, "")

"""