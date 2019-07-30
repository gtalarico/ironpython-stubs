class PropertyChangedEventArgs(EventArgs):
 """
 Provides data for the System.ComponentModel.INotifyPropertyChanged.PropertyChanged event.
 
 PropertyChangedEventArgs(propertyName: str)
 """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return PropertyChangedEventArgs()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 @staticmethod
 def __new__(self,propertyName):
  """ __new__(cls: type,propertyName: str) """
  pass
 PropertyName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the property that changed.

Get: PropertyName(self: PropertyChangedEventArgs) -> str

"""


