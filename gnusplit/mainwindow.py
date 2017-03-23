#!/usr/bin/env python
#coding: utf8


"""GNUSplit - Splits/Joins/Checksums files.

Main window module.

"""

__author__ = 'José Lopes de Oliveira Júnior'
__licence__ = 'GPLv3+'


import sys
import webbrowser
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

from jack import Jack
from aboutdialog import AboutDialog
from filechooserdialog import FileChooserDialog
from folderchooserdialog import FolderChooserDialog


GLADE_FILES_PATH = 'glade'


class MainWindow(object):

    """Main window class."""
    
    def __init__(self):
        """Initializes all attrs. and connects signals."""
        
        widgets_tree = gtk.glade.XML('{0}/mainwindow.glade'.\
                                     format(GLADE_FILES_PATH))
        self.window_main = widgets_tree.get_widget('window_main')
        
        # Not in tabs
        self.notebook = widgets_tree.get_widget('notebook')
        self.button_about = widgets_tree.get_widget('button_about')
        self.button_help = widgets_tree.get_widget('button_help')
        self.button_apply = widgets_tree.get_widget('button_apply')
        self.progressbar = widgets_tree.get_widget('progressbar')
        
        # Split tab
        self.entry_input_file_split = widgets_tree.get_widget('entry_input_file_split')
        self.entry_output_folder_split = widgets_tree.get_widget('entry_output_folder_split')
        self.spinbutton_output_size_split = widgets_tree.get_widget('spinbutton_output_size_split')
        self.combobox_output_size_split = widgets_tree.get_widget('combobox_output_size_split')
        
        # Join tab
        self.entry_input_file_join = widgets_tree.get_widget('entry_input_file_join')
        self.entry_output_folder_join = widgets_tree.get_widget('entry_output_folder_join')
        
        # Checksum tab
        self.entry_input_file_checksum = widgets_tree.get_widget('entry_input_file_checksum')
        self.entry_checksum_checksum = widgets_tree.get_widget('entry_checksum_checksum')
        self.label_status_checksum = widgets_tree.get_widget('label_status_checksum')
        
        # Configuring attrs.
        self.checksum_status = ['<span size="large" foreground="#2e3436"><b>Checksum Generated</b></span>', 
                                '<span size="large" foreground="#4e9a06"><b>Checksum OK</b></span>', 
                                '<span size="large" foreground="#a40000"><b>Checksum Wrong</b></span>']
        self.combobox_output_size_split.set_active(1)
        
        widgets_tree.signal_autoconnect(self)
        self.window_main.connect('destroy', self.destroy)
        self.window_main.show_all()
    
    def run(self):
        """Starts interface."""
        
        gtk.main()
    
    def destroy(self, widget, data=None):
        """Stops interface."""
        
        gtk.main_quit()
    
    def on_button_about_clicked(self, widget, data=None):
        """Shows about window."""
        
        AboutDialog().run()
    
    def on_button_help_clicked(self, widget, data=None): 
        """Opens system's default browser on GNUSpit's web page."""
        
        webbrowser.open('http://wiki.github.com/joselopes/gnusplit')
    
    def on_button_apply_clicked(self, widget, data=None):
        """Will execute actions depending on selected page."""
        
        if not self.notebook.get_current_page():  # Split
            
            #TODO: Check fields and capture exceptions.
            
            splitter = Jack(self.entry_input_file_split.get_text(), 
                            self.entry_output_folder_split.get_text(), 
                            int(self.spinbutton_output_size_split.get_value()), 
                            (self.combobox_output_size_split.get_active() + 1))
            
            self.progressbar.set_text('Processing')
            splitter.split()
            self.progressbar.set_text('Done')
        
        elif self.notebook.get_current_page() == 1:  # Join
            join = Jack(self.entry_input_file_join.get_text())
            
            self.progressbar.set_text('Processing')
            join.join()
            self.progressbar.set_text('Done')
        
        else:  # Checksum
            checksum = Jack(self.entry_input_file_checksum.get_text())
            
            self.progressbar.set_text('Processing')
            
            if self.entry_checksum_checksum.get_text():
                if checksum.checksum(self.entry_checksum_checksum.get_text()):
                    self.label_status_checksum.set_markup(self.checksum_status[1])
                else:
                    self.label_status_checksum.set_markup(self.checksum_status[2])
            else:
                self.entry_checksum_checksum.set_text(checksum.checksum())
                self.label_status_checksum.set_markup(self.checksum_status[0])
            
            self.progressbar.set_text('Done')
    
    def on_button_input_file_split_clicked(self, widget, data=None):
        """Displays a file selection dialog."""
        
        filechooserdialog = FileChooserDialog()
        filechooserdialog.run()
        
        if filechooserdialog.filename:
            self.entry_input_file_split.set_text(filechooserdialog.filename)
            
            if not self.entry_output_folder_split.get_text():
                self.entry_output_folder_split.set_text(filechooserdialog.folder)
            
            if not self.entry_input_file_join.get_text():
                self.entry_input_file_join.set_text(filechooserdialog.filename)
            if not self.entry_output_folder_join.get_text():
                self.entry_output_folder_join.set_text(filechooserdialog.folder)
            
            if not self.entry_input_file_checksum.get_text():
                self.entry_input_file_checksum.set_text(filechooserdialog.filename)
    
    def on_button_input_file_checksum_clicked(self, widget, data=None):
        """Displays a folder selection dialog."""
        
        folderchooserdialog = FolderChooserDialog()
        folderchooserdialog.run()
        self.entry_output_folder_split.set_text(folderchooserdialog.folder)
    
    def on_button_input_file_checksum_clicked(self, widget, data=None):
        """Selects a file to checksum."""
        
        filechooserdialog = FileChooserDialog()
        filechooserdialog.run()
        
        if filechooserdialog.filename:
            self.entry_input_file_checksum.set_text(filechooserdialog.filename)
            
            if not self.entry_input_file_split.get_text():
                self.entry_input_file_split.set_text(filechooserdialog.filename)
            if not self.entry_output_folder_split.get_text():
                self.entry_output_folder_split.set_text(filechooserdialog.folder)
            
            if not self.entry_input_file_join.get_text():
                self.entry_input_file_join.set_text(filechooserdialog.filename)
            if not self.entry_output_folder_join.get_text():
                self.entry_output_folder_join.set_text(filechooserdialog.folder)
    
    def on_button_checksum_checksum_clicked(self, widget, data=None):
        """Copies checksum to clipboard."""
        
        self.window_main.set_focus(self.entry_checksum_checksum)
        self.entry_checksum_checksum.copy_clipboard()


# 
# Main
# 

if __name__ == '__main__':
    mainwindow = MainWindow()
    mainwindow.run()

#EOF
