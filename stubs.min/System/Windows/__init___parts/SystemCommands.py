class SystemCommands(object):
 # no doc
 @staticmethod
 def CloseWindow(window):
  """ CloseWindow(window: Window) """
  pass
 @staticmethod
 def MaximizeWindow(window):
  """ MaximizeWindow(window: Window) """
  pass
 @staticmethod
 def MinimizeWindow(window):
  """ MinimizeWindow(window: Window) """
  pass
 @staticmethod
 def RestoreWindow(window):
  """ RestoreWindow(window: Window) """
  pass
 @staticmethod
 def ShowSystemMenu(window,screenLocation):
  """ ShowSystemMenu(window: Window,screenLocation: Point) """
  pass
 CloseWindowCommand=None
 MaximizeWindowCommand=None
 MinimizeWindowCommand=None
 RestoreWindowCommand=None
 ShowSystemMenuCommand=None
 __all__=[
  'CloseWindow',
  'MaximizeWindow',
  'MinimizeWindow',
  'RestoreWindow',
  'ShowSystemMenu',
 ]

