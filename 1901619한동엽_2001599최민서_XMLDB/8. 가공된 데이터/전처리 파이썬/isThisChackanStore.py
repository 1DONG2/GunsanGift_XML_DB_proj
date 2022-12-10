



kunsanstore=open('새 폴더\\finalresult2.csv','r',encoding='utf-8')
chackanStore=open("새 폴더\\전라북도 군산시_착한가격업소 현황_20220601.csv",'r',encoding='cp949')
finalresult=open('새 폴더\\finalresult3.csv','w',encoding='utf-8')
finalresult.write("id,legalName,category,RoadNameAddress,AdministrativeNeighborhood,isThisKunsancredit,isThisgoodrestaurant,isThisChackanStore\n")
strings=""
a=0
kunsanstorelines=kunsanstore.readlines()
chackanStorelines=chackanStore.readlines()

for kunsanstoreline in kunsanstorelines:    #2중 반복, 시간복잡도는 n^2
    kunsanstoresplit = kunsanstoreline.split(',')
    for chackanStoreline in chackanStorelines:
        chackanStoresplit=chackanStoreline.split(',')
        if chackanStoresplit[2]==kunsanstoresplit[1]:
            strings=kunsanstoresplit[0]+","+kunsanstoresplit[1]+","+kunsanstoresplit[2]+","+kunsanstoresplit[3]+","+kunsanstoresplit[4]+","+kunsanstoresplit[5]+','+kunsanstoresplit[6].replace("\n", "")+",true\n"   #만약 이름이 같을 경우 여부에 true
            finalresult.write(strings)
            a=1
    if a==0:
        strings=kunsanstoresplit[0]+","+kunsanstoresplit[1]+","+kunsanstoresplit[2]+","+kunsanstoresplit[3]+","+kunsanstoresplit[4]+","+kunsanstoresplit[5]+','+kunsanstoresplit[6].replace("\n", "")+",false\n" #여부에 false
        finalresult.write(strings)
    a=0
