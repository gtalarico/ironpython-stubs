class TextChange(object):
 """ Contains information about the changes that occur in the System.Windows.Controls.Primitives.TextBoxBase.TextChanged event. """
 AddedLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the number of symbols that have been added to the control.



Get: AddedLength(self: TextChange) -> int



"""

 Offset=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the position at which the change occurred.



Get: Offset(self: TextChange) -> int



"""

 RemovedLength=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the number of symbols that have been removed from the control.



Get: RemovedLength(self: TextChange) -> int



"""


