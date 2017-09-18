class SelectionRange(object):
 """
 Represents a date selection range in a month calendar control.

 

 SelectionRange()

 SelectionRange(lower: DateTime,upper: DateTime)

 SelectionRange(range: SelectionRange)
 """
 def ToString(self):
  """
  ToString(self: SelectionRange) -> str

  

   Returns a string that represents the System.Windows.Forms.SelectionRange.

   Returns: A string that represents the current System.Windows.Forms.SelectionRange.
  """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type)

  __new__(cls: type,lower: DateTime,upper: DateTime)

  __new__(cls: type,range: SelectionRange)
  """
  pass
 End=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the ending date and time of the selection range.



Get: End(self: SelectionRange) -> DateTime



Set: End(self: SelectionRange)=value

"""

 Start=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the starting date and time of the selection range.



Get: Start(self: SelectionRange) -> DateTime



Set: Start(self: SelectionRange)=value

"""


