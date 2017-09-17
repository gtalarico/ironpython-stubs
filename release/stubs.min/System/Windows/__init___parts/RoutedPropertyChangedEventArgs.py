class RoutedPropertyChangedEventArgs(RoutedEventArgs):
 """
 RoutedPropertyChangedEventArgs[T](oldValue: T,newValue: T)
 RoutedPropertyChangedEventArgs[T](oldValue: T,newValue: T,routedEvent: RoutedEvent)
 """
 @staticmethod
 def __new__(self,oldValue,newValue,routedEvent=None):
  """
  __new__(cls: type,oldValue: T,newValue: T)
  __new__(cls: type,oldValue: T,newValue: T,routedEvent: RoutedEvent)
  """
  pass
 NewValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the new value of a property as reported by a property changed event.

Get: NewValue(self: RoutedPropertyChangedEventArgs[T]) -> T

"""

 OldValue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the previous value of the property as reported by a property changed event.

Get: OldValue(self: RoutedPropertyChangedEventArgs[T]) -> T

"""


