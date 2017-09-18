# encoding: utf-8
# module Grasshopper.Kernel.Graphs calls itself Graphs
# from Grasshopper, Version=1.0.0.20, Culture=neutral, PublicKeyToken=dda4f5ec2cd80803
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# functions

def GH_GraphProxyObject(n_owner): # real signature unknown; restored from __doc__
    """ GH_GraphProxyObject(n_owner: IGH_Graph) """
    pass

# classes

class GH_AbstractGraph(object, IGH_Graph, GH_ISerializable):
    # no doc
    def AddGrip(self, *args): #cannot find CLR method
        """ AddGrip(self: GH_AbstractGraph, Grip: GH_GraphGrip) """
        pass

    def ClearCaches(self):
        """ ClearCaches(self: GH_AbstractGraph) """
        pass

    def ClearGrips(self, *args): #cannot find CLR method
        """ ClearGrips(self: GH_AbstractGraph) """
        pass

    def CreateDerivedDuplicate(self, *args): #cannot find CLR method
        """ CreateDerivedDuplicate(self: GH_AbstractGraph) -> GH_AbstractGraph """
        pass

    def CreateGrips(self, *args): #cannot find CLR method
        """ CreateGrips(self: GH_AbstractGraph) """
        pass

    def CurveToPointFArray(self, *args): #cannot find CLR method
        """ CurveToPointFArray(Crv: Curve, dest: RectangleF) -> Array[PointF] """
        pass

    def Draw_PostRenderGraph(self, g, cnt):
        """ Draw_PostRenderGraph(self: GH_AbstractGraph, g: Graphics, cnt: GH_GraphContainer) """
        pass

    def Draw_PostRenderGrid(self, g, cnt):
        """ Draw_PostRenderGrid(self: GH_AbstractGraph, g: Graphics, cnt: GH_GraphContainer) """
        pass

    def Draw_PostRenderGrip(self, g, cnt, index):
        """ Draw_PostRenderGrip(self: GH_AbstractGraph, g: Graphics, cnt: GH_GraphContainer, index: int) """
        pass

    def Draw_PostRenderTags(self, g, cnt):
        """ Draw_PostRenderTags(self: GH_AbstractGraph, g: Graphics, cnt: GH_GraphContainer) """
        pass

    def Draw_PreRenderGraph(self, g, cnt):
        """ Draw_PreRenderGraph(self: GH_AbstractGraph, g: Graphics, cnt: GH_GraphContainer) -> GH_GraphDrawInstruction """
        pass

    def Draw_PreRenderGrid(self, g, cnt):
        """ Draw_PreRenderGrid(self: GH_AbstractGraph, g: Graphics, cnt: GH_GraphContainer) -> GH_GraphDrawInstruction """
        pass

    def Draw_PreRenderGrip(self, g, cnt, index):
        """ Draw_PreRenderGrip(self: GH_AbstractGraph, g: Graphics, cnt: GH_GraphContainer, index: int) -> GH_GraphDrawInstruction """
        pass

    def Draw_PreRenderTags(self, g, cnt):
        """ Draw_PreRenderTags(self: GH_AbstractGraph, g: Graphics, cnt: GH_GraphContainer) -> GH_GraphDrawInstruction """
        pass

    def Duplicate(self):
        """ Duplicate(self: GH_AbstractGraph) -> IGH_Graph """
        pass

    def EmitProxyObject(self):
        """ EmitProxyObject(self: GH_AbstractGraph) -> IGH_GraphProxyObject """
        pass

    def GDI_GraphPath(self, reg):
        """ GDI_GraphPath(self: GH_AbstractGraph, reg: RectangleF) -> Array[PointF] """
        pass

    def GHGraphToPointArray(self, *args): #cannot find CLR method
        """
        GHGraphToPointArray(reg: RectangleF, pix_accuracy: float, eval: GH_Evaluator) -> Array[PointF]
        GHGraphToPointArray(self: GH_AbstractGraph, reg: RectangleF, pix_accuracy: float) -> Array[PointF]
        """
        pass

    def Internal_GripChanged(self, *args): #cannot find CLR method
        """ Internal_GripChanged(self: GH_AbstractGraph, grip: GH_GraphGrip, bIntermediate: bool) """
        pass

    def IntersectionEvaluate(self, *args): #cannot find CLR method
        """ IntersectionEvaluate(C: Curve, offset: float) -> float """
        pass

    def OnGraphChanged(self, bIntermediate):
        """ OnGraphChanged(self: GH_AbstractGraph, bIntermediate: bool) """
        pass

    def PrepareForUse(self):
        """ PrepareForUse(self: GH_AbstractGraph) """
        pass

    def Read(self, reader):
        """ Read(self: GH_AbstractGraph, reader: GH_IReader) -> bool """
        pass

    def UpdateEquation(self, *args): #cannot find CLR method
        """ UpdateEquation(self: GH_AbstractGraph) """
        pass

    def ValueAt(self, t):
        """ ValueAt(self: GH_AbstractGraph, t: float) -> float """
        pass

    def Write(self, writer):
        """ Write(self: GH_AbstractGraph, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, nName: str, nDescription: str) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: GH_AbstractGraph) -> str

"""

    GraphTypeID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GraphTypeID(self: GH_AbstractGraph) -> Guid

"""

    Grips = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Grips(self: GH_AbstractGraph) -> List[GH_GraphGrip]

"""

    Icon_16x16 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Icon_16x16(self: GH_AbstractGraph) -> Image

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: GH_AbstractGraph) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: GH_AbstractGraph) -> str

