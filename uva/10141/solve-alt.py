from sys import stdin

inp = stdin.read()
lines = inp.splitlines()

count = 0
suppliers = []
requirements = []

for line in lines:
  if '.' not in line and ' ' in line and line[0].isdigit():
    n, p = list(map(int, line.split()))
    if len(suppliers) > 0:
      max_match_suppliers = [supplier for supplier in suppliers if supplier[2] == max_match]

      if len(max_match_suppliers) == 1:
        print(max_match_suppliers[0][0])
      else:
        min_cost = min([supplier[1] for supplier in max_match_suppliers ])
        min_cost_suppliers = [supplier for supplier in max_match_suppliers if supplier[1] == min_cost]
        print(min_cost_suppliers[0][0])

    if n == 0:
      break
    elif count > 0:
      print('')
    count += 1
    print(f"RFP #{count}")
    suppliers = []
    requirements = []
    max_match = 0
  elif '.' in line:
    cost, match = line.split()
    cost = float(cost)
    match = int(match)
    if (match > max_match):
      max_match = match
    suppliers[-1] += (cost, match)
  elif len(requirements) != n:
    requirements.append(line)
  elif line in requirements:
    pass
  else:
    suppliers.append((line,))