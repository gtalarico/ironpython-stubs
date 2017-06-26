class PrintParameters(APIObject,IDisposable):
 """ An object that contains settings used for printing the document. """
 def Dispose(self):
  """ Dispose(self: APIObject,A_0: bool) """
  pass
 def ReleaseManagedResources(self,*args):
  """ ReleaseManagedResources(self: APIObject) """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: APIObject) """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 ColorDepth=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The color depth type.

Get: ColorDepth(self: PrintParameters) -> ColorDepthType

Set: ColorDepth(self: PrintParameters)=value
"""

 HiddenLineViews=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The hidden line views type.

Get: HiddenLineViews(self: PrintParameters) -> HiddenLineViewsType

Set: HiddenLineViews(self: PrintParameters)=value
"""

 HideCropBoundaries=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether to hide crop boundaries when printing.

Get: HideCropBoundaries(self: PrintParameters) -> bool

Set: HideCropBoundaries(self: PrintParameters)=value
"""

 HideReforWorkPlanes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether to hide reference/work planes when printing.

Get: HideReforWorkPlanes(self: PrintParameters) -> bool

Set: HideReforWorkPlanes(self: PrintParameters)=value
"""

 HideScopeBoxes=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether to hide scope boxes when printing.

Get: HideScopeBoxes(self: PrintParameters) -> bool

Set: HideScopeBoxes(self: PrintParameters)=value
"""

 HideUnreferencedViewTags=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether to hide unreferenced view tags when printing.

Get: HideUnreferencedViewTags(self: PrintParameters) -> bool

Set: HideUnreferencedViewTags(self: PrintParameters)=value
"""

 MarginType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The print margin type.

Get: MarginType(self: PrintParameters) -> MarginType

Set: MarginType(self: PrintParameters)=value
"""

 MaskCoincidentLines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether to mask coincident lines when printing.

Get: MaskCoincidentLines(self: PrintParameters) -> bool

Set: MaskCoincidentLines(self: PrintParameters)=value
"""

 PageOrientation=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The Page Orientation of the Print Setting.

Get: PageOrientation(self: PrintParameters) -> PageOrientationType

Set: PageOrientation(self: PrintParameters)=value
"""

 PaperPlacement=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The paper placement type.

Get: PaperPlacement(self: PrintParameters) -> PaperPlacementType

Set: PaperPlacement(self: PrintParameters)=value
"""

 PaperSize=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The page size.

Get: PaperSize(self: PrintParameters) -> PaperSize

Set: PaperSize(self: PrintParameters)=value
"""

 PaperSource=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The page source.

Get: PaperSource(self: PrintParameters) -> PaperSource

Set: PaperSource(self: PrintParameters)=value
"""

 RasterQuality=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The raster quality type.

Get: RasterQuality(self: PrintParameters) -> RasterQualityType

Set: RasterQuality(self: PrintParameters)=value
"""

 ReplaceHalftoneWithThinLines=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether to replace halftone with thin lines when printing.

Get: ReplaceHalftoneWithThinLines(self: PrintParameters) -> bool

Set: ReplaceHalftoneWithThinLines(self: PrintParameters)=value
"""

 UserDefinedMarginX=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The User defined X value of offset from left bottom corner.

Get: UserDefinedMarginX(self: PrintParameters) -> float

Set: UserDefinedMarginX(self: PrintParameters)=value
"""

 UserDefinedMarginY=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The User defined Y value of offset from left bottom corner

Get: UserDefinedMarginY(self: PrintParameters) -> float

Set: UserDefinedMarginY(self: PrintParameters)=value
"""

 ViewLinksinBlue=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether to view links in blue when printing.

Get: ViewLinksinBlue(self: PrintParameters) -> bool

Set: ViewLinksinBlue(self: PrintParameters)=value
"""

 Zoom=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The zoom value to a percentage of the original size.

Get: Zoom(self: PrintParameters) -> int

Set: Zoom(self: PrintParameters)=value
"""

 ZoomType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The zoom type.

Get: ZoomType(self: PrintParameters) -> ZoomType

Set: ZoomType(self: PrintParameters)=value
"""


