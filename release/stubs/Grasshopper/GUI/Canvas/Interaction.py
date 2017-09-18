# encoding: utf-8
# module Grasshopper.GUI.Canvas.Interaction calls itself Interaction
# from Grasshopper, Version=1.0.0.20, Culture=neutral, PublicKeyToken=dda4f5ec2cd80803
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class GH_AbstractInteraction(object, IGH_MouseInteraction, IGH_ResponsiveObject, IGH_TooltipAwareObject):
    # no doc
    def Destroy(self):
        """ Destroy(self: GH_AbstractInteraction) """
        pass

    def IsTooltipRegion(self, canvas_coordinate):
        """ IsTooltipRegion(self: GH_AbstractInteraction, canvas_coordinate: PointF) -> bool """
        pass

    def RespondToKeyDown(self, sender, e):
        """ RespondToKeyDown(self: GH_AbstractInteraction, sender: GH_Canvas, e: KeyEventArgs) -> GH_ObjectResponse """
        pass

    def RespondToKeyUp(self, sender, e):
        """ RespondToKeyUp(self: GH_AbstractInteraction, sender: GH_Canvas, e: KeyEventArgs) -> GH_ObjectResponse """
        pass

    def RespondToMouseDoubleClick(self, sender, e):
        """ RespondToMouseDoubleClick(self: GH_AbstractInteraction, sender: GH_Canvas, e: GH_CanvasMouseEvent) -> GH_ObjectResponse """
        pass

    def RespondToMouseDown(self, sender, e):
        """ RespondToMouseDown(self: GH_AbstractInteraction, sender: GH_Canvas, e: GH_CanvasMouseEvent) -> GH_ObjectResponse """
        pass

    def RespondToMouseMove(self, sender, e):
        """ RespondToMouseMove(self: GH_AbstractInteraction, sender: GH_Canvas, e: GH_CanvasMouseEvent) -> GH_ObjectResponse """
        pass

    def RespondToMouseUp(self, sender, e):
        """ RespondToMouseUp(self: GH_AbstractInteraction, sender: GH_Canvas, e: GH_CanvasMouseEvent) -> GH_ObjectResponse """
        pass

    def SetupTooltip(self, canvasPoint, e):
        """ SetupTooltip(self: GH_AbstractInteraction, canvasPoint: PointF, e: GH_TooltipDisplayEventArgs) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, canvas: GH_Canvas, mouseEvent: GH_CanvasMouseEvent, activeOnMotion: bool) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Canvas = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Canvas(self: GH_AbstractInteraction) -> GH_Canvas

"""

    CanvasPointDown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanvasPointDown(self: GH_AbstractInteraction) -> PointF

"""

    ControlPointDown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ControlPointDown(self: GH_AbstractInteraction) -> Point

"""

    DeactivateOnFocusLoss = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeactivateOnFocusLoss(self: GH_AbstractInteraction) -> bool

"""

    IsActive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsActive(self: GH_AbstractInteraction) -> bool

"""

    TooltipEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TooltipEnabled(self: GH_AbstractInteraction) -> bool

"""


    m_active = None
    m_canvas = None
    m_canvas_mousedown = None
    m_control_mousedown = None


class GH_CycleInteraction(GH_AbstractInteraction, IGH_MouseInteraction, IGH_ResponsiveObject, IGH_TooltipAwareObject):
    """ GH_CycleInteraction(parentCanvas: GH_Canvas) """
    def Destroy(self):
        """ Destroy(self: GH_CycleInteraction) """
        pass

    def RespondToKeyDown(self, sender, e):
        """ RespondToKeyDown(self: GH_CycleInteraction, sender: GH_Canvas, e: KeyEventArgs) -> GH_ObjectResponse """
        pass

    def RespondToKeyUp(self, sender, e):
        """ RespondToKeyUp(self: GH_CycleInteraction, sender: GH_Canvas, e: KeyEventArgs) -> GH_ObjectResponse """
        pass

    def RespondToMouseDoubleClick(self, sender, e):
        """ RespondToMouseDoubleClick(self: GH_CycleInteraction, sender: GH_Canvas, e: GH_CanvasMouseEvent) -> GH_ObjectResponse """
        pass

    def RespondToMouseDown(self, sender, e):
        """ RespondToMouseDown(self: GH_CycleInteraction, sender: GH_Canvas, e: GH_CanvasMouseEvent) -> GH_ObjectResponse """
        pass

    def RespondToMouseMove(self, sender, e):
        """ RespondToMouseMove(self: GH_CycleInteraction, sender: GH_Canvas, e: GH_CanvasMouseEvent) -> GH_ObjectResponse """
        pass

    def RespondToMouseUp(self, sender, e):
        """ RespondToMouseUp(self: GH_CycleInteraction, sender: GH_Canvas, e: GH_CanvasMouseEvent) -> GH_ObjectResponse """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, parentCanvas):
        """ __new__(cls: type, parentCanvas: GH_Canvas) """
        pass

    DeactivateOnFocusLoss = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeactivateOnFocusLoss(self: GH_CycleInteraction) -> bool

"""


    m_active = None
    m_canvas = None
    m_canvas_mousedown = None
    m_control_mousedown = None


