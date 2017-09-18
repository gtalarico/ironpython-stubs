class IDockablePaneProvider:
 """ Interface that the Revit UI will call during initialization of the user interface to gather information about add-in dockable pane windows. """
 def SetupDockablePane(self,data):
  """
  SetupDockablePane(self: IDockablePaneProvider,data: DockablePaneProviderData)

   Method called during initialization of the user interface to gather information 

    about a dockable pane window.

  

  

   data: Container for information about the new dockable pane.  Implementers should set 

    the 

     FrameworkElement and InitialState Properties. Optionally,providers 

    can set the 

     ContextualHelp property if they wish to provide or react to 

    help requests on the pane,

     or override the default EditorInteraction 

    property by setting it here.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
