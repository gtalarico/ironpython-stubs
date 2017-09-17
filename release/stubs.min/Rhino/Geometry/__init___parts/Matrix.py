class Matrix(object,IDisposable):
 """
 Matrix(rowCount: int,columnCount: int)
 Matrix(xform: Transform)
 """
 def BackSolve(self,zeroTolerance,b):
  """ BackSolve(self: Matrix,zeroTolerance: float,b: Array[float]) -> Array[float] """
  pass
 def BackSolvePoints(self,zeroTolerance,b):
  """ BackSolvePoints(self: Matrix,zeroTolerance: float,b: Array[Point3d]) -> Array[Point3d] """
  pass
 def Dispose(self):
  """ Dispose(self: Matrix) """
  pass
 def Duplicate(self):
  """ Duplicate(self: Matrix) -> Matrix """
  pass
 def GetHashCode(self):
  """ GetHashCode(self: Matrix) -> int """
  pass
 def Invert(self,zeroTolerance):
  """ Invert(self: Matrix,zeroTolerance: float) -> bool """
  pass
 def RowReduce(self,zeroTolerance,*__args):
  """
  RowReduce(self: Matrix,zeroTolerance: float,b: Array[Point3d]) -> (int,float)
  RowReduce(self: Matrix,zeroTolerance: float,b: Array[float]) -> (int,float)
  RowReduce(self: Matrix,zeroTolerance: float) -> (int,float,float)
  """
  pass
 def Scale(self,s):
  """ Scale(self: Matrix,s: float) """
  pass
 def SetDiagonal(self,d):
  """ SetDiagonal(self: Matrix,d: float) """
  pass
 def SwapColumns(self,columnA,columnB):
  """ SwapColumns(self: Matrix,columnA: int,columnB: int) -> bool """
  pass
 def SwapRows(self,rowA,rowB):
  """ SwapRows(self: Matrix,rowA: int,rowB: int) -> bool """
  pass
 def Transpose(self):
  """ Transpose(self: Matrix) -> bool """
  pass
 def Zero(self):
  """ Zero(self: Matrix) """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+y """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __getitem__(self,*args):
  """ x.__getitem__(y) <==> x[y] """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __mul__(self,*args):
  """ x.__mul__(y) <==> x*y """
  pass
 @staticmethod
 def __new__(self,*__args):
  """
  __new__(cls: type,rowCount: int,columnCount: int)
  __new__(cls: type,xform: Transform)
  """
  pass
 def __radd__(self,*args):
  """ __radd__(a: Matrix,b: Matrix) -> Matrix """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __rmul__(self,*args):
  """ __rmul__(a: Matrix,b: Matrix) -> Matrix """
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 ColumnCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ColumnCount(self: Matrix) -> int

"""

 IsColumnOrthogonal=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsColumnOrthogonal(self: Matrix) -> bool

"""

 IsColumnOrthoNormal=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsColumnOrthoNormal(self: Matrix) -> bool

"""

 IsRowOrthogonal=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsRowOrthogonal(self: Matrix) -> bool

"""

 IsRowOrthoNormal=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsRowOrthoNormal(self: Matrix) -> bool

"""

 IsSquare=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsSquare(self: Matrix) -> bool

"""

 IsValid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsValid(self: Matrix) -> bool

"""

 RowCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: RowCount(self: Matrix) -> int

"""


