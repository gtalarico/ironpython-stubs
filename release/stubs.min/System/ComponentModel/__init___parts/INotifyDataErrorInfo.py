class INotifyDataErrorInfo:
 # no doc
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return INotifyDataErrorInfo()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def GetErrors(self,propertyName):
  """ GetErrors(self: INotifyDataErrorInfo,propertyName: str) -> IEnumerable """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 HasErrors=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: HasErrors(self: INotifyDataErrorInfo) -> bool

"""


 ErrorsChanged=None

