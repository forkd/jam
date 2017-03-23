import xml.sax
import cStringIO

SAMPLE_DATA = """<?xml version="1.0"?>
<exam date="12/11/99">
<patient>Pat</patient>
<bloodtype>B</bloodtype>
</exam>"""

class ExamHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_data = ""
        self.blood_type = ""
    
    def characters(self, text):
        if self.current_data == "bloodtype":
            self.blood_type += text
    
    def startElement(self, tag, attributes):
        self.current_data = tag
    
    def endElement(self, tag):
        if self.current_data == "bloodtype":
            print "Blood type: ", self.blood_type
        self.current_data = ""

if __name__ == "__main__":
    my_parser = xml.sax.make_parser()
    my_parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    handler = ExamHandler()
    my_parser.setContentHandler(handler)
    string_file = cStringIO.StringIO(SAMPLE_DATA)
    my_source = xml.sax.InputSource("1")
    my_source.setByteStream(string_file)
    my_parser.parse(my_source)
