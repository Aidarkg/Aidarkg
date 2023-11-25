data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")
designations = []
codes = []

for i in data:
    if i.isnumeric():
        codes.append(i)
    else:
        designations.append(i)

operators = {}

while True:
    operators[designations[0]] = set(codes[0:1])
    operators[designations[1]] = set(codes[1:2])
    operators[designations[2]] = set(codes[2:3])
    operators[designations[3]] = set(codes[3:4])
    operators[designations[4]] = set(codes[4:])
    print(operators)
    del operators['Katel']
    del operators['Fonex']
    operators['O!'] = {'0705', '0700', '0500'}
    operators['Megacom'] = {'0550', '0999', '0555'}
    operators['Beeline'] = {'0770', '0222', '0777'}
    for i, o in operators.items():
        print(f'{i} - ', o)
    break
