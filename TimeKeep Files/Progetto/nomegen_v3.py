import random

FILENAME = "orari.txt"    # nome del file di output
LINES = 20              # righe che verranno stampate sul file

infile = open("9000_nomi_propri.txt", "r")
lines = infile.readlines()
outfile = open(FILENAME, "w")
list = set()
i = 0

while i < LINES:
    name = lines[random.randint(0,len(lines))].strip()
    if name in list:
        continue
    else:
        list.add(name)
        i = i+1
        
    min1 = (random.randint(0, 16) + 18) * 30  #numero mezz'ore randomizzate e tradotte in ore
    min2 = min1 + 60 #2 * 60
    
    time1 = '{:02d}:{:02d}'.format(*divmod(min1, 60))   #modulo sono le ore e resto i minuti
    time2 = '{:02d}:{:02d}'.format(*divmod(min2, 60))

    outfile.write(f'{name} {time1} {time2}\n')


infile.close()
outfile.close()
