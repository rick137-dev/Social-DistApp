from tabulate import tabulate
import xml.etree.ElementTree as ET
import qrcode
import sys
import operator


DECREE_MQ = 5  #square meters for every person in a shop
MQ_SHOP = 50  #dimension of a shop in square meters
PERSONNEL = 2 #people working at the same time in the shop'
PRECISION = 10


"""dimension of the timeslot for every timezone in minutes"""
DURATION_Z1 = 20
DURATION_Z2 = 20
DURATION_Z3 = 20
DURATION_Z4 = 20


class datain:
    def __init__(self, ID, name, hour, minutes):
        self.id = ID
        self.n = name
        self.h = hour
        self.m = minutes

    def printable(self):
        return [self.n, '{:02d}:{:02d}'.format(self.h, self.m)]


class dataout:
    def __init__(self, name, entryhour, entryminutes, leavinghour, leavingminutes):
        self.n = name
        self.eh = entryhour
        self.em = entryminutes
        self.lh = leavinghour
        self.lm = leavingminutes

    def printable(self):
        return [self.n, '{:02d}:{:02d}'.format(self.eh, self.em), '{:02d}:{:02d}'.format(self.lh, self.lm)]


class datadis:
    def __init__(self, ID, name, hour, minutes, reason):
        self.id = ID
        self.n = name
        self.h = hour
        self.m = minutes
        self.r = reason

    def printable(self):
        return [self.id, self.n, '{:02d}:{:02d}'.format(self.h, self.m), self.r]


def crowdcontrol(squarem):
    people = squarem // DECREE_MQ - PERSONNEL
    if people > 0: return people
    else: sys.exit("Could not process: Unsufficient space for allocating people\n")


def minutes_calc(h, m):
    return (h * 60 + m)


def sep_time(minutes):
    return divmod(minutes, 60)


def zone(minutes):
    if   minutes_calc(9, 0)  <= minutes < minutes_calc(11, 0): return DURATION_Z1, "N1"
    elif minutes_calc(11, 0) <= minutes < minutes_calc(13, 0): return DURATION_Z2, "N2"
    elif minutes_calc(15, 0) <= minutes < minutes_calc(17, 0): return DURATION_Z3, "N3"
    elif minutes_calc(17, 0) <= minutes < minutes_calc(19, 0): return DURATION_Z4, "N4"
    else: return None, "Forbidden"


def outside(intime, outime, name):
    if name == "N1":
        if intime < minutes_calc(9, 0) or outime > minutes_calc(11, 0): return 1
        else: return 0
    elif name == "N2":
        if intime < minutes_calc(11, 0) or outime > minutes_calc(13, 0): return 1
        else: return 0
    elif name == "N3":
        if intime < minutes_calc(15, 0) or outime > minutes_calc(17, 0): return 1
        else: return 0
    elif name == "N4":
        if intime < minutes_calc(17, 0) or outime > minutes_calc(19, 0): return 1
        else: return 0


def zone_adder_add(h, m, cont):
    zone_d, zone_n = zone(minutes_calc(h, m))
    if zone_n == "Forbidden":
        return "Forbidden", "Forbidden"
    intime = minutes_calc(h, m) + PRECISION*cont
    outime = minutes_calc(h, m) + zone_d + PRECISION*cont
    
    if outside(intime, outime, zone_n): 
        return "Unaviable", "Unaviable"
    else: 
        return intime, outime


def zone_adder_sub(h, m, cont):
    zone_d, zone_n = zone(minutes_calc(h, m))
    if zone_n == "Forbidden":
        return "Forbidden", "Forbidden"
    intime = minutes_calc(h, m) - PRECISION*cont
    outime = minutes_calc(h, m) + zone_d - PRECISION*cont
    
    if outside(intime, outime, zone_n): 
        return "Unaviable", "Unaviable"
    else: 
        return intime, outime


def load_database():
    tree = ET.parse('REQUEST.xml')
    root = tree.getroot()
    vett = []

    for i in range(len(root)):
        var = root[i][2].text.split(':')
        vett.append(datain(root[i][0].text, root[i][3].text, int(var[0]), int(var[1])))
    return vett


