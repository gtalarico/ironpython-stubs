# encoding: utf-8
# module Grasshopper.GUI.Widgets calls itself Widgets
# from Grasshopper, Version=1.0.0.20, Culture=neutral, PublicKeyToken=dda4f5ec2cd80803
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class GH_Widget(object, IGH_Widget, IGH_ResponsiveObject, IGH_TooltipAwareObject):
    # no doc
    def AppendToMenu(self, menu):
        """ AppendToMenu(self: GH_Widget, menu: ToolStripDropDownMenu) """
        pass

    def Contains(self, pt_control, pt_canvas):
        """ Contains(self: GH_Widget, pt_control: Point, pt_canvas: PointF) -> bool """
        pass

    def IsTooltipRegion(self, canvas_coordinate):
        """ IsTooltipRegion(self: GH_Widget, canvas_coordinate: PointF) -> bool """
        pass

    def Menu_AppendHideItem(self, *args): #cannot find CLR method
        """ Menu_AppendHideItem(self: GH_Widget, menu: ToolStripDropDownMenu) """
        pass

    def Render(self, Canvas):
        """ Render(self: GH_Widget, Canvas: GH_Canvas) """
        pass

    def RespondToKeyDown(self, sender, e):
        """ RespondToKeyDown(self: GH_Widget, sender: GH_Canvas, e: KeyEventArgs) -> GH_ObjectResponse """
        pass

    def RespondToKeyUp(self, sender, e):
        """ RespondToKeyUp(self: GH_Widget, sender: GH_Canvas, e: KeyEventArgs) -> GH_ObjectResponse """
        pass

    def RespondToMouseDoubleClick(self, sender, e):
        """ RespondToMouseDoubleClick(self: GH_Widget, sender: GH_Canvas, e: GH_CanvasMouseEvent) -> GH_ObjectResponse """
        pass

    def RespondToMouseDown(self, sender, e):
        """ RespondToMouseDown(self: GH_Widget, sender: GH_Canvas, e: GH_CanvasMouseEvent) -> GH_ObjectResponse """
        pass

    def RespondToMouseMove(self, sender, e):
        """ RespondToMouseMove(self: GH_Widget, sender: GH_Canvas, e: GH_CanvasMouseEvent) -> GH_ObjectResponse """
        pass

    def RespondToMouseUp(self, sender, e):
        """ RespondToMouseUp(self: GH_Widget, sender: GH_Canvas, e: GH_CanvasMouseEvent) -> GH_ObjectResponse """
        pass

    def SetupTooltip(self, canvasPoint, e):
        """ SetupTooltip(self: GH_Widget, canvasPoint: PointF, e: GH_TooltipDisplayEventArgs) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: GH_Widget) -> str

"""

    Icon_24x24 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Icon_24x24(self: GH_Widget) -> Bitmap

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: GH_Widget) -> str

"""

    Owner = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Owner(self: GH_Widget) -> GH_Canvas

Set: Owner(self: GH_Widget) = value
"""

    TooltipEnabled = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TooltipEnabled(self: GH_Widget) -> bool

"""

    TooltipText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TooltipText(self: GH_Widget) -> str

"""

    Visible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Visible(self: GH_Widget) -> bool

Set: Visible(self: GH_Widget) = value
"""


    m_owner = None


class GH_AlignWidget(GH_Widget, IGH_Widget, IGH_ResponsiveObject, IGH_TooltipAwareObject):
    """ GH_AlignWidget() """
    def Contains(self, pt_control, pt_canvas):
        """ Contains(self: GH_AlignWidget, pt_control: Point, pt_canvas: PointF) -> bool """
        pass

    def Menu_AppendHideItem(self, *args): #cannot find CLR method
        """ Menu_AppendHideItem(self: GH_Widget, menu: ToolStripDropDownMenu) """
        pass

    def Render(self, canvas):
        """ Render(self: GH_AlignWidget, canvas: GH_Canvas) """
        pass

    def RespondToMouseDown(self, sender, e):
        """ RespondToMouseDown(self: GH_AlignWidget, sender: GH_Canvas, e: GH_CanvasMouseEvent) -> GH_ObjectResponse """
        pass

    def RespondToMouseMove(self, sender, e):
        """ RespondToMouseMove(self: GH_AlignWidget, sender: GH_Canvas, e: GH_CanvasMouseEvent) -> GH_ObjectResponse """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: GH_AlignWidget) -> str

"""

    Icon_24x24 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Icon_24x24(self: GH_AlignWidget) -> Bitmap

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: GH_AlignWidget) -> str

