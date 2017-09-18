class HandleCollector(object):
 """
 Tracks outstanding handles and forces a garbage collection when the specified threshold is reached.

 

 HandleCollector(name: str,initialThreshold: int)

 HandleCollector(name: str,initialThreshold: int,maximumThreshold: int)
 """
 def Add(self):
  """
  Add(self: HandleCollector)

   Increments the current handle count.
  """
  pass
 def Remove(self):
  """
  Remove(self: HandleCollector)

   Decrements the current handle count.
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+y """
  pass
 @staticmethod
 def __new__(self,name,initialThreshold,maximumThreshold=None):
  """
  __new__(cls: type,name: str,initialThreshold: int)

  __new__(cls: type,name: str,initialThreshold: int,maximumThreshold: int)
  """
  pass
 Count=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the number of handles collected.



Get: Count(self: HandleCollector) -> int



"""

 InitialThreshold=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that specifies the point at which collections should begin.



Get: InitialThreshold(self: HandleCollector) -> int



"""

 MaximumThreshold=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that specifies the point at which collections must occur.



Get: MaximumThreshold(self: HandleCollector) -> int



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the name of a System.Runtime.InteropServices.HandleCollector object.



Get: Name(self: HandleCollector) -> str



"""


