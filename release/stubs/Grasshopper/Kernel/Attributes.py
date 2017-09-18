# encoding: utf-8
# module Grasshopper.Kernel.Attributes calls itself Attributes
# from Grasshopper, Version=1.0.0.20, Culture=neutral, PublicKeyToken=dda4f5ec2cd80803
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class GH_ComponentAttributes(GH_Attributes[IGH_Component], IGH_Attributes, GH_ISerializable, IGH_ResponsiveObject, IGH_TooltipAwareObject):
    """ GH_ComponentAttributes(component: IGH_Component) """
    def AppendToAttributeTree(self, attributes):
        """ AppendToAttributeTree(self: GH_ComponentAttributes, attributes: List[IGH_Attributes]) """
        pass

    def ExpireLayout(self):
        """ ExpireLayout(self: GH_ComponentAttributes) """
        pass

    def InvalidateCanvas(self, canvas, e):
        """ InvalidateCanvas(self: GH_ComponentAttributes, canvas: GH_Canvas, e: GH_CanvasMouseEvent) -> bool """
        pass

    def Layout(self, *args): #cannot find CLR method
        """ Layout(self: GH_ComponentAttributes) """
        pass

    @staticmethod
    def LayoutBounds(owner, bounds):
        """ LayoutBounds(owner: IGH_Component, bounds: RectangleF) -> RectangleF """
        pass

    @staticmethod
    def LayoutComponentBox(owner):
        """ LayoutComponentBox(owner: IGH_Component) -> RectangleF """
        pass

    @staticmethod
    def LayoutInputParams(owner, componentBox):
        """ LayoutInputParams(owner: IGH_Component, componentBox: RectangleF) """
        pass

    @staticmethod
    def LayoutOutputParams(owner, componentBox):
        """ LayoutOutputParams(owner: IGH_Component, componentBox: RectangleF) """
        pass

    def PrepareForRender(self, *args): #cannot find CLR method
        """ PrepareForRender(self: GH_Attributes[IGH_Component], canvas: GH_Canvas) """
        pass

    def Render(self, *args): #cannot find CLR method
        """ Render(self: GH_ComponentAttributes, canvas: GH_Canvas, graphics: Graphics, channel: GH_CanvasChannel) """
        pass

    def RenderComponentCapsule(self, *args): #cannot find CLR method
        """ RenderComponentCapsule(self: GH_ComponentAttributes, canvas: GH_Canvas, graphics: Graphics, drawComponentBaseBox: bool, drawComponentNameBox: bool, drawJaggedEdges: bool, drawParameterGrips: bool, drawParameterNames: bool, drawZuiElements: bool)RenderComponentCapsule(self: GH_ComponentAttributes, canvas: GH_Canvas, graphics: Graphics) """
        pass

    @staticmethod
    def RenderComponentParameters(canvas, graphics, owner, style):
        """ RenderComponentParameters(canvas: GH_Canvas, graphics: Graphics, owner: IGH_Component, style: GH_PaletteStyle) """
        pass

    def RenderIncomingWires(self, *args): #cannot find CLR method
        """ RenderIncomingWires(self: GH_Attributes[IGH_Component], painter: GH_Painter, sources: IEnumerable[IGH_Param], styles: IEnumerable[Pen])RenderIncomingWires(self: GH_Attributes[IGH_Component], painter: GH_Painter, sources: IEnumerable[IGH_Param], style: GH_ParamWireDisplay) """
        pass

    def RenderVariableParameterUI(self, *args): #cannot find CLR method
        """ RenderVariableParameterUI(self: GH_ComponentAttributes, canvas: GH_Canvas, graphics: Graphics) """
        pass

    def RespondToMouseDown(self, sender, e):
        """ RespondToMouseDown(self: GH_ComponentAttributes, sender: GH_Canvas, e: GH_CanvasMouseEvent) -> GH_ObjectResponse """
        pass

    def SetupTooltip(self, canvasPoint, e):
        """ SetupTooltip(self: GH_ComponentAttributes, canvasPoint: PointF, e: GH_TooltipDisplayEventArgs) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, component):
        """ __new__(cls: type, component: IGH_Component) """
        pass

    ContentBox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ContentBox(self: GH_ComponentAttributes) -> RectangleF

"""

    HasInputGrip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasInputGrip(self: GH_ComponentAttributes) -> bool

"""

    HasOutputGrip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasOutputGrip(self: GH_ComponentAttributes) -> bool

"""

    PathName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: PathName(self: GH_ComponentAttributes) -> str

