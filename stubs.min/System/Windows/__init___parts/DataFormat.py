class DataFormat(object):
 """
 Represents a data format by using a format name and numeric ID.
 
 DataFormat(name: str,id: int)
 """
 @staticmethod
 def __new__(self,name,id):
  """ __new__(cls: type,name: str,id: int) """
  pass
 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the numeric ID of the data format.

Get: Id(self: DataFormat) -> int

"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of the data format.

Get: Name(self: DataFormat) -> str

"""


