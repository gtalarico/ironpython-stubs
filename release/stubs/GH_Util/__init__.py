# encoding: utf-8
# module GH_Util
# from GH_Util, Version=1.0.0.0, Culture=neutral, PublicKeyToken=dda4f5ec2cd80803
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class GH_2DIndex(object, IComparable[GH_2DIndex]):
    """
    GH_2DIndex(new_i: int, new_j: int)
    GH_2DIndex(other: GH_2DIndex)
    """
    def Set(self, new_i, new_j):
        """ Set(self: GH_2DIndex, new_i: int, new_j: int) """
        pass

    def Shift(self, offset_i, offset_j):
        """ Shift(self: GH_2DIndex, offset_i: int, offset_j: int) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[GH_2DIndex]() -> GH_2DIndex
        
        __new__(cls: type, new_i: int, new_j: int)
        __new__(cls: type, other: GH_2DIndex)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    i = None
    j = None


class GH_2DSparseArray(object):
    """ GH_2DSparseArray[T]() """
    def AllIndices(self):
        """ AllIndices(self: GH_2DSparseArray[T]) -> List[GH_2DIndex] """
        pass

    def Clear(self):
        """ Clear(self: GH_2DSparseArray[T]) """
        pass

    def ContainsIndex(self, x, y):
        """ ContainsIndex(self: GH_2DSparseArray[T], x: int, y: int) -> bool """
        pass

    def Remove(self, x, y=None):
        """ Remove(self: GH_2DSparseArray[T], x: int, y: int)Remove(self: GH_2DSparseArray[T], x: int) """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    ValueProvider = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ValueProvider(self: GH_2DSparseArray[T]) -> ValueDelegate

Set: ValueProvider(self: GH_2DSparseArray[T]) = value
"""


    ValueDelegate = None


class GH_3DIndex(object, IComparable[GH_3DIndex]):
    """
    GH_3DIndex(new_i: int, new_j: int, new_k: int)
    GH_3DIndex(other: GH_3DIndex)
    """
    def Set(self, new_i, new_j, new_k):
        """ Set(self: GH_3DIndex, new_i: int, new_j: int, new_k: int) """
        pass

    def Shift(self, offset_i, offset_j, offset_k):
        """ Shift(self: GH_3DIndex, offset_i: int, offset_j: int, offset_k: int) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__[GH_3DIndex]() -> GH_3DIndex
        
        __new__(cls: type, new_i: int, new_j: int, new_k: int)
        __new__(cls: type, other: GH_3DIndex)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    i = None
    j = None
    k = None


class GH_NaturalComparer(object, IComparer[str]):
    """ GH_NaturalComparer() """
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class GH_NaturalStringComparer(object):
    """ GH_NaturalStringComparer() """
    @staticmethod
    def Compare(s1, s2):
        """ Compare(s1: str, s2: str) -> int """
        pass


# variables with complex values

