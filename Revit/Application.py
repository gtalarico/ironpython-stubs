# encoding: utf-8
# module Revit.Application calls itself Application
# from RevitNodes, Version=1.2.1.3083, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class Document(object):
    # no doc
    ActiveView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActiveView(self: Document) -> View

"""

    FilePath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: FilePath(self: Document) -> str

"""

    IsFamilyDocument = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsFamilyDocument(self: Document) -> bool

"""

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Location(self: Document) -> Location

"""


    Current = None


