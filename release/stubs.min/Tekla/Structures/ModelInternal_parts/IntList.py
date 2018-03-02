class IntList(CollectionBase):
 """
 IntList()
 IntList(integers: IEnumerable)
 """
 def Add(self,Value):
  """ Add(self: IntList,Value: int) -> int """
  pass
 def Contains(self,Value):
  """ Contains(self: IntList,Value: int) -> bool """
  pass
 def GetRange(self,Index,Count):
  """ GetRange(self: IntList,Index: int,Count: int) -> IntList """
  pass
 def IndexOf(self,Value,StartIndex=None,Count=None):
  """
  IndexOf(self: IntList,Value: int,StartIndex: int,Count: int) -> int
  IndexOf(self: IntList,Value: int,StartIndex: int) -> int
  IndexOf(self: IntList,Value: int) -> int
  """
  pass
 def Insert(self,Index,Value):
  """ Insert(self: IntList,Index: int,Value: int) """
  pass
 def IsEqual(self,ObjectToCompare):
  """ IsEqual(self: IntList,ObjectToCompare: object) -> bool """
  pass
 def LastIndexOf(self,Value,StartIndex=None,Count=None):
  """
  LastIndexOf(self: IntList,Value: int,StartIndex: int,Count: int) -> int
  LastIndexOf(self: IntList,Value: int,StartIndex: int) -> int
  LastIndexOf(self: IntList,Value: int) -> int
  """
  pass
 def Remove(self,Value):
  """ Remove(self: IntList,Value: int) """
  pass
 def RemoveRange(self,Index,Count):
  """ RemoveRange(self: IntList,Index: int,Count: int) """
  pass
 def ToArray(self):
  """ ToArray(self: IntList) -> Array[int] """
  pass
 @staticmethod
 def __new__(self,integers=None):
  """
  __new__(cls: type)
  __new__(cls: type,integers: IEnumerable)
  """
  pass
 InnerList=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an System.Collections.ArrayList containing the list of elements in the System.Collections.CollectionBase instance.

"""

 List=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an System.Collections.IList containing the list of elements in the System.Collections.CollectionBase instance.

"""


