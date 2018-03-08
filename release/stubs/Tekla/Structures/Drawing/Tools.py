# encoding: utf-8
# module Tekla.Structures.Drawing.Tools calls itself Tools
# from Tekla.Structures.Drawing, Version=2017.0.0.0, Culture=neutral, PublicKeyToken=2f04dbe497b71114
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class DrawingCoordinateConverter(object):
    """ DrawingCoordinateConverter() """
    @staticmethod
    def Convert(fromView, toView, *__args):
        """
        Convert(fromView: ViewBase, toView: ViewBase, pointList: PointList) -> PointList
        Convert(fromView: ViewBase, toView: ViewBase, point: Point) -> Point
        """
        pass


class InputDefinitionFactory(object):
    """ InputDefinitionFactory() """
    @staticmethod
    def CreateInputDefinition(*__args):
        """
        CreateInputDefinition(input: Tuple[PointList, ViewBase]) -> InputDefinition
        CreateInputDefinition(input: Tuple[Point, ViewBase]) -> InputDefinition
        CreateInputDefinition(view: ViewBase, drawingObject: DrawingObject) -> InputDefinition
        CreateInputDefinition(input: Tuple[DrawingObject, ViewBase]) -> InputDefinition
        CreateInputDefinition(view: ViewBase, point1: Point, point2: Point) -> InputDefinition
        CreateInputDefinition(view: ViewBase, point: Point) -> InputDefinition
        CreateInputDefinition(view: ViewBase, points: PointList) -> InputDefinition
        CreateInputDefinition(view: ViewBase, point1: Point, point2: Point, point3: Point) -> InputDefinition
        """
        pass

    @staticmethod
    def GetDrawingObject(input):
        """ GetDrawingObject(input: InputDefinition) -> DrawingObject """
        pass

    @staticmethod
    def GetPoint(input):
        """ GetPoint(input: InputDefinition) -> Point """
        pass

    @staticmethod
    def GetPoints(input):
        """ GetPoints(input: InputDefinition) -> PointList """
        pass

    @staticmethod
    def GetView(input):
        """ GetView(input: InputDefinition) -> ViewBase """
        pass


