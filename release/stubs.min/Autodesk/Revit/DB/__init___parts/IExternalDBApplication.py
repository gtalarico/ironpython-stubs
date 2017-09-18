class IExternalDBApplication:
 """ An interface that supports addition of DB-level external applications to Revit,to subscribe to DB-level events and updaters. """
 def OnShutdown(self,application):
  """
  OnShutdown(self: IExternalDBApplication,application: ControlledApplication) -> ExternalDBApplicationResult

  

   Implement this method to execute some tasks when Autodesk Revit shuts down.

  

   application: Handle to the Revit Application object.

   Returns: Indicates if the external db application completes its work successfully.
  """
  pass
 def OnStartup(self,application):
  """
  OnStartup(self: IExternalDBApplication,application: ControlledApplication) -> ExternalDBApplicationResult

  

   Implement this method to execute some tasks when Autodesk Revit starts.

  

   application: Handle to the Revit Application object.

   Returns: Indicates if the external db application completes its work successfully.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