"""


    GH_Evaluator = None
    GraphChanged = None


class GH_BezierGraph(GH_AbstractGraph, IGH_Graph, GH_ISerializable):
    """ GH_BezierGraph() """
    def AddGrip(self, *args): #cannot find CLR method
        """ AddGrip(self: GH_AbstractGraph, Grip: GH_GraphGrip) """
        pass

    def ClearCaches(self):
        """ ClearCaches(self: GH_BezierGraph) """
        pass

    def ClearGrips(self, *args): #cannot find CLR method
        """ ClearGrips(self: GH_AbstractGraph) """
        pass

    def CreateDerivedDuplicate(self, *args): #cannot find CLR method
        """ CreateDerivedDuplicate(self: GH_BezierGraph) -> GH_AbstractGraph """
        pass

    def CreateGrips(self, *args): #cannot find CLR method
        """ CreateGrips(self: GH_BezierGraph) """
        pass

    def Curve(self, *args): #cannot find CLR method
        """ Curve(self: GH_BezierGraph) -> Curve """
        pass

    def Draw_PreRenderGrip(self, g, cnt, index):
        """ Draw_PreRenderGrip(self: GH_BezierGraph, g: Graphics, cnt: GH_GraphContainer, index: int) -> GH_GraphDrawInstruction """
        pass

    def GDI_GraphPath(self, reg):
        """ GDI_GraphPath(self: GH_BezierGraph, reg: RectangleF) -> Array[PointF] """
        pass

    def GHGraphToPointArray(self, *args): #cannot find CLR method
        """
        GHGraphToPointArray(reg: RectangleF, pix_accuracy: float, eval: GH_Evaluator) -> Array[PointF]
        GHGraphToPointArray(self: GH_AbstractGraph, reg: RectangleF, pix_accuracy: float) -> Array[PointF]
        """
        pass

    def Internal_GripChanged(self, *args): #cannot find CLR method
        """ Internal_GripChanged(self: GH_AbstractGraph, grip: GH_GraphGrip, bIntermediate: bool) """
        pass

    def Read(self, reader):
        """ Read(self: GH_BezierGraph, reader: GH_IReader) -> bool """
        pass

    def UpdateEquation(self, *args): #cannot find CLR method
        """ UpdateEquation(self: GH_BezierGraph) """
        pass

    def ValueAt(self, t):
        """ ValueAt(self: GH_BezierGraph, t: float) -> float """
        pass

    def Write(self, writer):
        """ Write(self: GH_BezierGraph, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    GraphTypeID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GraphTypeID(self: GH_BezierGraph) -> Guid

"""

    Icon_16x16 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Icon_16x16(self: GH_BezierGraph) -> Image

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: GH_BezierGraph) -> bool

"""



class GH_ConicGraph(GH_AbstractGraph, IGH_Graph, GH_ISerializable):
    """ GH_ConicGraph() """
    def AddGrip(self, *args): #cannot find CLR method
        """ AddGrip(self: GH_AbstractGraph, Grip: GH_GraphGrip) """
        pass

    def ClearGrips(self, *args): #cannot find CLR method
        """ ClearGrips(self: GH_AbstractGraph) """
        pass

    def CreateDerivedDuplicate(self, *args): #cannot find CLR method
        """ CreateDerivedDuplicate(self: GH_ConicGraph) -> GH_AbstractGraph """
        pass

    def CreateGrips(self, *args): #cannot find CLR method
        """ CreateGrips(self: GH_ConicGraph) """
        pass

    def Curve(self, *args): #cannot find CLR method
        """ Curve(self: GH_ConicGraph) -> NurbsCurve """
        pass

    def DestroyCurve(self, *args): #cannot find CLR method
        """ DestroyCurve(self: GH_ConicGraph) """
        pass

    def FitConic(self, *args): #cannot find CLR method
        """ FitConic(self: GH_ConicGraph, S: Point3d) -> NurbsCurve """
        pass

    def GDI_GraphPath(self, reg):
        """ GDI_GraphPath(self: GH_ConicGraph, reg: RectangleF) -> Array[PointF] """
        pass

    def GHGraphToPointArray(self, *args): #cannot find CLR method
        """
        GHGraphToPointArray(reg: RectangleF, pix_accuracy: float, eval: GH_Evaluator) -> Array[PointF]
        GHGraphToPointArray(self: GH_AbstractGraph, reg: RectangleF, pix_accuracy: float) -> Array[PointF]
        """
        pass

    def Internal_GripChanged(self, *args): #cannot find CLR method
        """ Internal_GripChanged(self: GH_AbstractGraph, grip: GH_GraphGrip, bIntermediate: bool) """
        pass

    def MakeConic(self, *args): #cannot find CLR method
        """ MakeConic(self: GH_ConicGraph, w: float) -> NurbsCurve """
        pass

    def Read(self, reader):
        """ Read(self: GH_ConicGraph, reader: GH_IReader) -> bool """
        pass

    def UpdateEquation(self, *args): #cannot find CLR method
        """ UpdateEquation(self: GH_ConicGraph) """
        pass

    def ValueAt(self, t):
        """ ValueAt(self: GH_ConicGraph, t: float) -> float """
        pass

    def Write(self, writer):
        """ Write(self: GH_ConicGraph, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    GraphTypeID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GraphTypeID(self: GH_ConicGraph) -> Guid

"""

    Icon_16x16 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Icon_16x16(self: GH_ConicGraph) -> Image

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: GH_ConicGraph) -> bool

