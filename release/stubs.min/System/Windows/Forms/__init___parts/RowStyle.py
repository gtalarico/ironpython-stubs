class RowStyle(TableLayoutStyle):
 """
 Represents the look and feel of a row in a table layout.

 

 RowStyle(sizeType: SizeType,height: Single)

 RowStyle()

 RowStyle(sizeType: SizeType)
 """
 @staticmethod
 def __new__(self,sizeType=None,height=None):
  """
  __new__(cls: type)

  __new__(cls: type,sizeType: SizeType)

  __new__(cls: type,sizeType: SizeType,height: Single)
  """
  pass
 Height=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the height of a row.



Get: Height(self: RowStyle) -> Single



Set: Height(self: RowStyle)=value

"""


