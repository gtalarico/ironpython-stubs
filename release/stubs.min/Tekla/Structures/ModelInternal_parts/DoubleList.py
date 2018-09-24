class DoubleList(CollectionBase):
 """
 DoubleList()
 DoubleList(doubles: IEnumerable)
 """
 def Add(self,value):
  """ Add(self: DoubleList,value: float) -> int """
  pass
 def Contains(self,value):
  """ Contains(self: DoubleList,value: float) -> bool """
  pass
 def GetRange(self,index,count):
  """ GetRange(self: DoubleList,index: int,count: int) -> DoubleList """
  pass
 def IndexOf(self,value,startIndex=None,count=None):
  """
  IndexOf(self: DoubleList,value: float,startIndex: int,count: int) -> int
  IndexOf(self: DoubleList,value: float,startIndex: int) -> int
  IndexOf(self: DoubleList,value: float) -> int
  """
  pass
 def Insert(self,index,value):
  """ Insert(self: DoubleList,index: int,value: float) """
  pass
 def IsEqual(self,objectToCompare):
  """ IsEqual(self: DoubleList,objectToCompare: object) -> bool """
  pass
 def LastIndexOf(self,value,startIndex=None,count=None):
  """
  LastIndexOf(self: DoubleList,value: float,startIndex: int,count: int) -> int
  LastIndexOf(self: DoubleList,value: float,startIndex: int) -> int
  LastIndexOf(self: DoubleList,value: float) -> int
  """
  pass
 def Remove(self,value):
  """ Remove(self: DoubleList,value: float) """
  pass
 def RemoveRange(self,index,count):
  """ RemoveRange(self: DoubleList,index: int,count: int) """
  pass
 def ToArray(self):
  """ ToArray(self: DoubleList) -> Array[float] """
  pass
 @staticmethod
 def __new__(self,doubles=None):
  """
  __new__(cls: type)
  __new__(cls: type,doubles: IEnumerable)
  """
  pass
 InnerList=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an System.Collections.ArrayList containing the list of elements in the System.Collections.CollectionBase instance.

"""

 List=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an System.Collections.IList containing the list of elements in the System.Collections.CollectionBase instance.

"""