"""



class GH_DoubleSineGraph(GH_AbstractGraph, IGH_Graph, GH_ISerializable):
    """ GH_DoubleSineGraph() """
    def AddGrip(self, *args): #cannot find CLR method
        """ AddGrip(self: GH_AbstractGraph, Grip: GH_GraphGrip) """
        pass

    def ClearCaches(self):
        """ ClearCaches(self: GH_DoubleSineGraph) """
        pass

    def ClearGrips(self, *args): #cannot find CLR method
        """ ClearGrips(self: GH_AbstractGraph) """
        pass

    def CreateDerivedDuplicate(self, *args): #cannot find CLR method
        """ CreateDerivedDuplicate(self: GH_DoubleSineGraph) -> GH_AbstractGraph """
        pass

    def CreateGrips(self, *args): #cannot find CLR method
        """ CreateGrips(self: GH_DoubleSineGraph) """
        pass

    def Draw_PreRenderGraph(self, g, cnt):
        """ Draw_PreRenderGraph(self: GH_DoubleSineGraph, g: Graphics, cnt: GH_GraphContainer) -> GH_GraphDrawInstruction """
        pass

    def Draw_PreRenderGrip(self, g, cnt, index):
        """ Draw_PreRenderGrip(self: GH_DoubleSineGraph, g: Graphics, cnt: GH_GraphContainer, index: int) -> GH_GraphDrawInstruction """
        pass

    def GDI_GraphPath(self, reg):
        """ GDI_GraphPath(self: GH_DoubleSineGraph, reg: RectangleF) -> Array[PointF] """
        pass

    def GHGraphToPointArray(self, *args): #cannot find CLR method
        """
        GHGraphToPointArray(reg: RectangleF, pix_accuracy: float, eval: GH_Evaluator) -> Array[PointF]
        GHGraphToPointArray(self: GH_AbstractGraph, reg: RectangleF, pix_accuracy: float) -> Array[PointF]
        """
        pass

    def GraphAccuracy(self, *args): #cannot find CLR method
        """ GraphAccuracy(self: GH_DoubleSineGraph, reg: RectangleF) -> float """
        pass

    def Internal_GripChanged(self, *args): #cannot find CLR method
        """ Internal_GripChanged(self: GH_AbstractGraph, grip: GH_GraphGrip, bIntermediate: bool) """
        pass

    def Read(self, reader):
        """ Read(self: GH_DoubleSineGraph, reader: GH_IReader) -> bool """
        pass

    def RecFromPoints(self, *args): #cannot find CLR method
        """ RecFromPoints(self: GH_DoubleSineGraph, a: PointF, b: PointF) -> Rectangle """
        pass

    def UpdateEquation(self, *args): #cannot find CLR method
        """ UpdateEquation(self: GH_DoubleSineGraph) """
        pass

    def ValueAt(self, t):
        """ ValueAt(self: GH_DoubleSineGraph, t: float) -> float """
        pass

    def Write(self, writer):
        """ Write(self: GH_DoubleSineGraph, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    GraphTypeID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GraphTypeID(self: GH_DoubleSineGraph) -> Guid

"""

    Icon_16x16 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Icon_16x16(self: GH_DoubleSineGraph) -> Image

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: GH_DoubleSineGraph) -> bool

"""


    m_eq0 = None
    m_eq1 = None
    m_path0 = None
    m_path1 = None


class GH_GaussianGraph(GH_AbstractGraph, IGH_Graph, GH_ISerializable):
    """ GH_GaussianGraph() """
    def AddGrip(self, *args): #cannot find CLR method
        """ AddGrip(self: GH_AbstractGraph, Grip: GH_GraphGrip) """
        pass

    def ClearGrips(self, *args): #cannot find CLR method
        """ ClearGrips(self: GH_AbstractGraph) """
        pass

    def CreateDerivedDuplicate(self, *args): #cannot find CLR method
        """ CreateDerivedDuplicate(self: GH_GaussianGraph) -> GH_AbstractGraph """
        pass

    def CreateGrips(self, *args): #cannot find CLR method
        """ CreateGrips(self: GH_GaussianGraph) """
        pass

    def GHGraphToPointArray(self, *args): #cannot find CLR method
        """
        GHGraphToPointArray(reg: RectangleF, pix_accuracy: float, eval: GH_Evaluator) -> Array[PointF]
        GHGraphToPointArray(self: GH_AbstractGraph, reg: RectangleF, pix_accuracy: float) -> Array[PointF]
        """
        pass

    def Internal_GripChanged(self, *args): #cannot find CLR method
        """ Internal_GripChanged(self: GH_GaussianGraph, grip: GH_GraphGrip, bIntermediate: bool) """
        pass

    def Read(self, reader):
        """ Read(self: GH_GaussianGraph, reader: GH_IReader) -> bool """
        pass

    def UpdateEquation(self, *args): #cannot find CLR method
        """ UpdateEquation(self: GH_GaussianGraph) """
        pass

    def ValueAt(self, t):
        """ ValueAt(self: GH_GaussianGraph, t: float) -> float """
        pass

    def Write(self, writer):
        """ Write(self: GH_GaussianGraph, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    GraphTypeID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GraphTypeID(self: GH_GaussianGraph) -> Guid

"""

    Icon_16x16 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Icon_16x16(self: GH_GaussianGraph) -> Image

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: GH_GaussianGraph) -> bool

