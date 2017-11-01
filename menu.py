class Item:
    def __init__(self,label,func, *args):
        self.label = label
        self.func = func
        self.args = args

        
    def call_func(self):
        return self.func(self.args)

    
class Menu:
    def __init__(self,items):
        self.items = items


    def display(self):
        while True:
            for i,val in enumerate(self.items):
                print '[%s] %s' % (i,val.label)
            inp = raw_input('Select option: ')
            try:
                sel = int(inp)
                items[sel].call_func()
            except ValueError:
                print('Invalid input')
                continue
            

def print_arg(arg):
    print(arg)

    
items = [Item('print a',print_arg,'a'),Item('print b',print_arg,'b')]
m = Menu(items)
m.display()
