import xml.etree.ElementTree as elemTree
'''
Idea from
https://stackoverflow.com/questions/3095434/inserting-newlines-in-xml-file-generated-via-xml-etree-elementtree-in-python
'''


def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


def display(tree, abstract=False):
    if abstract:
        for i, assignment in enumerate(tree.findall("assignment")):
            print("%d. %s" % (i + 1, assignment.find('id').text))

        return

    for i, assignment in enumerate(tree.findall("assignment")):
        print("%d. " %(i+1), end='')
        print(assignment.find("id").text)
        print("  Deadline: ", assignment.find("deadline").text)

        mint = assignment.find("executiontime").find("min").text
        maxt = assignment.find("executiontime").find("max").text
        print("  Execution Time: %s~%s"% (mint, maxt))
        print("  This is %s mission." %(assignment.find("difficulty").text))
        print("  Also, this mission is %s."%(assignment.find("importance").text), end="\n\n")


def append(tree):
    # 변수 선언
    print("Initializing new assignment:")
    assignment = elemTree.SubElement(tree.getroot(), "assignment")

    elemTree.SubElement(assignment, "id").text = input("Name: ")
    elemTree.SubElement(assignment, "deadline").text = input("Deadline: ")

    execution = elemTree.SubElement(assignment, "executiontime")
    elemTree.SubElement(execution, "min").text = input("Minimum Execution Time: ")
    elemTree.SubElement(execution, "max").text = input("Maximum Execution Time: ")

    elemTree.SubElement(assignment, "difficulty").text = input("Difficulty: ")
    elemTree.SubElement(assignment, "importance").text = input("Importance: ")


def delete(tree, num=None):
    if num==None:
        display(tree, abstract=True)
        num = int(input("Which task do you want to delete? "))

    root = tree.getroot()
    root.remove(root.findall("assignment")[num-1])


def save(tree, pretty_print=True):
    if pretty_print:
        indent(tree.getroot())
    tree.write('data/data.xml')


if __name__ == '__main__':
    tree = elemTree.parse('data/data.xml')

    message = """
    =======================================
    This is CLI-based Assignment mannager.
    Please type your command.
    =======================================
    """

    print(message)

    while True:
        cmd = input(">>>")
        cmd = cmd.split(' ')

        if cmd[0] == "add":
            append(tree)
        elif cmd[0] == "delete":
            if len(cmd)>1:
                delete(tree, int(cmd[1]))
            else:
                delete(tree)
        elif cmd[0] == "display":
            if len(cmd)>1 and cmd[1]=="--all":
                display(tree)
            else:
                display(tree, abstract=True)
        elif cmd[0] == "save":
            save(tree)
        elif cmd[0] == "quit":
            save(tree)
            exit(0)