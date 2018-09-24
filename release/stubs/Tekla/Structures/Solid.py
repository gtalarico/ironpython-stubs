# encoding: utf-8
# module Tekla.Structures.Solid calls itself Solid
# from Tekla.Structures, Version=2017.0.0.0, Culture=neutral, PublicKeyToken=2f04dbe497b71114
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class Edge(object):
    # no doc
    def Clone(self):
        """ Clone(self: Edge) -> object """
        pass

    EndPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: EndPoint(self: Edge) -> Point

"""

    StartPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StartPoint(self: Edge) -> Point

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Type(self: Edge) -> EdgeTypeEnum

"""


    EdgeTypeEnum = None


class EdgeEnumerator(object):
    # no doc
    def MoveNext(self):
        """ MoveNext(self: EdgeEnumerator) -> bool """
        pass

    def next(self, *args): #cannot find CLR method
        """ next(self: object) -> object """
        pass

    def Reset(self):
        """ Reset(self: EdgeEnumerator) """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerator) -> object """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Current(self: EdgeEnumerator) -> object

"""



class Face(object):
    # no doc
    def GetLoopEnumerator(self):
        """ GetLoopEnumerator(self: Face) -> LoopEnumerator """
        pass

    Normal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Normal(self: Face) -> Vector

"""

    OriginPartId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: OriginPartId(self: Face) -> Identifier

"""



class FaceEnumerator(object):
    # no doc
    def MoveNext(self):
        """ MoveNext(self: FaceEnumerator) -> bool """
        pass

    def next(self, *args): #cannot find CLR method
        """ next(self: object) -> object """
        pass

    def Reset(self):
        """ Reset(self: FaceEnumerator) """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerator) -> object """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Current(self: FaceEnumerator) -> Face

"""



class ISolid:
    # no doc
    def GetEdgeEnumerator(self):
        """ GetEdgeEnumerator(self: ISolid) -> EdgeEnumerator """
        pass

    def GetFaceEnumerator(self):
        """ GetFaceEnumerator(self: ISolid) -> FaceEnumerator """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    MaximumPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MaximumPoint(self: ISolid) -> Point

"""

    MinimumPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: MinimumPoint(self: ISolid) -> Point

"""



class Loop(object):
    # no doc
    def GetVertexEnumerator(self):
        """ GetVertexEnumerator(self: Loop) -> VertexEnumerator """
        pass


class LoopEnumerator(object):
    # no doc
    def MoveNext(self):
        """ MoveNext(self: LoopEnumerator) -> bool """
        pass

    def next(self, *args): #cannot find CLR method
        """ next(self: object) -> object """
        pass

    def Reset(self):
        """ Reset(self: LoopEnumerator) """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerator) -> object """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Current(self: LoopEnumerator) -> Loop

"""



class Shell(object):
    # no doc
    def GetEdgeEnumerator(self):
        """ GetEdgeEnumerator(self: Shell) -> EdgeEnumerator """
        pass

    def GetFaceEnumerator(self):
        """ GetFaceEnumerator(self: Shell) -> FaceEnumerator """
        pass


class ShellEnumerator(object):
    # no doc
    def MoveNext(self):
        """ MoveNext(self: ShellEnumerator) -> bool """
        pass

    def next(self, *args): #cannot find CLR method
        """ next(self: object) -> object """
        pass

    def Reset(self):
        """ Reset(self: ShellEnumerator) """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerator) -> object """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Current(self: ShellEnumerator) -> object

"""



class VertexEnumerator(object):
    # no doc
    def MoveNext(self):
        """ MoveNext(self: VertexEnumerator) -> bool """
        pass

    def next(self, *args): #cannot find CLR method
        """ next(self: object) -> object """
        pass

    def Reset(self):
        """ Reset(self: VertexEnumerator) """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerator) -> object """
        pass

    Current = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Current(self: VertexEnumerator) -> Point

"""



