class IDataErrorInfo:
 """ Provides the functionality to offer custom error information that a user interface can bind to. """
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 Error=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an error message indicating what is wrong with this object.



Get: Error(self: IDataErrorInfo) -> str



"""


