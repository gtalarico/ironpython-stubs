class PropertyChangingEventArgs(EventArgs):
 """
 Provides data for the System.ComponentModel.INotifyPropertyChanging.PropertyChanging event.
 
 PropertyChangingEventArgs(propertyName: str)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return PropertyChangingEventArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def __new__(self,propertyName):
  """ __new__(cls: type,propertyName: str) """
  pass
 PropertyName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the property whose value is changing.

Get: PropertyName(self: PropertyChangingEventArgs) -> str

"""


