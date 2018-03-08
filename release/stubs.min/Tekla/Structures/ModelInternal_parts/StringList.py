class StringList(CollectionBase):
 """
 StringList(Capacity: int)
 StringList()
 """
 def Add(self,Value):
  """ Add(self: StringList,Value: str) -> int """
  pass
 def Contains(self,Value):
  """ Contains(self: StringList,Value: str) -> bool """
  pass
 def GetRange(self,Index,Count):
  """ GetRange(self: StringList,Index: int,Count: int) -> StringList """
  pass
 def IndexOf(self,Value,StartIndex=None,Count=None):
  """
  IndexOf(self: StringList,Value: str,StartIndex: int,Count: int) -> int
  IndexOf(self: StringList,Value: str,StartIndex: int) -> int
  IndexOf(self: StringList,Value: str) -> int
  """
  pass
 def Insert(self,Index,Value):
  """ Insert(self: StringList,Index: int,Value: str) """
  pass
 def IsEqual(self,ObjectToCompare):
  """ IsEqual(self: StringList,ObjectToCompare: object) -> bool """
  pass
 def LastIndexOf(self,Value,StartIndex=None,Count=None):
  """
  LastIndexOf(self: StringList,Value: str,StartIndex: int,Count: int) -> int
  LastIndexOf(self: StringList,Value: str,StartIndex: int) -> int
  LastIndexOf(self: StringList,Value: str) -> int
  """
  pass
 def Remove(self,Value):
  """ Remove(self: StringList,Value: str) """
  pass
 def RemoveRange(self,Index,Count):
  """ RemoveRange(self: StringList,Index: int,Count: int) """
  pass
 def ToArray(self):
  """ ToArray(self: StringList) -> Array[str] """
  pass
 @staticmethod
 def __new__(self,Capacity=None):
  """
  __new__(cls: type,Capacity: int)
  __new__(cls: type)
  """
  pass
 InnerList=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an System.Collections.ArrayList containing the list of elements in the System.Collections.CollectionBase instance.

"""

 List=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an System.Collections.IList containing the list of elements in the System.Collections.CollectionBase instance.

"""


