class CursorInteropHelper(object):
 """ Provides a static helper class for WPF/Win32 interoperation with one method,which is used to obtain a Windows Presentation Foundation (WPF)�System.Windows.Input.Cursor object based on a provided Win32 cursor handle. """
 @staticmethod
 def Create(cursorHandle):
  """
  Create(cursorHandle: SafeHandle) -> Cursor
  
   Returns a Windows Presentation Foundation (WPF)�System.Windows.Input.Cursor 
    object based on a provided Win32 cursor handle.
  
  
   cursorHandle: Cursor reference to use for interoperation.
   Returns: The Windows Presentation Foundation (WPF)�cursor object based on the provided 
    Win32 cursor handle.
  """
  pass
 __all__=[
  'Create',
 ]

