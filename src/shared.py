#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from skl_shared_qt.localize import _
import skl_shared_qt.logic as lg
import skl_shared_qt.gui as gi
import skl_shared_qt.message.controller as ms

FONT1 = 'Serif 14'
FONT2 = 'Sans 11'


class Debug:

    def __init__(self, func='__main__', mes=''):
        self.set_gui()
        if mes:
            self.reset(func, mes)
    
    def reset(self, func, mes):
        self.set_title(func)
        self.fill(mes)
    
    def set_gui(self):
        self.gui = gi.Debug()
        self.gui.set_icon()
        self.set_bindings()
    
    def set_bindings(self):
        self.gui.bind(('Escape',), self.close)
    
    def fill(self, text):
        self.gui.fill(text)
    
    def set_title(self, title):
        self.gui.set_title(title)
    
    def show(self):
        self.gui.show_maximized()
    
    def close(self):
        self.gui.close()



class FileDialog:
    
    def __init__(self, parent=None, filter_='', folder='', caption=''):
        self.parent = parent
        self.filter = filter_
        self.folder = folder
        self.caption = caption
        self.set_folder()
        self.set_filter()
        self.gui = gi.FileDialog(self.parent)
        self.gui.set_parent()
        self.gui.set_icon()
    
    def set_folder(self):
        if not self.folder or not Directory(self.folder).Success:
            self.folder = Home().get_home()
    
    def set_filter(self):
        if not self.filter:
            self.filter = _('All files (*.*)')
    
    def save(self):
        if not self.caption:
            self.caption = _('Save File As:')
        try:
            file = self.gui.save (caption = self.caption
                                 ,folder = self.folder
                                 ,filter_ = self.filter
                                 )
        except Exception as e:
            com.rep_third_party(f, e)
        return file



class ProgressBar:
    
    def __init__(self, *args, **kwargs):
        pass
    
    def set_text(self, text=None):
        pass
    
    def set_title(self, text=''):
        pass
    
    def add(self):
        pass
    
    def show(self):
        pass
    
    def close(self):
        pass
    
    def update(self, count, limit):
        #f = '[SharedQt] shared.ProgressBar.update'
        pass



class Top:

    def __init__(self, title='', icon=''):
        self.gui = gi.Top()
        self.widget = self.gui.widget
        self.title = title
        self.icon = icon
    
    def add_widget(self, item):
        f = '[SharedQt] shared.Top.add_widget'
        if hasattr(item, 'widget'):
            self.gui.add_widget(item.widget)
        else:
            mes = _('Wrong input data!')
            ms.Message(f, mes).show_error()
    
    def show(self):
        self.gui.show()
    
    def close(self):
        self.gui.close()
    
    def bind(self, hotkeys, action):
        self.gui.bind(hotkeys, action)



class TestTop(Top):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_bindings()
    
    def set_bindings(self):
        self.bind(('Ctrl+Q',), self.close)
        self.bind(('Esc',), self.close)



class OptionMenu:
    
    def __init__ (self, items=[], default=None, font_family=None
                 ,font_size=None, action=None):
        self.items = []
        self.action = action
        self.gui = gi.OptionMenu()
        self.widget = self.gui.widget
        # Qt changes default font family upon receiving None
        if font_family and font_size:
            self.gui.set_font(font_family, font_size)
        if items:
            self.reset(items, default)
        self.set_action()
        
    def set_action(self, action=None):
        if action:
            self.action = action
        if self.action:
            self.widget.activated.connect(self.action)
    
    def change_font_size(self, delta=1):
        f = '[SharedQt] shared.OptionMenu.change_font_size'
        size = self.gui.get_font_size()
        if not size:
            com.rep_empty(f)
            return
        if size + delta <= 0:
            mes = f'{size} + {delta} > 0'
            com.rep_condition(f, mes)
            return
        self.gui.set_font_size(size+delta)
    
    def enable(self):
        self.gui.enable()
    
    def disable(self):
        self.gui.disable()
        
    def set(self, item):
        f = '[SharedQt] shared.OptionMenu.set'
        item = str(item)
        if item in self.items:
            self.gui.set(item)
        else:
            mes = _('An unknown mode "{}"!\n\nThe following modes are supported: "{}".')
            mes = mes.format(item, '; '.join(self.items))
            ms.Message(f, mes, True).show_error()
    
    def fill(self):
        self.gui.fill(self.items)

    def reset(self, items=[], default=None):
        self.items = [str(item) for item in items]
        self.fill()
        if default is not None:
            self.set(default)
        if len(self.items) < 2:
            self.disable()
        else:
            self.enable()

    def get(self):
        return self.gui.get()
    
    def get_index(self):
        return self.gui.get_index()
    
    def set_index(self, index_):
        return self.gui.set_index(index_)

    def set_prev(self):
        index_ = self.get_index()
        if index_ == 0:
            index_ = len(self.items) - 1
        else:
            index_ -= 1
        self.set_index(index_)

    def set_next(self):
        index_ = self.get_index()
        if index_ == len(self.items) - 1:
            index_ = 0
        else:
            index_ += 1
        self.set_index(index_)



