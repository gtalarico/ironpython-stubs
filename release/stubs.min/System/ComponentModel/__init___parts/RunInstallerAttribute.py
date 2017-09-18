class RunInstallerAttribute(Attribute,_Attribute):
 """
 Specifies whether the Visual Studio Custom Action Installer or the Installutil.exe (Installer Tool) should be invoked when the assembly is installed.

 

 RunInstallerAttribute(runInstaller: bool)
 """
 def Equals(self,obj):
  """
  Equals(self: RunInstallerAttribute,obj: object) -> bool

  

   Determines whether the value of the specified System.ComponentModel.RunInstallerAttribute is 

    equivalent to the current System.ComponentModel.RunInstallerAttribute.

  

  

   obj: The object to compare.

   Returns: true if the specified System.ComponentModel.RunInstallerAttribute is equal to the current 

    System.ComponentModel.RunInstallerAttribute; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: RunInstallerAttribute) -> int

  

   Generates a hash code for the current System.ComponentModel.RunInstallerAttribute.

   Returns: A hash code for the current System.ComponentModel.RunInstallerAttribute.
  """
  pass
 def IsDefaultAttribute(self):
  """
  IsDefaultAttribute(self: RunInstallerAttribute) -> bool

  

   Determines if this attribute is the default.

   Returns: true if the attribute is the default value for this attribute class; otherwise,false.
  """
  pass
 def __eq__(self,*args):
  """ x.__eq__(y) <==> x==y """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 @staticmethod
 def __new__(self,runInstaller):
  """ __new__(cls: type,runInstaller: bool) """
  pass
 def __ne__(self,*args):
  pass
 RunInstaller=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether an installer should be invoked during installation of an assembly.



Get: RunInstaller(self: RunInstallerAttribute) -> bool



"""


 Default=None
 No=None
 Yes=None

