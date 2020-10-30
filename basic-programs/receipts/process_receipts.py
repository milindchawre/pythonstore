import os
import json
import shutil
import glob

try:
    os.mkdir('./processed')
except OSError:
    print("'processed' directory already exists")

receipts = glob.glob('./new/receipt-[0-9]*.json')
subtotal = 0.0

# to get even numbered receipts used re package
#receipts = [f for f in glob.iglob('./new/receipt-[0-9]*.json') if re.match('./new/receipt-[0-9]*[24680].json', f)]

# with iterator glob function use less memory footprint
#for path in glob.iglob('./new/receipt-[0-9]*.json'):
for path in receipts:
    with open(path) as f:
        content = json.load(f)
        subtotal += float(content['value'])
    name = path.split('/')[-1]
    #path.replace('new','processed')
    destination = f"./processed/{name}"
    shutil.move(path,destination)
    print(f"moved '{path}' to '{destination}'")

print(f"Receipt subtotal: $%.2f" % subtotal)
#print(f"Receipt subtotal: ${math.ceil(subtotal)})
#print(f"Receipt subtotal: ${math.floor(subtotal)})
#print(f"Receipt subtotal: ${round(subtotal, 2)})
