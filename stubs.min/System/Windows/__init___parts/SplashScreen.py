class SplashScreen(object):
 """
 Provides a startup screen for a Windows Presentation Foundation (WPF) application.
 
 SplashScreen(resourceName: str)
 SplashScreen(resourceAssembly: Assembly,resourceName: str)
 """
 def Close(self,fadeoutDuration):
  """
  Close(self: SplashScreen,fadeoutDuration: TimeSpan)
   Closes the splash screen.
  
   fadeoutDuration: A System.TimeSpan that specifies how long it will take for the splash screen to 
    fade after the close operation has been initiated.
  """
  pass
 def Show(self,autoClose,topMost=None):
  """
  Show(self: SplashScreen,autoClose: bool,topMost: bool)
   Displays the splash screen.
  
   autoClose: true to automatically close the splash screen; false to close the splash screen 
    manually.
  
   topMost: true if the splash screen window should use the WS_EX_TOPMOST style; otherwise 
    false.
  
  Show(self: SplashScreen,autoClose: bool)
   Displays the splash screen.
  
   autoClose: true to automatically close the splash screen; false to close the splash screen 
    manually.
  """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type,resourceName: str)
  __new__(cls: type,resourceAssembly: Assembly,resourceName: str)
  """
  pass
