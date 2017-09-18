class DimensionType(ElementType,IDisposable):
 """ An object that represents a dimension style. """
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def GetAlternateUnitsFormatOptions(self):
  """
  GetAlternateUnitsFormatOptions(self: DimensionType) -> FormatOptions

  

   Gets the FormatOptions to optionally override the default settings in the Units 

    class for the alternate units value.

  

   Returns: A copy of the FormatOptions.
  """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: Element,view: View) -> BoundingBoxXYZ """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def SetAlternateUnitsFormatOptions(self,formatOptions):
  """
  SetAlternateUnitsFormatOptions(self: DimensionType,formatOptions: FormatOptions)

   Sets the FormatOptions to optionally override the default settings in the Units 

    class for the alternate units value.

  

  

   formatOptions: The FormatOptions.
  """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 AlternateUnits=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The alternate units display mode for this DimensionType.



Get: AlternateUnits(self: DimensionType) -> AlternateUnits



Set: AlternateUnits(self: DimensionType)=value

"""

 AlternateUnitsPrefix=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The prefix text for the alternate units value.



Get: AlternateUnitsPrefix(self: DimensionType) -> str



Set: AlternateUnitsPrefix(self: DimensionType)=value

"""

 AlternateUnitsSuffix=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The suffix text for the alternate units value.



Get: AlternateUnitsSuffix(self: DimensionType) -> str



Set: AlternateUnitsSuffix(self: DimensionType)=value

"""

 StyleType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The dimension style type of this DimensionType.



Get: StyleType(self: DimensionType) -> DimensionStyleType



"""

 UnitType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The unit type of this dimension style.



Get: UnitType(self: DimensionType) -> UnitType



"""


