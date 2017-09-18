# encoding: utf-8
# module Grasshopper.GUI.Stacks calls itself Stacks
# from Grasshopper, Version=1.0.0.20, Culture=neutral, PublicKeyToken=dda4f5ec2cd80803
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class GH_Interpolation(Enum, IComparable, IFormattable, IConvertible):
    """ enum GH_Interpolation, values: cubic (2), linear (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    cubic = None
    linear = None
    value__ = None


class GH_Motion(object):
    """
    GH_Motion(rec_0: Rectangle, rec_1: Rectangle, duration: int)
    GH_Motion(rec_0: Rectangle, rec_1: Rectangle, time_0: Int64, time_1: Int64)
    """
    def ResizeContainer(self, region, fit_horizontal, fit_vertical):
        """ ResizeContainer(self: GH_Motion, region: Rectangle, fit_horizontal: bool, fit_vertical: bool) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, rec_0, rec_1, *__args):
        """
        __new__(cls: type, rec_0: Rectangle, rec_1: Rectangle, duration: int)
        __new__(cls: type, rec_0: Rectangle, rec_1: Rectangle, time_0: Int64, time_1: Int64)
        """
        pass

    CurrentBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentBox(self: GH_Motion) -> Rectangle

"""

    FinalBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FinalBox(self: GH_Motion) -> Rectangle

"""

    InitialBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InitialBox(self: GH_Motion) -> Rectangle

"""

    InMotion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InMotion(self: GH_Motion) -> bool

"""

    Interpolation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Interpolation(self: GH_Motion) -> GH_Interpolation

Set: Interpolation(self: GH_Motion) = value
"""

    Parameter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Parameter(self: GH_Motion) -> float

"""

    t0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: t0(self: GH_Motion) -> Int64

"""

    t1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: t1(self: GH_Motion) -> Int64

"""



class GH_Stack(object):
    """
    GH_Stack()
    GH_Stack(update_interval: int)
    GH_Stack(update_interval: int, animation_length: int)
    GH_Stack(update_interval: int, animation_length: int, animation_interpolation: GH_Interpolation)
    """
    def AddElement(self, *__args):
        """ AddElement(self: GH_Stack, rec_0: Rectangle, rec_1: Rectangle, duration_override: int)AddElement(self: GH_Stack, rec_0: Rectangle, rec_1: Rectangle)AddElement(self: GH_Stack, rec: Rectangle) """
        pass

    def Clear(self):
        """ Clear(self: GH_Stack) """
        pass

    def Destroy(self):
        """ Destroy(self: GH_Stack) """
        pass

    def InsertElement(self, index, *__args):
        """ InsertElement(self: GH_Stack, index: int, rec_0: Rectangle, rec_1: Rectangle, duration_override: int)InsertElement(self: GH_Stack, index: int, rec_0: Rectangle, rec_1: Rectangle)InsertElement(self: GH_Stack, index: int, rec: Rectangle) """
        pass

    def RemoveElement(self, index):
        """ RemoveElement(self: GH_Stack, index: int) """
        pass

    def ResizeContainer(self, region, fit_horizontal, fit_vertical):
        """ ResizeContainer(self: GH_Stack, region: Rectangle, fit_horizontal: bool, fit_vertical: bool) """
        pass

    def SetNewTarget(self, index, element, bAnimate=None):
        """ SetNewTarget(self: GH_Stack, index: int, element: Rectangle, bAnimate: bool)SetNewTarget(self: GH_Stack, index: int, element: Rectangle) """
        pass

    def SetOwner(self, ui_thread_owner, ui_thread_update, ui_thread_complete=None):
        """ SetOwner(self: GH_Stack, ui_thread_owner: Control, ui_thread_update: GH_StackEventDelegate, ui_thread_complete: GH_StackEventDelegate)SetOwner(self: GH_Stack, ui_thread_owner: Control, ui_thread_update: GH_StackEventDelegate) """
        pass

    @staticmethod # known case of __new__
    def __new__(self, update_interval=None, animation_length=None, animation_interpolation=None):
        """
        __new__(cls: type)
        __new__(cls: type, update_interval: int)
        __new__(cls: type, update_interval: int, animation_length: int)
        __new__(cls: type, update_interval: int, animation_length: int, animation_interpolation: GH_Interpolation)
        """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: GH_Stack) -> int

"""

    Duration = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Duration(self: GH_Stack) -> int

Set: Duration(self: GH_Stack) = value
"""

    InMotion = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: InMotion(self: GH_Stack) -> bool

"""

    Interpolation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Interpolation(self: GH_Stack) -> GH_Interpolation

Set: Interpolation(self: GH_Stack) = value
"""

    UpdateInterval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UpdateInterval(self: GH_Stack) -> int

Set: UpdateInterval(self: GH_Stack) = value
"""


    GH_StackEventDelegate = None


