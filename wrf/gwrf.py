#!/usr/bin/env python
# -*- coding: utf8 -*-


"""GWRF - A GTK interface for Windows Registry Fixer.

Main window module.

"""

__author__ = "José Lopes de Oliveira Júnior"
__licence__ = "GPLv3"

# Informations about versioning can be found in
# aboutdialog.py file.


import webbrowser

import pygtk
pygtk.require("2.0")
import gtk, gtk.glade

import wrf
from aboutdialog import AboutDialog


GLADE_FILES_PATH = "glade"


class MainWindow(object):

    """Main window class."""
    
    def __init__(self):
        widgets_tree = gtk.glade.XML("%s/gwrf.glade" % GLADE_FILES_PATH)
        
        self.window_main = widgets_tree.get_widget("window_main")
        self.button_about = widgets_tree.get_widget("button_about")
        self.button_help = widgets_tree.get_widget("button_help")
        self.button_apply = widgets_tree.get_widget("button_apply")
        
        # 1st Column
        self.checkbutton_autorun = widgets_tree.get_widget("checkbutton_autorun")
        self.checkbutton_cached_logons_count = widgets_tree.get_widget("checkbutton_cached_logons_count")
        self.entry_cached_logons_count = widgets_tree.get_widget("entry_cached_logons_count")
        self.checkbutton_delete_roaming_cache = widgets_tree.get_widget("checkbutton_delete_roaming_cache")
        self.checkbutton_srv_comment = widgets_tree.get_widget("checkbutton_srv_comment")
        self.entry_srv_comment = widgets_tree.get_widget("entry_srv_comment")
        self.checkbutton_show_admin_tools = widgets_tree.get_widget("checkbutton_show_admin_tools")
        self.checkbutton_dont_disp_last_username = widgets_tree.get_widget("checkbutton_dont_disp_last_username")
        self.checkbutton_welcome_text = widgets_tree.get_widget("checkbutton_welcome_text")
        self.entry_welcome_text = widgets_tree.get_widget("entry_welcome_text")
        self.checkbutton_logon_prompt = widgets_tree.get_widget("checkbutton_logon_prompt")
        self.entry_logon_prompt = widgets_tree.get_widget("entry_logon_prompt")
        self.checkbutton_shutdown_without_logon = widgets_tree.get_widget("checkbutton_shutdown_without_logon")
        self.checkbutton_legal_notice = widgets_tree.get_widget("checkbutton_legal_notice")
        self.entry_legal_notice = widgets_tree.get_widget("entry_legal_notice")
        self.checkbutton_disable_system_recovery_tools = widgets_tree.get_widget("checkbutton_disable_system_recovery_tools")
        self.checkbutton_remove_windows_messenger_from_ie = widgets_tree.get_widget("checkbutton_remove_windows_messenger_from_ie")
        self.checkbutton_icons_visibility = widgets_tree.get_widget("checkbutton_icons_visibility")
        self.checkbutton_show_admin_account = widgets_tree.get_widget("checkbutton_show_admin_account")
        self.checkbutton_no_auto_update = widgets_tree.get_widget("checkbutton_auto_update") # Change to no_auto_update!!!
        self.checkbutton_clear_page_file_at_shutdown = widgets_tree.get_widget("checkbutton_clear_page_file_at_shutdown")
        self.checkbutton_exclude_profile_dirs = widgets_tree.get_widget("checkbutton_exclude_profile_dirs")
        self.entry_exclude_profile_dirs = widgets_tree.get_widget("entry_exclude_profile_dirs")
        self.checkbutton_disable_current_user_run = widgets_tree.get_widget("checkbutton_disable_current_user_run")
        self.checkbutton_disallow_run = widgets_tree.get_widget("checkbutton_disallow_run")
        self.entry_disallow_run = widgets_tree.get_widget("entry_disallow_run")
        self.checkbutton_restrict_run = widgets_tree.get_widget("checkbutton_restrict_run")
        self.entry_restrict_run = widgets_tree.get_widget("entry_restrict_run")
        self.checkbutton_no_ad = widgets_tree.get_widget("checkbutton_no_ad")
        self.checkbutton_no_set_ad = widgets_tree.get_widget("checkbutton_no_set_ad")
        
        # 2nd Column
        self.checkbutton_no_control_panel = widgets_tree.get_widget("checkbutton_no_control_panel")
        self.checkbutton_no_set_folders = widgets_tree.get_widget("checkbutton_no_set_folders")
        self.checkbutton_no_choose_programs_page = widgets_tree.get_widget("checkbutton_no_choose_programs_page")
        self.checkbutton_no_disp_cpl = widgets_tree.get_widget("checkbutton_no_disp_cpl")
        self.checkbutton_no_disp_bg_page = widgets_tree.get_widget("checkbutton_no_disp_bg_page")
        self.checkbutton_no_themes_tab = widgets_tree.get_widget("checkbutton_no_themes_tab")
        self.checkbutton_no_desktop_control_themes = widgets_tree.get_widget("checkbutton_no_desktop_control_themes")
        self.checkbutton_no_change_animation = widgets_tree.get_widget("checkbutton_no_change_animation")
        self.checkbutton_no_disp_settings_page = widgets_tree.get_widget("checkbutton_no_disp_settings_page")
        self.checkbutton_no_disp_scr_sav_page = widgets_tree.get_widget("checkbutton_no_disp_scr_sav_page")
        self.checkbutton_no_disp_appearance_page = widgets_tree.get_widget("checkbutton_no_disp_appearance_page")
        self.checkbutton_no_add_printer = widgets_tree.get_widget("checkbutton_no_add_printer")
        self.checkbutton_no_delete_printer = widgets_tree.get_widget("checkbutton_no_delete_printer")
        self.checkbutton_no_properties_recycle_bin = widgets_tree.get_widget("checkbutton_no_properties_recycle_bin")
        self.checkbutton_no_properties_my_computer = widgets_tree.get_widget("checkbutton_no_properties_my_computer")
        self.checkbutton_no_properties_my_documents = widgets_tree.get_widget("checkbutton_no_properties_my_documents")
        self.checkbutton_scr_sav_is_secure = widgets_tree.get_widget("checkbutton_scr_sav_is_secure")
        self.checkbutton_enforce_shell_extension_security = widgets_tree.get_widget("checkbutton_enforce_shell_extension_security")
        self.checkbutton_wallpaper_image_and_style = widgets_tree.get_widget("checkbutton_wallpaper_image_and_style")
        self.entry_wallpaper_image_and_style = widgets_tree.get_widget("entry_wallpaper_image_and_style")
        self.checkbutton_no_security_tab = widgets_tree.get_widget("checkbutton_no_security_tab")
        self.checkbutton_no_hardware_tab = widgets_tree.get_widget("checkbutton_no_hardware_tab")
        self.checkbutton_no_file_associate = widgets_tree.get_widget("checkbutton_no_file_associate")
        
        # 3rd Column
        self.checkbutton_disable_password_caching = widgets_tree.get_widget("checkbutton_disable_password_caching")
        self.checkbutton_alphanum_passwords = widgets_tree.get_widget("checkbutton_alphanum_passwords")
        self.checkbutton_no_net_connect_disconnect = widgets_tree.get_widget("checkbutton_no_net_connect_disconnect")
        self.checkbutton_no_change_start_menu = widgets_tree.get_widget("checkbutton_no_change_start_menu")
        self.checkbutton_no_run = widgets_tree.get_widget("checkbutton_no_run")
        self.checkbutton_no_set_task_bar = widgets_tree.get_widget("checkbutton_no_set_task_bar")
        self.checkbutton_no_recent_docs_history = widgets_tree.get_widget("checkbutton_no_recent_docs_history")
        self.checkbutton_no_start_menu_music = widgets_tree.get_widget("checkbutton_no_start_menu_music")
        self.checkbutton_no_show_menu_my_pics = widgets_tree.get_widget("checkbutton_no_show_menu_my_pics")
        self.checkbutton_no_faves_menu = widgets_tree.get_widget("checkbutton_no_faves_menu")
        self.checkbutton_change_special_dirs_path = widgets_tree.get_widget("checkbutton_change_special_dirs_path")
        self.entry_change_special_dirs_path = widgets_tree.get_widget("entry_change_special_dirs_path")
        self.checkbutton_prompt_password_on_resume = widgets_tree.get_widget("checkbutton_prompt_password_on_resume")
        self.checkbutton_ie_restrictions = widgets_tree.get_widget("checkbutton_ie_restrictions")
        self.checkbutton_no_desktop_cleanup_wizard = widgets_tree.get_widget("checkbutton_no_desktop_cleanup_wizard")
        self.checkbutton_no_internet_icon = widgets_tree.get_widget("checkbutton_no_internet_icon")
        self.checkbutton_no_view_context_menu = widgets_tree.get_widget("checkbutton_no_view_context_menu")
        self.checkbutton_cancel_registry_imports = widgets_tree.get_widget("checkbutton_cancel_registry_imports")
        self.checkbutton_logon_wallpaper_and_style = widgets_tree.get_widget("checkbutton_logon_wallpaper_and_style")
        self.entry_logon_wallpaper_and_style = widgets_tree.get_widget("entry_logon_wallpaper_and_style")
        self.checkbutton_no_tray_context_menu = widgets_tree.get_widget("checkbutton_no_tray_context_menu")
        self.checkbutton_enable_auto_tray = widgets_tree.get_widget("checkbutton_enable_auto_tray")
        self.checkbutton_no_save_settings = widgets_tree.get_widget("checkbutton_no_save_settings")
        self.checkbutton_show_copy_move_send = widgets_tree.get_widget("checkbutton_show_copy_move_send")
        
        
        # Connect all signals to its respective callbacks.
        widgets_tree.signal_autoconnect(self)
        
        self.window_main.connect("destroy", self.destroy)
        self.window_main.show_all()
    
    def run(self):
        gtk.main()
    
    def destroy(self, widget, data=None):
        gtk.main_quit()
    
    def on_button_about_clicked(self, widget, data=None):
        """Shows about window."""
        
        AboutDialog().run()
    
    def on_button_help_clicked(self, widget, data=None): 
        """Opens system's default browser on GMP3Gain web page."""
        
        webbrowser.open("http://code.google.com/p/windowsregistryfixer/")
    
    def on_checkbutton_cached_logons_count_toggled(self, widget, data=None):
        self.entry_cached_logons_count.set_editable(not self.entry_cached_logons_count.get_editable())
        
        if self.entry_cached_logons_count.get_editable():
            self.window_main.set_focus(self.entry_cached_logons_count)
        
        else:
            self.entry_cached_logons_count.set_text("0")
    
    def on_checkbutton_srv_comment_toggled(self, widget, data=None):
        self.entry_srv_comment.set_editable(not self.entry_srv_comment.get_editable())
        
        if self.entry_srv_comment.get_editable():
            self.window_main.set_focus(self.entry_srv_comment)
        
        else:
            self.entry_srv_comment.set_text("LAN Machine")
    
    def on_checkbutton_welcome_text_toggled(self, widget, data=None):
        self.entry_welcome_text.set_editable(not self.entry_welcome_text.get_editable())
        
        if self.entry_welcome_text.get_editable():
            self.window_main.set_focus(self.entry_welcome_text)
        
        else:
            self.entry_welcome_text.set_text("WRF")
    
    def on_checkbutton_logon_prompt_toggled(self, widget, data=None):
        self.entry_logon_prompt.set_editable(not self.entry_logon_prompt.get_editable())
        
        if self.entry_logon_prompt.get_editable():
            self.window_main.set_focus(self.entry_logon_prompt)
        
        else:
            self.entry_logon_prompt.set_text("Modified with WRF.")
    
    def on_checkbutton_legal_notice_toggled(self, widget, data=None):
        self.entry_logon_prompt.set_editable(not self.entry_legal_notice.get_editable())
        
        if self.entry_legal_notice.get_editable():
            self.window_main.set_focus(self.entry_legal_notice)
        
        else:
            self.entry_legal_notice.set_text("Modified with WRF.")
    
    def on_checkbutton_exclude_profile_dirs_toggled(self, widget, data=None):
        self.entry_exclude_profile_dirs.set_editable(not self.entry_exclude_profile_dirs.get_editable())
        
        if self.entry_exclude_profile_dirs.get_editable():
            self.window_main.set_focus(self.entry_exclude_profile_dirs)
        
        else:
            self.entry_exclude_profile_dirs.set_text("C:\dir1; C:\dir2; etc.")
    
    def on_checkbutton_disallow_run_toggled(self, widget, data=None):
        self.entry_disallow_run.set_editable(not self.entry_disallow_run.get_editable())
        
        if self.entry_disallow_run.get_editable():
            self.checkbutton_restrict_run.set_active(False)
            self.window_main.set_focus(self.entry_disallow_run)
        
        else:
            self.entry_disallow_run.set_text("Calc.exe;Notepad.exe;etc.")
    
    def on_checkbutton_restrict_run_toggled(self, widget, data=None):
        self.entry_restrict_run.set_editable(not self.entry_restrict_run.get_editable())
        
        if self.entry_restrict_run.get_editable():
            self.checkbutton_disallow_run.set_active(False)
            self.window_main.set_focus(self.entry_restrict_run)
        
        else:
            self.entry_restrict_run.set_text("Virus.exe;Trojan.exe;etc.")
    
    def on_checkbutton_wallpaper_image_and_style_toggled(self, widget, data=None):
        self.entry_wallpaper_image_and_style.set_editable(not self.entry_wallpaper_image_and_style.get_editable())
        
        if self.entry_wallpaper_image_and_style.get_editable():
            self.window_main.set_focus(self.entry_wallpaper_image_and_style)
        
        else:
            self.entry_wallpaper_image_and_style.set_text("0;C:\\Wallpaper.bmp;0")
    
    def on_checkbutton_change_special_dirs_path_toggled(self, widget, data=None):
        self.entry_change_special_dirs_path.set_editable(not self.entry_change_special_dirs_path.get_editable())
        
        if self.entry_change_special_dirs_path.get_editable():
            self.window_main.set_focus(self.entry_change_special_dirs_path)
        
        else:
            self.entry_change_special_dirs_path.set_text("Directory;Path")
    
    def on_checkbutton_logon_wallpaper_and_style_toggled(self, widget, data=None):
        self.entry_logon_wallpaper_and_style.set_editable(not self.entry_logon_wallpaper_and_style.get_editable())
        
        if self.entry_logon_wallpaper_and_style.get_editable():
            self.window_main.set_focus(self.entry_logon_wallpaper_and_style)
        
        else:
            self.entry_logon_wallpaper_and_style.set_text("0;C:\\Wallpaper.bmp;0")
    
    def on_button_apply_clicked(self, widget, data=None):
        """Process selected options and generates output file."""
        file = open("wrf.reg", "w+t")  # Open or overwrite a wrf.reg file.
        
        file.write("REGEDIT4\n")
        file.write("% Generated with GWRF.\n\n\n")
        
        # 1st Column
        file.write(wrf.autorun(self.checkbutton_autorun.get_active()) + '\n')

        try:
            file.write(wrf.cached_logons_count(int(self.entry_cached_logons_count.get_text())) + '\n')
        except ValueError:
            print "Cached logons count values must be integers."
                        
        file.write(wrf.delete_roaming_cache(self.checkbutton_delete_roaming_cache.get_active()) + '\n')
        file.write(wrf.srv_comment(self.entry_srv_comment.get_text()) + '\n')
        file.write(wrf.show_admin_tools(self.checkbutton_show_admin_tools.get_active()) + '\n')
        file.write(wrf.dont_disp_last_username(self.checkbutton_dont_disp_last_username.get_active()) + '\n')
        file.write(wrf.welcome_text(self.entry_welcome_text.get_text()) + '\n')
        file.write(wrf.logon_prompt(self.entry_logon_prompt.get_text()) + '\n')
        file.write(wrf.shutdown_without_logon(self.checkbutton_shutdown_without_logon.get_active()) + '\n')
        file.write(wrf.legal_notice(text=self.entry_legal_notice.get_text()) + '\n')
        file.write(wrf.disable_system_recovery_tools(self.checkbutton_disable_system_recovery_tools.get_active()) + '\n')
        file.write(wrf.remove_windows_messenger_from_ie(self.checkbutton_remove_windows_messenger_from_ie.get_active()) + '\n')
        file.write(wrf.icons_visibility(self.checkbutton_icons_visibility.get_active()) + '\n')
        file.write(wrf.show_admin_account(self.checkbutton_show_admin_account.get_active()) + '\n')
        file.write(wrf.no_auto_update(self.checkbutton_no_auto_update.get_active()) + '\n')
        file.write(wrf.clear_page_file_at_shutdown(self.checkbutton_clear_page_file_at_shutdown.get_active()) + '\n')
        file.write(wrf.exclude_profile_dirs(self.entry_exclude_profile_dirs.get_text()) + '\n')
        file.write(wrf.disable_current_user_run(self.checkbutton_disable_current_user_run.get_active()) + '\n')
        file.write(wrf.disallow_run(self.checkbutton_disallow_run.get_active(), self.entry_disallow_run.get_text().split(';')))
        file.write(wrf.restrict_run(self.checkbutton_restrict_run.get_active(), self.entry_restrict_run.get_text().split(';')))
        file.write(wrf.no_ad(self.checkbutton_no_ad.get_active()) + '\n')
        file.write(wrf.no_set_ad(self.checkbutton_no_set_ad.get_active()) + '\n')
        
        # 2nd Column
        file.write(wrf.no_control_panel(self.checkbutton_no_control_panel.get_active()) + '\n')
        file.write(wrf.no_set_folders(self.checkbutton_no_set_folders.get_active()) + '\n')
        file.write(wrf.no_choose_programs_page(self.checkbutton_no_choose_programs_page.get_active()) + '\n')
        file.write(wrf.no_disp_cpl(self.checkbutton_no_disp_cpl.get_active()) + '\n')
        file.write(wrf.no_disp_bg_page(self.checkbutton_no_disp_bg_page.get_active()) + '\n')
        file.write(wrf.no_themes_tab(self.checkbutton_no_themes_tab.get_active()) + '\n')
        file.write(wrf.no_desktop_control_themes(self.checkbutton_no_desktop_control_themes.get_active()) + '\n')
        file.write(wrf.no_change_animation(self.checkbutton_no_change_animation.get_active()) + '\n')
        file.write(wrf.no_disp_settings_page(self.checkbutton_no_disp_settings_page.get_active()) + '\n')
        file.write(wrf.no_disp_scr_sav_page(self.checkbutton_no_disp_scr_sav_page.get_active()) + '\n')
        file.write(wrf.no_disp_appearance_page(self.checkbutton_no_disp_appearance_page.get_active()) + '\n')
        file.write(wrf.no_add_printer(self.checkbutton_no_add_printer.get_active()) + '\n')
        file.write(wrf.no_delete_printer(self.checkbutton_no_delete_printer.get_active()) + '\n')
        file.write(wrf.no_properties_recycle_bin(self.checkbutton_no_properties_recycle_bin.get_active()) + '\n')
        file.write(wrf.no_properties_my_computer(self.checkbutton_no_properties_my_computer.get_active()) + '\n')
        file.write(wrf.no_properties_my_documents(self.checkbutton_no_properties_my_documents.get_active()) + '\n')
        file.write(wrf.scr_sav_is_secure(self.checkbutton_scr_sav_is_secure.get_active()) + '\n')
        file.write(wrf.enforce_shell_extension_security(self.checkbutton_enforce_shell_extension_security.get_active()) + '\n')
        
        if self.checkbutton_wallpaper_image_and_style.get_active():
            try:
                file.write(wrf.wallpaper_image_and_style(self.entry_wallpaper_image_and_style.get_text().split(';')))
            except ValueError:
                print "Tile and stile parameters must be integers."

        file.write(wrf.no_security_tab(self.checkbutton_no_security_tab.get_active()) + '\n')
        file.write(wrf.no_hardware_tab(self.checkbutton_no_hardware_tab.get_active()) + '\n')
        file.write(wrf.no_file_associate(self.checkbutton_no_file_associate.get_active()) + '\n')
        
        # 3rd Column
        file.write(wrf.disable_password_caching(self.checkbutton_disable_password_caching.get_active()) + '\n')
        file.write(wrf.alphanum_passwords(self.checkbutton_alphanum_passwords.get_active()) + '\n')
        file.write(wrf.no_net_connect_disconnect(self.checkbutton_no_net_connect_disconnect.get_active()) + '\n')
        file.write(wrf.no_change_start_menu(self.checkbutton_no_change_start_menu.get_active()) + '\n')
        file.write(wrf.no_run(self.checkbutton_no_run.get_active()) + '\n')
        file.write(wrf.no_set_task_bar(self.checkbutton_no_set_task_bar.get_active()) + '\n')
        file.write(wrf.no_recent_docs_history(self.checkbutton_no_recent_docs_history.get_active()) + '\n')
        file.write(wrf.no_start_menu_music(self.checkbutton_no_start_menu_music.get_active()) + '\n')
        file.write(wrf.no_show_menu_my_pics(self.checkbutton_no_show_menu_my_pics.get_active()) + '\n')
        file.write(wrf.no_faves_menu(self.checkbutton_no_faves_menu.get_active()) + '\n')
        
        if self.checkbutton_change_special_dirs_path.get_active():
            file.write(wrf.change_special_dirs_path(self.entry_change_special_dirs_path.get_text().split(';')))
        
        file.write(wrf.prompt_password_on_resume(self.checkbutton_prompt_password_on_resume.get_active()) + '\n')
        file.write(wrf.ie_restrictions(self.checkbutton_ie_restrictions.get_active()) + '\n')
        file.write(wrf.no_desktop_cleanup_wizard(self.checkbutton_no_desktop_cleanup_wizard.get_active()) + '\n')
        file.write(wrf.no_internet_icon(self.checkbutton_no_internet_icon.get_active()) + '\n')
        file.write(wrf.no_view_context_menu(self.checkbutton_no_view_context_menu.get_active()) + '\n')
        file.write(wrf.cancel_registry_imports(self.checkbutton_cancel_registry_imports.get_active()) + '\n')
        
        if self.checkbutton_logon_wallpaper_and_style.get_active():
            try:
                file.write(wrf.logon_wallpaper_and_style(self.entry_logon_wallpaper_and_style.get_text().split(';')))
            except ValueError:
                print "Tile and stile parameters must be integers."
        
        file.write(wrf.no_tray_context_menu(self.checkbutton_no_tray_context_menu.get_active()) + '\n')
        file.write(wrf.enable_auto_tray(self.checkbutton_enable_auto_tray.get_active()) + '\n')
        file.write(wrf.no_save_settings(self.checkbutton_no_save_settings.get_active()) + '\n')
        file.write(wrf.show_copy_move_send(self.checkbutton_show_copy_move_send.get_active()) + '\n')
        
        file.write("\n\n% EOF")
        
        file.close()  # Closes generated file.
        
        
# 
# Main
# 

if __name__ == "__main__":
    mainwindow = MainWindow()
    mainwindow.run()