"""



class GH_GraphContainer(object, GH_ISerializable, IGH_ResponsiveObject):
    """
    GH_GraphContainer(n_graph: IGH_Graph)
    GH_GraphContainer(n_graph: IGH_Graph, n_x0: float, n_x1: float, n_y0: float, n_y1: float)
    """
    def ClearCaches(self):
        """ ClearCaches(self: GH_GraphContainer) """
        pass

    def Duplicate(self):
        """ Duplicate(self: GH_GraphContainer) -> GH_GraphContainer """
        pass

    def FromX(self, t):
        """ FromX(self: GH_GraphContainer, t: float) -> float """
        pass

    def FromY(self, t):
        """ FromY(self: GH_GraphContainer, t: float) -> float """
        pass

    def Internal_Render_Graph(self, *args): #cannot find CLR method
        """ Internal_Render_Graph(self: GH_GraphContainer, G: Graphics) """
        pass

    def Internal_Render_Grip(self, *args): #cannot find CLR method
        """ Internal_Render_Grip(self: GH_GraphContainer, g: Graphics, x: int, y: int) """
        pass

    def Internal_Render_Grips(self, *args): #cannot find CLR method
        """ Internal_Render_Grips(self: GH_GraphContainer, G: Graphics) """
        pass

    def Internal_Render_HorizontalConstraint(self, *args): #cannot find CLR method
        """ Internal_Render_HorizontalConstraint(self: GH_GraphContainer, g: Graphics, y: int) """
        pass

    def Internal_Render_InvalidIcon(self, *args): #cannot find CLR method
        """ Internal_Render_InvalidIcon(self: GH_GraphContainer, g: Graphics) """
        pass

    def Internal_Render_LockedIcon(self, *args): #cannot find CLR method
        """ Internal_Render_LockedIcon(self: GH_GraphContainer, g: Graphics) """
        pass

    def Internal_Render_TagGDIObjects(self, *args): #cannot find CLR method
        """ Internal_Render_TagGDIObjects(self: GH_GraphContainer, zoom: Single, bg_brush: SolidBrush, fg_brush: SolidBrush, fg_pen: Pen) -> (SolidBrush, SolidBrush, Pen) """
        pass

    def Internal_Render_TagX(self, *args): #cannot find CLR method
        """ Internal_Render_TagX(self: GH_GraphContainer, g: Graphics, graphrec: RectangleF, r_a: float, r_b: float) """
        pass

    def Internal_Render_TagY(self, *args): #cannot find CLR method
        """ Internal_Render_TagY(self: GH_GraphContainer, g: Graphics, graphrec: RectangleF, r_a: float, r_b: float) """
        pass

    def Internal_Render_TextTag(self, *args): #cannot find CLR method
        """ Internal_Render_TextTag(self: GH_GraphContainer, g: Graphics, graphrec: RectangleF, lowerright: bool, tag: str) """
        pass

    def Internal_Render_VerticalConstraint(self, *args): #cannot find CLR method
        """ Internal_Render_VerticalConstraint(self: GH_GraphContainer, g: Graphics, x: int) """
        pass

    def NearestGrip(self, *args): #cannot find CLR method
        """ NearestGrip(self: GH_GraphContainer, pt: PointF, max_search: float) -> int """
        pass

    def OnGraphChanged(self, bIntermediate):
        """ OnGraphChanged(self: GH_GraphContainer, bIntermediate: bool) """
        pass

    def PrepareForUse(self):
        """ PrepareForUse(self: GH_GraphContainer) """
        pass

    def Read(self, reader):
        """ Read(self: GH_GraphContainer, reader: GH_IReader) -> bool """
        pass

    def RemapPointsToGraphRegion(self, pts):
        """ RemapPointsToGraphRegion(self: GH_GraphContainer, pts: Array[PointF]) """
        pass

    def Render(self, G, bIncludeDomainTags, samples):
        """ Render(self: GH_GraphContainer, G: Graphics, bIncludeDomainTags: bool, samples: List[float]) """
        pass

    @staticmethod
    def Render_GraphBackground(G, region, bActive):
        """ Render_GraphBackground(G: Graphics, region: RectangleF, bActive: bool) """
        pass

    @staticmethod
    def Render_GraphGrid(G, region):
        """ Render_GraphGrid(G: Graphics, region: RectangleF) """
        pass

    @staticmethod
    def Render_GraphPen():
        """ Render_GraphPen() -> Pen """
        pass

    @staticmethod
    def Render_GuidePen():
        """ Render_GuidePen() -> Pen """
        pass

    @staticmethod
    def Render_HorizontalConstraint(g, rec, t):
        """ Render_HorizontalConstraint(g: Graphics, rec: RectangleF, t: float) """
        pass

    @staticmethod
    def Render_VerticalConstraint(g, rec, t):
        """ Render_VerticalConstraint(g: Graphics, rec: RectangleF, t: float) """
        pass

    def RespondToKeyDown(self, sender, e):
        """ RespondToKeyDown(self: GH_GraphContainer, sender: GH_Canvas, e: KeyEventArgs) -> GH_ObjectResponse """
        pass

    def RespondToKeyUp(self, sender, e):
        """ RespondToKeyUp(self: GH_GraphContainer, sender: GH_Canvas, e: KeyEventArgs) -> GH_ObjectResponse """
        pass

    def RespondToMouseDoubleClick(self, sender, e):
        """ RespondToMouseDoubleClick(self: GH_GraphContainer, sender: GH_Canvas, e: GH_CanvasMouseEvent) -> GH_ObjectResponse """
        pass

    def RespondToMouseDown(self, sender, e):
        """ RespondToMouseDown(self: GH_GraphContainer, sender: GH_Canvas, e: GH_CanvasMouseEvent) -> GH_ObjectResponse """
        pass

    def RespondToMouseMove(self, sender, e):
        """ RespondToMouseMove(self: GH_GraphContainer, sender: GH_Canvas, e: GH_CanvasMouseEvent) -> GH_ObjectResponse """
        pass

    def RespondToMouseUp(self, sender, e):
        """ RespondToMouseUp(self: GH_GraphContainer, sender: GH_Canvas, e: GH_CanvasMouseEvent) -> GH_ObjectResponse """
        pass

    def SolveGraphPath(self, *args): #cannot find CLR method
        """ SolveGraphPath(self: GH_GraphContainer) -> GraphicsPath """
        pass

    def ToRegionBox(self, pt):
        """ ToRegionBox(self: GH_GraphContainer, pt: PointF) -> PointF """
        pass

    def ToRegionBox_x(self, x):
        """ ToRegionBox_x(self: GH_GraphContainer, x: float) -> Single """
        pass

    def ToRegionBox_y(self, y):
        """ ToRegionBox_y(self: GH_GraphContainer, y: float) -> Single """
        pass

    def ToUnitBox(self, pt):
        """ ToUnitBox(self: GH_GraphContainer, pt: PointF) -> PointF """
        pass

    def ToX(self, t_unit):
        """ ToX(self: GH_GraphContainer, t_unit: float) -> float """
        pass

    def ToY(self, t_unit):
        """ ToY(self: GH_GraphContainer, t_unit: float) -> float """
        pass

    def TryValueAt(self, t):
        """ TryValueAt(self: GH_GraphContainer, t: float) -> float """
        pass

    def ValueAt(self, t):
        """ ValueAt(self: GH_GraphContainer, t: float) -> float """
        pass

    def Write(self, writer):
        """ Write(self: GH_GraphContainer, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, n_graph, n_x0=None, n_x1=None, n_y0=None, n_y1=None):
        """
        __new__(cls: type, n_graph: IGH_Graph)
        __new__(cls: type, n_graph: IGH_Graph, n_x0: float, n_x1: float, n_y0: float, n_y1: float)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Graph = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Graph(self: GH_GraphContainer) -> IGH_Graph

Set: Graph(self: GH_GraphContainer) = value
"""

    LockGrips = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LockGrips(self: GH_GraphContainer) -> bool

