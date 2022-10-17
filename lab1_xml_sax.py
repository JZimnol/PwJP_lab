import xml.sax

class NoteHanlder(xml.sax.ContentHandler):
    def __init__(self):
        self.current = ""
        self.to = ""
        self._from = ""
        self.heading = ""
        self.body = ""

    def startElement(self, name, attrs):
        self.current = name
        if name == "note":
            print(f"--- notka {attrs['id']} ---")

    def characters(self, content):
        if self.current == "to":
            self.to = content
        elif self.current == "from":
            self._from = content
        elif self.current == "heading":
            self.heading = content
        elif self.current == "body":
            self.body = content

    def endElement(self, name):
        if self.current == "to":
            print(f"To: {self.to}")
        elif self.current == "from":
            print(f"From: {self._from}")
        elif self.current == "heading":
            print(f"Heading: {self.heading}")
        elif self.current == "body":
            print(f"Body: {self.body}")
        self.current = ""


handler = NoteHanlder()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse("input_xml.xml")