class GH_DragInteraction(GH_AbstractInteraction, IGH_MouseInteraction, IGH_ResponsiveObject, IGH_TooltipAwareObject):
    """ GH_DragInteraction(canvas: GH_Canvas, e: GH_CanvasMouseEvent) """
    def AddAttribute(self, attribute):
        """ AddAttribute(self: GH_DragInteraction, attribute: IGH_Attributes) """
        pass

    def AddSnapAttributes(self, attribute):
        """ AddSnapAttributes(self: GH_DragInteraction, attribute: IGH_Attributes) """
        pass

    def Destroy(self):
        """ Destroy(self: GH_DragInteraction) """
        pass

    def RespondToKeyDown(self, sender, e):
        """ RespondToKeyDown(self: GH_DragInteraction, sender: GH_Canvas, e: KeyEventArgs) -> GH_ObjectResponse """
        pass

    def RespondToKeyUp(self, sender, e):
        """ RespondToKeyUp(self: GH_DragInteraction, sender: GH_Canvas, e: KeyEventArgs) -> GH_ObjectResponse """
        pass

    def RespondToMouseDown(self, sender, e):
        """ RespondToMouseDown(self: GH_DragInteraction, sender: GH_Canvas, e: GH_CanvasMouseEvent) -> GH_ObjectResponse """
        pass

    def RespondToMouseMove(self, sender, e):
        """ RespondToMouseMove(self: GH_DragInteraction, sender: GH_Canvas, e: GH_CanvasMouseEvent) -> GH_ObjectResponse """
        pass

    def RespondToMouseUp(self, sender, e):
        """ RespondToMouseUp(self: GH_DragInteraction, sender: GH_Canvas, e: GH_CanvasMouseEvent) -> GH_ObjectResponse """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, canvas, e):
        """ __new__(cls: type, canvas: GH_Canvas, e: GH_CanvasMouseEvent) """
        pass

    AttributeCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: AttributeCount(self: GH_DragInteraction) -> int

"""


    m_active = None
    m_canvas = None
    m_canvas_mousedown = None
    m_control_mousedown = None


class GH_DumpInteraction(GH_AbstractInteraction, IGH_MouseInteraction, IGH_ResponsiveObject, IGH_TooltipAwareObject):
    """
    GH_DumpInteraction(parent: GH_Canvas)
    GH_DumpInteraction(parent: GH_Canvas, objectId: Guid)
    """
    def AppendProxy(self, proxy):
        """ AppendProxy(self: GH_DumpInteraction, proxy: IGH_ObjectProxy) """
        pass

    def Destroy(self):
        """ Destroy(self: GH_DumpInteraction) """
        pass

    def RespondToKeyDown(self, sender, e):
        """ RespondToKeyDown(self: GH_DumpInteraction, sender: GH_Canvas, e: KeyEventArgs) -> GH_ObjectResponse """
        pass

    def RespondToMouseDown(self, sender, e):
        """ RespondToMouseDown(self: GH_DumpInteraction, sender: GH_Canvas, e: GH_CanvasMouseEvent) -> GH_ObjectResponse """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, parent, objectId=None):
        """
        __new__(cls: type, parent: GH_Canvas)
        __new__(cls: type, parent: GH_Canvas, objectId: Guid)
        """
        pass

    IsAggregating = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsAggregating(self: GH_DumpInteraction) -> bool

"""


    m_active = None
    m_canvas = None
    m_canvas_mousedown = None
    m_control_mousedown = None


