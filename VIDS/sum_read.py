import csv

bp = None
p = None
rr = None
O2 = None
t = None
loc = None
age = None
name = None
gender = None

p_health = 80
O2_health = 100
rr_health = 20
t_health = 98.6
bp_health = 1.5
loc_health = 5

with open('patient_0_v2.csv') as myReadFile:
    reader = csv.reader(myReadFile)
    next(reader, None)
    for row in reader:

        name = row[3]
        age = row[4]
        gender = row[5]
        p = float(row[6])
        O2 = float(row[9])
        rr = float(row[12])
        t = float(row[18])
        bp = float(row[24])
        loc = float(row[31])

# Normalize the variables
p = (p / p_health) * 100
O2 = (O2 / O2_health) * 100
rr = (rr / rr_health) * 100
t = (t / t_health) * 100
bp = (bp / bp_health) * 100
loc = (loc / loc_health) * 100

# Reset if minimum value of 0 is met
if p == 0.0:
    p = 3
if O2 == 0.0:
    O2 = 3
if rr == 0.0:
    rr = 3
if t == 0.0:
    t = 3
if bp == 0.0:
    bp = 3
if loc == 0.0:
    loc = 3

myWriteFile = open('v_summary.csv', 'w')
with myWriteFile:
    myFields = ['vital', 'url', 'score']
    writer = csv.DictWriter(myWriteFile, fieldnames=myFields)
    writer.writeheader()
    writer.writerow({'vital' : 'Blood Pressure', 'url': 'BloodPressure.html',
    'score' : bp})
    writer.writerow({'vital' : 'Consciousness', 'url': 'Consciousness.html',
    'score' : loc})
    writer.writerow({'vital' : 'Pulse', 'url': 'Pulse.html',
    'score' : p})
    writer.writerow({'vital' : 'Respiratory', 'url': 'Respiratory_rate.html',
    'score' : rr})
    writer.writerow({'vital' : 'SpO2', 'url': 'SpO2.html',
    'score' : O2})
    writer.writerow({'vital' : 'Temperature', 'url': 'Temp.html',
    'score' : t})

myWriteFile = open('v_person.csv', 'w')
with myWriteFile:
    myFields = ['name', 'age', 'gender']
    writer = csv.DictWriter(myWriteFile, fieldnames=myFields)
    writer.writeheader()
    writer.writerow({'name' : name, 'age': age, 'gender' : gender})
