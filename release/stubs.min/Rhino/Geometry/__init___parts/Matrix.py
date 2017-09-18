class Matrix(object,IDisposable):
 """
 Represents an arbitrarily sized matrix of System.Doubledouble-precision

    floating point numbers. If you are working with a 4x4 matrix,then you may want

    to use the Rhino.Geometry.Transform class instead.

 

 Matrix(rowCount: int,columnCount: int)

 Matrix(xform: Transform)
 """
 def BackSolve(self,zeroTolerance,b):
  """
  BackSolve(self: Matrix,zeroTolerance: float,b: Array[float]) -> Array[float]

  

   Solves M*x=b where M is upper triangular with a unit diagonal and

     b is a column of 

    values.

  

  

   zeroTolerance: (>=0.0) used to test for "zero" values in b

     in underdetermined systems of equations.

   b: The values in B[RowCount],...,B[B.Length-1] are tested to

     make sure they are within 

    "zeroTolerance".

  

   Returns: Array of length ColumnCount on success. null on error.
  """
  pass
 def BackSolvePoints(self,zeroTolerance,b):
  """
  BackSolvePoints(self: Matrix,zeroTolerance: float,b: Array[Point3d]) -> Array[Point3d]

  

   Solves M*x=b where M is upper triangular with a unit diagonal and

     b is a column of 

    3d points.

  

  

   zeroTolerance: (>=0.0) used to test for "zero" values in b

     in underdetermined systems of equations.

   b: The values in B[RowCount],...,B[B.Length-1] are tested to

     make sure they are "zero".

   Returns: Array of length ColumnCount on success. null on error.
  """
  pass
 def Dispose(self):
  """
  Dispose(self: Matrix)

   Actively reclaims unmanaged resources that this instance uses.
  """
  pass
 def Duplicate(self):
  """
  Duplicate(self: Matrix) -> Matrix

  

   Create a duplicate of this matrix.

   Returns: An exact duplicate of this matrix.
  """
  pass
 def GetHashCode(self):
  """
  GetHashCode(self: Matrix) -> int

  

   Gets the hash code for this matrix. The hash code will change 

     when the matrix 

    changes so you cannot change matrices while they are stored in 

     hash tables.

  

   Returns: Hash code.
  """
  pass
 def Invert(self,zeroTolerance):
  """
  Invert(self: Matrix,zeroTolerance: float) -> bool

  

   Modifies this matrix to become its own inverse.

     Matrix might be non-invertible 

    (singular) and the return value will be false.

  

  

   zeroTolerance: The admitted tolerance for 0.

   Returns: true if operation succeeded; otherwise false.
  """
  pass
 def RowReduce(self,zeroTolerance,*__args):
  """
  RowReduce(self: Matrix,zeroTolerance: float,b: Array[Point3d]) -> (int,float)

  

   Row reduces a matrix as the first step in solving M*X=b where

     b is a column of 3d 

    points.

  

  

   zeroTolerance: (>=0.0) zero tolerance for pivot test. If the absolute value of a pivot

     is <= 

    zero_tolerance,then the pivot is assumed to be zero.

  

   b: An array of RowCount 3d points that is row reduced with the matrix.

   Returns: Rank of the matrix.

  RowReduce(self: Matrix,zeroTolerance: float,b: Array[float]) -> (int,float)

  

   Row reduces a matrix as the first step in solving M*X=b where

     b is a column of 

    values.

  

  

   zeroTolerance: (>=0.0) zero tolerance for pivot test. If the absolute value of a pivot

     is <= 

    zero_tolerance,then the pivot is assumed to be zero.

  

   b: an array of RowCount values that is row reduced with the matrix.

   Returns: Rank of the matrix.

  RowReduce(self: Matrix,zeroTolerance: float) -> (int,float,float)

  

   Row reduces a matrix to calculate rank and determinant.

  

   zeroTolerance: (>=0.0) zero tolerance for pivot test.  If a the absolute value of

     a pivot is <= 

    zeroTolerance,then the pivot is assumed to be zero.

  

   Returns: Rank of the matrix.
  """
  pass
 def Scale(self,s):
  """
  Scale(self: Matrix,s: float)

   Modifies the current matrix by multiplying its values by a number.

  

   s: A scale factor.
  """
  pass
 def SetDiagonal(self,d):
  """
  SetDiagonal(self: Matrix,d: float)

   Sets diagonal value and zeros off all non-diagonal values.

  

   d: The new diagonal value.
  """
  pass
 def SwapColumns(self,columnA,columnB):
  """
  SwapColumns(self: Matrix,columnA: int,columnB: int) -> bool

  

   Exchanges two columns.

  

   columnA: A first column.

   columnB: Another column.

   Returns: true if operation succeeded; otherwise false.
  """
  pass
 def SwapRows(self,rowA,rowB):
  """
  SwapRows(self: Matrix,rowA: int,rowB: int) -> bool

  

   Exchanges two rows.

  

   rowA: A first row.

   rowB: Another row.

   Returns: true if operation succeeded; otherwise false.
  """
  pass
 def Transpose(self):
  """
  Transpose(self: Matrix) -> bool

  

   Modifies this matrix to be its transpose.

     This is like swapping rows with 

    columns.http://en.wikipedia.org/wiki/Transpose

  

   Returns: true if operation succeeded; otherwise false.
  """
  pass
 def Zero(self):
  """
  Zero(self: Matrix)

   Sets all values inside the matrix to zero.
  """
  pass
 def __add__(self,*args):
  """ x.__add__(y) <==> x+y """
  pass
 def __enter__(self,*args):
  """
  __enter__(self: IDisposable) -> object

  

   Provides the implementation of __enter__ for objects which implement IDisposable.
  """
  pass
 def __exit__(self,*args):
  """
  __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object)

   Provides the implementation of __exit__ for objects which implement IDisposable.
  """
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
  """
  __radd__(a: Matrix,b: Matrix) -> Matrix

  

   Adds two matrices and returns a new sum matrix.

  

   a: A first matrix to use in calculation.

   b: Another matrix to use in calculation.

   Returns: The sum matrix.
  """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 def __rmul__(self,*args):
  """
  __rmul__(a: Matrix,b: Matrix) -> Matrix

  

   Multiplies two matrices and returns a new product matrix.

  

   a: A first matrix to use in calculation.

   b: Another matrix to use in calculation.

   Returns: The product matrix.
  """
  pass
 def __setitem__(self,*args):
  """ x.__setitem__(i,y) <==> x[i]= """
  pass
 ColumnCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the amount of columns.



Get: ColumnCount(self: Matrix) -> int



"""

 IsColumnOrthogonal=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the matrix is column orthogonal.



Get: IsColumnOrthogonal(self: Matrix) -> bool



"""

 IsColumnOrthoNormal=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the matrix is column orthonormal.



Get: IsColumnOrthoNormal(self: Matrix) -> bool



"""

 IsRowOrthogonal=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the matrix is row orthogonal.



Get: IsRowOrthogonal(self: Matrix) -> bool



"""

 IsRowOrthoNormal=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether the matrix is row orthonormal.



Get: IsRowOrthoNormal(self: Matrix) -> bool



"""

 IsSquare=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this matrix has the same number of rows

   and columns. 0x0 matrices are not considered square.



Get: IsSquare(self: Matrix) -> bool



"""

 IsValid=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets a value indicating whether this matrix is valid.



Get: IsValid(self: Matrix) -> bool



"""

 RowCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the amount of rows.



Get: RowCount(self: Matrix) -> int



"""