class GH_PanInteraction(GH_AbstractInteraction, IGH_MouseInteraction, IGH_ResponsiveObject, IGH_TooltipAwareObject):
    """ GH_PanInteraction(iParent: GH_Canvas, mEvent: GH_CanvasMouseEvent) """
    def RespondToMouseMove(self, sender, e):
        """ RespondToMouseMove(self: GH_PanInteraction, sender: GH_Canvas, e: GH_CanvasMouseEvent) -> GH_ObjectResponse """
        pass

    def RespondToMouseUp(self, sender, e):
        """ RespondToMouseUp(self: GH_PanInteraction, sender: GH_Canvas, e: GH_CanvasMouseEvent) -> GH_ObjectResponse """
        pass

    def WrapCursor(self, *args): #cannot find CLR method
        """ WrapCursor(self: GH_PanInteraction) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, iParent, mEvent):
        """ __new__(cls: type, iParent: GH_Canvas, mEvent: GH_CanvasMouseEvent) """
        pass

    m_active = None
    m_canvas = None
    m_canvas_mousedown = None
    m_control_mousedown = None
    m_newCursor = None
    m_originalTarget = None
    m_panStart = None
    m_preventUpdate = None


class GH_RadialMenuInteraction(GH_AbstractInteraction, IGH_MouseInteraction, IGH_ResponsiveObject, IGH_TooltipAwareObject):
    """ GH_RadialMenuInteraction(canvas: GH_Canvas, e: GH_CanvasMouseEvent) """
    def Destroy(self):
        """ Destroy(self: GH_RadialMenuInteraction) """
        pass

    def IsTooltipRegion(self, canvas_coordinate):
        """ IsTooltipRegion(self: GH_RadialMenuInteraction, canvas_coordinate: PointF) -> bool """
        pass

    def RespondToMouseDown(self, sender, e):
        """ RespondToMouseDown(self: GH_RadialMenuInteraction, sender: GH_Canvas, e: GH_CanvasMouseEvent) -> GH_ObjectResponse """
        pass

    def RespondToMouseMove(self, sender, e):
        """ RespondToMouseMove(self: GH_RadialMenuInteraction, sender: GH_Canvas, e: GH_CanvasMouseEvent) -> GH_ObjectResponse """
        pass

    def RespondToMouseUp(self, sender, e):
        """ RespondToMouseUp(self: GH_RadialMenuInteraction, sender: GH_Canvas, e: GH_CanvasMouseEvent) -> GH_ObjectResponse """
        pass

    def SetupTooltip(self, point, e):
        """ SetupTooltip(self: GH_RadialMenuInteraction, point: PointF, e: GH_TooltipDisplayEventArgs) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, canvas, e):
        """ __new__(cls: type, canvas: GH_Canvas, e: GH_CanvasMouseEvent) """
        pass

    DeactivateOnFocusLoss = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeactivateOnFocusLoss(self: GH_RadialMenuInteraction) -> bool

"""

    TooltipEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TooltipEnabled(self: GH_RadialMenuInteraction) -> bool

"""


    m_active = None
    m_canvas = None
    m_canvas_mousedown = None
    m_control_mousedown = None


class GH_RewireInteraction(GH_AbstractInteraction, IGH_MouseInteraction, IGH_ResponsiveObject, IGH_TooltipAwareObject):
    """ GH_RewireInteraction(iParent: GH_Canvas, mEvent: GH_CanvasMouseEvent, Source: IGH_Param) """
    def Destroy(self):
        """ Destroy(self: GH_RewireInteraction) """
        pass

    def RespondToKeyDown(self, sender, e):
        """ RespondToKeyDown(self: GH_RewireInteraction, sender: GH_Canvas, e: KeyEventArgs) -> GH_ObjectResponse """
        pass

    def RespondToKeyUp(self, sender, e):
        """ RespondToKeyUp(self: GH_RewireInteraction, sender: GH_Canvas, e: KeyEventArgs) -> GH_ObjectResponse """
        pass

    def RespondToMouseMove(self, sender, e):
        """ RespondToMouseMove(self: GH_RewireInteraction, sender: GH_Canvas, e: GH_CanvasMouseEvent) -> GH_ObjectResponse """
        pass

    def RespondToMouseUp(self, sender, e):
        """ RespondToMouseUp(self: GH_RewireInteraction, sender: GH_Canvas, e: GH_CanvasMouseEvent) -> GH_ObjectResponse """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, iParent, mEvent, Source):
        """ __new__(cls: type, iParent: GH_Canvas, mEvent: GH_CanvasMouseEvent, Source: IGH_Param) """
        pass

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: GH_RewireInteraction) -> bool