def load_input(num):
    raw = input()
    var = raw.split()
    if len(var) != 3: return []

    name = var[0] + " " + var[1]
    var = var[2].split(':')
    if len(var) != 2: return []
    if var[0] + "x" == "x" or var[1] + "x" == "x" : return []

    out = datain(num, name, int(var[0]), int(var[1]))
    return out


def load_ask():
    raw = input()
    var = raw.split()
    if len(var) != 2: return []

    out = var[0] + " " + var[1]
    return out


def print_pref(vett):
    ls = []
    for i in range(len(vett)):
        ls.append(vett[i].printable())

    if vett == []: print("      ___Empty___       \n")
    else:
        print(tabulate(ls, ["Name", "Preference"], tablefmt="pretty"))
        print("\n")


def print_as(vett):
    ls = []
    for i in range(len(vett)):
        ls.append(vett[i].printable())

    if vett == []: print("      ___Empty___       \n")
    else:
        print(tabulate(ls, ["Name", "Entrance", "Leaving"], tablefmt="pretty"))
        print()


def print_dis(vett):
    ls = []
    for i in range(len(vett)):
        ls.append(vett[i].printable())

    if vett == []: print("      ___Empty___       \n")
    else:
        print(tabulate(ls, ["Request_ID", "Name", "Preference", "Reason"], tablefmt="pretty"))
        print("\n")


def formatter(data):
    mydata = ET.tostring(data)
    mydata = mydata.decode("utf-8")
    mydata = mydata.split("><")
    form = mydata[0]

    for i in range(len(mydata)-1):
        form = form + ">\n<" + mydata[i+1]

    return form


def print_db(vett):
    data = ET.Element('dataroot')

    for i in range(len(vett)):
        items = ET.SubElement(data, 'TIMESLOT')
        item1 = ET.SubElement(items, 'Client')
        item2 = ET.SubElement(items, 'Start')
        item3 = ET.SubElement(items, 'End')

        item1.text = f'{vett[i].n}'
        item2.text = '{:02d}:{:02d}'.format(vett[i].eh, vett[i].em)
        item3.text = '{:02d}:{:02d}'.format(vett[i].lh, vett[i].lm)

    converted = formatter(data)
    outfile = open("EXPORTED.xml", "w")
    outfile.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    outfile.write(converted)

    print("DATA EXPORTED WITHOUT ERRORS")


def overlaps(vett1, vett2):
    if minutes_calc(vett1.eh, vett1.em) < minutes_calc(vett2.lh, vett2.lm) and minutes_calc(vett2.eh, vett2.em) < minutes_calc(vett1.lh, vett1.lm):
        return 1
    else: return 0


def odd_or_even(num):
    if num % 2: return 1
    else: return 0


def scheduler(data, assigned, discarded):
    crowd = crowdcontrol(MQ_SHOP)
    counter, exeptodd, exepteven = 0, 0, 0
    even, odd = 1, 0
    possible = []

    while True:
        counter = counter + 1
        present, overl = 0, 0

        for i in range(len(assigned)):
            if data.n == assigned[i].n:
                present = 1
        
        if present == 1:
            reason = "User already present today"
            discarded.append(datadis(data.id, data.n, data.h, data.m, reason))
            break

        if odd_or_even(counter): 
            intime, outime = zone_adder_add(data.h, data.m, odd)
            if intime == "Forbidden": 
                reason = "Request outside allowed timezone"
                discarded.append(datadis(data.id, data.n, data.h, data.m, reason))
                break
            if intime == "Unaviable": 
                exeptodd =  1
                if exeptodd == 1 and exepteven == 1:
                    if check_if_full(discarded):
                        reason = "Day is full"
                    else: 
                        _, zone_n = zone(minutes_calc(data.h, data.m))
                        reason = f"Zone {zone_n} is full"
                    discarded.append(datadis(data.id, data.n, data.h, data.m, reason))
                    break

                else: continue
            a, b = sep_time(intime)
            c, d = sep_time(outime)
            possible = dataout(data.n, a, b, c, d)

        else:
            intime, outime = zone_adder_sub(data.h, data.m, even)
            if intime == "Forbidden": 
                discarded.append(data)
                break
            if intime == "Unaviable": 
                exepteven = 1
                if exeptodd == 1 and exepteven == 1:
                    if check_if_full(discarded):
                        reason = "Day is full"
                    else: 
                        _, zone_n = zone(minutes_calc(data.h, data.m))
                        reason = f"Zone {zone_n} is full"
                    discarded.append(datadis(data.id, data.n, data.h, data.m, reason))
                    break

                else: continue
            a, b = sep_time(intime)
            c, d = sep_time(outime)
            possible = dataout(data.n, a, b, c, d)
       
        for i in range(len(assigned)):
            if overlaps (possible, assigned[i]):
                overl = overl + 1

        if overl < crowd: 
            assigned.append(possible)
            break
        
        if odd_or_even(counter): odd = odd + 1
        else: even = even + 1


