class WindowInteropHelper(object):
 """
 Assists interoperation between Windows Presentation Foundation (WPF) and Win32 code.
 
 WindowInteropHelper(window: Window)
 """
 def EnsureHandle(self):
  """
  EnsureHandle(self: WindowInteropHelper) -> IntPtr
  
   Creates the HWND of the window if the HWND has not been created yet.
   Returns: An System.IntPtr that represents the HWND.
  """
  pass
 @staticmethod
 def __new__(self,window):
  """ __new__(cls: type,window: Window) """
  pass
 Handle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the window handle for a Windows Presentation Foundation (WPF) window�that is used to create this System.Windows.Interop.WindowInteropHelper.

Get: Handle(self: WindowInteropHelper) -> IntPtr

"""

 Owner=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the handle of the Windows Presentation Foundation (WPF)�owner window.

Get: Owner(self: WindowInteropHelper) -> IntPtr

Set: Owner(self: WindowInteropHelper)=value
"""