"""


    m_innerBounds = None


class GH_FloatingParamAttributes(GH_Attributes[IGH_Param], IGH_Attributes, GH_ISerializable, IGH_ResponsiveObject, IGH_TooltipAwareObject):
    """ GH_FloatingParamAttributes(param: IGH_Param) """
    def ExpireLayout(self):
        """ ExpireLayout(self: GH_FloatingParamAttributes) """
        pass

    def Layout(self, *args): #cannot find CLR method
        """ Layout(self: GH_FloatingParamAttributes) """
        pass

    def PrepareForRender(self, *args): #cannot find CLR method
        """ PrepareForRender(self: GH_Attributes[IGH_Param], canvas: GH_Canvas) """
        pass

    def Render(self, *args): #cannot find CLR method
        """ Render(self: GH_FloatingParamAttributes, canvas: GH_Canvas, graphics: Graphics, channel: GH_CanvasChannel) """
        pass

    def RenderIncomingWires(self, *args): #cannot find CLR method
        """ RenderIncomingWires(self: GH_Attributes[IGH_Param], painter: GH_Painter, sources: IEnumerable[IGH_Param], styles: IEnumerable[Pen])RenderIncomingWires(self: GH_Attributes[IGH_Param], painter: GH_Painter, sources: IEnumerable[IGH_Param], style: GH_ParamWireDisplay) """
        pass

    def RespondToMouseDoubleClick(self, sender, e):
        """ RespondToMouseDoubleClick(self: GH_FloatingParamAttributes, sender: GH_Canvas, e: GH_CanvasMouseEvent) -> GH_ObjectResponse """
        pass

    def SetupTooltip(self, point, e):
        """ SetupTooltip(self: GH_FloatingParamAttributes, point: PointF, e: GH_TooltipDisplayEventArgs) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, param):
        """ __new__(cls: type, param: IGH_Param) """
        pass

    DefaultWidth = 50
    IconHeight = 24
    TextHeight = 20


class GH_LinkedParamAttributes(GH_Attributes[IGH_Param], IGH_Attributes, GH_ISerializable, IGH_ResponsiveObject, IGH_TooltipAwareObject):
    """ GH_LinkedParamAttributes(param: IGH_Param, parent: IGH_Attributes) """
    def Layout(self, *args): #cannot find CLR method
        """ Layout(self: GH_LinkedParamAttributes) """
        pass

    def PrepareForRender(self, *args): #cannot find CLR method
        """ PrepareForRender(self: GH_Attributes[IGH_Param], canvas: GH_Canvas) """
        pass

    def Render(self, *args): #cannot find CLR method
        """ Render(self: GH_LinkedParamAttributes, canvas: GH_Canvas, graphics: Graphics, channel: GH_CanvasChannel) """
        pass

    def RenderIncomingWires(self, *args): #cannot find CLR method
        """ RenderIncomingWires(self: GH_Attributes[IGH_Param], painter: GH_Painter, sources: IEnumerable[IGH_Param], styles: IEnumerable[Pen])RenderIncomingWires(self: GH_Attributes[IGH_Param], painter: GH_Painter, sources: IEnumerable[IGH_Param], style: GH_ParamWireDisplay) """
        pass

    def SetupTooltip(self, point, e):
        """ SetupTooltip(self: GH_LinkedParamAttributes, point: PointF, e: GH_TooltipDisplayEventArgs) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, param, parent):
        """ __new__(cls: type, param: IGH_Param, parent: IGH_Attributes) """
        pass

    HasInputGrip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasInputGrip(self: GH_LinkedParamAttributes) -> bool

"""

    HasOutputGrip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: HasOutputGrip(self: GH_LinkedParamAttributes) -> bool

"""



class GH_ResizableAttributes(GH_Attributes[T], IGH_Attributes, GH_ISerializable, IGH_ResponsiveObject, IGH_TooltipAwareObject):
    # no doc
    def Layout(self, *args): #cannot find CLR method
        """ Layout(self: GH_Attributes[T]) """
        pass

    def PrepareForRender(self, *args): #cannot find CLR method
        """ PrepareForRender(self: GH_Attributes[T], canvas: GH_Canvas) """
        pass

    def Render(self, *args): #cannot find CLR method
        """ Render(self: GH_Attributes[T], canvas: GH_Canvas, graphics: Graphics, channel: GH_CanvasChannel) """
        pass

    def RenderIncomingWires(self, *args): #cannot find CLR method
        """ RenderIncomingWires(self: GH_Attributes[T], painter: GH_Painter, sources: IEnumerable[IGH_Param], styles: IEnumerable[Pen])RenderIncomingWires(self: GH_Attributes[T], painter: GH_Painter, sources: IEnumerable[IGH_Param], style: GH_ParamWireDisplay) """
        pass

    def RespondToMouseDown(self, sender, e):
        """ RespondToMouseDown(self: GH_ResizableAttributes[T], sender: GH_Canvas, e: GH_CanvasMouseEvent) -> GH_ObjectResponse """
        pass

    def RespondToMouseMove(self, sender, e):
        """ RespondToMouseMove(self: GH_ResizableAttributes[T], sender: GH_Canvas, e: GH_CanvasMouseEvent) -> GH_ObjectResponse """
        pass

    def RespondToMouseUp(self, sender, e):
        """ RespondToMouseUp(self: GH_ResizableAttributes[T], sender: GH_Canvas, e: GH_CanvasMouseEvent) -> GH_ObjectResponse """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, owner: T) """
        pass

    MaximumSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    MinimumSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    SizingBorders = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



