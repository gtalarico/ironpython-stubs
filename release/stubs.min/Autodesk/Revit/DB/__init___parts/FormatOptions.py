class FormatOptions(object,IDisposable):
 """
 Options for formatting numbers with units.

 

 FormatOptions(other: FormatOptions)

 FormatOptions(displayUnit: DisplayUnitType,unitSymbol: UnitSymbolType,accuracy: float)

 FormatOptions(displayUnit: DisplayUnitType,accuracy: float)

 FormatOptions(displayUnit: DisplayUnitType,unitSymbol: UnitSymbolType)

 FormatOptions(displayUnit: DisplayUnitType)

 FormatOptions()
 """
 def CanHaveUnitSymbol(self,displayUnit=None):
  """
  CanHaveUnitSymbol(displayUnit: DisplayUnitType) -> bool

  

   Checks whether a unit symbol can be specified for a given display unit.

  

   displayUnit: The display unit.

   Returns: True if a unit symbol can be specified,false otherwise.

  CanHaveUnitSymbol(self: FormatOptions) -> bool

  

   Checks whether a unit symbol can be specified for the display unit in this 

    FormatOptions.

  

   Returns: True if a unit symbol can be specified,false otherwise.
  """
  pass
 def CanSuppressLeadingZeros(self,displayUnit=None):
  """
  CanSuppressLeadingZeros(displayUnit: DisplayUnitType) -> bool

  

   Checks whether leading zeros can be suppressed for a given display unit.

  

   displayUnit: The display unit.

   Returns: True if leading zeros can be suppressed,false otherwise.

  CanSuppressLeadingZeros(self: FormatOptions) -> bool

  

   Checks whether leading zeros can be suppressed for the display unit in this 

    FormatOptions.

  

   Returns: True if leading zeros can be suppressed,false otherwise.
  """
  pass
 def CanSuppressSpaces(self,displayUnit=None):
  """
  CanSuppressSpaces(displayUnit: DisplayUnitType) -> bool

  

   Checks whether spaces can be suppressed for a given display unit.

  

   displayUnit: The display unit.

   Returns: True if spaces can be suppressed,false otherwise.

  CanSuppressSpaces(self: FormatOptions) -> bool

  

   Checks whether spaces can be suppressed for the display unit in this 

    FormatOptions.

  

   Returns: True if spaces can be suppressed,false otherwise.
  """
  pass
 def CanSuppressTrailingZeros(self,displayUnit=None):
  """
  CanSuppressTrailingZeros(displayUnit: DisplayUnitType) -> bool

  

   Checks whether trailing zeros can be suppressed for a given display unit.

  

   displayUnit: The display unit.

   Returns: True if trailing zeros can be suppressed,false otherwise.

  CanSuppressTrailingZeros(self: FormatOptions) -> bool

  

   Checks whether trailing zeros can be suppressed for the display unit in this 

    FormatOptions.

  

   Returns: True if trailing zeros can be suppressed,false otherwise.
  """
  pass
 def CanUsePlusPrefix(self,displayUnit=None):
  """
  CanUsePlusPrefix(displayUnit: DisplayUnitType) -> bool

  

   Checks whether a plus prefix can be displayed for a given display unit.

  

   displayUnit: The display unit.

   Returns: True if a plus prefix can be displayed,false otherwise.

  CanUsePlusPrefix(self: FormatOptions) -> bool

  

   Checks whether a plus prefix can be displayed for the display unit in this 

    FormatOptions.

  

   Returns: True if a plus prefix can be displayed,false otherwise.
  """
  pass
 def Dispose(self):
  """ Dispose(self: FormatOptions) """
  pass
 def GetValidUnitSymbols(self,displayUnit=None):
  """
  GetValidUnitSymbols(displayUnit: DisplayUnitType) -> IList[UnitSymbolType]

  

   Gets all valid unit symbols for a given display unit.

  

   displayUnit: The display unit.

   Returns: The valid unit symbols.

  GetValidUnitSymbols(self: FormatOptions) -> IList[UnitSymbolType]

  

   Gets all valid unit symbols for the display unit in this FormatOptions.

   Returns: The valid unit symbols.
  """
  pass
 def IsValidAccuracy(self,*__args):
  """
  IsValidAccuracy(displayUnit: DisplayUnitType,accuracy: float) -> bool

  

   Checks whether an accuracy is valid for a given display unit.

  

   displayUnit: The display unit.

   accuracy: The accuracy to check.

   Returns: True if the accuracy is valid,false otherwise.

  IsValidAccuracy(self: FormatOptions,accuracy: float) -> bool

  

   Checks whether an accuracy is valid for the display unit in this FormatOptions.

  

   accuracy: The accuracy to check.

   Returns: True if the accuracy is valid,false otherwise.
  """
  pass
 def IsValidForUnitType(self,unitType):
  """
  IsValidForUnitType(self: FormatOptions,unitType: UnitType) -> bool

  

   Checks whether this FormatOptions is valid for a given unit type.

  

   unitType: The unit type.

   Returns: True if the FormatOptions is valid,false otherwise.
  """
  pass
 def IsValidUnitSymbol(self,*__args):
  """
  IsValidUnitSymbol(displayUnit: DisplayUnitType,unitSymbol: UnitSymbolType) -> bool

  

   Checks whether a unit symbol is valid for a given display unit.

  

   displayUnit: The display unit.

   unitSymbol: The unit symbol to check.

   Returns: True if the unit symbol is valid,false otherwise.

  IsValidUnitSymbol(self: FormatOptions,unitSymbol: UnitSymbolType) -> bool

  

   Checks whether a unit symbol is valid for the display unit in this 

    FormatOptions.

  

  

   unitSymbol: The unit symbol to check.

   Returns: True if the unit symbol is valid,false otherwise.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: FormatOptions,disposing: bool) """
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
 def __new__(self,*__args):
  """
  __new__(cls: type,other: FormatOptions)

  __new__(cls: type,displayUnit: DisplayUnitType,unitSymbol: UnitSymbolType,accuracy: float)

  __new__(cls: type,displayUnit: DisplayUnitType,accuracy: float)

  __new__(cls: type,displayUnit: DisplayUnitType,unitSymbol: UnitSymbolType)

  __new__(cls: type,displayUnit: DisplayUnitType)

  __new__(cls: type)
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 Accuracy=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The accuracy to which values will be rounded.



Get: Accuracy(self: FormatOptions) -> float



Set: Accuracy(self: FormatOptions)=value

"""

 DisplayUnits=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The units and display format used to format values.



