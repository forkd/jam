#!/usr/bin/env python
#coding: utf8


"""GNUSplit - Splits/Joins/Checksums files.

About dialog module.

"""

__author__ = 'José Lopes de Oliveira Júnior'
__licence__ = 'GPLv3+'
__version__ = '0.0.5'


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


class AboutDialog(object):
    
    """About dialog class."""
    
    def __init__(self):
        """Initializes all attrs. and connects signals."""
        
        widgets_tree = gtk.glade.XML('{0}/aboutdialog.glade'.\
                                     format(GLADE_FILES_PATH))
        self.aboutdialog = widgets_tree.get_widget('aboutdialog')
        
        # This hack enables close button in this window.
        self.aboutdialog.connect('response', lambda d, r: d.destroy())
        
        self.aboutdialog.set_version(__version__)
        
        self.aboutdialog.connect('destroy', self.destroy)
        self.aboutdialog.show_all()
    
    def run(self):
        gtk.main()
    
    def destroy(self, widget, data=None):
        gtk.main_quit()


# 
# Main
# 

if __name__ == '__main__':
    aboutdialog = AboutDialog()
    aboutdialog.run()
    
#EOF
