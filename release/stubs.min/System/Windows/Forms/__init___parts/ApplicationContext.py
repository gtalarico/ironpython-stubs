class ApplicationContext(object,IDisposable):
 """
 Specifies the contextual information about an application thread.

 

 ApplicationContext()

 ApplicationContext(mainForm: Form)
 """
 def Dispose(self):
  """
  Dispose(self: ApplicationContext)

   Releases all resources used by the System.Windows.Forms.ApplicationContext.
  """
  pass
 def ExitThread(self):
  """
  ExitThread(self: ApplicationContext)

   Terminates the message loop of the thread.
  """
  pass
 def ExitThreadCore(self,*args):
  """
  ExitThreadCore(self: ApplicationContext)

   Terminates the message loop of the thread.
  """
  pass
 def OnMainFormClosed(self,*args):
  """
  OnMainFormClosed(self: ApplicationContext,sender: object,e: EventArgs)

   Calls System.Windows.Forms.ApplicationContext.ExitThreadCore,which raises the 

    System.Windows.Forms.ApplicationContext.ThreadExit event.

  

  

   sender: The object that raised the event.

   e: The System.EventArgs that contains the event data.
  """
  pass
 def __enter__(self,*args):
  """
  __enter__(self: IDisposable) -> object

  

   Provides the implementation of __enter__ for objects which implement IDisposable.
  """
  pass
 def __exit__(self,*args):
  """
  __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object)

   Provides the implementation of __exit__ for objects which implement IDisposable.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,mainForm=None):
  """
  __new__(cls: type)

  __new__(cls: type,mainForm: Form)
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 MainForm=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the System.Windows.Forms.Form to use as context.



Get: MainForm(self: ApplicationContext) -> Form



Set: MainForm(self: ApplicationContext)=value

"""

 Tag=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets an object that contains data about the control.



Get: Tag(self: ApplicationContext) -> object



Set: Tag(self: ApplicationContext)=value

"""


 ThreadExit=None

