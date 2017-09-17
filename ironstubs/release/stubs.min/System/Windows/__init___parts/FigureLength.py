class FigureLength(object,IEquatable[FigureLength]):
 """
 Describes the height or width of a System.Windows.Documents.Figure.
 
 FigureLength(pixels: float)
 FigureLength(value: float,type: FigureUnitType)
 """
 def Equals(self,*__args):
  """
  Equals(self: FigureLength,figureLength: FigureLength) -> bool
  
   Compares two System.Windows.FigureLength structures for equality.
  
   figureLength: The System.Windows.FigureLength to compare to this instance.
   Returns: true if figureLength is identical to this System.Windows.FigureLength; 
    otherwise,false.
  
  Equals(self: FigureLength,oCompare: object) -> bool
  
   Determines whether the specified System.Object is a System.Windows.FigureLength 
    and whether it is identical to this System.Windows.FigureLength.
  
  
   oCompare: The System.Object to compare to this instance.
   Returns: true if oCompare is a System.Windows.FigureLength and is identical to this 
    System.Windows.FigureLength; otherwise,false.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: FigureLength) -> int
  
   Returns the hash code for this System.Windows.FigureLength.
   Returns: The hash code for this System.Windows.FigureLength structure.
  """
  pass
 def ToString(self):
  """
  ToString(self: FigureLength) -> str
  
   Creates a System.String representation of this System.Windows.FigureLength.
   Returns: A System.String representation of this System.Windows.FigureLength.
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
  __new__[FigureLength]() -> FigureLength
  
  __new__(cls: type,pixels: float)
  __new__(cls: type,value: float,type: FigureUnitType)
  """
  pass
 def __ne__(self,*args):
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __str__(self,*args):
  pass
 FigureUnitType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the unit type of the System.Windows.FigureLength.Value.

Get: FigureUnitType(self: FigureLength) -> FigureUnitType

"""

 IsAbsolute=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that determines whether this System.Windows.FigureLength holds an absolute value (in pixels).

Get: IsAbsolute(self: FigureLength) -> bool

"""

 IsAuto=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that determines whether this System.Windows.FigureLength is automatic (not specified).

Get: IsAuto(self: FigureLength) -> bool

"""

 IsColumn=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that determines whether this System.Windows.FigureLength has a System.Windows.FigureUnitType property value of System.Windows.FigureUnitType.Column.

Get: IsColumn(self: FigureLength) -> bool

"""

 IsContent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that determines whether this System.Windows.FigureLength has a System.Windows.FigureUnitType property value of System.Windows.FigureUnitType.Content.

Get: IsContent(self: FigureLength) -> bool

"""

 IsPage=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value that determines whether this System.Windows.FigureLength has a System.Windows.FigureUnitType property value of System.Windows.FigureUnitType.Page.

Get: IsPage(self: FigureLength) -> bool

"""

 Value=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the value of this System.Windows.FigureLength.

Get: Value(self: FigureLength) -> float

"""


