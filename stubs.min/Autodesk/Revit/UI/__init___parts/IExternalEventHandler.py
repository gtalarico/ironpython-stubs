class IExternalEventHandler:
 """ An interface to be executed when an external event is raised. """
 def Execute(self,app):
  """
  Execute(self: IExternalEventHandler,app: UIApplication)
   This method is called to handle the external event.
  """
  pass
 def GetName(self):
  """
  GetName(self: IExternalEventHandler) -> str
  
   String identification of the event handler.
   Returns: The event's name
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