def qr_code(data):
    img = qrcode.make(data.n + ' {:02d}:{:02d}'.format(data.eh, data.em) + ' {:02d}:{:02d}'.format(data.lh, data.lm))
    img.show()


def check_if_full(discarded):
    a, b, c, d = 0, 0, 0, 0
    for i in range(len(discarded)):
        _, namezone = zone(minutes_calc(discarded[i].h, discarded[i].m))

        if namezone == "N1": a = 1
        elif namezone == "N2": b = 1
        elif namezone == "N3": c = 1
        elif namezone == "N4": d = 1
        else: None

        if (a + b + c + d) >= 4:
            return 1

    return 0


def fill_with_list(invett):
    assigned = []
    discarded = []

    for i in range(len(invett)):
        scheduler(invett[i], assigned, discarded)

    assigned = sorted(assigned, key=operator.attrgetter('em'))
    assigned = sorted(assigned, key=operator.attrgetter('eh'))

    return assigned, discarded


def fill_from_input(assigned, discarded):
    while True:
        print("INSERT DATA IN THE FOLLOWING FORMAT: Name Surname hh:mm")
        text = load_input(len(assigned))

        if text == []: print("INCORRECT FORMAT, RETRY\n")
        else: break

    scheduler(text, assigned, discarded)

    assigned = sorted(assigned, key=operator.attrgetter('em'))
    assigned = sorted(assigned, key=operator.attrgetter('eh'))

    print("\n\n***************FULL SCHEDULING:***************")
    print("-ASSIGNED TIMESLOTS:")
    print_as(assigned)
    print("-COULD NOT FIND A TIMESLOT:")
    print_dis(discarded)


def ask_qr(assigned):
    found = 0
    while True:
        print("SEARCH FOR USERS IN THE FOLLOWING FORMAT: Name Surname")
        text = load_ask()

        if text == []: print("INCORRECT FORMAT, RETRY\n")
        else: break

    for i in range(len(assigned)):
        if text == assigned[i].n: 
            qr_code(assigned[i])
            found = 1
            break
    
    if not found: print(f"NO USERS IN MEMORY NAMED: {text}")
    print()


def instant_response(assigned, discarded):
    while True:
        print("ENTER A COMMAND FROM THE LIST:")
        print("------------------------------")
        print("COMMAND Insert - Insert new request")
        print("COMMAND Ask - Ask for a qr code generation of a scheduled request")
        print("COMMAND Export - Export assigned timeslots to XML document")
        print("COMMAND Exit - Exit the program\n")
        
        text = input()
        if text == "Exit": break
        elif text == "Insert": fill_from_input(assigned, discarded)
        elif text == "Ask": ask_qr(assigned)
        elif text == "Export": print_db(assigned)
        else: print("\nCOMMAND NOT PRESENT IN THE LIST, RETRY")



invett = load_database()

print("\n-------------------------------Scheduling Algorithm, developed by Andrea Caiulo-------------------------------\n")
print("PRESS ENTER TO START")
input()

print("*********INCOMING DATA:**********")
print_pref(invett)

print("****************FULL SCHEDULING:****************")
print()
asvett, disvett = fill_with_list(invett)
print("-ASSIGNED TIMESLOTS:")
print_as(asvett)
print("-COULD NOT FIND A TIMESLOT:")
print_dis(disvett)

instant_response(asvett, disvett)