"""


    m_active = None
    m_canvas = None
    m_canvas_mousedown = None
    m_control_mousedown = None


class GH_SketchInteraction(GH_AbstractInteraction, IGH_MouseInteraction, IGH_ResponsiveObject, IGH_TooltipAwareObject):
    """ GH_SketchInteraction(iParent: GH_Canvas) """
    def AttributesChanged(self, *args): #cannot find CLR method
        """ AttributesChanged(self: GH_SketchInteraction, sender: GH_MarkupAttributesDialog) """
        pass

    def Complete(self, *args): #cannot find CLR method
        """ Complete(self: GH_SketchInteraction) """
        pass

    def Destroy(self):
        """ Destroy(self: GH_SketchInteraction) """
        pass

    def OnAttributesAccepted(self, *args): #cannot find CLR method
        """ OnAttributesAccepted(self: GH_SketchInteraction, sender: GH_MarkupAttributesDialog) """
        pass

    def OnAttributesDenied(self, *args): #cannot find CLR method
        """ OnAttributesDenied(self: GH_SketchInteraction, sender: GH_MarkupAttributesDialog) """
        pass

    def RespondToKeyDown(self, sender, e):
        """ RespondToKeyDown(self: GH_SketchInteraction, sender: GH_Canvas, e: KeyEventArgs) -> GH_ObjectResponse """
        pass

    def RespondToMouseDown(self, sender, e):
        """ RespondToMouseDown(self: GH_SketchInteraction, sender: GH_Canvas, e: GH_CanvasMouseEvent) -> GH_ObjectResponse """
        pass

    def RespondToMouseMove(self, sender, e):
        """ RespondToMouseMove(self: GH_SketchInteraction, sender: GH_Canvas, e: GH_CanvasMouseEvent) -> GH_ObjectResponse """
        pass

    def RespondToMouseUp(self, sender, e):
        """ RespondToMouseUp(self: GH_SketchInteraction, sender: GH_Canvas, e: GH_CanvasMouseEvent) -> GH_ObjectResponse """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, iParent):
        """ __new__(cls: type, iParent: GH_Canvas) """
        pass

    Att = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    m_active = None
    m_canvas = None
    m_canvas_mousedown = None
    m_control_mousedown = None
    m_dlg = None
    m_externalrelease = None
    m_markup = None
    m_path = None
    m_point = None
    m_stripe = None


class GH_SplitInteraction(GH_AbstractInteraction, IGH_MouseInteraction, IGH_ResponsiveObject, IGH_TooltipAwareObject):
    """ GH_SplitInteraction(canvas: GH_Canvas, e: GH_CanvasMouseEvent) """
    def AddAttribute(self, Attribute):
        """ AddAttribute(self: GH_SplitInteraction, Attribute: IGH_Attributes) """
        pass

    def Destroy(self):
        """ Destroy(self: GH_SplitInteraction) """
        pass

    def RespondToKeyDown(self, sender, e):
        """ RespondToKeyDown(self: GH_SplitInteraction, sender: GH_Canvas, e: KeyEventArgs) -> GH_ObjectResponse """
        pass

    def RespondToKeyUp(self, sender, e):
        """ RespondToKeyUp(self: GH_SplitInteraction, sender: GH_Canvas, e: KeyEventArgs) -> GH_ObjectResponse """
        pass

    def RespondToMouseMove(self, sender, e):
        """ RespondToMouseMove(self: GH_SplitInteraction, sender: GH_Canvas, e: GH_CanvasMouseEvent) -> GH_ObjectResponse """
        pass

    def RespondToMouseUp(self, sender, e):
        """ RespondToMouseUp(self: GH_SplitInteraction, sender: GH_Canvas, e: GH_CanvasMouseEvent) -> GH_ObjectResponse """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, canvas, e):
        """ __new__(cls: type, canvas: GH_Canvas, e: GH_CanvasMouseEvent) """
        pass

    m_active = None
    m_canvas = None
    m_canvas_mousedown = None
    m_control_mousedown = None


class GH_WindowSelectInteraction(GH_AbstractInteraction, IGH_MouseInteraction, IGH_ResponsiveObject, IGH_TooltipAwareObject):
    """ GH_WindowSelectInteraction(canvas: GH_Canvas, mEvent: GH_CanvasMouseEvent) """
    def Destroy(self):
        """ Destroy(self: GH_WindowSelectInteraction) """
        pass

    def RespondToKeyDown(self, sender, e):
        """ RespondToKeyDown(self: GH_WindowSelectInteraction, sender: GH_Canvas, e: KeyEventArgs) -> GH_ObjectResponse """
        pass

    def RespondToKeyUp(self, sender, e):
        """ RespondToKeyUp(self: GH_WindowSelectInteraction, sender: GH_Canvas, e: KeyEventArgs) -> GH_ObjectResponse """
        pass

    def RespondToMouseMove(self, sender, e):
        """ RespondToMouseMove(self: GH_WindowSelectInteraction, sender: GH_Canvas, e: GH_CanvasMouseEvent) -> GH_ObjectResponse """
        pass

    def RespondToMouseUp(self, sender, e):
        """ RespondToMouseUp(self: GH_WindowSelectInteraction, sender: GH_Canvas, e: GH_CanvasMouseEvent) -> GH_ObjectResponse """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, canvas, mEvent):
        """ __new__(cls: type, canvas: GH_Canvas, mEvent: GH_CanvasMouseEvent) """
        pass

    DeactivateOnFocusLoss = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeactivateOnFocusLoss(self: GH_WindowSelectInteraction) -> bool

"""


    m_active = None
    m_canvas = None
    m_canvas_mousedown = None
    m_control_mousedown = None