"""

    TooltipText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TooltipText(self: GH_AlignWidget) -> str

"""

    Visible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Visible(self: GH_AlignWidget) -> bool

Set: Visible(self: GH_AlignWidget) = value
"""


    m_owner = None
    SharedVisible = True
    WidgetVisibleChanged = None
    WidgetVisibleChangedEventHandler = None


class GH_CanvasWidget_FixedObject(GH_Widget, IGH_Widget, IGH_ResponsiveObject, IGH_TooltipAwareObject):
    # no doc
    def CanvasLocation(self, vp):
        """ CanvasLocation(self: GH_CanvasWidget_FixedObject, vp: GH_Viewport) -> PointF """
        pass

    def ControlLocation(self, vp):
        """ ControlLocation(self: GH_CanvasWidget_FixedObject, vp: GH_Viewport) -> Point """
        pass

    def Menu_AppendHideItem(self, *args): #cannot find CLR method
        """ Menu_AppendHideItem(self: GH_Widget, menu: ToolStripDropDownMenu) """
        pass

    def Render(self, canvas):
        """ Render(self: GH_CanvasWidget_FixedObject, canvas: GH_Canvas) """
        pass

    def Render_Internal(self, *args): #cannot find CLR method
        """ Render_Internal(self: GH_CanvasWidget_FixedObject, canvas: GH_Canvas, controlAnchor: Point, canvasAnchor: PointF, controlFrame: Rectangle, canvasFrame: RectangleF) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Padding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Padding(self: GH_CanvasWidget_FixedObject) -> int

"""

    Ratio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Ratio(self: GH_CanvasWidget_FixedObject) -> SizeF

Set: Ratio(self: GH_CanvasWidget_FixedObject) = value
"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Size(self: GH_CanvasWidget_FixedObject) -> Size

"""


    m_owner = None


class GH_CompassWidget(GH_CanvasWidget_FixedObject, IGH_Widget, IGH_ResponsiveObject, IGH_TooltipAwareObject):
    """ GH_CompassWidget() """
    def AppendToMenu(self, menu):
        """ AppendToMenu(self: GH_CompassWidget, menu: ToolStripDropDownMenu) """
        pass

    def Contains(self, pt_control, pt_canvas):
        """ Contains(self: GH_CompassWidget, pt_control: Point, pt_canvas: PointF) -> bool """
        pass

    def Menu_AppendHideItem(self, *args): #cannot find CLR method
        """ Menu_AppendHideItem(self: GH_Widget, menu: ToolStripDropDownMenu) """
        pass

    def Render_Internal(self, *args): #cannot find CLR method
        """ Render_Internal(self: GH_CompassWidget, canvas: GH_Canvas, controlAnchor: Point, canvasAnchor: PointF, controlFrame: Rectangle, canvasFrame: RectangleF) """
        pass

    def RespondToKeyDown(self, sender, e):
        """ RespondToKeyDown(self: GH_CompassWidget, sender: GH_Canvas, e: KeyEventArgs) -> GH_ObjectResponse """
        pass

    def RespondToMouseDown(self, sender, e):
        """ RespondToMouseDown(self: GH_CompassWidget, sender: GH_Canvas, e: GH_CanvasMouseEvent) -> GH_ObjectResponse """
        pass

    def RespondToMouseMove(self, sender, e):
        """ RespondToMouseMove(self: GH_CompassWidget, sender: GH_Canvas, e: GH_CanvasMouseEvent) -> GH_ObjectResponse """
        pass

    def RespondToMouseUp(self, sender, e):
        """ RespondToMouseUp(self: GH_CompassWidget, sender: GH_Canvas, e: GH_CanvasMouseEvent) -> GH_ObjectResponse """
        pass

    def ScaleSegment(self, *args): #cannot find CLR method
        """ ScaleSegment(self: GH_CompassWidget, A: PointF, B: PointF, d0: float, d1: float) -> (bool, PointF, PointF) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: GH_CompassWidget) -> str

"""

    Icon_24x24 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Icon_24x24(self: GH_CompassWidget) -> Bitmap

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: GH_CompassWidget) -> str

