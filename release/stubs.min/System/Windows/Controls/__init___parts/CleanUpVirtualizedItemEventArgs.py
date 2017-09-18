class CleanUpVirtualizedItemEventArgs(RoutedEventArgs):
 """
 Provides data for the System.Windows.Controls.VirtualizingStackPanel.CleanUpVirtualizedItem event.

 

 CleanUpVirtualizedItemEventArgs(value: object,element: UIElement)
 """
 @staticmethod
 def __new__(self,value,element):
  """ __new__(cls: type,value: object,element: UIElement) """
  pass
 Cancel=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that indicates whether this item should not be re-virtualized.



Get: Cancel(self: CleanUpVirtualizedItemEventArgs) -> bool



Set: Cancel(self: CleanUpVirtualizedItemEventArgs)=value

"""

 UIElement=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an instance of the visual element that represents the data value.



Get: UIElement(self: CleanUpVirtualizedItemEventArgs) -> UIElement



"""

 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an System.Object that represents the original data value.



Get: Value(self: CleanUpVirtualizedItemEventArgs) -> object



"""


