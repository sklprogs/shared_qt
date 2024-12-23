#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from skl_shared_qt.message.controller import rep
from skl_shared_qt.graphics.clipboard.gui import Clipboard as guiClipboard


class Clipboard:

    def __init__(self, Graphical=True):
        self.Graphical = Graphical
        self.gui = guiClipboard()

    def copy(self, text, CopyEmpty=True):
        f = '[SharedQt] graphics.clipboard.controller.Clipboard.copy'
        if not (text or CopyEmpty):
            rep.empty(f, self.Graphical)
            return
        try:
            self.gui.copy(text)
        except Exception as e:
            rep.failed(f, e, self.Graphical)

    def paste(self):
        f = '[SharedQt] graphics.clipboard.controller.Clipboard.paste'
        try:
            text = self.gui.paste()
        except Exception as e:
            text = ''
            rep.failed(f, e, self.Graphical)
        # Further possible actions: strip, delete double line breaks
        return text


CLIPBOARD = Clipboard()
