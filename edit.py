import xml.etree.ElementTree as elemTree

tree = elemTree.parse('./data.xml')

def display(tree):
    for i, assignment in enumerate(tree.findall("assignment")):
        print("%d. " %(i+1), end='')
        print(assignment.find("id").text)
        print("Deadline: ", assignment.find("deadline").text)
        print("Execution Time: ", assignment.find("executiontime").find("min").text)
        print("This is %s mission." %(assignment.find("difficulty").text))
        print("Also, this mission is %s."%(assignment.find("importance").text), end="\n\n")

display(tree)