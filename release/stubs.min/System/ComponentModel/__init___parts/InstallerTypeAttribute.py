class InstallerTypeAttribute(Attribute,_Attribute):
 """
 Specifies the installer for a type that installs components.

 

 InstallerTypeAttribute(installerType: Type)

 InstallerTypeAttribute(typeName: str)
 """
 def Equals(self,obj):
  """
  Equals(self: InstallerTypeAttribute,obj: object) -> bool

  

   Returns whether the value of the given object is equal to the current 

    System.ComponentModel.InstallerTypeAttribute.

  

  

   obj: The object to test the value equality of.

   Returns: true if the value of the given object is equal to that of the current; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: InstallerTypeAttribute) -> int

  

   Returns the hashcode for this object.

   Returns: A hash code for the current System.ComponentModel.InstallerTypeAttribute.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type,installerType: Type)

  __new__(cls: type,typeName: str)
  """
  pass
 def __ne__(self,*args):
  pass
 InstallerType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the type of installer associated with this attribute.



Get: InstallerType(self: InstallerTypeAttribute) -> Type



"""


