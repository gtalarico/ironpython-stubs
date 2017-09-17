# encoding: utf-8
# module Revit.Application calls itself Application
# from RevitNodes, Version=1.2.1.3083, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class Document(object):
    """ A Revit Document """
    ActiveView = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the active view for the document

Get: ActiveView(self: Document) -> View

"""

    FilePath = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The full path of the Document.

Get: FilePath(self: Document) -> str

"""

    IsFamilyDocument = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Is the Document a Family?

Get: IsFamilyDocument(self: Document) -> bool

"""

    Location = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Extracts Latitude and Longitude from Revit

Get: Location(self: Document) -> Location

"""


    Current = None


