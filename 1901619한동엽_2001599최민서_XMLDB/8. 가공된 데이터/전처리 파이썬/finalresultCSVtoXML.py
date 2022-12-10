import csv
reader = csv.reader(open('새 폴더\\finalresult3.csv', 'r',encoding="utf-8-sig"), delimiter=",")

f=open('새 폴더\\finalresult.xml', 'w', encoding="utf-8-sig")
i=0
f.write('<?xml version="1.0" encoding="utf-8"?>\n\n')

f.write('<kunsancredit>\n')
for row in reader:
      f.write('\t<store id=\"'+str(i)+'\" isThisKunsancredit=\"'+row[5]+'\" isThisgoodrestaurant=\"'+row[6]+'\" isThisChackanStore=\"'+row[7]+'\">\n')
      f.write('\t\t<legalName>' + row[1] + '</legalName>\n')
      f.write('\t\t<category>' + row[2] + '</category>\n')
      f.write('\t\t<RoadNameAddress>' + row[3] + '</RoadNameAddress>\n')
      f.write('\t\t<AdministrativeNeighborhood>' + row[4] + '</AdministrativeNeighborhood>\n')
      f.write('\t</store>\n')
      i=i+1
f.write('</kunsancredit>')
