#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import PyQt5
import PyQt5.QtWidgets
from skl_shared_qt.localize import _
import skl_shared_qt.shared as sh


class OptionMenu:
    
    def __init__(self,parent):
        self.parent = parent
        self.widget = PyQt5.QtWidgets.QComboBox(self.parent)
    
    def enable(self):
        self.widget.setEnabled(True)
    
    def disable(self):
        self.widget.setEnabled(False)
        
    def set(self,item):
        self.widget.setCurrentText(item)
    
    def fill(self,items):
        self.widget.clear()
        self.widget.addItems(items)

    def get(self):
        return self.widget.currentText()
    
    def get_index(self):
        return self.widget.currentIndex()
    
    def set_index(self,index_):
        return self.widget.setCurrentIndex(index_)



class Button:
    
    def __init__ (self,parent,text='',action=None,width=36
                 ,height=36,hint='',active='',inactive=''
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
        self.widget.resize(self.width,self.height)
    
    def set_icon(self):
        ''' Setting a button image with
            button.setStyleSheet('image: url({})'.format(path)) causes
            tooltip glitches.
        '''
        if self.icon:
            self.widget.setIcon(PyQt5.QtGui.QIcon(self.icon))
    
    def set_size(self):
        if self.width and self.height:
            self.widget.setIconSize(PyQt5.QtCore.QSize(self.width,self.height))
    
    def set_border(self):
        if self.icon:
            self.widget.setStyleSheet('border: 0px')
    
    def set_action(self):
        if self.action:
            self.widget.clicked.connect(self.action)
    
    def set_gui(self):
        self.widget = PyQt5.QtWidgets.QPushButton(self.text,self.parent)
        self.resize()
        self.set_icon()
        self.set_size()
        self.set_border()
        self.set_hint()
        self.set_action()



class Commands:
    
    def get_image(self,path,width,height):
        return tk.PhotoImage (file = path
                             ,master = objs.get_root().widget
                             ,width = width
                             ,height = height
                             )
        
    def get_mod_color(self,color):
        try:
            return objs.get_root().widget.winfo_rgb(color=color)
        except tk._tkinter.TclError:
            pass
    
    def show_save_dialog(self,options=()):
        return tkinter.filedialog.asksaveasfilename(**options)
    
    def bind(self,obj,binding,action):
        try:
            obj.widget.bind(binding,action)
            return True
        except tk.TclError:
            pass



class MessageBuilder:
    ''' Not using tkinter.messagebox because it blocks main GUI (even
        if we specify a non-root parent).
    '''
    def __init__(self,parent):
        self.parent = parent
        self.widget = self.parent.widget
    
    def show(self,event=None):
        self.parent.show()
    
    def close(self,event=None):
        self.parent.close()
    
    def set_image(self,path,obj):
        ''' Without explicitly indicating 'master', we get
            "image pyimage1 doesn't exist".
        '''
        return tk.PhotoImage (master = obj.widget
                             ,file = path
                             )
        
    def set_title(self,text=''):
        self.parent.set_title(text)
        
    def set_icon(self,path):
        self.parent.set_icon(path)



class Objects:

    def __init__(self):
        self.root = self.warning = self.error = self.question \
                  = self.info = self.entry = None
    
    def get_root(self,Close=True):
        if not self.root:
            self.root = Root()
            if Close:
                self.root.close()
        return self.root

    def start(self,Close=True):
        self.get_root(Close=Close)

    def end(self):
        self.get_root().kill()
        self.root.run()

    def get_warning(self):
        if not self.warning:
            self.warning = MessageBuilder (parent = self.get_root()
                                          ,level = _('WARNING')
                                          )
        return self.warning

    def get_error(self):
        if not self.error:
            self.error = MessageBuilder (parent = self.get_root()
                                        ,level = _('ERROR')
                                        )
        return self.error

    def get_question(self):
        if not self.question:
            self.question = MessageBuilder (parent = self.get_root()
                                           ,level = _('QUESTION')
                                           )
        return self.question

    def get_info(self):
        if not self.info:
            self.info = MessageBuilder (parent = self.get_root()
                                       ,level = _('INFO')
                                       )
        return self.info



''' If there are problems with import or tkinter's wait_variable, put
    this beneath 'if __name__'
'''
objs = Objects()
com = Commands()


if __name__ == '__main__':
    objs.start()
    objs.end()
