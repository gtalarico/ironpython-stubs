class IWindowTarget:
 """ Defines the communication layer between a control and the Win32 API. """
 def OnHandleChange(self,newHandle):
  """
  OnHandleChange(self: IWindowTarget,newHandle: IntPtr)

   Sets the handle of the System.Windows.Forms.IWindowTarget to the specified handle.

  

   newHandle: The new handle of the System.Windows.Forms.IWindowTarget.
  """
  pass
 def OnMessage(self,m):
  """
  OnMessage(self: IWindowTarget,m: Message) -> Message

  

   Processes the Windows messages.

  

   m: The Windows message to process.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
