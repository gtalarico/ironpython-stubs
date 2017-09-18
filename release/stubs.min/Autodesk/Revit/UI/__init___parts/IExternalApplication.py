class IExternalApplication:
 """ An interface that supports addition of external applications to Revit. """
 def OnShutdown(self,application):
  """
  OnShutdown(self: IExternalApplication,application: UIControlledApplication) -> Result

  

   Implement this method to execute some tasks when Autodesk Revit shuts down.

  

   application: A handle to the application being shut down.

   Returns: Indicates if the external application completes its work successfully.
  """
  pass
 def OnStartup(self,application):
  """
  OnStartup(self: IExternalApplication,application: UIControlledApplication) -> Result

  

   Implement this method to execute some tasks when Autodesk Revit starts.

  

   application: A handle to the application being started.

   Returns: Indicates if the external application completes its work successfully.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
