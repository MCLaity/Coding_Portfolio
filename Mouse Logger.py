
from pynput.mouse import Listener
def on_move(x, y):
    print('Mouse moved to {0}'.format((x, y)))                                     #something about curley brackets and string exeptions
    

def on_click(x, y, button, pressed):   
    print('{0} at {1}'.format('pressed' if pressed else 'released',(x, y)))
    
    click_location = (x,y)  #actually prints the location of the mouse when clicked
    print('Click location =',click_location) 
    
    
    print('exeted listener')
    Listener.stop()                                                                 #Gotta remember the cap

def on_scroll(x, y, dx, dy ):
    print('mouse scrolled {0} at {1}'.format('down' if dy < 0 else 'up',(x, y)))

with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as Listener:
    Listener.join()


input('press ENTER to exit')
