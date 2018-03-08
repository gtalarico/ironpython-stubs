# encoding: utf-8
# module Tekla.Structures.Forming calls itself Forming
# from Tekla.Structures, Version=2017.0.0.0, Culture=neutral, PublicKeyToken=2f04dbe497b71114
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class DeformingType(Enum):
    """ enum DeformingType, values: DEFORMED (1), NOT_SPECIFIED (0), UNDEFORMED (2) """
    DEFORMED = None
    NOT_SPECIFIED = None
    UNDEFORMED = None
    value__ = None


class FoldingType(Enum):
    """ enum FoldingType, values: FOLDED (1), NOT_SPECIFIED (0), UNFOLDED (2) """
    FOLDED = None
    NOT_SPECIFIED = None
    UNFOLDED = None
    value__ = None


class FormingStates(object):
    """
    FormingStates()
    FormingStates(deforming: DeformingType)
    FormingStates(folding: FoldingType)
    FormingStates(wrapping: WrappingType)
    FormingStates(deforming: DeformingType, folding: FoldingType, wrapping: WrappingType)
    """
    def Clone(self):
        """ Clone(self: FormingStates) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, deforming: DeformingType)
        __new__(cls: type, folding: FoldingType)
        __new__(cls: type, wrapping: WrappingType)
        __new__(cls: type, deforming: DeformingType, folding: FoldingType, wrapping: WrappingType)
        """
        pass

    Deforming = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Deforming(self: FormingStates) -> DeformingType

Set: Deforming(self: FormingStates) = value
"""

    Folding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Folding(self: FormingStates) -> FoldingType

Set: Folding(self: FormingStates) = value
"""

    Wrapping = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Wrapping(self: FormingStates) -> WrappingType

Set: Wrapping(self: FormingStates) = value
"""



class WrappingType(Enum):
    """ enum WrappingType, values: NOT_SPECIFIED (0), UNWRAPPED (2), WRAPPED (1) """
    NOT_SPECIFIED = None
    UNWRAPPED = None
    value__ = None
    WRAPPED = None


