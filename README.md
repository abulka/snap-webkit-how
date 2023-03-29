# snap-webkit-how

How to snap wxPython app which uses webkit?

This repo is a minimal example of a wxPython app which uses the webkit based html wxPython widget ` wx.html2.WebView`.  It runs fine when run with `python3 main.py` but when snapped, it crashes. 

Reported to
https://forum.snapcraft.io/t/how-to-snap-wxpython-app-which-uses-webkit/34517

## Problem

How do I stage webkit incl. something called `WebKitNetworkProcess` with my wxPython app which uses the webkit based html wxPython widget ` wx.html2.WebView`.  

Staging `libwebkit2gtk-4.0-37` doesn't seem to be enough and doesn't supply the file `WebKitNetworkProcess`. My snap always crashes with
```
$ snap-webkit-how.gitm

** (gitm:116459): ERROR **: 22:42:28.444: 
Unable to spawn a new child process: 
Failed to spawn child process “/usr/lib/x86_64-linux-gnu/webkit2gtk-4.0/WebKitNetworkProcess” (No such file or directory)
```

# Repro on Ubuntu 22.04
1. Run `python3 main.py` and see it runs ok.
2. Build and install the snap, run ` snap-webkit-how.gitm` and watch it crash

## main.py
Here is a barebones example, `main.py` which runs OK `python3 main.py`  but when snapped, crashes.
```python
import wx
import wx.html # old, doesn't support css and javascript
import wx.html2 # modern, webkit, supports css and javascript

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="HTML Panel App")
        
        # Create HTML panel
        self.html_panel = wx.html2.WebView.New(self) # fails in snap, causes Failed to spawn child process “/usr/lib/x86_64-linux-gnu/webkit2gtk-4.0/WebKitNetworkProcess” (No such file or directory)
        # self.html_panel = wx.html.HtmlWindow(self) # worksin snap
        
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
```

## setup.py
```python
import os
from setuptools import setup, find_packages
import sys
setup(
    name='snap-webkit-how',
    version='1.0.0',
    url='https://github.com/blah/snap-webkit-how',
    author='Blah',
    author_email='blah@gmail.com',
    py_modules=['main'],
    entry_points={
        'console_scripts': [
            'gitm=main:run',
        ],
    },    
)
```
## snapcraft.yaml
```yaml
# Requires snapcraft snapcraft 7.3.1.post21+gitfa823013 from edge or later to build this snap
name: snap-webkit-how
version: git
summary: 'Blah'
description: |
     Blah blah:

grade: stable
confinement: devmode
base: core22
architectures:
  - build-on: [amd64]

apps:
  gitm:
    command: bin/gitm
    plugs:
      - desktop
      - desktop-legacy
      - x11
      - home
      - gsettings
      - network
      - network-bind
      - removable-media
    extensions:
      - gnome

parts:
  build-the-python-stuff-please:
    plugin: python
    source: .
    stage-packages:
      - libwebkit2gtk-4.0-37
      - libsdl2-2.0-0
    python-packages:
      - https://extras.wxpython.org/wxPython4/extras/linux/gtk3/ubuntu-22.04/wxPython-4.2.0-cp310-cp310-linux_x86_64.whl
```
