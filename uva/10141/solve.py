count = 0

while True:
  n, p = list(map(int, input().split()))
  if n == 0:
    break
  elif count > 0:
    print('')
  count += 1
  print(f"RFP #{count}")

  for _ in range(n):
    input()
  max_match = 0
  suppliers = []
  for i in range(p):
    suppliers.append((input(),))
    cost, match = input().split()
    match = int(match)
    suppliers[i] += (float(cost), match)
    if (match > max_match):
      max_match = match
    for _ in range(match):
      input()

  max_match_suppliers = [supplier for supplier in suppliers if supplier[2] == max_match]

  if len(max_match_suppliers) == 1:
    print(max_match_suppliers[0][0])
  else:
    min_cost = min([supplier[1] for supplier in max_match_suppliers ])
    min_cost_suppliers = [supplier for supplier in max_match_suppliers if supplier[1] == min_cost]
    print(min_cost_suppliers[0][0])
