import random
import xml.etree.ElementTree as ET


FILENAME = "REQUEST.xml"    # output file name
LINES = 140              # lines printed


infile_n = open("list_names.txt", "r")
lines_n = infile_n.readlines()

infile_s = open("list_surnames.txt", "r")
lines_s = infile_s.readlines()

data = ET.Element('dataroot')

list_n = []
list_s = []
vett = []
i = 0

while i < LINES:
    name = lines_n[random.randint(0,len(lines_n))].strip()
    surname = lines_s[random.randint(0,len(lines_s))].strip()
    if name in list_n or surname in list_s:
        continue
    
    list_n.append(name)
    list_s.append(surname)  
        
    min = (random.randint(0, 57) + 54) * 10  #numero mezz'ore randomizzate e tradotte in ore
    if 26 * 30 <= min < 30 * 30 : continue
    
    time = '{:02d}:{:02d}'.format(*divmod(min, 60))   #modulo sono le ore e resto i minuti
    i = i+1

    items = ET.SubElement(data, 'REQUEST')
    item1 = ET.SubElement(items, 'Request_ID')
    item2 = ET.SubElement(items, 'Date')
    item3 = ET.SubElement(items, 'Time')
    item4 = ET.SubElement(items, 'Username')

    item1.text = i
    item2.text = '07-01-2021'
    item3.text = time
    item4.text = name + " " + surname


mydata = ET.tostring(data)
mydata = mydata.decode("utf-8")
mydata = mydata.split("><")
formatter = mydata[0]

for i in range(len(mydata)-1):
    formatter = formatter + ">\n<" + mydata[i+1]

outfile = open(FILENAME, "w")
outfile.write('<?xml version="1.0" encoding="UTF-8"?>\n')
outfile.write(formatter)


infile_n.close()
infile_s.close()
outfile.close()