"""

    Padding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Padding(self: GH_CompassWidget) -> int

"""

    Radius = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Radius(self: GH_CompassWidget) -> int

"""

    Ratio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Ratio(self: GH_CompassWidget) -> SizeF

Set: Ratio(self: GH_CompassWidget) = value
"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Size(self: GH_CompassWidget) -> Size

"""

    Visible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Visible(self: GH_CompassWidget) -> bool

Set: Visible(self: GH_CompassWidget) = value
"""


    DrawObjects = True
    DrawSelectionOnly = False
    m_owner = None
    SharedVisible = True
    WidgetDrawModeChanged = None
    WidgetDrawModeChangedEventHandler = None
    WidgetVisibleChanged = None
    WidgetVisibleChangedEventHandler = None


class GH_MarkovWidget(GH_Widget, IGH_Widget, IGH_ResponsiveObject, IGH_TooltipAwareObject):
    """ GH_MarkovWidget() """
    def AppendToMenu(self, menu):
        """ AppendToMenu(self: GH_MarkovWidget, menu: ToolStripDropDownMenu) """
        pass

    def Contains(self, pt_control, pt_canvas):
        """ Contains(self: GH_MarkovWidget, pt_control: Point, pt_canvas: PointF) -> bool """
        pass

    def Menu_AppendHideItem(self, *args): #cannot find CLR method
        """ Menu_AppendHideItem(self: GH_Widget, menu: ToolStripDropDownMenu) """
        pass

    def Render(self, Canvas):
        """ Render(self: GH_MarkovWidget, Canvas: GH_Canvas) """
        pass

    def RespondToMouseDown(self, sender, e):
        """ RespondToMouseDown(self: GH_MarkovWidget, sender: GH_Canvas, e: GH_CanvasMouseEvent) -> GH_ObjectResponse """
        pass

    def RespondToMouseMove(self, sender, e):
        """ RespondToMouseMove(self: GH_MarkovWidget, sender: GH_Canvas, e: GH_CanvasMouseEvent) -> GH_ObjectResponse """
        pass

    def RespondToMouseUp(self, sender, e):
        """ RespondToMouseUp(self: GH_MarkovWidget, sender: GH_Canvas, e: GH_CanvasMouseEvent) -> GH_ObjectResponse """
        pass

    def SetupTooltip(self, canvasPoint, e):
        """ SetupTooltip(self: GH_MarkovWidget, canvasPoint: PointF, e: GH_TooltipDisplayEventArgs) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: GH_MarkovWidget) -> str

"""

    Icon_24x24 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Icon_24x24(self: GH_MarkovWidget) -> Bitmap

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: GH_MarkovWidget) -> str

"""

    Visible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Visible(self: GH_MarkovWidget) -> bool

Set: Visible(self: GH_MarkovWidget) = value
"""


    DockCorner = None
    DockCornerChanged = None
    DockCornerChangedEventHandler = None
    IconLimit = 5
    IconLimitChanged = None
    IconLimitChangedEventHandler = None
    m_owner = None
    SharedVisible = True
    WidgetVisibleChanged = None
    WidgetVisibleChangedEventHandler = None


class GH_MarkovWidgetDock(Enum, IComparable, IFormattable, IConvertible):
    """ enum GH_MarkovWidgetDock, values: BottomLeft (1), BottomRight (3), TopLeft (0), TopRight (2) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    BottomLeft = None
    BottomRight = None
    TopLeft = None
    TopRight = None
    value__ = None


