class PointList(CollectionBase):
 """ PointList() """
 def Add(self,Value):
  """ Add(self: PointList,Value: Point) -> int """
  pass
 def Contains(self,Value):
  """ Contains(self: PointList,Value: Point) -> bool """
  pass
 def GetRange(self,Index,Count):
  """ GetRange(self: PointList,Index: int,Count: int) -> PointList """
  pass
 def IndexOf(self,Value,StartIndex=None,Count=None):
  """
  IndexOf(self: PointList,Value: Point,StartIndex: int,Count: int) -> int
  IndexOf(self: PointList,Value: Point,StartIndex: int) -> int
  IndexOf(self: PointList,Value: Point) -> int
  """
  pass
 def Insert(self,Index,Value):
  """ Insert(self: PointList,Index: int,Value: Point) """
  pass
 def IsEqual(self,ObjectToCompare):
  """ IsEqual(self: PointList,ObjectToCompare: object) -> bool """
  pass
 def LastIndexOf(self,Value,StartIndex=None,Count=None):
  """
  LastIndexOf(self: PointList,Value: Point,StartIndex: int,Count: int) -> int
  LastIndexOf(self: PointList,Value: Point,StartIndex: int) -> int
  LastIndexOf(self: PointList,Value: Point) -> int
  """
  pass
 def Remove(self,Value):
  """ Remove(self: PointList,Value: Point) """
  pass
 def RemoveRange(self,Index,Count):
  """ RemoveRange(self: PointList,Index: int,Count: int) """
  pass
 def ToArray(self):
  """ ToArray(self: PointList) -> Array[Point] """
  pass
 InnerList=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an System.Collections.ArrayList containing the list of elements in the System.Collections.CollectionBase instance.

"""

 List=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets an System.Collections.IList containing the list of elements in the System.Collections.CollectionBase instance.

"""