Get: DisplayUnits(self: FormatOptions) -> DisplayUnitType



Set: DisplayUnits(self: FormatOptions)=value

"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: FormatOptions) -> bool



"""

 RoundingMethod=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The method used to round values: round to nearest,round up,or round down.



Get: RoundingMethod(self: FormatOptions) -> RoundingMethod



Set: RoundingMethod(self: FormatOptions)=value

"""

 SuppressLeadingZeros=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if leading zeros should be suppressed in feet and fractional inches.



Get: SuppressLeadingZeros(self: FormatOptions) -> bool



Set: SuppressLeadingZeros(self: FormatOptions)=value

"""

 SuppressSpaces=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if spaces around the dash should be suppressed in feet and fractional inches.



Get: SuppressSpaces(self: FormatOptions) -> bool



Set: SuppressSpaces(self: FormatOptions)=value

"""

 SuppressTrailingZeros=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if trailing zeros after the decimal point should be

   suppressed.



Get: SuppressTrailingZeros(self: FormatOptions) -> bool



Set: SuppressTrailingZeros(self: FormatOptions)=value

"""

 UnitSymbol=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The unit symbol that should be displayed to indicate the units of the value.



Get: UnitSymbol(self: FormatOptions) -> UnitSymbolType



Set: UnitSymbol(self: FormatOptions)=value

"""

 UseDefault=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether default or custom formatting should be used.



Get: UseDefault(self: FormatOptions) -> bool



Set: UseDefault(self: FormatOptions)=value

"""

 UseDigitGrouping=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if digit grouping symbols should be displayed.



Get: UseDigitGrouping(self: FormatOptions) -> bool



Set: UseDigitGrouping(self: FormatOptions)=value

"""

 UsePlusPrefix=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates if a plus sign prefix should be displayed for positive and zero values.



Get: UsePlusPrefix(self: FormatOptions) -> bool



Set: UsePlusPrefix(self: FormatOptions)=value

"""


