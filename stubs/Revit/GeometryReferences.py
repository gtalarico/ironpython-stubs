# encoding: utf-8
# module Revit.GeometryReferences calls itself GeometryReferences
# from RevitNodes, Version=1.2.1.3083, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class ElementGeometryReference(object):
    """ A base class for revit Reference objects """

class ElementCurveReference(ElementGeometryReference):
    """ A stable reference to a Revit curve derived from a Revit Element """
    DefaultTag = 'RevitCurveReference'


class ElementFaceReference(ElementGeometryReference):
    """ A stable reference to a Revit Face, usually derived from a Revit Element """
    DefaultTag = 'RevitFaceReference'


class ElementPlaneReference(ElementGeometryReference):
    """ A Reference to a plane extracted from a Revit ELement """

