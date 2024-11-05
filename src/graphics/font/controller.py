#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from skl_shared_qt.localize import _
import skl_shared_qt.message.controller as ms


class Font:
    
    def __init__(self, widget, family, size):
        self.Success = True
        self.font = None
        self.family = ''
        self.gui = gi.Font()
        self.widget = widget
        self.family = family
        self.size = size
        self.check()
    
    def fail(self, f, e):
        self.Success = False
        mes = _('Third-party module has failed!\n\nDetails: {}').format(e)
        ms.Message(f, mes, True).show_error()
    
    def set_parent(self):
        f = '[SharedQt] graphics.font.controller.Font.set_parent'
        if not self.Success:
            ms.rep.cancel(f)
            return
        try:
            self.gui.set_parent(self.widget, self.font)
        except Exception as e:
            self.fail(f, e)
    
    def set_family(self):
        f = '[SharedQt] graphics.font.controller.Font.set_family'
        if not self.Success:
            ms.rep.cancel(f)
            return
        try:
            self.gui.set_family(self.font, self.family)
        except Exception as e:
            self.fail(f, e)
    
    def set_size(self):
        f = '[SharedQt] graphics.font.controller.Font.set_size'
        if not self.Success:
            ms.rep.cancel(f)
            return
        try:
            self.gui.set_size(self.font, self.size)
        except Exception as e:
            self.fail(f, e)
    
    def set_font(self):
        f = '[SharedQt] graphics.font.controller.Font.set_font'
        if not self.Success:
            ms.rep.cancel(f)
            return
        try:
            self.font = self.gui.get_font()
        except Exception as e:
            self.fail(f, e)
        
    def check(self):
        f = '[SharedQt] graphics.font.controller.Font.check'
        if not self.widget:
            ms.rep.empty(f)
            self.Success = False
            return
        if not self.family:
            ms.rep.empty(f)
            self.Success = False
            return
        if not self.size:
            ms.rep.empty(f)
            self.Success = False
            return
    
    def run(self):
        self.set_font()
        self.set_family()
        self.set_size()
        self.set_parent()