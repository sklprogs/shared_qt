#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import sys
import PyQt5
import PyQt5.QtWidgets
from skl_shared_qt.localize import _


ICON = ''


class Debug(PyQt5.QtWidgets.QWidget):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_gui()
    
    def set_icon(self):
        # Does not accent None
        self.setWindowIcon(objs.get_icon())
    
    def centralize(self):
        self.move(objs.get_root().desktop().screen().rect().center() - self.rect().center())
    
    def fill(self, text):
        self.textbox.clear()
        self.cursor.insertText(text, self.char_fmt)
        self.textbox.moveCursor(self.cursor.Start)
    
    def set_title(self, title):
        self.setWindowTitle(title)
    
    def set_layout(self):
        self.layout_ = PyQt5.QtWidgets.QVBoxLayout()
        self.layout_.setContentsMargins(0, 0, 0, 0)
    
    def set_gui(self):
        self.set_layout()
        self.textbox = PyQt5.QtWidgets.QTextEdit()
        self.doc = PyQt5.QtGui.QTextDocument()
        self.cursor = PyQt5.QtGui.QTextCursor(self.doc)
        self.char_fmt = self.cursor.charFormat()
        self.textbox.setDocument(self.doc)
        self.textbox.setReadOnly(True)
        self.font = PyQt5.QtGui.QFont('Mono', 11)
        self.char_fmt.setFont(self.font)
        self.layout_.addWidget(self.textbox)
        self.setLayout(self.layout_)
    
    def bind(self, hotkeys, action):
        for hotkey in hotkeys:
            PyQt5.QtWidgets.QShortcut(PyQt5.QtGui.QKeySequence(hotkey), self).activated.connect(action)
    
    def show_maximized(self):
        self.showMaximized()



class Color:
    
    def __init__(self, color):
        ''' This accepts everything without exceptions - None, '', hex value,
            color name, even gibberish. Default color is black.
        '''
        self.qcolor = PyQt5.QtGui.QColor(color)
    
    def get_hex(self):
        return self.qcolor.name()
    
    def modify(self, factor):
        darker = self.qcolor.darker(factor).name()
        lighter = self.qcolor.lighter(factor).name()
        return(darker, lighter)



class FileDialog:
    
    def __init__(self, parent=None):
        #NOTE: A widget is required here, not a wrapper
        self.parent = parent
    
    def set_icon(self):
        self.parent.setWindowIcon(objs.get_icon())
    
    def set_parent(self):
        if not self.parent:
            self.parent = PyQt5.QtWidgets.QWidget()
    
    def save(self, caption, folder, filter_):
        # Empty output is ('', '')
        return PyQt5.QtWidgets.QFileDialog.getSaveFileName (parent = self.parent
                                                           ,caption = caption
                                                           ,directory = folder
                                                           ,filter = filter_
                                                           )[0]



class Clipboard:
    
    def __init__(self):
        self.clipboard = objs.get_root().clipboard()
    
    def copy(self, text):
        self.clipboard.setText(text)
    
    def paste(self):
        return self.clipboard.text()



class Font:
    
    def get_font(self):
        return PyQt5.QtGui.QFont()
    
    def set_parent(self, widget, ifont):
        widget.setFont(ifont)
    
    def set_family(self, ifont, family):
        ifont.setFamily(family)
    
    def set_size(self, ifont, size):
        ifont.setPointSize(size)



class Entry:
    
    def __init__(self, parent=None):
        self.parent = None
        self.set_gui()
    
    def get_width(self):
        return self.widget.width()
    
    def get_root_y(self):
        return self.widget.frameGeometry().y()
    
    def get_x(self):
        return self.widget.pos().x()
    
    def set_min_width(self, width):
        self.widget.setMinimumWidth(width)
    
    def set_max_width(self, width):
        self.widget.setMaximumWidth(width)
    
    def bind(self, hotkeys, action):
        for hotkey in hotkeys:
            PyQt5.QtWidgets.QShortcut(PyQt5.QtGui.QKeySequence(hotkey), self).activated.connect(action)
    
    def set_gui(self):
        self.widget = PyQt5.QtWidgets.QLineEdit(self.parent)
    
    def clear(self):
        self.widget.clear()
    
    def get(self):
        return self.widget.text()
    
    def insert(self, text):
        self.widget.insert(text)
    
    def set_text(self, text):
        self.widget.setText(text)
    
    def focus(self):
        self.widget.setFocus()



class Top(PyQt5.QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_gui()
    
    def add_widget(self, widget):
        self.layout.addWidget(widget)
    
    def bind(self, hotkeys, action):
        for hotkey in hotkeys:
            PyQt5.QtWidgets.QShortcut(PyQt5.QtGui.QKeySequence(hotkey), self).activated.connect(action)
    
    def set_gui(self):
        self.widget = self
        self.layout = PyQt5.QtWidgets.QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)



class OptionMenu:
    
    def __init__(self):
        self.widget = PyQt5.QtWidgets.QComboBox()
    
    def get_font_size(self):
        size = self.widget.font().pointSize()
        # We will get -1 if the font size was specified in pixels
        if size > 0:
            return size
    
    def set_font_size(self, size):
        qfont = self.widget.font()
        qfont.setPointSize(size)
        self.widget.setFont(qfont)
    
    def set_font(self, family, size):
        self.widget.setFont(PyQt5.QtGui.QFont(family, size))
    
    def enable(self):
        self.widget.setEnabled(True)
    
    def disable(self):
        self.widget.setEnabled(False)
        
    def set(self, item):
        self.widget.setCurrentText(item)
    
    def fill(self, items):
        self.widget.clear()
        self.widget.addItems(items)

    def get(self):
        return self.widget.currentText()
    
    def get_index(self):
        return self.widget.currentIndex()
    
    def set_index(self, index_):
        return self.widget.setCurrentIndex(index_)



