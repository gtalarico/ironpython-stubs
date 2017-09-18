class ColumnStyle(TableLayoutStyle):
 """
 Represents the look and feel of a column in a table layout.

 

 ColumnStyle(sizeType: SizeType,width: Single)

 ColumnStyle()

 ColumnStyle(sizeType: SizeType)
 """
 @staticmethod
 def __new__(self,sizeType=None,width=None):
  """
  __new__(cls: type)

  __new__(cls: type,sizeType: SizeType)

  __new__(cls: type,sizeType: SizeType,width: Single)
  """
  pass
 Width=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the width value for a column.



Get: Width(self: ColumnStyle) -> Single



Set: Width(self: ColumnStyle)=value

"""


