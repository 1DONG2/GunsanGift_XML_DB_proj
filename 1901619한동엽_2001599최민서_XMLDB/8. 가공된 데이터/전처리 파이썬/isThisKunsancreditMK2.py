

kunsanstore=open('새 폴더\\gunsanStore-csv.csv','r',encoding='utf-8')
kunsancredit=open('새 폴더\\secondmodified.csv','r',encoding='utf-8')

finalresult=open('새 폴더\\finalresult.csv','w',encoding='utf-8')

finalresult.write("id,legalName,category,RoadNameAddress,AdministrativeNeighborhood,isThisKunsancredit")
strings=""
a=0
kunsanstorelines=kunsanstore.readlines()
kunsancreditlines=kunsancredit.readlines()


for kunsanstoreline in kunsanstorelines:    #2중 반복, 시간복잡도는 n^2
    kunsanstoresplit = kunsanstoreline.split(',')
    for kunsancreditline in kunsancreditlines:
        kunsancreditsplit=kunsancreditline.split(',')
        if kunsancreditsplit[2]==kunsanstoresplit[1]:
            strings=kunsanstoresplit[0]+","+kunsanstoresplit[1]+","+kunsanstoresplit[2]+","+kunsanstoresplit[3]+","+kunsanstoresplit[5].replace("\n", "")+",true\n"   #만약 이름이 같을 경우 여부에 true
            finalresult.write(strings)
            a=1#그리고 true라는 것을 증명하는 a를 1로
    if a==0: #반복문이 끝날 때 까지 a가 1이 되지 않았다는 것은 군산사랑상품권 csv에 이름이 없다는 것이므로
        strings =kunsanstoresplit[0]+","+kunsanstoresplit[1]+","+kunsanstoresplit[2]+","+kunsanstoresplit[3]+","+kunsanstoresplit[5].replace("\n", "")+",false\n" #여부에 false
        finalresult.write(strings)
    a=0
#약 200만번 연산함.
#1분 30초쯤 걸리는 것 같음. 이렇게 오래 걸리는 코딩은 처음 해 봄