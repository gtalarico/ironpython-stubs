class ICustomFactory:
 """ Enables users to write activation code for managed objects that extend System.MarshalByRefObject. """
 def ZZZ(self):
  """hardcoded/mock instance of the class"""
  return ICustomFactory()
 instance=ZZZ()
 """hardcoded/returns an instance of the class"""
 def CreateInstance(self,serverType):
  """
  CreateInstance(self: ICustomFactory,serverType: Type) -> MarshalByRefObject
  
   Creates a new instance of the specified type.
  
   serverType: The type to activate.
   Returns: A System.MarshalByRefObject associated with the specified type.
  """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
