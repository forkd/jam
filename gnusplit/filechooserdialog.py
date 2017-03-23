#!/usr/bin/env python
#coding: utf8


"""GNUSplit - Splits/Joins/Checksums files.

File chooser dialog module.

"""

__author__ = 'José Lopes de Oliveira Júnior'
__licence__ = 'GPLv3'


import os.path
import sys
try:
    import pygtk
    pygtk.require('2.0')
except:
    pass
try:
    import gtk
    import gtk.glade
except:
    sys.exit(1)


GLADE_FILES_PATH = 'glade'


class FileChooserDialog(object):
    
    """File chooser dialog class."""
    
    def __init__(self, directory_path=os.path.expanduser('~')):
        """Initializes all attrs. and connects signals."""
        
        widgets_tree = gtk.glade.XML("{0}/filechooserdialog.glade".format(GLADE_FILES_PATH))
        self.filechooserdialog = widgets_tree.get_widget('filechooserdialog')
        
        self.filechooserdialog.set_current_folder(directory_path)
        self.filename = None
        self.folder = None
        
        self.filechooserdialog.add_button(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL)
        self.filechooserdialog.add_button(gtk.STOCK_OPEN, gtk.RESPONSE_OK)
        self.filechooserdialog.set_default_response(gtk.RESPONSE_OK)
    
    def run(self):
        """Starts interface and changes object's attrs."""
        
        if self.filechooserdialog.run() == gtk.RESPONSE_OK:
                self.filename = self.filechooserdialog.get_filename()
                self.folder = '{0}/'.format(os.path.dirname(self.filename))
            
        self.destroy()
    
    def destroy(self):
        """Stops interface."""
        
        self.filechooserdialog.destroy()


# 
# Main
# 

if __name__ == '__main__':
    filechooserdialog = FileChooserDialog()
    filechooserdialog.run()
    print('Chosen file..: {0}\nChosen folder: {1}'.format(filechooserdialog.\
                                                          filename, 
                                                          filechooserdialog.\
                                                          folder))

#EOF
