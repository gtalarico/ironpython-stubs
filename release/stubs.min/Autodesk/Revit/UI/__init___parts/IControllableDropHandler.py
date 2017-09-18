class IControllableDropHandler(IDropHandler):
 """
 An interface to be executed when custom data is dragged and dropped onto the Revit user interface.

    This interface is different from IDropHandler in that it allows the handler to verify whether the drop event can be executed on the given view.
 """
 def CanExecute(self,document,data,dropViewId):
  """
  CanExecute(self: IControllableDropHandler,document: UIDocument,data: object,dropViewId: ElementId) -> bool

  

   Implement this method to inform Revit whether the drop event can be executed 

    onto the given view.

  

  

   document: The document on which the data was dropped.

   data: The data.

   dropViewId: The view upon which the user will drop.

   Returns: Return true to activate the target view and execute the drop. 

  Return false to 

    cancel the activation and the drop execution.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
