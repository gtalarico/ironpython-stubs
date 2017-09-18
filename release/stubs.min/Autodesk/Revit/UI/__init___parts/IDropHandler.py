class IDropHandler:
 """ An interface to be executed when custom data is dragged and dropped onto the Revit user interface. """
 def Execute(self,document,data):
  """
  Execute(self: IDropHandler,document: UIDocument,data: object)
   Implement this method to handle the drop event for your data.
  
   document: The document on which the data was dropped.
   data: The data.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
