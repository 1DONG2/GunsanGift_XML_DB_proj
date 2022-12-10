import csv
reader = csv.reader(open('새 폴더\\secondmodified.csv', 'r',encoding="utf-8-sig"), delimiter=",")

f=open('새 폴더\\kunsancredit.xml', 'w+', encoding="utf-8-sig")
i=0
f.write('<?xml version="1.0" encoding="utf-8"?>\n\n')

f.write('<kunsancredit>\n')
for row in reader:
      f.write('\t<store id=\"'+str(i)+'\">\n')
      f.write('\t\t<legalName>' + row[2] + '</legalName>\n')
      f.write('\t\t<category>' + row[3] + '</category>\n')
      f.write('\t\t<RoadNameAddress>' + row[4] + '</RoadNameAddress>\n')
      f.write('\t\t<LegalStatusNeighborhood>' + row[5] + '</LegalStatusNeighborhood>\n')
      f.write('\t\t<telephone>' + row[6] + '</telephone>\n')
      f.write('\t\t<AdministrativeNeighborhood>' + row[7] + '</AdministrativeNeighborhood>\n')

      f.write('\t</store>\n')
      i=i+1
f.write('</kunsancredit>')
