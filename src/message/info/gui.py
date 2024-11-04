#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from PyQt6.QtWidgets import QMessageBox
from skl_shared_qt.localize import _


class Message(QMessageBox):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_gui()
        
    def set_message(self, message):
        self.setText(message)
    
    def set_title(self):
        self.setWindowTitle(_('Info'))
        
    def set_icon(self):
        self.setIcon(QMessageBox.Icon.Information)
    
    def set_gui(self):
        self.set_title()
        self.set_icon()
    
    def show_blocked(self):
        self.exec()


INFO = Message()