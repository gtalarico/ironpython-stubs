class GuidEnum(object):
 """
 Base class of all GUID-based enum classes.
 
 GuidEnum(guid: Guid)
 """
 def Equals(self,obj):
  """
  Equals(self: GuidEnum,obj: object) -> bool
  
   Compares two Guid-based enum object based on their concrete class and GUID 
    value.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: GuidEnum) -> int
  
   Generates a hash code for this Guid-based enum object.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 @staticmethod
 def __new__(self,guid):
  """
  __new__(cls: type,guid: str)
  __new__(cls: type,guid: Guid)
  """
  pass
 def __ne__(self,*args):
  pass
 Guid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The Guid of GUID-based enum object.

Get: Guid(self: GuidEnum) -> Guid

"""