Set: LockGrips(self: GH_GraphContainer) = value
"""

    Region = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Region(self: GH_GraphContainer) -> RectangleF

Set: Region(self: GH_GraphContainer) = value
"""

    X0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: X0(self: GH_GraphContainer) -> float

Set: X0(self: GH_GraphContainer) = value
"""

    X1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: X1(self: GH_GraphContainer) -> float

Set: X1(self: GH_GraphContainer) = value
"""

    Y0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Y0(self: GH_GraphContainer) -> float

Set: Y0(self: GH_GraphContainer) = value
"""

    Y1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Y1(self: GH_GraphContainer) -> float

Set: Y1(self: GH_GraphContainer) = value
"""


    GraphChanged = None
    GraphChangedEventHandler = None
    m_graphpath = None


class GH_GraphDrawInstruction(Enum, IComparable, IFormattable, IConvertible):
    """ enum GH_GraphDrawInstruction, values: none (0), skip (1) """
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

    none = None
    skip = None
    value__ = None


class GH_GraphGrip(object):
    """
    GH_GraphGrip()
    GH_GraphGrip(nX: float, nY: float)
    GH_GraphGrip(nX: float, nY: float, nConstraint: GH_GripConstraint)
    GH_GraphGrip(nOther: GH_GraphGrip)
    """
    def LimitToUnitDomain(self, bLimitX, bLimitY):
        """ LimitToUnitDomain(self: GH_GraphGrip, bLimitX: bool, bLimitY: bool) """
        pass

    def OnGripChanged(self, bIntermediate):
        """ OnGripChanged(self: GH_GraphGrip, bIntermediate: bool) """
        pass

    def SetIndex(self, nIndex):
        """ SetIndex(self: GH_GraphGrip, nIndex: int) """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, nX: float, nY: float)
        __new__(cls: type, nX: float, nY: float, nConstraint: GH_GripConstraint)
        __new__(cls: type, nOther: GH_GraphGrip)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Constraint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Constraint(self: GH_GraphGrip) -> GH_GripConstraint

Set: Constraint(self: GH_GraphGrip) = value
"""

    Index = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Index(self: GH_GraphGrip) -> int

"""

    Point = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Point(self: GH_GraphGrip) -> PointF

"""

    X = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: X(self: GH_GraphGrip) -> float

Set: X(self: GH_GraphGrip) = value
"""

    Y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Y(self: GH_GraphGrip) -> float

Set: Y(self: GH_GraphGrip) = value
"""


    GripChanged = None
    GripChangedEventHandler = None
    m_c = None
    m_i = None
    m_x = None
    m_y = None


class GH_GripConstraint(Enum, IComparable, IFormattable, IConvertible):
    """ enum GH_GripConstraint, values: horizontal (1), none (0), vertical (2) """
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

    horizontal = None
    none = None
    value__ = None
    vertical = None


class GH_LinearGraph(GH_AbstractGraph, IGH_Graph, GH_ISerializable):
    """ GH_LinearGraph() """
    def AddGrip(self, *args): #cannot find CLR method
        """ AddGrip(self: GH_AbstractGraph, Grip: GH_GraphGrip) """
        pass

    def ClearGrips(self, *args): #cannot find CLR method
        """ ClearGrips(self: GH_AbstractGraph) """
        pass

    def CreateDerivedDuplicate(self, *args): #cannot find CLR method
        """ CreateDerivedDuplicate(self: GH_LinearGraph) -> GH_AbstractGraph """
        pass

    def CreateGrips(self, *args): #cannot find CLR method
        """ CreateGrips(self: GH_LinearGraph) """
        pass

    def Draw_PreRenderGraph(self, g, cnt):
        """ Draw_PreRenderGraph(self: GH_LinearGraph, g: Graphics, cnt: GH_GraphContainer) -> GH_GraphDrawInstruction """
        pass

    def EmitProxyObject(self):
        """ EmitProxyObject(self: GH_LinearGraph) -> IGH_GraphProxyObject """
        pass

    def GDI_GraphPath(self, reg):
        """ GDI_GraphPath(self: GH_LinearGraph, reg: RectangleF) -> Array[PointF] """
        pass

    def GHGraphToPointArray(self, *args): #cannot find CLR method
        """
        GHGraphToPointArray(reg: RectangleF, pix_accuracy: float, eval: GH_Evaluator) -> Array[PointF]
        GHGraphToPointArray(self: GH_AbstractGraph, reg: RectangleF, pix_accuracy: float) -> Array[PointF]
        """
        pass

    def Internal_GripChanged(self, *args): #cannot find CLR method
        """ Internal_GripChanged(self: GH_AbstractGraph, grip: GH_GraphGrip, bIntermediate: bool) """
        pass

    def Read(self, reader):
        """ Read(self: GH_LinearGraph, reader: GH_IReader) -> bool """
        pass

    def SetFromParameters(self, nA, nB):
        """ SetFromParameters(self: GH_LinearGraph, nA: float, nB: float) """
        pass

    def UpdateEquation(self, *args): #cannot find CLR method
        """ UpdateEquation(self: GH_LinearGraph) """
        pass

    def ValueAt(self, t):
        """ ValueAt(self: GH_LinearGraph, t: float) -> float """
        pass

    def Write(self, writer):
        """ Write(self: GH_LinearGraph, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    GraphTypeID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GraphTypeID(self: GH_LinearGraph) -> Guid

"""

    Icon_16x16 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Icon_16x16(self: GH_LinearGraph) -> Image

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: GH_LinearGraph) -> bool

"""


    GH_LinearGraphProxy = None


class GH_ParabolaGraph(GH_AbstractGraph, IGH_Graph, GH_ISerializable):
    """ GH_ParabolaGraph() """
    def AddGrip(self, *args): #cannot find CLR method
        """ AddGrip(self: GH_AbstractGraph, Grip: GH_GraphGrip) """
        pass

    def ClearGrips(self, *args): #cannot find CLR method
        """ ClearGrips(self: GH_AbstractGraph) """
        pass

    def CreateDerivedDuplicate(self, *args): #cannot find CLR method
        """ CreateDerivedDuplicate(self: GH_ParabolaGraph) -> GH_AbstractGraph """
        pass

    def CreateGrips(self, *args): #cannot find CLR method
        """ CreateGrips(self: GH_ParabolaGraph) """
        pass

    def Draw_PreRenderGraph(self, g, cnt):
        """ Draw_PreRenderGraph(self: GH_ParabolaGraph, g: Graphics, cnt: GH_GraphContainer) -> GH_GraphDrawInstruction """
        pass

    def GHGraphToPointArray(self, *args): #cannot find CLR method
        """
        GHGraphToPointArray(reg: RectangleF, pix_accuracy: float, eval: GH_Evaluator) -> Array[PointF]
        GHGraphToPointArray(self: GH_AbstractGraph, reg: RectangleF, pix_accuracy: float) -> Array[PointF]
        """
        pass

    def Internal_GripChanged(self, *args): #cannot find CLR method
        """ Internal_GripChanged(self: GH_AbstractGraph, grip: GH_GraphGrip, bIntermediate: bool) """
        pass

    def Read(self, reader):
        """ Read(self: GH_ParabolaGraph, reader: GH_IReader) -> bool """
        pass

    def UpdateEquation(self, *args): #cannot find CLR method
        """ UpdateEquation(self: GH_ParabolaGraph) """
        pass

    def ValueAt(self, t):
        """ ValueAt(self: GH_ParabolaGraph, t: float) -> float """
        pass

    def Write(self, writer):
        """ Write(self: GH_ParabolaGraph, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    GraphTypeID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GraphTypeID(self: GH_ParabolaGraph) -> Guid

"""

    Icon_16x16 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Icon_16x16(self: GH_ParabolaGraph) -> Image

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: GH_ParabolaGraph) -> bool

