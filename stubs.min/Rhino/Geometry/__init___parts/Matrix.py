class Matrix(object, IDisposable):
    """
    Matrix(rowCount: int, columnCount: int)
    Matrix(xform: Transform)
    """
    def BackSolve(self, zeroTolerance, b):
        """ BackSolve(self: Matrix, zeroTolerance: float, b: Array[float]) -> Array[float] """
        pass

    def BackSolvePoints(self, zeroTolerance, b):
        """ BackSolvePoints(self: Matrix, zeroTolerance: float, b: Array[Point3d]) -> Array[Point3d] """
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

    def Invert(self, zeroTolerance):
        """ Invert(self: Matrix, zeroTolerance: float) -> bool """
        pass

    def RowReduce(self, zeroTolerance, *__args):
        """
        RowReduce(self: Matrix, zeroTolerance: float, b: Array[Point3d]) -> (int, float)
        RowReduce(self: Matrix, zeroTolerance: float, b: Array[float]) -> (int, float)
        RowReduce(self: Matrix, zeroTolerance: float) -> (int, float, float)
        """
        pass

    def Scale(self, s):
        """ Scale(self: Matrix, s: float) """
        pass

    def SetDiagonal(self, d):
        """ SetDiagonal(self: Matrix, d: float) """
        pass

    def SwapColumns(self, columnA, columnB):
        """ SwapColumns(self: Matrix, columnA: int, columnB: int) -> bool """
        pass

    def SwapRows(self, rowA, rowB):
        """ SwapRows(self: Matrix, rowA: int, rowB: int) -> bool """
        pass

    def Transpose(self):
        """ Transpose(self: Matrix) -> bool """
        pass

    def Zero(self):
        """ Zero(self: Matrix) """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __mul__(self, *args): #cannot find CLR method
        """ x.__mul__(y) <==> x*y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, rowCount: int, columnCount: int)
        __new__(cls: type, xform: Transform)
        """
        pass

    def __radd__(self, *args): #cannot find CLR method
        """ __radd__(a: Matrix, b: Matrix) -> Matrix """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __rmul__(self, *args): #cannot find CLR method
        """ __rmul__(a: Matrix, b: Matrix) -> Matrix """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    ColumnCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ColumnCount(self: Matrix) -> int

"""

    IsColumnOrthogonal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsColumnOrthogonal(self: Matrix) -> bool

"""

    IsColumnOrthoNormal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsColumnOrthoNormal(self: Matrix) -> bool

"""

    IsRowOrthogonal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsRowOrthogonal(self: Matrix) -> bool

"""

    IsRowOrthoNormal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsRowOrthoNormal(self: Matrix) -> bool

"""

    IsSquare = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSquare(self: Matrix) -> bool

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: Matrix) -> bool

"""

    RowCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: RowCount(self: Matrix) -> int

"""


