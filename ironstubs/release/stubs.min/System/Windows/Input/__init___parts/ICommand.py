class ICommand:
 # no doc
 def CanExecute(self,parameter):
  """ CanExecute(self: ICommand,parameter: object) -> bool """
  pass
 def Execute(self,parameter):
  """ Execute(self: ICommand,parameter: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 CanExecuteChanged=None