"""



class GH_PerlinGraph(GH_AbstractGraph, IGH_Graph, GH_ISerializable):
    """ GH_PerlinGraph() """
    def AddGrip(self, *args): #cannot find CLR method
        """ AddGrip(self: GH_AbstractGraph, Grip: GH_GraphGrip) """
        pass

    def ClearGrips(self, *args): #cannot find CLR method
        """ ClearGrips(self: GH_AbstractGraph) """
        pass

    def CreateDerivedDuplicate(self, *args): #cannot find CLR method
        """ CreateDerivedDuplicate(self: GH_PerlinGraph) -> GH_AbstractGraph """
        pass

    def CreateGrips(self, *args): #cannot find CLR method
        """ CreateGrips(self: GH_PerlinGraph) """
        pass

    def GHGraphToPointArray(self, *args): #cannot find CLR method
        """
        GHGraphToPointArray(reg: RectangleF, pix_accuracy: float, eval: GH_Evaluator) -> Array[PointF]
        GHGraphToPointArray(self: GH_AbstractGraph, reg: RectangleF, pix_accuracy: float) -> Array[PointF]
        """
        pass

    def Internal_GripChanged(self, *args): #cannot find CLR method
        """ Internal_GripChanged(self: GH_PerlinGraph, grip: GH_GraphGrip, bIntermediate: bool) """
        pass

    def Interpolate(self, *args): #cannot find CLR method
        """ Interpolate(self: GH_PerlinGraph, v0: float, v1: float, v2: float, v3: float, a: float) -> float """
        pass

    def Noise(self, *args): #cannot find CLR method
        """ Noise(self: GH_PerlinGraph, i: int) -> float """
        pass

    def Read(self, reader):
        """ Read(self: GH_PerlinGraph, reader: GH_IReader) -> bool """
        pass

    def Smooth(self, *args): #cannot find CLR method
        """ Smooth(self: GH_PerlinGraph, x: float) -> float """
        pass

    def UpdateEquation(self, *args): #cannot find CLR method
        """ UpdateEquation(self: GH_PerlinGraph) """
        pass

    def ValueAt(self, t):
        """ ValueAt(self: GH_PerlinGraph, t: float) -> float """
        pass

    def Write(self, writer):
        """ Write(self: GH_PerlinGraph, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    GraphTypeID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GraphTypeID(self: GH_PerlinGraph) -> Guid

"""

    Icon_16x16 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Icon_16x16(self: GH_PerlinGraph) -> Image

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: GH_PerlinGraph) -> bool

"""


    amplitude = None
    decay = None
    frequency = None
    x_offset = None
    y_offset = None


class GH_PowerGraph(GH_AbstractGraph, IGH_Graph, GH_ISerializable):
    """ GH_PowerGraph() """
    def AddGrip(self, *args): #cannot find CLR method
        """ AddGrip(self: GH_AbstractGraph, Grip: GH_GraphGrip) """
        pass

    def ClearGrips(self, *args): #cannot find CLR method
        """ ClearGrips(self: GH_AbstractGraph) """
        pass

    def CreateDerivedDuplicate(self, *args): #cannot find CLR method
        """ CreateDerivedDuplicate(self: GH_PowerGraph) -> GH_AbstractGraph """
        pass

    def CreateGrips(self, *args): #cannot find CLR method
        """ CreateGrips(self: GH_PowerGraph) """
        pass

    def GHGraphToPointArray(self, *args): #cannot find CLR method
        """
        GHGraphToPointArray(reg: RectangleF, pix_accuracy: float, eval: GH_Evaluator) -> Array[PointF]
        GHGraphToPointArray(self: GH_AbstractGraph, reg: RectangleF, pix_accuracy: float) -> Array[PointF]
        """
        pass

    def Internal_GripChanged(self, *args): #cannot find CLR method
        """ Internal_GripChanged(self: GH_AbstractGraph, grip: GH_GraphGrip, bIntermediate: bool) """
        pass

    def Read(self, reader):
        """ Read(self: GH_PowerGraph, reader: GH_IReader) -> bool """
        pass

    def UpdateEquation(self, *args): #cannot find CLR method
        """ UpdateEquation(self: GH_PowerGraph) """
        pass

    def ValueAt(self, t):
        """ ValueAt(self: GH_PowerGraph, t: float) -> float """
        pass

    def Write(self, writer):
        """ Write(self: GH_PowerGraph, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    GraphTypeID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GraphTypeID(self: GH_PowerGraph) -> Guid

"""

    Icon_16x16 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Icon_16x16(self: GH_PowerGraph) -> Image

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: GH_PowerGraph) -> bool

