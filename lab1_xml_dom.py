import xml.dom.minidom


domtree = xml.dom.minidom.parse('input_xml.xml')
group = domtree.documentElement
notes = group.getElementsByTagName('note')

for note in notes:
    print(f"Note {note.getAttribute('id')}")
    to = note.getElementsByTagName('to')[0].childNodes[0].nodeValue
    _from = note.getElementsByTagName('from')[0].childNodes[0].nodeValue
    heading = note.getElementsByTagName('heading')[0].childNodes[0].nodeValue
    body = note.getElementsByTagName('body')[0].childNodes[0].nodeValue
    print(f"\tTo: {to}\n\tFrom: {_from}\n\tHeading: {heading}\n\tBody: {body}")

notes[0].getElementsByTagName('to')[0].childNodes[0].nodeValue = "Michalek"

new_note = domtree.createElement("note")
new_note.setAttribute("id", "100")

to = domtree.createElement("to")
to.appendChild(domtree.createTextNode("Lukasz"))
_from = domtree.createElement("from")
_from.appendChild(domtree.createTextNode("Krzysiek"))
heading = domtree.createElement("note")
heading.appendChild(domtree.createTextNode("przykladowe note"))
body = domtree.createElement("body")
body.appendChild(domtree.createTextNode("proste body"))

new_note.appendChild(to)
new_note.appendChild(_from)
new_note.appendChild(heading)
new_note.appendChild(body)
group.appendChild(new_note)

domtree.writexml(open("output_xml.xml", 'w'))
