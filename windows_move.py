import win32gui, win32api,os

class SlidingWindow():
    def __init__(self, Name, Range):
        self.x_move=True
        self.y_move=True
        self.Name=Name
        self.Range=Range
    
    def sliding_window(self, hwnd, lPara):
        print(self.x_move, self.y_move)
        if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd)==self.Name:
            rect=win32gui.GetWindowRect(hwnd)
            x1, y1, x2, y2=rect[0], rect[1], rect[2], rect[3]
            w, h=x2-x1, y2-y1

            if x1<=0: self.x_move=True
            if x2>=win32api.GetSystemMetrics(0): self.x_move=False
            if y1<=0: self.y_move=True
            if y2>=win32api.GetSystemMetrics(1): self.y_move=False

            if self.x_move and self.y_move: win32gui.MoveWindow(hwnd, x1+self.Range, y1+self.Range, w, h, True)
            if self.x_move and not self.y_move: win32gui.MoveWindow(hwnd, x1+self.Range, y1-self.Range, w, h, True)
            if not self.x_move and self.y_move: win32gui.MoveWindow(hwnd, x1-self.Range, y1+self.Range, w, h, True)
            if not self.x_move and not self.y_move: win32gui.MoveWindow(hwnd, x1-self.Range, y1-self.Range, w, h, True)

def show_name():
    ls=list()
    def sub_function(hwnd, lParm):
        if win32gui.IsWindowVisible(hwnd):
            ls.append(win32gui.GetWindowText(hwnd))
    win32gui.EnumWindows(sub_function, None)
    for i in set(ls): print(i)

if __name__=='__main__':
    #show_name()
	
    path, filename = os.path.split(os.path.abspath(__file__))
    str1= path.split('\\')

    sw=SlidingWindow('SlidingWindow', 3)
    sw2=SlidingWindow(str1[len(str1)-1], 3)
    while True:
        win32gui.EnumWindows(sw.sliding_window, None)
        win32gui.EnumWindows(sw2.sliding_window, None)