"""



class GH_SincGraph(GH_AbstractGraph, IGH_Graph, GH_ISerializable):
    """ GH_SincGraph() """
    def AddGrip(self, *args): #cannot find CLR method
        """ AddGrip(self: GH_AbstractGraph, Grip: GH_GraphGrip) """
        pass

    def ClearGrips(self, *args): #cannot find CLR method
        """ ClearGrips(self: GH_AbstractGraph) """
        pass

    def CreateDerivedDuplicate(self, *args): #cannot find CLR method
        """ CreateDerivedDuplicate(self: GH_SincGraph) -> GH_AbstractGraph """
        pass

    def CreateGrips(self, *args): #cannot find CLR method
        """ CreateGrips(self: GH_SincGraph) """
        pass

    def GDI_GraphPath(self, reg):
        """ GDI_GraphPath(self: GH_SincGraph, reg: RectangleF) -> Array[PointF] """
        pass

    def GHGraphToPointArray(self, *args): #cannot find CLR method
        """
        GHGraphToPointArray(reg: RectangleF, pix_accuracy: float, eval: GH_Evaluator) -> Array[PointF]
        GHGraphToPointArray(self: GH_AbstractGraph, reg: RectangleF, pix_accuracy: float) -> Array[PointF]
        """
        pass

    def Internal_GripChanged(self, *args): #cannot find CLR method
        """ Internal_GripChanged(self: GH_AbstractGraph, grip: GH_GraphGrip, bIntermediate: bool) """
        pass

    def Read(self, reader):
        """ Read(self: GH_SincGraph, reader: GH_IReader) -> bool """
        pass

    def UpdateEquation(self, *args): #cannot find CLR method
        """ UpdateEquation(self: GH_SincGraph) """
        pass

    def ValueAt(self, t):
        """ ValueAt(self: GH_SincGraph, t: float) -> float """
        pass

    def Write(self, writer):
        """ Write(self: GH_SincGraph, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    GraphTypeID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GraphTypeID(self: GH_SincGraph) -> Guid

"""

    Icon_16x16 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Icon_16x16(self: GH_SincGraph) -> Image

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: GH_SincGraph) -> bool

"""


    amplitude = None
    frequency = None
    X0 = None
    X1 = None
    x_shift = None
    Y0 = None
    Y1 = None
    y_shift = None


class GH_SineEquation(object, GH_ISerializable):
    """ GH_SineEquation() """
    def Read(self, reader):
        """ Read(self: GH_SineEquation, reader: GH_IReader) -> bool """
        pass

    def SetEquationFromGrips(self):
        """ SetEquationFromGrips(self: GH_SineEquation) """
        pass

    def ValueAt(self, t):
        """ ValueAt(self: GH_SineEquation, t: float) -> float """
        pass

    def Write(self, writer):
        """ Write(self: GH_SineEquation, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    amplitude = None
    frequency = None
    offset = None
    shift = None
    X0 = None
    X1 = None
    Y0 = None
    Y1 = None


class GH_SineGraph(GH_AbstractGraph, IGH_Graph, GH_ISerializable):
    """ GH_SineGraph() """
    def AddGrip(self, *args): #cannot find CLR method
        """ AddGrip(self: GH_AbstractGraph, Grip: GH_GraphGrip) """
        pass

    def ClearGrips(self, *args): #cannot find CLR method
        """ ClearGrips(self: GH_AbstractGraph) """
        pass

    def CreateDerivedDuplicate(self, *args): #cannot find CLR method
        """ CreateDerivedDuplicate(self: GH_SineGraph) -> GH_AbstractGraph """
        pass

    def CreateGrips(self, *args): #cannot find CLR method
        """ CreateGrips(self: GH_SineGraph) """
        pass

    def GDI_GraphPath(self, reg):
        """ GDI_GraphPath(self: GH_SineGraph, reg: RectangleF) -> Array[PointF] """
        pass

    def GHGraphToPointArray(self, *args): #cannot find CLR method
        """
        GHGraphToPointArray(reg: RectangleF, pix_accuracy: float, eval: GH_Evaluator) -> Array[PointF]
        GHGraphToPointArray(self: GH_AbstractGraph, reg: RectangleF, pix_accuracy: float) -> Array[PointF]
        """
        pass

    def Internal_GripChanged(self, *args): #cannot find CLR method
        """ Internal_GripChanged(self: GH_AbstractGraph, grip: GH_GraphGrip, bIntermediate: bool) """
        pass

    def Read(self, reader):
        """ Read(self: GH_SineGraph, reader: GH_IReader) -> bool """
        pass

    def UpdateEquation(self, *args): #cannot find CLR method
        """ UpdateEquation(self: GH_SineGraph) """
        pass

    def ValueAt(self, t):
        """ ValueAt(self: GH_SineGraph, t: float) -> float """
        pass

    def Write(self, writer):
        """ Write(self: GH_SineGraph, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    GraphTypeID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GraphTypeID(self: GH_SineGraph) -> Guid

"""

    Icon_16x16 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Icon_16x16(self: GH_SineGraph) -> Image

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: GH_SineGraph) -> bool

"""


    m_eq = None


class GH_SquareRootGraph(GH_AbstractGraph, IGH_Graph, GH_ISerializable):
    """ GH_SquareRootGraph() """
    def AddGrip(self, *args): #cannot find CLR method
        """ AddGrip(self: GH_AbstractGraph, Grip: GH_GraphGrip) """
        pass

    def ClearGrips(self, *args): #cannot find CLR method
        """ ClearGrips(self: GH_AbstractGraph) """
        pass

    def CreateDerivedDuplicate(self, *args): #cannot find CLR method
        """ CreateDerivedDuplicate(self: GH_SquareRootGraph) -> GH_AbstractGraph """
        pass

    def CreateGrips(self, *args): #cannot find CLR method
        """ CreateGrips(self: GH_SquareRootGraph) """
        pass

    def Draw_PreRenderGraph(self, g, cnt):
        """ Draw_PreRenderGraph(self: GH_SquareRootGraph, g: Graphics, cnt: GH_GraphContainer) -> GH_GraphDrawInstruction """
        pass

    def GHGraphToPointArray(self, *args): #cannot find CLR method
        """
        GHGraphToPointArray(reg: RectangleF, pix_accuracy: float, eval: GH_Evaluator) -> Array[PointF]
        GHGraphToPointArray(self: GH_AbstractGraph, reg: RectangleF, pix_accuracy: float) -> Array[PointF]
        """
        pass

    def Internal_GripChanged(self, *args): #cannot find CLR method
        """ Internal_GripChanged(self: GH_AbstractGraph, grip: GH_GraphGrip, bIntermediate: bool) """
        pass

    def Read(self, reader):
        """ Read(self: GH_SquareRootGraph, reader: GH_IReader) -> bool """
        pass

    def UpdateEquation(self, *args): #cannot find CLR method
        """ UpdateEquation(self: GH_SquareRootGraph) """
        pass

    def ValueAt(self, t):
        """ ValueAt(self: GH_SquareRootGraph, t: float) -> float """
        pass

    def Write(self, writer):
        """ Write(self: GH_SquareRootGraph, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    GraphTypeID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GraphTypeID(self: GH_SquareRootGraph) -> Guid

"""

    Icon_16x16 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Icon_16x16(self: GH_SquareRootGraph) -> Image

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: GH_SquareRootGraph) -> bool

"""



class IGH_Graph(GH_ISerializable):
    # no doc
    def ClearCaches(self):
        """ ClearCaches(self: IGH_Graph) """
        pass

    def Draw_PostRenderGraph(self, g, cnt):
        """ Draw_PostRenderGraph(self: IGH_Graph, g: Graphics, cnt: GH_GraphContainer) """
        pass

    def Draw_PostRenderGrid(self, g, cnt):
        """ Draw_PostRenderGrid(self: IGH_Graph, g: Graphics, cnt: GH_GraphContainer) """
        pass

    def Draw_PostRenderGrip(self, g, cnt, index):
        """ Draw_PostRenderGrip(self: IGH_Graph, g: Graphics, cnt: GH_GraphContainer, index: int) """
        pass

    def Draw_PostRenderTags(self, g, cnt):
        """ Draw_PostRenderTags(self: IGH_Graph, g: Graphics, cnt: GH_GraphContainer) """
        pass

    def Draw_PreRenderGraph(self, g, cnt):
        """ Draw_PreRenderGraph(self: IGH_Graph, g: Graphics, cnt: GH_GraphContainer) -> GH_GraphDrawInstruction """
        pass

    def Draw_PreRenderGrid(self, g, cnt):
        """ Draw_PreRenderGrid(self: IGH_Graph, g: Graphics, cnt: GH_GraphContainer) -> GH_GraphDrawInstruction """
        pass

    def Draw_PreRenderGrip(self, g, cnt, index):
        """ Draw_PreRenderGrip(self: IGH_Graph, g: Graphics, cnt: GH_GraphContainer, index: int) -> GH_GraphDrawInstruction """
        pass

    def Draw_PreRenderTags(self, g, cnt):
        """ Draw_PreRenderTags(self: IGH_Graph, g: Graphics, cnt: GH_GraphContainer) -> GH_GraphDrawInstruction """
        pass

    def Duplicate(self):
        """ Duplicate(self: IGH_Graph) -> IGH_Graph """
        pass

    def EmitProxyObject(self):
        """ EmitProxyObject(self: IGH_Graph) -> IGH_GraphProxyObject """
        pass

    def GDI_GraphPath(self, reg):
        """ GDI_GraphPath(self: IGH_Graph, reg: RectangleF) -> Array[PointF] """
        pass

    def OnGraphChanged(self, bIntermediate):
        """ OnGraphChanged(self: IGH_Graph, bIntermediate: bool) """
        pass

    def PrepareForUse(self):
        """ PrepareForUse(self: IGH_Graph) """
        pass

    def ValueAt(self, t):
        """ ValueAt(self: IGH_Graph, t: float) -> float """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    Description = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Description(self: IGH_Graph) -> str

"""

    GraphTypeID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: GraphTypeID(self: IGH_Graph) -> Guid

"""

    Grips = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Grips(self: IGH_Graph) -> List[GH_GraphGrip]

"""

    Icon_16x16 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Icon_16x16(self: IGH_Graph) -> Image

"""

    IsValid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsValid(self: IGH_Graph) -> bool

"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Name(self: IGH_Graph) -> str

"""


    GraphChanged = None
    GraphChangedEventHandler = None


class IGH_GraphProxyObject:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


