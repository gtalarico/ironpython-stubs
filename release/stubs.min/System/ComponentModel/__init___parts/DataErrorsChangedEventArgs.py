class DataErrorsChangedEventArgs(EventArgs):
 """ DataErrorsChangedEventArgs(propertyName: str) """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return DataErrorsChangedEventArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def __new__(self,propertyName):
  """ __new__(cls: type,propertyName: str) """
  pass
 PropertyName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: PropertyName(self: DataErrorsChangedEventArgs) -> str

"""


