# encoding: utf-8
# module Autodesk.DesignScript.Geometry.Core calls itself Core
# from ProtoGeometry, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class EntityTags(object):
    """ EntityTags(tags: Dictionary[str, object], parent: DesignScriptEntity) """
    def AddTag(self, tag, data):
        """ AddTag(self: EntityTags, tag: str, data: object) """
        pass

    def LookupTag(self, name):
        """ LookupTag(self: EntityTags, name: str) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, tags, parent):
        """ __new__(cls: type, tags: Dictionary[str, object], parent: DesignScriptEntity) """
        pass

    Parent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Parent(self: EntityTags) -> DesignScriptEntity

Set: Parent(self: EntityTags) = value
"""



