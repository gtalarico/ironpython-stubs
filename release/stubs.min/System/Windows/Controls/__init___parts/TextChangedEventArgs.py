class TextChangedEventArgs(RoutedEventArgs):
 """
 Provides data for the System.Windows.Controls.Primitives.TextBoxBase.TextChanged event.

 

 TextChangedEventArgs(id: RoutedEvent,action: UndoAction,changes: ICollection[TextChange])

 TextChangedEventArgs(id: RoutedEvent,action: UndoAction)
 """
 @staticmethod
 def __new__(self,id,action,changes=None):
  """
  __new__(cls: type,id: RoutedEvent,action: UndoAction,changes: ICollection[TextChange])

  __new__(cls: type,id: RoutedEvent,action: UndoAction)
  """
  pass
 Changes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a collection of objects that contains information about the changes that occurred.



Get: Changes(self: TextChangedEventArgs) -> ICollection[TextChange]



"""

 UndoAction=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets how the undo stack is caused or affected by this text change



Get: UndoAction(self: TextChangedEventArgs) -> UndoAction



"""


