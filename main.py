names = ["Alex", "Beth", "Caroline", "Eleanor", "Freddie"]
new_names = [name.upper() for name in names if len(name) > 5]
for name in new_names:
  print(name)