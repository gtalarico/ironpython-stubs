# encoding: utf-8
# module Tekla.Structures.Drawing.Automation calls itself Automation
# from Tekla.Structures.Drawing, Version=2017.0.0.0, Culture=neutral, PublicKeyToken=2f04dbe497b71114
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AutoDrawingRule(object):
    """ AutoDrawingRule(RuleFromFile: str) """
    @staticmethod # known case of __new__
    def __new__(self, RuleFromFile):
        """ __new__(cls: type, RuleFromFile: str) """
        pass

    Filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Filename(self: AutoDrawingRule) -> str

Set: Filename(self: AutoDrawingRule) = value
"""



class AutoDrawingsStatusEnum(Enum):
    """ enum AutoDrawingsStatusEnum, values: ERROR_DRAWING_EDITOR_MUST_BE_CLOSED (3), ERROR_NUMBERING_NOT_UPTODATE (2), OPERATION_FAILED (1), OPERATION_OK (0) """
    ERROR_DRAWING_EDITOR_MUST_BE_CLOSED = None
    ERROR_NUMBERING_NOT_UPTODATE = None
    OPERATION_FAILED = None
    OPERATION_OK = None
    value__ = None


class DrawingCreator(object):
    # no doc
    @staticmethod
    def CreateDrawings(Rule, *__args):
        """
        CreateDrawings(Rule: AutoDrawingRule, ModelObjectIdentifier: Identifier) -> bool
        CreateDrawings(Rule: AutoDrawingRule, ModelObjectIdentifier: Identifier) -> (bool, AutoDrawingsStatusEnum)
        CreateDrawings(Rule: AutoDrawingRule, aModelObjectIdentifier: List[Identifier]) -> (bool, AutoDrawingsStatusEnum)
        """
        pass

    __all__ = [
        '__reduce_ex__',
        'CreateDrawings',
    ]


