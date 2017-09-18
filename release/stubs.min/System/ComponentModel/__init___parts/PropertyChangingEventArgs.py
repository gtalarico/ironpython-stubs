class PropertyChangingEventArgs(EventArgs):
 """
 Provides data for the System.ComponentModel.INotifyPropertyChanging.PropertyChanging event.

 

 PropertyChangingEventArgs(propertyName: str)
 """
 @staticmethod
 def __new__(self,propertyName):
  """ __new__(cls: type,propertyName: str) """
  pass
 PropertyName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the property whose value is changing.



Get: PropertyName(self: PropertyChangingEventArgs) -> str



"""