class Directory(lg.Directory):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



class Email(lg.Email):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



class FastTable(lg.FastTable):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



class File(lg.File):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



class Get(lg.Get):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



class Home(lg.Home):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



class Input(lg.Input):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



class Launch(lg.Launch):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



class List(lg.List):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



class OSSpecific(lg.OSSpecific):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



class Online(lg.Online):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



class ProgramDir(lg.ProgramDir):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



class Path(lg.Path):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



class ReadTextFile(lg.ReadTextFile):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



class Search(lg.Search):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



class Text(lg.Text):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



class Time(lg.Time):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



class Timer(lg.Timer):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



class WriteTextFile(lg.WriteTextFile):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



class Objects(lg.Objects):
    
    def __init__(self):
        ''' #NOTE: Since we use 'super' here, attributes of 'lg.Objects'
            set directly in the controller will not be reflected in
            'logic'. Use 'logic' methods to set attributes.
        '''
        super().__init__()
        self.question = self.info = self.warning = self.debug = self.error \
                      = self.mes = self.waitbox = None
    
    def get_waitbox(self, icon=''):
        if self.waitbox is None:
            if not icon:
                icon = self.icon
            #TODO: Implement
            self.waitbox = None
            #self.waitbox = WaitBox(icon)
        return self.waitbox

    

class Commands(lg.Commands):
    
    def __init__(self):
        super().__init__()
        
    def get_image(self, path, width, height):
        f = '[SharedQt] shared.Commands.get_image'
        try:
            return gi.com.get_image (path = path
                                    ,width = width
                                    ,height = height
                                    )
        except Exception as e:
            mes = _('Third-party module has failed!\n\nDetails: {}').format(e)
            ms.Message(f, mes).show_warning()
    
    def start(self):
        gi.objs.start()
    
    def end(self):
        gi.objs.end()


com = Commands()
objs = Objects()


if __name__ == '__main__':
    f = '[SharedQt] shared.__main__'
    com.start()
    #lg.ReadTextFile('/tmp/aaa').get()
    #Geometry(Top()).activate()
    #idebug = Debug(f, 'Here should be some debug info')
    # This MUST be on a separate line, the widget will not be shown otherwise
    #idebug.show()
    Graphical = True
    Block = False
    '''
    mes = 'This is a standard message.'
    ms.Message(f, mes, Graphical).show_info()
    mes = 'Here should be some debug info'
    ms.Message(f, mes, Graphical).show_debug()
    mes = 'This is a warning'
    ms.Message(f, mes, Graphical).show_warning()
    mes = 'And this is an error!'
    ms.Message(f, mes, Graphical).show_error()
    '''
    mes = 'Have you read this?'
    answer = ms.Message(f, mes, Graphical, False).show_question()
    if answer:
        answer = 'Yes'
    else:
        answer = 'No'
    mes = f'Your answer is {answer}'
    ms.Message(f, mes, True).show_debug()
    # To quit correctly, the last GUI message must be non-blocking
    com.end()