class GH_WireInteraction(GH_AbstractInteraction, IGH_MouseInteraction, IGH_ResponsiveObject, IGH_TooltipAwareObject):
    """ GH_WireInteraction(iParent: GH_Canvas, mEvent: GH_CanvasMouseEvent, Source: IGH_Param) """
    def Destroy(self):
        """ Destroy(self: GH_WireInteraction) """
        pass

    def RespondToKeyDown(self, sender, e):
        """ RespondToKeyDown(self: GH_WireInteraction, sender: GH_Canvas, e: KeyEventArgs) -> GH_ObjectResponse """
        pass

    def RespondToKeyUp(self, sender, e):
        """ RespondToKeyUp(self: GH_WireInteraction, sender: GH_Canvas, e: KeyEventArgs) -> GH_ObjectResponse """
        pass

    def RespondToMouseDown(self, sender, e):
        """ RespondToMouseDown(self: GH_WireInteraction, sender: GH_Canvas, e: GH_CanvasMouseEvent) -> GH_ObjectResponse """
        pass

    def RespondToMouseMove(self, sender, e):
        """ RespondToMouseMove(self: GH_WireInteraction, sender: GH_Canvas, e: GH_CanvasMouseEvent) -> GH_ObjectResponse """
        pass

    def RespondToMouseUp(self, sender, e):
        """ RespondToMouseUp(self: GH_WireInteraction, sender: GH_Canvas, e: GH_CanvasMouseEvent) -> GH_ObjectResponse """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, iParent, mEvent, Source):
        """ __new__(cls: type, iParent: GH_Canvas, mEvent: GH_CanvasMouseEvent, Source: IGH_Param) """
        pass

    m_active = None
    m_canvas = None
    m_canvas_mousedown = None
    m_control_mousedown = None


class GH_ZoomInteraction(GH_AbstractInteraction, IGH_MouseInteraction, IGH_ResponsiveObject, IGH_TooltipAwareObject):
    """ GH_ZoomInteraction(iParent: GH_Canvas, mEvent: GH_CanvasMouseEvent) """
    def RespondToMouseMove(self, sender, e):
        """ RespondToMouseMove(self: GH_ZoomInteraction, sender: GH_Canvas, e: GH_CanvasMouseEvent) -> GH_ObjectResponse """
        pass

    def RespondToMouseUp(self, sender, e):
        """ RespondToMouseUp(self: GH_ZoomInteraction, sender: GH_Canvas, e: GH_CanvasMouseEvent) -> GH_ObjectResponse """
        pass

    def WrapCursor(self, *args): #cannot find CLR method
        """ WrapCursor(self: GH_ZoomInteraction) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, iParent, mEvent):
        """ __new__(cls: type, iParent: GH_Canvas, mEvent: GH_CanvasMouseEvent) """
        pass

    m_active = None
    m_anchorPoint = None
    m_canvas = None
    m_canvas_mousedown = None
    m_control_mousedown = None
    m_newCursor = None
    m_originalZoom = None
    m_preventUpdate = None
    m_targetVector = None
    m_wrapped = None
    m_zoomLevel = None


class IGH_MouseInteraction(IGH_ResponsiveObject, IGH_TooltipAwareObject):
    # no doc
    def Destroy(self):
        """ Destroy(self: IGH_MouseInteraction) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    CanvasPointDown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CanvasPointDown(self: IGH_MouseInteraction) -> PointF

"""

    ControlPointDown = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ControlPointDown(self: IGH_MouseInteraction) -> Point

"""

    DeactivateOnFocusLoss = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: DeactivateOnFocusLoss(self: IGH_MouseInteraction) -> bool

"""

    IsActive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsActive(self: IGH_MouseInteraction) -> bool

"""

    Owner = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Owner(self: IGH_MouseInteraction) -> GH_Canvas

"""



