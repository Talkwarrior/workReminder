import xml.etree.ElementTree as elemTree
import subprocess


tree = elemTree.parse('data/data.xml')
ids =[]
for assignment in tree.findall("assignment"):
    ids.append(assignment.find("id").text)

for id in ids:
    subprocess.call ("pythonw notice.py %s" %id , shell=False)