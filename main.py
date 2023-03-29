import wx
import wx.html # old, doesn't support css and javascript
import wx.html2 # modern supports css and javascript

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="HTML Panel App")
        
        # Create HTML panel
        self.html_panel = wx.html2.WebView.New(self)
        # self.html_panel = wx.html.HtmlWindow(self)
        
        # Create text entry area
        self.text_entry = wx.TextCtrl(self)
        
        # Create vertical sizer to stack panels
        self.vert_sizer = wx.BoxSizer(wx.VERTICAL)
        self.vert_sizer.Add(self.html_panel, 1, wx.EXPAND)
        self.vert_sizer.Add(self.text_entry, 0, wx.EXPAND)
        
        # Set main sizer for frame
        self.SetSizer(self.vert_sizer)
        
        # Load initial HTML content
        self.html_panel.SetPage("<html><body><h1>Hello, World!</h1></body></html>", "")
        # self.html_panel.SetPage("<html><body><h1>Hello, World!</h1></body></html>")

def run():
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()
    
if __name__ == '__main__':
    run()