class Button:
    
    def __init__ (self, text='', action=None, parent=None, width=36, height=36
                 ,hint='' ,active='', inactive=''
                 ):
        self.Status = False
        self.parent = parent
        self.text = text
        self.action = action
        self.width = width
        self.height = height
        self.hint = hint
        self.active = active
        self.icon = self.inactive = inactive
        self.set_gui()
    
    def activate(self):
        if not self.Status:
            self.Status = True
            self.icon = self.active
            self.set_icon()

    def inactivate(self):
        if self.Status:
            self.Status = False
            self.icon = self.inactive
            self.set_icon()
    
    def set_hint(self):
        if self.hint:
            self.widget.setToolTip(self.hint)
    
    def resize(self):
        self.widget.resize(self.width, self.height)
    
    def set_icon(self):
        ''' Setting a button image with
            button.setStyleSheet('image: url({})'.format(path)) causes
            tooltip glitches.
        '''
        if self.icon:
            self.widget.setIcon(PyQt5.QtGui.QIcon(self.icon))
    
    def set_size(self):
        if self.width and self.height:
            self.widget.setIconSize(PyQt5.QtCore.QSize(self.width, self.height))
    
    def set_border(self):
        if self.icon:
            self.widget.setStyleSheet('border: 0px')
    
    def set_action(self, action=None):
        if action:
            self.action = action
        if self.action:
            self.widget.clicked.connect(self.action)
    
    def set_gui(self):
        self.widget = PyQt5.QtWidgets.QPushButton(self.text, self.parent)
        self.resize()
        self.set_icon()
        self.set_size()
        #FIX: this may cause the button to not show itself in complex widgets
        self.set_border()
        self.set_hint()
        self.set_action()




class Message(PyQt5.QtWidgets.QMessageBox):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def set_text(self, text):
        self.setText(text)
    
    def set_title(self, text):
        self.setWindowTitle(text)
        
    def set_icon(self, obj):
        self.setIcon(obj)
    
    def get_error(self):
        self.set_title(_('Error'))
        self.set_icon(PyQt5.QtWidgets.QMessageBox.Critical)
        return self
    
    def get_warning(self):
        self.set_title(_('Warning'))
        self.set_icon(PyQt5.QtWidgets.QMessageBox.Warning)
        return self
    
    def get_info(self):
        self.set_title(_('Info'))
        self.set_icon(PyQt5.QtWidgets.QMessageBox.Information)
        return self
    
    def get_debug(self):
        self.set_title(_('Debug'))
        self.set_icon(PyQt5.QtWidgets.QMessageBox.Information)
        return self
    
    def get_question(self):
        self.set_title(_('Question'))
        self.set_icon(PyQt5.QtWidgets.QMessageBox.Question)
        return self



class Objects:

    def __init__(self):
        self.root = self.warning = self.error = self.question \
                  = self.info = self.entry = self.icon = None
    
    def get_icon(self):
        if self.icon is None:
            self.icon = PyQt5.QtGui.QIcon(ICON)
        return self.icon
    
    def get_root(self):
        if self.root is None:
            self.root = PyQt5.QtWidgets.QApplication(sys.argv)
        return self.root

    def start(self):
        self.get_root()

    def end(self):
        sys.exit(self.root.exec_())

    def get_warning(self):
        if self.warning is None:
            self.warning = Message().get_warning()
        return self.warning

    def get_error(self):
        if self.error is None:
            self.error = Message().get_error()
        return self.error

    def get_question(self):
        if self.question is None:
            self.question = Message().get_question()
        return self.question

    def get_info(self):
        if self.info is None:
            self.info = Message().get_info()
        return self.info



class CheckBox:
    
    def __init__(self):
        self.set_gui()
    
    def get_font_size(self):
        size = self.widget.font().pointSize()
        # We will get -1 if the font size was specified in pixels
        if size > 0:
            return size
    
    def set_font_size(self, size):
        qfont = self.widget.font()
        qfont.setPointSize(size)
        self.widget.setFont(qfont)
    
    def set_gui(self):
        self.widget = PyQt5.QtWidgets.QCheckBox()
    
    def set_font(self, family, size):
        self.widget.setFont(PyQt5.QtGui.QFont(family, size))
    
    def get(self):
        return self.widget.isChecked()
    
    def enable(self):
        self.widget.setChecked(True)
    
    def disable(self):
        self.widget.setChecked(False)
    
    def toggle(self):
        if self.get():
            self.disable()
        else:
            self.enable()
    
    def set_text(self, text=''):
        if text:
            self.widget.setText(text)



class Label:
    
    def __init__(self):
        self.set_gui()
    
    def get_font_size(self):
        size = self.widget.font().pointSize()
        # We will get -1 if the font size was specified in pixels
        if size > 0:
            return size
    
    def set_font_size(self, size):
        qfont = self.widget.font()
        qfont.setPointSize(size)
        self.widget.setFont(qfont)
    
    def set_gui(self):
        self.widget = PyQt5.QtWidgets.QLabel()
    
    def set_text(self, text):
        self.widget.setText(text)
    
    def set_font(self, family, size):
        self.widget.setFont(PyQt5.QtGui.QFont(family, size))



''' If there are issues with import or tkinter's wait_variable, put this
    beneath 'if __name__'.
'''
objs = Objects()


if __name__ == '__main__':
    objs.start()
    objs.end()
