#!/usr/bin/env python
#coding: utf8


"""GNUSplit - Splits/Joins/Checksums files.

Folder chooser dialog module.

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


class FolderChooserDialog(object):
    
    """File chooser dialog class."""
    
    def __init__(self, directory_path=os.path.expanduser('~')):
        """Initializes all attrs. and connects signals."""
        
        widgets_tree = gtk.glade.XML("{0}/folderchooserdialog.glade".format(GLADE_FILES_PATH))
        self.folderchooserdialog = widgets_tree.get_widget('folderchooserdialog')
        
        self.folderchooserdialog.set_current_folder(directory_path)
        self.folder = None
        
        self.folderchooserdialog.add_button(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL)
        self.folderchooserdialog.add_button(gtk.STOCK_OPEN, gtk.RESPONSE_OK)
        self.folderchooserdialog.set_default_response(gtk.RESPONSE_OK)
    
    def run(self):
        """Starts interface and changes object's attrs."""
        
        if self.folderchooserdialog.run() == gtk.RESPONSE_OK:
                self.folder = self.folderchooserdialog.get_current_folder()
            
        self.destroy()
    
    def destroy(self):
        """Stops interface."""
        
        self.folderchooserdialog.destroy()


# 
# Main
# 

if __name__ == '__main__':
    folderchooserdialog = FolderChooserDialog()
    folderchooserdialog.run()
    print('Chosen folder: {0}'.format(folderchooserdialog.folder))

#EOF
