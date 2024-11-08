#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import sys
from PyQt6.QtWidgets import QApplication


class Root:
    
    def __init__(self):
        self.widget = QApplication(sys.argv)
    
    def get_clipboard(self):
        return self.widget.clipboard()
    
    def end(self):
        sys.exit(self.widget.exec())