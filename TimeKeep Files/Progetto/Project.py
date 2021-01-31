MAXPERS = 3  #persone permesse per ogni fascia oraria
MAXNOME = 128  #lunghezza massima di un nome
TIMESLOT = 30  #durata consentita per ogni persona
CROWD = 1 #numero massimo di persone ammesse

class data:
    def __init__(self, nome, oreiniziali, minutiniziali, orefinali, minutifinali):
        self.n = nome
        self.oin = oreiniziali
        self.min = minutiniziali
        self.ofin = orefinali
        self.mfin = minutifinali


def carica_elenco(file):
    vett =[]
    for i in range(len(file)):
        var = file[i].split()
        name = var[0]
        var = var[1].split(':') + var[2].split(':')
        vett.append(data(name, int(var[0]), int(var[1]), int(var[2]), int(var[3])))
    return vett

def stampa_elenco(vett):
    for i in range(len(vett)):
        print (f'{vett[i].n} {vett[i].oin}:{vett[i].min} {vett[i].ofin}:{vett[i].mfin}')
    print()

def orario(h, m):
    return (h * 60 + m)

def intervallo(h1, h2, m1, m2):
    tempo = orario(h2, m2) - orario(h1, m1)
    return tempo


def controllo_intervallo(vett):
    k = 0
    for i in range(len(vett)):
        tempo = intervallo(vett[i].oin, vett[i].ofin, vett[i].min, vett[i].mfin)
        if ( (tempo % TIMESLOT) or ((vett[i].min !=0) and (vett[i].min != 30)) or ((vett[i].mfin !=0) and (vett[i].mfin != 30)) ):
            k = k + 1
            print(f'Fascia oraria incorretta per utente {vett[i].n}, notificare\n')
    if (not k):
        print("Nessuna fascia oraria incorretta\n")


def elenco_occupati(vett):
    k = 0
    while k < 24:
        print(f'Fascia orario: {k}.00 - {k+1}.00\nPresenze:\n')
        j = 0
        for i in range(len(vett)):
            if ( ((vett[i].oin <= k) and (vett[i].ofin > k)) ):
                print(vett[i].n)
                j = j + 1
                if (j > CROWD):
                    print("!!!!!!!!!!!!Overcrowded!!!!!!!!!!!!!!!!")
                    break
        k = k + 1
        print()


def confronto_fine(h1, h2, m1, m2):
    tempo = intervallo(h1, h2, m1, m2)
    if tempo >= 0:
        return 1
    else: return 0


def pick_early_finish(vett):
    k = 0
    for i in range(1, len(vett)):
        a = confronto_fine(vett[i].ofin, vett[k].ofin, vett[i].mfin, vett[k].mfin)
        if a: k = i
    return k
    

def overlaps(vett, ind1, ind2):
    if orario(vett[ind1].oin, vett[ind1].min) < orario(vett[ind2].ofin, vett[ind2].mfin) and orario(vett[ind2].oin, vett[ind2].min) < orario(vett[ind1].ofin, vett[ind1].mfin):
        return 1
    else: return 0


def algoritmo(vett):
    assigned = []
    discarded = []
    unassigned = vett[:]
    unassigned2 = vett[:]
    l = 0

    while len(unassigned):
        k = 0
        index = pick_early_finish(unassigned)
        assigned.append(unassigned[index])
        l = l + 1
        for i in range(len(unassigned)):
            if overlaps (unassigned, index, i):
                if (unassigned[i].n != unassigned[index].n):
                    discarded.append(unassigned[i])
                unassigned2.remove(unassigned[i])
        unassigned.clear()
        unassigned = unassigned2[:]

    return assigned, discarded
    

def assegnatore(vett):
    a = []
    b = []
    totdisp = vett[:]
    totass = []

    for i in range(CROWD):
        a.clear()
        b.clear()
        a, b = algoritmo(totdisp)
        totass.extend(a)
        totdisp.clear()
        totdisp = b[:]
    
    return totass, totdisp




infile = open("orari.txt", "r")
lines = infile.readlines()

invett = carica_elenco(lines)

print("**********DATI IN ARRIVO:**********")
stampa_elenco(invett)
	
#print("**********CONTROLLO FASCE ORARIO:**********")
#controllo_intervallo(invett)
	
#print("**********PRESENZE PER INTERVALLI:**********")
#elenco_occupati(invett)

print("**********Assegnazione posti:**********")
assvett, disvett = assegnatore(invett)
print("Posti assegnati:")
stampa_elenco(assvett)
print("Posti rifiutati:")
stampa_elenco(disvett)

#input()