class GH_MessageWidget(GH_Widget, IGH_Widget, IGH_ResponsiveObject, IGH_TooltipAwareObject):
    """ GH_MessageWidget() """
    def Contains(self, pt_control, pt_canvas):
        """ Contains(self: GH_MessageWidget, pt_control: Point, pt_canvas: PointF) -> bool """
        pass

    def Menu_AppendHideItem(self, *args): #cannot find CLR method
        """ Menu_AppendHideItem(self: GH_Widget, menu: ToolStripDropDownMenu) """
        pass

    def Render(self, canvas):
        """ Render(self: GH_MessageWidget, canvas: GH_Canvas) """
        pass

    def RespondToMouseDown(self, sender, e):
        """ RespondToMouseDown(self: GH_MessageWidget, sender: GH_Canvas, e: GH_CanvasMouseEvent) -> GH_ObjectResponse """
        pass

    def SetupTooltip(self, canvasPoint, e):
        """ SetupTooltip(self: GH_MessageWidget, canvasPoint: PointF, e: GH_TooltipDisplayEventArgs) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: GH_MessageWidget) -> str

"""

    Icon_24x24 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Icon_24x24(self: GH_MessageWidget) -> Bitmap

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: GH_MessageWidget) -> str

"""

    Visible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Visible(self: GH_MessageWidget) -> bool

Set: Visible(self: GH_MessageWidget) = value
"""


    m_owner = None
    SharedVisible = True
    WidgetLevelChanged = None
    WidgetLevelChangedEventHandler = None
    WidgetVisibleChanged = None
    WidgetVisibleChangedEventHandler = None


class GH_ProfilerWidget(GH_Widget, IGH_Widget, IGH_ResponsiveObject, IGH_TooltipAwareObject):
    """ GH_ProfilerWidget() """
    def AppendToMenu(self, menu):
        """ AppendToMenu(self: GH_ProfilerWidget, menu: ToolStripDropDownMenu) """
        pass

    def Contains(self, pt_control, pt_canvas):
        """ Contains(self: GH_ProfilerWidget, pt_control: Point, pt_canvas: PointF) -> bool """
        pass

    def Menu_AppendHideItem(self, *args): #cannot find CLR method
        """ Menu_AppendHideItem(self: GH_Widget, menu: ToolStripDropDownMenu) """
        pass

    def Render(self, Canvas):
        """ Render(self: GH_ProfilerWidget, Canvas: GH_Canvas) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: GH_ProfilerWidget) -> str

"""

    Icon_24x24 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Icon_24x24(self: GH_ProfilerWidget) -> Bitmap

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: GH_ProfilerWidget) -> str

"""

    Visible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Visible(self: GH_ProfilerWidget) -> bool

Set: Visible(self: GH_ProfilerWidget) = value
"""


    m_owner = None
    ProfilerThresholdChanged = None
    ProfilerThresholdChangedEventHandler = None
    SharedVisible = False
    Threshold = 2
    WidgetVisibleChanged = None
    WidgetVisibleChangedEventHandler = None


class IGH_Widget(IGH_ResponsiveObject, IGH_TooltipAwareObject):
    # no doc
    def AppendToMenu(self, menu):
        """ AppendToMenu(self: IGH_Widget, menu: ToolStripDropDownMenu) """
        pass

    def Contains(self, pt_control, pt_canvas):
        """ Contains(self: IGH_Widget, pt_control: Point, pt_canvas: PointF) -> bool """
        pass

    def Render(self, Canvas):
        """ Render(self: IGH_Widget, Canvas: GH_Canvas) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: IGH_Widget) -> str

"""

    Icon_24x24 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Icon_24x24(self: IGH_Widget) -> Bitmap

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: IGH_Widget) -> str

"""

    Owner = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Owner(self: IGH_Widget) -> GH_Canvas

Set: Owner(self: IGH_Widget) = value
"""

    TooltipText = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: TooltipText(self: IGH_Widget) -> str

"""

    Visible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Visible(self: IGH_Widget) -> bool

Set: Visible(self: IGH_Widget) = value
"""



