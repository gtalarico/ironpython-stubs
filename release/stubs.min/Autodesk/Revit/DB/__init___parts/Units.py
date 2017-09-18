class Units(object,IDisposable):
 """
 A document's default settings for formatting numbers with units.
 
 Units(unitSystem: UnitSystem)
 """
 def Dispose(self):
  """ Dispose(self: Units) """
  pass
 def GetFormatOptions(self,unitType):
  """
  GetFormatOptions(self: Units,unitType: UnitType) -> FormatOptions
  
   Gets the default FormatOptions for a unit type.
  
   unitType: The unit type.
   Returns: A copy of the FormatOptions.
  """
  pass
 @staticmethod
 def GetModifiableUnitTypes():
  """
  GetModifiableUnitTypes() -> IList[UnitType]
  
   Gets all unit types for which the default FormatOptions can be modified.
   Returns: The unit types for which the FormatOptions can be modified.
  """
  pass
 @staticmethod
 def IsModifiableUnitType(unitType):
  """
  IsModifiableUnitType(unitType: UnitType) -> bool
  
   Checks whether the default FormatOptions can be modified for a given unit type.
  
   unitType: The unit type to check.
   Returns: True if the FormatOptions can be modified,false otherwise.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Units,disposing: bool) """
  pass
 def SetFormatOptions(self,unitType,options):
  """
  SetFormatOptions(self: Units,unitType: UnitType,options: FormatOptions)
   Sets the default FormatOptions for a unit type.
  
   unitType: The unit type.
   options: The ForrmatOptions.
  """
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
 @staticmethod
 def __new__(self,unitSystem):
  """ __new__(cls: type,unitSystem: UnitSystem) """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 DecimalSymbol=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The symbol used to separate the integer and fractional parts of a number.

Get: DecimalSymbol(self: Units) -> DecimalSymbol

Set: DecimalSymbol(self: Units)=value
"""

 DigitGroupingAmount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The number of digits in each group when numbers are formatted with digit grouping.

Get: DigitGroupingAmount(self: Units) -> DigitGroupingAmount

Set: DigitGroupingAmount(self: Units)=value
"""

 DigitGroupingSymbol=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The symbol used to separate groups of digits when numbers are formatted with digit grouping.

Get: DigitGroupingSymbol(self: Units) -> DigitGroupingSymbol

Set: DigitGroupingSymbol(self: Units)=value
"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: Units) -> bool

"""


