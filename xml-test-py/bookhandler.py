import xml.sax.handler

class BookHandler(xml.sax.handler.ContentHandler):
    def __init__(self):
        self.in_title = 0
        self.mapping = {}

    def startElement(self, name, attributes):
        if name == "book":
            self.buffer = ""
            self.isbn = attributes["isbn"]
        elif name == "title":
            self.in_title = 1
    
    def characters(self, data):
        if self.in_title: self.buffer += data
    
    def endElement(self, name):
        if name == "title":
            self.in_title = 0
            self.mapping[self.isbn] = self.buffer

