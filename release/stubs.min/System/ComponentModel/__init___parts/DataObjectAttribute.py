class DataObjectAttribute(Attribute,_Attribute):
 """
 Identifies a type as an object suitable for binding to an System.Web.UI.WebControls.ObjectDataSource object. This class cannot be inherited.

 

 DataObjectAttribute()

 DataObjectAttribute(isDataObject: bool)
 """
 def Equals(self,obj):
  """
  Equals(self: DataObjectAttribute,obj: object) -> bool

  

   Determines whether this instance of System.ComponentModel.DataObjectAttribute fits the pattern 

    of another object.

  

  

   obj: An object to compare with this instance of System.ComponentModel.DataObjectAttribute.

   Returns: true if this instance is the same as the instance specified by the obj parameter; otherwise,

    false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: DataObjectAttribute) -> int

  

   Returns the hash code for this instance.

   Returns: A 32-bit signed integer hash code.
  """
  pass
 def IsDefaultAttribute(self):
  """
  IsDefaultAttribute(self: DataObjectAttribute) -> bool

  

   Gets a value indicating whether the current value of the attribute is the default value for the 

    attribute.

  

   Returns: true if the current value of the attribute is the default; otherwise,false.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,isDataObject=None):
  """
  __new__(cls: type)

  __new__(cls: type,isDataObject: bool)
  """
  pass
 def __ne__(self,*args):
  pass
 IsDataObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether an object should be considered suitable for binding to an System.Web.UI.WebControls.ObjectDataSource object at design time.



Get: IsDataObject(self: DataObjectAttribute) -> bool



"""


 DataObject=None
 Default=None
 NonDataObject=None

