# encoding: utf-8
# module System.Drawing.Imaging calls itself Imaging
# from System.Drawing, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class BitmapData(object):
    """
    Specifies the attributes of a bitmap image. The System.Drawing.Imaging.BitmapData class is used by the erload:System.Drawing.Bitmap.LockBits and System.Drawing.Bitmap.UnlockBits(System.Drawing.Imaging.BitmapData) methods of the System.Drawing.Bitmap class. Not inheritable.
    
    BitmapData()
    """
    Height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the pixel height of the System.Drawing.Bitmap object. Also sometimes referred to as the number of scan lines.

Get: Height(self: BitmapData) -> int

Set: Height(self: BitmapData) = value
"""

    PixelFormat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the format of the pixel information in the System.Drawing.Bitmap object that returned this System.Drawing.Imaging.BitmapData object.

Get: PixelFormat(self: BitmapData) -> PixelFormat

Set: PixelFormat(self: BitmapData) = value
"""

    Reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reserved. Do not use.

Get: Reserved(self: BitmapData) -> int

Set: Reserved(self: BitmapData) = value
"""

    Scan0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the address of the first pixel data in the bitmap. This can also be thought of as the first scan line in the bitmap.

Get: Scan0(self: BitmapData) -> IntPtr

Set: Scan0(self: BitmapData) = value
"""

    Stride = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the stride width (also called scan width) of the System.Drawing.Bitmap object.

Get: Stride(self: BitmapData) -> int

Set: Stride(self: BitmapData) = value
"""

    Width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the pixel width of the System.Drawing.Bitmap object. This can also be thought of as the number of pixels in one scan line.

Get: Width(self: BitmapData) -> int

Set: Width(self: BitmapData) = value
"""



class ColorAdjustType(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies which GDI+ objects use color adjustment information.
    
    enum ColorAdjustType, values: Any (6), Bitmap (1), Brush (2), Count (5), Default (0), Pen (3), Text (4)
    """
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

    Any = None
    Bitmap = None
    Brush = None
    Count = None
    Default = None
    Pen = None
    Text = None
    value__ = None


class ColorChannelFlag(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies individual channels in the CMYK (cyan, magenta, yellow, black) color space. This enumeration is used by the erload:System.Drawing.Imaging.ImageAttributes.SetOutputChannel methods.
    
    enum ColorChannelFlag, values: ColorChannelC (0), ColorChannelK (3), ColorChannelLast (4), ColorChannelM (1), ColorChannelY (2)
    """
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

    ColorChannelC = None
    ColorChannelK = None
    ColorChannelLast = None
    ColorChannelM = None
    ColorChannelY = None
    value__ = None


class ColorMap(object):
    """
    Defines a map for converting colors. Several methods of the System.Drawing.Imaging.ImageAttributes class adjust image colors by using a color-remap table, which is an array of System.Drawing.Imaging.ColorMap structures. Not inheritable.
    
    ColorMap()
    """
    NewColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the new System.Drawing.Color structure to which to convert.

Get: NewColor(self: ColorMap) -> Color

Set: NewColor(self: ColorMap) = value
"""

    OldColor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the existing System.Drawing.Color structure to be converted.

Get: OldColor(self: ColorMap) -> Color

Set: OldColor(self: ColorMap) = value
"""



class ColorMapType(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the types of color maps.
    
    enum ColorMapType, values: Brush (1), Default (0)
    """
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

    Brush = None
    Default = None
    value__ = None


class ColorMatrix(object):
    """
    Defines a 5 x 5 matrix that contains the coordinates for the RGBAW space. Several methods of the System.Drawing.Imaging.ImageAttributes class adjust image colors by using a color matrix. This class cannot be inherited.
    
    ColorMatrix()
    ColorMatrix(newColorMatrix: Array[Array[Single]])
    """
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    @staticmethod # known case of __new__
    def __new__(self, newColorMatrix=None):
        """
        __new__(cls: type)
        __new__(cls: type, newColorMatrix: Array[Array[Single]])
        """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Matrix00 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the element at the 0 (zero) row and 0 column of this System.Drawing.Imaging.ColorMatrix.

Get: Matrix00(self: ColorMatrix) -> Single

Set: Matrix00(self: ColorMatrix) = value
"""

    Matrix01 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the element at the 0 (zero) row and first column of this System.Drawing.Imaging.ColorMatrix.

Get: Matrix01(self: ColorMatrix) -> Single

Set: Matrix01(self: ColorMatrix) = value
"""

    Matrix02 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the element at the 0 (zero) row and second column of this System.Drawing.Imaging.ColorMatrix.

Get: Matrix02(self: ColorMatrix) -> Single

Set: Matrix02(self: ColorMatrix) = value
"""

    Matrix03 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the element at the 0 (zero) row and third column of this System.Drawing.Imaging.ColorMatrix. Represents the alpha component.

Get: Matrix03(self: ColorMatrix) -> Single

Set: Matrix03(self: ColorMatrix) = value
"""

    Matrix04 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the element at the 0 (zero) row and fourth column of this System.Drawing.Imaging.ColorMatrix.

Get: Matrix04(self: ColorMatrix) -> Single

Set: Matrix04(self: ColorMatrix) = value
"""

    Matrix10 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the element at the first row and 0 (zero) column of this System.Drawing.Imaging.ColorMatrix.

Get: Matrix10(self: ColorMatrix) -> Single

Set: Matrix10(self: ColorMatrix) = value
"""

    Matrix11 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the element at the first row and first column of this System.Drawing.Imaging.ColorMatrix.

Get: Matrix11(self: ColorMatrix) -> Single

Set: Matrix11(self: ColorMatrix) = value
"""

    Matrix12 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the element at the first row and second column of this System.Drawing.Imaging.ColorMatrix.

Get: Matrix12(self: ColorMatrix) -> Single

Set: Matrix12(self: ColorMatrix) = value
"""

    Matrix13 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the element at the first row and third column of this System.Drawing.Imaging.ColorMatrix. Represents the alpha component.

Get: Matrix13(self: ColorMatrix) -> Single

Set: Matrix13(self: ColorMatrix) = value
"""

    Matrix14 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the element at the first row and fourth column of this System.Drawing.Imaging.ColorMatrix.

Get: Matrix14(self: ColorMatrix) -> Single

Set: Matrix14(self: ColorMatrix) = value
"""

    Matrix20 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the element at the second row and 0 (zero) column of this System.Drawing.Imaging.ColorMatrix.

Get: Matrix20(self: ColorMatrix) -> Single

Set: Matrix20(self: ColorMatrix) = value
"""

    Matrix21 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the element at the second row and first column of this System.Drawing.Imaging.ColorMatrix.

Get: Matrix21(self: ColorMatrix) -> Single

Set: Matrix21(self: ColorMatrix) = value
"""

    Matrix22 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the element at the second row and second column of this System.Drawing.Imaging.ColorMatrix.

Get: Matrix22(self: ColorMatrix) -> Single

Set: Matrix22(self: ColorMatrix) = value
"""

    Matrix23 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the element at the second row and third column of this System.Drawing.Imaging.ColorMatrix.

Get: Matrix23(self: ColorMatrix) -> Single

Set: Matrix23(self: ColorMatrix) = value
"""

    Matrix24 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the element at the second row and fourth column of this System.Drawing.Imaging.ColorMatrix.

Get: Matrix24(self: ColorMatrix) -> Single

Set: Matrix24(self: ColorMatrix) = value
"""

    Matrix30 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the element at the third row and 0 (zero) column of this System.Drawing.Imaging.ColorMatrix.

Get: Matrix30(self: ColorMatrix) -> Single

Set: Matrix30(self: ColorMatrix) = value
"""

    Matrix31 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the element at the third row and first column of this System.Drawing.Imaging.ColorMatrix.

Get: Matrix31(self: ColorMatrix) -> Single

Set: Matrix31(self: ColorMatrix) = value
"""

    Matrix32 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the element at the third row and second column of this System.Drawing.Imaging.ColorMatrix.

Get: Matrix32(self: ColorMatrix) -> Single

Set: Matrix32(self: ColorMatrix) = value
"""

    Matrix33 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the element at the third row and third column of this System.Drawing.Imaging.ColorMatrix. Represents the alpha component.

Get: Matrix33(self: ColorMatrix) -> Single

Set: Matrix33(self: ColorMatrix) = value
"""

    Matrix34 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the element at the third row and fourth column of this System.Drawing.Imaging.ColorMatrix.

Get: Matrix34(self: ColorMatrix) -> Single

Set: Matrix34(self: ColorMatrix) = value
"""

    Matrix40 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the element at the fourth row and 0 (zero) column of this System.Drawing.Imaging.ColorMatrix.

Get: Matrix40(self: ColorMatrix) -> Single

Set: Matrix40(self: ColorMatrix) = value
"""

    Matrix41 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the element at the fourth row and first column of this System.Drawing.Imaging.ColorMatrix.

Get: Matrix41(self: ColorMatrix) -> Single

Set: Matrix41(self: ColorMatrix) = value
"""

    Matrix42 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the element at the fourth row and second column of this System.Drawing.Imaging.ColorMatrix.

Get: Matrix42(self: ColorMatrix) -> Single

Set: Matrix42(self: ColorMatrix) = value
"""

    Matrix43 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the element at the fourth row and third column of this System.Drawing.Imaging.ColorMatrix. Represents the alpha component.

Get: Matrix43(self: ColorMatrix) -> Single

Set: Matrix43(self: ColorMatrix) = value
"""

    Matrix44 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the element at the fourth row and fourth column of this System.Drawing.Imaging.ColorMatrix.

Get: Matrix44(self: ColorMatrix) -> Single

Set: Matrix44(self: ColorMatrix) = value
"""



class ColorMatrixFlag(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the types of images and colors that will be affected by the color and grayscale adjustment settings of an System.Drawing.Imaging.ImageAttributes.
    
    enum ColorMatrixFlag, values: AltGrays (2), Default (0), SkipGrays (1)
    """
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

    AltGrays = None
    Default = None
    SkipGrays = None
    value__ = None


class ColorMode(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies two modes for color component values.
    
    enum ColorMode, values: Argb32Mode (0), Argb64Mode (1)
    """
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

    Argb32Mode = None
    Argb64Mode = None
    value__ = None


class ColorPalette(object):
    """ Defines an array of colors that make up a color palette. The colors are 32-bit ARGB colors. Not inheritable. """
    Entries = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets an array of System.Drawing.Color structures.

Get: Entries(self: ColorPalette) -> Array[Color]

"""

    Flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a value that specifies how to interpret the color information in the array of colors.

Get: Flags(self: ColorPalette) -> int

"""



class EmfPlusRecordType(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the methods available for use with a metafile to read and write graphic commands.
    
    enum EmfPlusRecordType, values: BeginContainer (16423), BeginContainerNoParams (16424), Clear (16393), Comment (16387), DrawArc (16402), DrawBeziers (16409), DrawClosedCurve (16407), DrawCurve (16408), DrawDriverString (16438), DrawEllipse (16399), DrawImage (16410), DrawImagePoints (16411), DrawLines (16397), DrawPath (16405), DrawPie (16401), DrawRects (16395), DrawString (16412), EmfAbortPath (68), EmfAlphaBlend (114), EmfAngleArc (41), EmfArcTo (55), EmfBeginPath (59), EmfBitBlt (76), EmfChord (46), EmfCloseFigure (61), EmfColorCorrectPalette (111), EmfColorMatchToTargetW (121), EmfCreateBrushIndirect (39), EmfCreateColorSpace (99), EmfCreateColorSpaceW (122), EmfCreateDibPatternBrushPt (94), EmfCreateMonoBrush (93), EmfCreatePalette (49), EmfCreatePen (38), EmfDeleteColorSpace (101), EmfDeleteObject (40), EmfDrawEscape (105), EmfEllipse (42), EmfEndPath (60), EmfEof (14), EmfExcludeClipRect (29), EmfExtCreateFontIndirect (82), EmfExtCreatePen (95), EmfExtEscape (106), EmfExtFloodFill (53), EmfExtSelectClipRgn (75), EmfExtTextOutA (83), EmfExtTextOutW (84), EmfFillPath (62), EmfFillRgn (71), EmfFlattenPath (65), EmfForceUfiMapping (109), EmfFrameRgn (72), EmfGdiComment (70), EmfGlsBoundedRecord (103), EmfGlsRecord (102), EmfGradientFill (118), EmfHeader (1), EmfIntersectClipRect (30), EmfInvertRgn (73), EmfLineTo (54), EmfMaskBlt (78), EmfMax (122), EmfMin (1), EmfModifyWorldTransform (36), EmfMoveToEx (27), EmfNamedEscpae (110), EmfOffsetClipRgn (26), EmfPaintRgn (74), EmfPie (47), EmfPixelFormat (104), EmfPlgBlt (79), EmfPlusRecordBase (16384), EmfPolyBezier (2), EmfPolyBezier16 (85), EmfPolyBezierTo (5), EmfPolyBezierTo16 (88), EmfPolyDraw (56), EmfPolyDraw16 (92), EmfPolygon (3), EmfPolygon16 (86), EmfPolyline (4), EmfPolyline16 (87), EmfPolyLineTo (6), EmfPolylineTo16 (89), EmfPolyPolygon (8), EmfPolyPolygon16 (91), EmfPolyPolyline (7), EmfPolyPolyline16 (90), EmfPolyTextOutA (96), EmfPolyTextOutW (97), EmfRealizePalette (52), EmfRectangle (43), EmfReserved069 (69), EmfReserved117 (117), EmfResizePalette (51), EmfRestoreDC (34), EmfRoundArc (45), EmfRoundRect (44), EmfSaveDC (33), EmfScaleViewportExtEx (31), EmfScaleWindowExtEx (32), EmfSelectClipPath (67), EmfSelectObject (37), EmfSelectPalette (48), EmfSetArcDirection (57), EmfSetBkColor (25), EmfSetBkMode (18), EmfSetBrushOrgEx (13), EmfSetColorAdjustment (23), EmfSetColorSpace (100), EmfSetDIBitsToDevice (80), EmfSetIcmMode (98), EmfSetIcmProfileA (112), EmfSetIcmProfileW (113), EmfSetLayout (115), EmfSetLinkedUfis (119), EmfSetMapMode (17), EmfSetMapperFlags (16), EmfSetMetaRgn (28), EmfSetMiterLimit (58), EmfSetPaletteEntries (50), EmfSetPixelV (15), EmfSetPolyFillMode (19), EmfSetROP2 (20), EmfSetStretchBltMode (21), EmfSetTextAlign (22), EmfSetTextColor (24), EmfSetTextJustification (120), EmfSetViewportExtEx (11), EmfSetViewportOrgEx (12), EmfSetWindowExtEx (9), EmfSetWindowOrgEx (10), EmfSetWorldTransform (35), EmfSmallTextOut (108), EmfStartDoc (107), EmfStretchBlt (77), EmfStretchDIBits (81), EmfStrokeAndFillPath (63), EmfStrokePath (64), EmfTransparentBlt (116), EmfWidenPath (66), EndContainer (16425), EndOfFile (16386), FillClosedCurve (16406), FillEllipse (16398), FillPath (16404), FillPie (16400), FillPolygon (16396), FillRects (16394), FillRegion (16403), GetDC (16388), Header (16385), Invalid (16384), Max (16438), Min (16385), MultiFormatEnd (16391), MultiFormatSection (16390), MultiFormatStart (16389), MultiplyWorldTransform (16428), Object (16392), OffsetClip (16437), ResetClip (16433), ResetWorldTransform (16427), Restore (16422), RotateWorldTransform (16431), Save (16421), ScaleWorldTransform (16430), SetAntiAliasMode (16414), SetClipPath (16435), SetClipRect (16434), SetClipRegion (16436), SetCompositingMode (16419), SetCompositingQuality (16420), SetInterpolationMode (16417), SetPageTransform (16432), SetPixelOffsetMode (16418), SetRenderingOrigin (16413), SetTextContrast (16416), SetTextRenderingHint (16415), SetWorldTransform (16426), Total (16439), TranslateWorldTransform (16429), WmfAnimatePalette (66614), WmfArc (67607), WmfBitBlt (67874), WmfChord (67632), WmfCreateBrushIndirect (66300), WmfCreateFontIndirect (66299), WmfCreatePalette (65783), WmfCreatePatternBrush (66041), WmfCreatePenIndirect (66298), WmfCreateRegion (67327), WmfDeleteObject (66032), WmfDibBitBlt (67904), WmfDibCreatePatternBrush (65858), WmfDibStretchBlt (68417), WmfEllipse (66584), WmfEscape (67110), WmfExcludeClipRect (66581), WmfExtFloodFill (66888), WmfExtTextOut (68146), WmfFillRegion (66088), WmfFloodFill (66585), WmfFrameRegion (66601), WmfIntersectClipRect (66582), WmfInvertRegion (65834), WmfLineTo (66067), WmfMoveTo (66068), WmfOffsetCilpRgn (66080), WmfOffsetViewportOrg (66065), WmfOffsetWindowOrg (66063), WmfPaintRegion (65835), WmfPatBlt (67101), WmfPie (67610), WmfPolygon (66340), WmfPolyline (66341), WmfPolyPolygon (66872), WmfRealizePalette (65589), WmfRecordBase (65536), WmfRectangle (66587), WmfResizePalette (65849), WmfRestoreDC (65831), WmfRoundRect (67100), WmfSaveDC (65566), WmfScaleViewportExt (66578), WmfScaleWindowExt (66576), WmfSelectClipRegion (65836), WmfSelectObject (65837), WmfSelectPalette (66100), WmfSetBkColor (66049), WmfSetBkMode (65794), WmfSetDibToDev (68915), WmfSetLayout (65865), WmfSetMapMode (65795), WmfSetMapperFlags (66097), WmfSetPalEntries (65591), WmfSetPixel (66591), WmfSetPolyFillMode (65798), WmfSetRelAbs (65797), WmfSetROP2 (65796), WmfSetStretchBltMode (65799), WmfSetTextAlign (65838), WmfSetTextCharExtra (65800), WmfSetTextColor (66057), WmfSetTextJustification (66058), WmfSetViewportExt (66062), WmfSetViewportOrg (66061), WmfSetWindowExt (66060), WmfSetWindowOrg (66059), WmfStretchBlt (68387), WmfStretchDib (69443), WmfTextOut (66849)
    """
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

    BeginContainer = None
    BeginContainerNoParams = None
    Clear = None
    Comment = None
    DrawArc = None
    DrawBeziers = None
    DrawClosedCurve = None
    DrawCurve = None
    DrawDriverString = None
    DrawEllipse = None
    DrawImage = None
    DrawImagePoints = None
    DrawLines = None
    DrawPath = None
    DrawPie = None
    DrawRects = None
    DrawString = None
    EmfAbortPath = None
    EmfAlphaBlend = None
    EmfAngleArc = None
    EmfArcTo = None
    EmfBeginPath = None
    EmfBitBlt = None
    EmfChord = None
    EmfCloseFigure = None
    EmfColorCorrectPalette = None
    EmfColorMatchToTargetW = None
    EmfCreateBrushIndirect = None
    EmfCreateColorSpace = None
    EmfCreateColorSpaceW = None
    EmfCreateDibPatternBrushPt = None
    EmfCreateMonoBrush = None
    EmfCreatePalette = None
    EmfCreatePen = None
    EmfDeleteColorSpace = None
    EmfDeleteObject = None
    EmfDrawEscape = None
    EmfEllipse = None
    EmfEndPath = None
    EmfEof = None
    EmfExcludeClipRect = None
    EmfExtCreateFontIndirect = None
    EmfExtCreatePen = None
    EmfExtEscape = None
    EmfExtFloodFill = None
    EmfExtSelectClipRgn = None
    EmfExtTextOutA = None
    EmfExtTextOutW = None
    EmfFillPath = None
    EmfFillRgn = None
    EmfFlattenPath = None
    EmfForceUfiMapping = None
    EmfFrameRgn = None
    EmfGdiComment = None
    EmfGlsBoundedRecord = None
    EmfGlsRecord = None
    EmfGradientFill = None
    EmfHeader = None
    EmfIntersectClipRect = None
    EmfInvertRgn = None
    EmfLineTo = None
    EmfMaskBlt = None
    EmfMax = None
    EmfMin = None
    EmfModifyWorldTransform = None
    EmfMoveToEx = None
    EmfNamedEscpae = None
    EmfOffsetClipRgn = None
    EmfPaintRgn = None
    EmfPie = None
    EmfPixelFormat = None
    EmfPlgBlt = None
    EmfPlusRecordBase = None
    EmfPolyBezier = None
    EmfPolyBezier16 = None
    EmfPolyBezierTo = None
    EmfPolyBezierTo16 = None
    EmfPolyDraw = None
    EmfPolyDraw16 = None
    EmfPolygon = None
    EmfPolygon16 = None
    EmfPolyline = None
    EmfPolyline16 = None
    EmfPolyLineTo = None
    EmfPolylineTo16 = None
    EmfPolyPolygon = None
    EmfPolyPolygon16 = None
    EmfPolyPolyline = None
    EmfPolyPolyline16 = None
    EmfPolyTextOutA = None
    EmfPolyTextOutW = None
    EmfRealizePalette = None
    EmfRectangle = None
    EmfReserved069 = None
    EmfReserved117 = None
    EmfResizePalette = None
    EmfRestoreDC = None
    EmfRoundArc = None
    EmfRoundRect = None
    EmfSaveDC = None
    EmfScaleViewportExtEx = None
    EmfScaleWindowExtEx = None
    EmfSelectClipPath = None
    EmfSelectObject = None
    EmfSelectPalette = None
    EmfSetArcDirection = None
    EmfSetBkColor = None
    EmfSetBkMode = None
    EmfSetBrushOrgEx = None
    EmfSetColorAdjustment = None
    EmfSetColorSpace = None
    EmfSetDIBitsToDevice = None
    EmfSetIcmMode = None
    EmfSetIcmProfileA = None
    EmfSetIcmProfileW = None
    EmfSetLayout = None
    EmfSetLinkedUfis = None
    EmfSetMapMode = None
    EmfSetMapperFlags = None
    EmfSetMetaRgn = None
    EmfSetMiterLimit = None
    EmfSetPaletteEntries = None
    EmfSetPixelV = None
    EmfSetPolyFillMode = None
    EmfSetROP2 = None
    EmfSetStretchBltMode = None
    EmfSetTextAlign = None
    EmfSetTextColor = None
    EmfSetTextJustification = None
    EmfSetViewportExtEx = None
    EmfSetViewportOrgEx = None
    EmfSetWindowExtEx = None
    EmfSetWindowOrgEx = None
    EmfSetWorldTransform = None
    EmfSmallTextOut = None
    EmfStartDoc = None
    EmfStretchBlt = None
    EmfStretchDIBits = None
    EmfStrokeAndFillPath = None
    EmfStrokePath = None
    EmfTransparentBlt = None
    EmfWidenPath = None
    EndContainer = None
    EndOfFile = None
    FillClosedCurve = None
    FillEllipse = None
    FillPath = None
    FillPie = None
    FillPolygon = None
    FillRects = None
    FillRegion = None
    GetDC = None
    Header = None
    Invalid = None
    Max = None
    Min = None
    MultiFormatEnd = None
    MultiFormatSection = None
    MultiFormatStart = None
    MultiplyWorldTransform = None
    Object = None
    OffsetClip = None
    ResetClip = None
    ResetWorldTransform = None
    Restore = None
    RotateWorldTransform = None
    Save = None
    ScaleWorldTransform = None
    SetAntiAliasMode = None
    SetClipPath = None
    SetClipRect = None
    SetClipRegion = None
    SetCompositingMode = None
    SetCompositingQuality = None
    SetInterpolationMode = None
    SetPageTransform = None
    SetPixelOffsetMode = None
    SetRenderingOrigin = None
    SetTextContrast = None
    SetTextRenderingHint = None
    SetWorldTransform = None
    Total = None
    TranslateWorldTransform = None
    value__ = None
    WmfAnimatePalette = None
    WmfArc = None
    WmfBitBlt = None
    WmfChord = None
    WmfCreateBrushIndirect = None
    WmfCreateFontIndirect = None
    WmfCreatePalette = None
    WmfCreatePatternBrush = None
    WmfCreatePenIndirect = None
    WmfCreateRegion = None
    WmfDeleteObject = None
    WmfDibBitBlt = None
    WmfDibCreatePatternBrush = None
    WmfDibStretchBlt = None
    WmfEllipse = None
    WmfEscape = None
    WmfExcludeClipRect = None
    WmfExtFloodFill = None
    WmfExtTextOut = None
    WmfFillRegion = None
    WmfFloodFill = None
    WmfFrameRegion = None
    WmfIntersectClipRect = None
    WmfInvertRegion = None
    WmfLineTo = None
    WmfMoveTo = None
    WmfOffsetCilpRgn = None
    WmfOffsetViewportOrg = None
    WmfOffsetWindowOrg = None
    WmfPaintRegion = None
    WmfPatBlt = None
    WmfPie = None
    WmfPolygon = None
    WmfPolyline = None
    WmfPolyPolygon = None
    WmfRealizePalette = None
    WmfRecordBase = None
    WmfRectangle = None
    WmfResizePalette = None
    WmfRestoreDC = None
    WmfRoundRect = None
    WmfSaveDC = None
    WmfScaleViewportExt = None
    WmfScaleWindowExt = None
    WmfSelectClipRegion = None
    WmfSelectObject = None
    WmfSelectPalette = None
    WmfSetBkColor = None
    WmfSetBkMode = None
    WmfSetDibToDev = None
    WmfSetLayout = None
    WmfSetMapMode = None
    WmfSetMapperFlags = None
    WmfSetPalEntries = None
    WmfSetPixel = None
    WmfSetPolyFillMode = None
    WmfSetRelAbs = None
    WmfSetROP2 = None
    WmfSetStretchBltMode = None
    WmfSetTextAlign = None
    WmfSetTextCharExtra = None
    WmfSetTextColor = None
    WmfSetTextJustification = None
    WmfSetViewportExt = None
    WmfSetViewportOrg = None
    WmfSetWindowExt = None
    WmfSetWindowOrg = None
    WmfStretchBlt = None
    WmfStretchDib = None
    WmfTextOut = None


class EmfType(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the nature of the records that are placed in an Enhanced Metafile (EMF) file. This enumeration is used by several constructors in the System.Drawing.Imaging.Metafile class.
    
    enum EmfType, values: EmfOnly (3), EmfPlusDual (5), EmfPlusOnly (4)
    """
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

    EmfOnly = None
    EmfPlusDual = None
    EmfPlusOnly = None
    value__ = None


class Encoder(object):
    """
    An System.Drawing.Imaging.Encoder object encapsulates a globally unique identifier (GUID) that identifies the category of an image encoder parameter.
    
    Encoder(guid: Guid)
    """
    @staticmethod # known case of __new__
    def __new__(self, guid):
        """ __new__(cls: type, guid: Guid) """
        pass

    Guid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a globally unique identifier (GUID) that identifies an image encoder parameter category.

Get: Guid(self: Encoder) -> Guid

"""


    ChrominanceTable = None
    ColorDepth = None
    Compression = None
    LuminanceTable = None
    Quality = None
    RenderMethod = None
    SaveFlag = None
    ScanMethod = None
    Transformation = None
    Version = None


class EncoderParameter(object, IDisposable):
    """
    Used to pass a value, or an array of values, to an image encoder.
    
    EncoderParameter(encoder: Encoder, value: Byte)
    EncoderParameter(encoder: Encoder, value: Byte, undefined: bool)
    EncoderParameter(encoder: Encoder, value: Int16)
    EncoderParameter(encoder: Encoder, value: Int64)
    EncoderParameter(encoder: Encoder, numerator: int, denominator: int)
    EncoderParameter(encoder: Encoder, rangebegin: Int64, rangeend: Int64)
    EncoderParameter(encoder: Encoder, numerator1: int, demoninator1: int, numerator2: int, demoninator2: int)
    EncoderParameter(encoder: Encoder, value: str)
    EncoderParameter(encoder: Encoder, value: Array[Byte])
    EncoderParameter(encoder: Encoder, value: Array[Byte], undefined: bool)
    EncoderParameter(encoder: Encoder, value: Array[Int16])
    EncoderParameter(encoder: Encoder, value: Array[Int64])
    EncoderParameter(encoder: Encoder, numerator: Array[int], denominator: Array[int])
    EncoderParameter(encoder: Encoder, rangebegin: Array[Int64], rangeend: Array[Int64])
    EncoderParameter(encoder: Encoder, numerator1: Array[int], denominator1: Array[int], numerator2: Array[int], denominator2: Array[int])
    EncoderParameter(encoder: Encoder, NumberOfValues: int, Type: int, Value: int)
    EncoderParameter(encoder: Encoder, numberValues: int, type: EncoderParameterValueType, value: IntPtr)
    """
    def Dispose(self):
        """
        Dispose(self: EncoderParameter)
            Releases all resources used by this System.Drawing.Imaging.EncoderParameter object.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, encoder, *__args):
        """
        __new__(cls: type, encoder: Encoder, value: Byte)
        __new__(cls: type, encoder: Encoder, value: Byte, undefined: bool)
        __new__(cls: type, encoder: Encoder, value: Int16)
        __new__(cls: type, encoder: Encoder, value: Int64)
        __new__(cls: type, encoder: Encoder, numerator: int, denominator: int)
        __new__(cls: type, encoder: Encoder, rangebegin: Int64, rangeend: Int64)
        __new__(cls: type, encoder: Encoder, numerator1: int, demoninator1: int, numerator2: int, demoninator2: int)
        __new__(cls: type, encoder: Encoder, value: str)
        __new__(cls: type, encoder: Encoder, value: Array[Byte])
        __new__(cls: type, encoder: Encoder, value: Array[Byte], undefined: bool)
        __new__(cls: type, encoder: Encoder, value: Array[Int16])
        __new__(cls: type, encoder: Encoder, value: Array[Int64])
        __new__(cls: type, encoder: Encoder, numerator: Array[int], denominator: Array[int])
        __new__(cls: type, encoder: Encoder, rangebegin: Array[Int64], rangeend: Array[Int64])
        __new__(cls: type, encoder: Encoder, numerator1: Array[int], denominator1: Array[int], numerator2: Array[int], denominator2: Array[int])
        __new__(cls: type, encoder: Encoder, NumberOfValues: int, Type: int, Value: int)
        __new__(cls: type, encoder: Encoder, numberValues: int, type: EncoderParameterValueType, value: IntPtr)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Encoder = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the System.Drawing.Imaging.Encoder object associated with this System.Drawing.Imaging.EncoderParameter object. The System.Drawing.Imaging.Encoder object encapsulates the globally unique identifier (GUID) that specifies the category (for example System.Drawing.Imaging.Encoder.Quality, System.Drawing.Imaging.Encoder.ColorDepth, or System.Drawing.Imaging.Encoder.Compression) of the parameter stored in this System.Drawing.Imaging.EncoderParameter object.

Get: Encoder(self: EncoderParameter) -> Encoder

Set: Encoder(self: EncoderParameter) = value
"""

    NumberOfValues = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of elements in the array of values stored in this System.Drawing.Imaging.EncoderParameter object.

Get: NumberOfValues(self: EncoderParameter) -> int

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the data type of the values stored in this System.Drawing.Imaging.EncoderParameter object.

Get: Type(self: EncoderParameter) -> EncoderParameterValueType

"""

    ValueType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the data type of the values stored in this System.Drawing.Imaging.EncoderParameter object.

Get: ValueType(self: EncoderParameter) -> EncoderParameterValueType

"""



class EncoderParameters(object, IDisposable):
    """
    Encapsulates an array of System.Drawing.Imaging.EncoderParameter objects.
    
    EncoderParameters(count: int)
    EncoderParameters()
    """
    def Dispose(self):
        """
        Dispose(self: EncoderParameters)
            Releases all resources used by this System.Drawing.Imaging.EncoderParameters object.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, count=None):
        """
        __new__(cls: type, count: int)
        __new__(cls: type)
        """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Param = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets an array of System.Drawing.Imaging.EncoderParameter objects.

Get: Param(self: EncoderParameters) -> Array[EncoderParameter]

Set: Param(self: EncoderParameters) = value
"""



class EncoderParameterValueType(Enum, IComparable, IFormattable, IConvertible):
    """
    Used to specify the data type of the System.Drawing.Imaging.EncoderParameter used with the erload:System.Drawing.Image.Save or erload:System.Drawing.Image.SaveAdd method of an image.
    
    enum EncoderParameterValueType, values: ValueTypeAscii (2), ValueTypeByte (1), ValueTypeLong (4), ValueTypeLongRange (6), ValueTypeRational (5), ValueTypeRationalRange (8), ValueTypeShort (3), ValueTypeUndefined (7)
    """
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

    ValueTypeAscii = None
    ValueTypeByte = None
    ValueTypeLong = None
    ValueTypeLongRange = None
    ValueTypeRational = None
    ValueTypeRationalRange = None
    ValueTypeShort = None
    ValueTypeUndefined = None
    value__ = None


class EncoderValue(Enum, IComparable, IFormattable, IConvertible):
    """
    Used to specify the parameter value passed to a JPEG or TIFF image encoder when using the System.Drawing.Image.Save(System.String,System.Drawing.Imaging.ImageCodecInfo,System.Drawing.Imaging.EncoderParameters) or System.Drawing.Image.SaveAdd(System.Drawing.Imaging.EncoderParameters) methods.
    
    enum EncoderValue, values: ColorTypeCMYK (0), ColorTypeYCCK (1), CompressionCCITT3 (3), CompressionCCITT4 (4), CompressionLZW (2), CompressionNone (6), CompressionRle (5), Flush (20), FrameDimensionPage (23), FrameDimensionResolution (22), FrameDimensionTime (21), LastFrame (19), MultiFrame (18), RenderNonProgressive (12), RenderProgressive (11), ScanMethodInterlaced (7), ScanMethodNonInterlaced (8), TransformFlipHorizontal (16), TransformFlipVertical (17), TransformRotate180 (14), TransformRotate270 (15), TransformRotate90 (13), VersionGif87 (9), VersionGif89 (10)
    """
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

    ColorTypeCMYK = None
    ColorTypeYCCK = None
    CompressionCCITT3 = None
    CompressionCCITT4 = None
    CompressionLZW = None
    CompressionNone = None
    CompressionRle = None
    Flush = None
    FrameDimensionPage = None
    FrameDimensionResolution = None
    FrameDimensionTime = None
    LastFrame = None
    MultiFrame = None
    RenderNonProgressive = None
    RenderProgressive = None
    ScanMethodInterlaced = None
    ScanMethodNonInterlaced = None
    TransformFlipHorizontal = None
    TransformFlipVertical = None
    TransformRotate180 = None
    TransformRotate270 = None
    TransformRotate90 = None
    value__ = None
    VersionGif87 = None
    VersionGif89 = None


class FrameDimension(object):
    """
    Provides properties that get the frame dimensions of an image. Not inheritable.
    
    FrameDimension(guid: Guid)
    """
    def Equals(self, o):
        """
        Equals(self: FrameDimension, o: object) -> bool
        
            Returns a value that indicates whether the specified object is a 
             System.Drawing.Imaging.FrameDimension equivalent to this System.Drawing.Imaging.FrameDimension 
             object.
        
        
            o: The object to test.
            Returns: Returns true if o is a System.Drawing.Imaging.FrameDimension equivalent to this 
             System.Drawing.Imaging.FrameDimension object; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: FrameDimension) -> int
        
            Returns a hash code for this System.Drawing.Imaging.FrameDimension object.
            Returns: Returns an int value that is the hash code of this System.Drawing.Imaging.FrameDimension object.
        """
        pass

    def ToString(self):
        """
        ToString(self: FrameDimension) -> str
        
            Converts this System.Drawing.Imaging.FrameDimension object to a human-readable string.
            Returns: A string that represents this System.Drawing.Imaging.FrameDimension object.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, guid):
        """ __new__(cls: type, guid: Guid) """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Guid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a globally unique identifier (GUID) that represents this System.Drawing.Imaging.FrameDimension object.

Get: Guid(self: FrameDimension) -> Guid

"""


    Page = None
    Resolution = None
    Time = None


class ImageAttributes(object, ICloneable, IDisposable):
    """
    Contains information about how bitmap and metafile colors are manipulated during rendering.
    
    ImageAttributes()
    """
    def ClearBrushRemapTable(self):
        """
        ClearBrushRemapTable(self: ImageAttributes)
            Clears the brush color-remap table of this System.Drawing.Imaging.ImageAttributes object.
        """
        pass

    def ClearColorKey(self, type=None):
        """
        ClearColorKey(self: ImageAttributes)
            Clears the color key (transparency range) for the default category.
        ClearColorKey(self: ImageAttributes, type: ColorAdjustType)
            Clears the color key (transparency range) for a specified category.
        
            type: An element of System.Drawing.Imaging.ColorAdjustType that specifies the category for which the 
             color key is cleared.
        """
        pass

    def ClearColorMatrix(self, type=None):
        """
        ClearColorMatrix(self: ImageAttributes, type: ColorAdjustType)
            Clears the color-adjustment matrix for a specified category.
        
            type: An element of System.Drawing.Imaging.ColorAdjustType that specifies the category for which the 
             color-adjustment matrix is cleared.
        
        ClearColorMatrix(self: ImageAttributes)
            Clears the color-adjustment matrix for the default category.
        """
        pass

    def ClearGamma(self, type=None):
        """
        ClearGamma(self: ImageAttributes, type: ColorAdjustType)
            Disables gamma correction for a specified category.
        
            type: An element of System.Drawing.Imaging.ColorAdjustType that specifies the category for which gamma 
             correction is disabled.
        
        ClearGamma(self: ImageAttributes)
            Disables gamma correction for the default category.
        """
        pass

    def ClearNoOp(self, type=None):
        """
        ClearNoOp(self: ImageAttributes, type: ColorAdjustType)
            Clears the NoOp setting for a specified category.
        
            type: An element of System.Drawing.Imaging.ColorAdjustType that specifies the category for which the 
             NoOp setting is cleared.
        
        ClearNoOp(self: ImageAttributes)
            Clears the NoOp setting for the default category.
        """
        pass

    def ClearOutputChannel(self, type=None):
        """
        ClearOutputChannel(self: ImageAttributes, type: ColorAdjustType)
            Clears the (cyan-magenta-yellow-black) output channel setting for a specified category.
        
            type: An element of System.Drawing.Imaging.ColorAdjustType that specifies the category for which the 
             output channel setting is cleared.
        
        ClearOutputChannel(self: ImageAttributes)
            Clears the CMYK (cyan-magenta-yellow-black) output channel setting for the default category.
        """
        pass

    def ClearOutputChannelColorProfile(self, type=None):
        """
        ClearOutputChannelColorProfile(self: ImageAttributes, type: ColorAdjustType)
            Clears the output channel color profile setting for a specified category.
        
            type: An element of System.Drawing.Imaging.ColorAdjustType that specifies the category for which the 
             output channel profile setting is cleared.
        
        ClearOutputChannelColorProfile(self: ImageAttributes)
            Clears the output channel color profile setting for the default category.
        """
        pass

    def ClearRemapTable(self, type=None):
        """
        ClearRemapTable(self: ImageAttributes, type: ColorAdjustType)
            Clears the color-remap table for a specified category.
        
            type: An element of System.Drawing.Imaging.ColorAdjustType that specifies the category for which the 
             remap table is cleared.
        
        ClearRemapTable(self: ImageAttributes)
            Clears the color-remap table for the default category.
        """
        pass

    def ClearThreshold(self, type=None):
        """
        ClearThreshold(self: ImageAttributes, type: ColorAdjustType)
            Clears the threshold value for a specified category.
        
            type: An element of System.Drawing.Imaging.ColorAdjustType that specifies the category for which the 
             threshold is cleared.
        
        ClearThreshold(self: ImageAttributes)
            Clears the threshold value for the default category.
        """
        pass

    def Clone(self):
        """
        Clone(self: ImageAttributes) -> object
        
            Creates an exact copy of this System.Drawing.Imaging.ImageAttributes object.
            Returns: The System.Drawing.Imaging.ImageAttributes object this class creates, cast as an object.
        """
        pass

    def Dispose(self):
        """
        Dispose(self: ImageAttributes)
            Releases all resources used by this System.Drawing.Imaging.ImageAttributes object.
        """
        pass

    def GetAdjustedPalette(self, palette, type):
        """
        GetAdjustedPalette(self: ImageAttributes, palette: ColorPalette, type: ColorAdjustType)
            Adjusts the colors in a palette according to the adjustment settings of a specified category.
        
            palette: A System.Drawing.Imaging.ColorPalette that on input contains the palette to be adjusted, and on 
             output contains the adjusted palette.
        
            type: An element of System.Drawing.Imaging.ColorAdjustType that specifies the category whose 
             adjustment settings will be applied to the palette.
        """
        pass

    def SetBrushRemapTable(self, map):
        """
        SetBrushRemapTable(self: ImageAttributes, map: Array[ColorMap])
            Sets the color-remap table for the brush category.
        
            map: An array of System.Drawing.Imaging.ColorMap objects.
        """
        pass

    def SetColorKey(self, colorLow, colorHigh, type=None):
        """
        SetColorKey(self: ImageAttributes, colorLow: Color, colorHigh: Color, type: ColorAdjustType)
            Sets the color key (transparency range) for a specified category.
        
            colorLow: The low color-key value.
            colorHigh: The high color-key value.
            type: An element of System.Drawing.Imaging.ColorAdjustType that specifies the category for which the 
             color key is set.
        
        SetColorKey(self: ImageAttributes, colorLow: Color, colorHigh: Color)
            Sets the color key for the default category.
        
            colorLow: The low color-key value.
            colorHigh: The high color-key value.
        """
        pass

    def SetColorMatrices(self, newColorMatrix, grayMatrix, *__args):
        """
        SetColorMatrices(self: ImageAttributes, newColorMatrix: ColorMatrix, grayMatrix: ColorMatrix, mode: ColorMatrixFlag, type: ColorAdjustType)
            Sets the color-adjustment matrix and the grayscale-adjustment matrix for a specified category.
        
            newColorMatrix: The color-adjustment matrix.
            grayMatrix: The grayscale-adjustment matrix.
            mode: An element of System.Drawing.Imaging.ColorMatrixFlag that specifies the type of image and color 
             that will be affected by the color-adjustment and grayscale-adjustment matrices.
        
            type: An element of System.Drawing.Imaging.ColorAdjustType that specifies the category for which the 
             color-adjustment and grayscale-adjustment matrices are set.
        
        SetColorMatrices(self: ImageAttributes, newColorMatrix: ColorMatrix, grayMatrix: ColorMatrix, flags: ColorMatrixFlag)
            Sets the color-adjustment matrix and the grayscale-adjustment matrix for the default category.
        
            newColorMatrix: The color-adjustment matrix.
            grayMatrix: The grayscale-adjustment matrix.
            flags: An element of System.Drawing.Imaging.ColorMatrixFlag that specifies the type of image and color 
             that will be affected by the color-adjustment and grayscale-adjustment matrices.
        
        SetColorMatrices(self: ImageAttributes, newColorMatrix: ColorMatrix, grayMatrix: ColorMatrix)
            Sets the color-adjustment matrix and the grayscale-adjustment matrix for the default category.
        
            newColorMatrix: The color-adjustment matrix.
            grayMatrix: The grayscale-adjustment matrix.
        """
        pass

    def SetColorMatrix(self, newColorMatrix, *__args):
        """
        SetColorMatrix(self: ImageAttributes, newColorMatrix: ColorMatrix, flags: ColorMatrixFlag)
            Sets the color-adjustment matrix for the default category.
        
            newColorMatrix: The color-adjustment matrix.
            flags: An element of System.Drawing.Imaging.ColorMatrixFlag that specifies the type of image and color 
             that will be affected by the color-adjustment matrix.
        
        SetColorMatrix(self: ImageAttributes, newColorMatrix: ColorMatrix)
            Sets the color-adjustment matrix for the default category.
        
            newColorMatrix: The color-adjustment matrix.
        SetColorMatrix(self: ImageAttributes, newColorMatrix: ColorMatrix, mode: ColorMatrixFlag, type: ColorAdjustType)
            Sets the color-adjustment matrix for a specified category.
        
            newColorMatrix: The color-adjustment matrix.
            mode: An element of System.Drawing.Imaging.ColorMatrixFlag that specifies the type of image and color 
             that will be affected by the color-adjustment matrix.
        
            type: An element of System.Drawing.Imaging.ColorAdjustType that specifies the category for which the 
             color-adjustment matrix is set.
        """
        pass

    def SetGamma(self, gamma, type=None):
        """
        SetGamma(self: ImageAttributes, gamma: Single, type: ColorAdjustType)
            Sets the gamma value for a specified category.
        
            gamma: The gamma correction value.
            type: An element of the System.Drawing.Imaging.ColorAdjustType enumeration that specifies the category 
             for which the gamma value is set.
        
        SetGamma(self: ImageAttributes, gamma: Single)
            Sets the gamma value for the default category.
        
            gamma: The gamma correction value.
        """
        pass

    def SetNoOp(self, type=None):
        """
        SetNoOp(self: ImageAttributes, type: ColorAdjustType)
            Turns off color adjustment for a specified category. You can call the 
             erload:System.Drawing.Imaging.ImageAttributes.ClearNoOp method to reinstate the color-adjustment 
             settings that were in place before the call to the 
             erload:System.Drawing.Imaging.ImageAttributes.SetNoOp method.
        
        
            type: An element of System.Drawing.Imaging.ColorAdjustType that specifies the category for which color 
             correction is turned off.
        
        SetNoOp(self: ImageAttributes)
            Turns off color adjustment for the default category. You can call the 
             erload:System.Drawing.Imaging.ImageAttributes.ClearNoOp method to reinstate the color-adjustment 
             settings that were in place before the call to the 
             erload:System.Drawing.Imaging.ImageAttributes.SetNoOp method.
        """
        pass

    def SetOutputChannel(self, flags, type=None):
        """
        SetOutputChannel(self: ImageAttributes, flags: ColorChannelFlag, type: ColorAdjustType)
            Sets the CMYK (cyan-magenta-yellow-black) output channel for a specified category.
        
            flags: An element of System.Drawing.Imaging.ColorChannelFlag that specifies the output channel.
            type: An element of System.Drawing.Imaging.ColorAdjustType that specifies the category for which the 
             output channel is set.
        
        SetOutputChannel(self: ImageAttributes, flags: ColorChannelFlag)
            Sets the CMYK (cyan-magenta-yellow-black) output channel for the default category.
        
            flags: An element of System.Drawing.Imaging.ColorChannelFlag that specifies the output channel.
        """
        pass

    def SetOutputChannelColorProfile(self, colorProfileFilename, type=None):
        """
        SetOutputChannelColorProfile(self: ImageAttributes, colorProfileFilename: str, type: ColorAdjustType)
            Sets the output channel color-profile file for a specified category.
        
            colorProfileFilename: The path name of a color-profile file. If the color-profile file is in the 
             %SystemRoot%\System32\Spool\Drivers\Color directory, this parameter can be the file name. 
             Otherwise, this parameter must be the fully qualified path name.
        
            type: An element of System.Drawing.Imaging.ColorAdjustType that specifies the category for which the 
             output channel color-profile file is set.
        
        SetOutputChannelColorProfile(self: ImageAttributes, colorProfileFilename: str)
            Sets the output channel color-profile file for the default category.
        
            colorProfileFilename: The path name of a color-profile file. If the color-profile file is in the 
             %SystemRoot%\System32\Spool\Drivers\Color directory, this parameter can be the file name. 
             Otherwise, this parameter must be the fully qualified path name.
        """
        pass

    def SetRemapTable(self, map, type=None):
        """
        SetRemapTable(self: ImageAttributes, map: Array[ColorMap], type: ColorAdjustType)
            Sets the color-remap table for a specified category.
        
            map: An array of color pairs of type System.Drawing.Imaging.ColorMap. Each color pair contains an 
             existing color (the first value) and the color that it will be mapped to (the second value).
        
            type: An element of System.Drawing.Imaging.ColorAdjustType that specifies the category for which the 
             color-remap table is set.
        
        SetRemapTable(self: ImageAttributes, map: Array[ColorMap])
            Sets the color-remap table for the default category.
        
            map: An array of color pairs of type System.Drawing.Imaging.ColorMap. Each color pair contains an 
             existing color (the first value) and the color that it will be mapped to (the second value).
        """
        pass

    def SetThreshold(self, threshold, type=None):
        """
        SetThreshold(self: ImageAttributes, threshold: Single, type: ColorAdjustType)
            Sets the threshold (transparency range) for a specified category.
        
            threshold: A threshold value from 0.0 to 1.0 that is used as a breakpoint to sort colors that will be 
             mapped to either a maximum or a minimum value.
        
            type: An element of System.Drawing.Imaging.ColorAdjustType that specifies the category for which the 
             color threshold is set.
        
        SetThreshold(self: ImageAttributes, threshold: Single)
            Sets the threshold (transparency range) for the default category.
        
            threshold: A real number that specifies the threshold value.
        """
        pass

    def SetWrapMode(self, mode, color=None, clamp=None):
        """
        SetWrapMode(self: ImageAttributes, mode: WrapMode, color: Color, clamp: bool)
            Sets the wrap mode and color used to decide how to tile a texture across a shape, or at shape 
             boundaries. A texture is tiled across a shape to fill it in when the texture is smaller than the 
             shape it is filling.
        
        
            mode: An element of System.Drawing.Drawing2D.WrapMode that specifies how repeated copies of an image 
             are used to tile an area.
        
            color: A color object that specifies the color of pixels outside of a rendered image. This color is 
             visible if the mode parameter is set to System.Drawing.Drawing2D.WrapMode.Clamp and the source 
             rectangle passed to erload:System.Drawing.Graphics.DrawImage is larger than the image itself.
        
            clamp: This parameter has no effect. Set it to false.
        SetWrapMode(self: ImageAttributes, mode: WrapMode, color: Color)
            Sets the wrap mode and color used to decide how to tile a texture across a shape, or at shape 
             boundaries. A texture is tiled across a shape to fill it in when the texture is smaller than the 
             shape it is filling.
        
        
            mode: An element of System.Drawing.Drawing2D.WrapMode that specifies how repeated copies of an image 
             are used to tile an area.
        
            color: An System.Drawing.Imaging.ImageAttributes object that specifies the color of pixels outside of a 
             rendered image. This color is visible if the mode parameter is set to 
             System.Drawing.Drawing2D.WrapMode.Clamp and the source rectangle passed to 
             erload:System.Drawing.Graphics.DrawImage is larger than the image itself.
        
        SetWrapMode(self: ImageAttributes, mode: WrapMode)
            Sets the wrap mode that is used to decide how to tile a texture across a shape, or at shape 
             boundaries. A texture is tiled across a shape to fill it in when the texture is smaller than the 
             shape it is filling.
        
        
            mode: An element of System.Drawing.Drawing2D.WrapMode that specifies how repeated copies of an image 
             are used to tile an area.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass


class ImageCodecFlags(Enum, IComparable, IFormattable, IConvertible):
    """
    Provides attributes of an image encoder/decoder (codec).
    
    enum (flags) ImageCodecFlags, values: BlockingDecode (32), Builtin (65536), Decoder (2), Encoder (1), SeekableEncode (16), SupportBitmap (4), SupportVector (8), System (131072), User (262144)
    """
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

    BlockingDecode = None
    Builtin = None
    Decoder = None
    Encoder = None
    SeekableEncode = None
    SupportBitmap = None
    SupportVector = None
    System = None
    User = None
    value__ = None


class ImageCodecInfo(object):
    """ The System.Drawing.Imaging.ImageCodecInfo class provides the necessary storage members and methods to retrieve all pertinent information about the installed image encoders and decoders (called codecs). Not inheritable. """
    @staticmethod
    def GetImageDecoders():
        """
        GetImageDecoders() -> Array[ImageCodecInfo]
        
            Returns an array of System.Drawing.Imaging.ImageCodecInfo objects that contain information about 
             the image decoders built into GDI+.
        
            Returns: An array of System.Drawing.Imaging.ImageCodecInfo objects. Each 
             System.Drawing.Imaging.ImageCodecInfo object in the array contains information about one of the 
             built-in image decoders.
        """
        pass

    @staticmethod
    def GetImageEncoders():
        """
        GetImageEncoders() -> Array[ImageCodecInfo]
        
            Returns an array of System.Drawing.Imaging.ImageCodecInfo objects that contain information about 
             the image encoders built into GDI+.
        
            Returns: An array of System.Drawing.Imaging.ImageCodecInfo objects. Each 
             System.Drawing.Imaging.ImageCodecInfo object in the array contains information about one of the 
             built-in image encoders.
        """
        pass

    Clsid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a System.Guid structure that contains a GUID that identifies a specific codec.

Get: Clsid(self: ImageCodecInfo) -> Guid

Set: Clsid(self: ImageCodecInfo) = value
"""

    CodecName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a string that contains the name of the codec.

Get: CodecName(self: ImageCodecInfo) -> str

Set: CodecName(self: ImageCodecInfo) = value
"""

    DllName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets string that contains the path name of the DLL that holds the codec. If the codec is not in a DLL, this pointer is null.

Get: DllName(self: ImageCodecInfo) -> str

Set: DllName(self: ImageCodecInfo) = value
"""

    FilenameExtension = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets string that contains the file name extension(s) used in the codec. The extensions are separated by semicolons.

Get: FilenameExtension(self: ImageCodecInfo) -> str

Set: FilenameExtension(self: ImageCodecInfo) = value
"""

    Flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets 32-bit value used to store additional information about the codec. This property returns a combination of flags from the System.Drawing.Imaging.ImageCodecFlags enumeration.

Get: Flags(self: ImageCodecInfo) -> ImageCodecFlags

Set: Flags(self: ImageCodecInfo) = value
"""

    FormatDescription = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a string that describes the codec's file format.

Get: FormatDescription(self: ImageCodecInfo) -> str

Set: FormatDescription(self: ImageCodecInfo) = value
"""

    FormatID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a System.Guid structure that contains a GUID that identifies the codec's format.

Get: FormatID(self: ImageCodecInfo) -> Guid

Set: FormatID(self: ImageCodecInfo) = value
"""

    MimeType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a string that contains the codec's Multipurpose Internet Mail Extensions (MIME) type.

Get: MimeType(self: ImageCodecInfo) -> str

Set: MimeType(self: ImageCodecInfo) = value
"""

    SignatureMasks = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a two dimensional array of bytes that can be used as a filter.

Get: SignatureMasks(self: ImageCodecInfo) -> Array[Array[Byte]]

Set: SignatureMasks(self: ImageCodecInfo) = value
"""

    SignaturePatterns = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a two dimensional array of bytes that represents the signature of the codec.

Get: SignaturePatterns(self: ImageCodecInfo) -> Array[Array[Byte]]

Set: SignaturePatterns(self: ImageCodecInfo) = value
"""

    Version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the version number of the codec.

Get: Version(self: ImageCodecInfo) -> int

Set: Version(self: ImageCodecInfo) = value
"""



class ImageFlags(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the attributes of the pixel data contained in an System.Drawing.Image object. The System.Drawing.Image.Flags property returns a member of this enumeration.
    
    enum (flags) ImageFlags, values: Caching (131072), ColorSpaceCmyk (32), ColorSpaceGray (64), ColorSpaceRgb (16), ColorSpaceYcbcr (128), ColorSpaceYcck (256), HasAlpha (2), HasRealDpi (4096), HasRealPixelSize (8192), HasTranslucent (4), None (0), PartiallyScalable (8), ReadOnly (65536), Scalable (1)
    """
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

    Caching = None
    ColorSpaceCmyk = None
    ColorSpaceGray = None
    ColorSpaceRgb = None
    ColorSpaceYcbcr = None
    ColorSpaceYcck = None
    HasAlpha = None
    HasRealDpi = None
    HasRealPixelSize = None
    HasTranslucent = None
    None = None
    PartiallyScalable = None
    ReadOnly = None
    Scalable = None
    value__ = None


class ImageFormat(object):
    """
    Specifies the file format of the image. Not inheritable.
    
    ImageFormat(guid: Guid)
    """
    def Equals(self, o):
        """
        Equals(self: ImageFormat, o: object) -> bool
        
            Returns a value that indicates whether the specified object is an 
             System.Drawing.Imaging.ImageFormat object that is equivalent to this 
             System.Drawing.Imaging.ImageFormat object.
        
        
            o: The object to test.
            Returns: true if o is an System.Drawing.Imaging.ImageFormat object that is equivalent to this 
             System.Drawing.Imaging.ImageFormat object; otherwise, false.
        """
        pass

    def GetHashCode(self):
        """
        GetHashCode(self: ImageFormat) -> int
        
            Returns a hash code value that represents this object.
            Returns: A hash code that represents this object.
        """
        pass

    def ToString(self):
        """
        ToString(self: ImageFormat) -> str
        
            Converts this System.Drawing.Imaging.ImageFormat object to a human-readable string.
            Returns: A string that represents this System.Drawing.Imaging.ImageFormat object.
        """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    @staticmethod # known case of __new__
    def __new__(self, guid):
        """ __new__(cls: type, guid: Guid) """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    Guid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Guid structure that represents this System.Drawing.Imaging.ImageFormat object.

Get: Guid(self: ImageFormat) -> Guid

"""


    Bmp = None
    Emf = None
    Exif = None
    Gif = None
    Icon = None
    Jpeg = None
    MemoryBmp = None
    Png = None
    Tiff = None
    Wmf = None


class ImageLockMode(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies flags that are passed to the flags parameter of the erload:System.Drawing.Bitmap.LockBits method. The erload:System.Drawing.Bitmap.LockBits method locks a portion of an image so that you can read or write the pixel data.
    
    enum ImageLockMode, values: ReadOnly (1), ReadWrite (3), UserInputBuffer (4), WriteOnly (2)
    """
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

    ReadOnly = None
    ReadWrite = None
    UserInputBuffer = None
    value__ = None
    WriteOnly = None


class Metafile(Image, ISerializable, ICloneable, IDisposable):
    """
    Defines a graphic metafile. A metafile contains records that describe a sequence of graphics operations that can be recorded (constructed) and played back (displayed). This class is not inheritable.
    
    Metafile(hmetafile: IntPtr, wmfHeader: WmfPlaceableFileHeader)
    Metafile(hmetafile: IntPtr, wmfHeader: WmfPlaceableFileHeader, deleteWmf: bool)
    Metafile(henhmetafile: IntPtr, deleteEmf: bool)
    Metafile(filename: str)
    Metafile(stream: Stream)
    Metafile(referenceHdc: IntPtr, emfType: EmfType)
    Metafile(referenceHdc: IntPtr, emfType: EmfType, description: str)
    Metafile(referenceHdc: IntPtr, frameRect: RectangleF)
    Metafile(referenceHdc: IntPtr, frameRect: RectangleF, frameUnit: MetafileFrameUnit)
    Metafile(referenceHdc: IntPtr, frameRect: RectangleF, frameUnit: MetafileFrameUnit, type: EmfType)
    Metafile(referenceHdc: IntPtr, frameRect: RectangleF, frameUnit: MetafileFrameUnit, type: EmfType, description: str)
    Metafile(referenceHdc: IntPtr, frameRect: Rectangle)
    Metafile(referenceHdc: IntPtr, frameRect: Rectangle, frameUnit: MetafileFrameUnit)
    Metafile(referenceHdc: IntPtr, frameRect: Rectangle, frameUnit: MetafileFrameUnit, type: EmfType)
    Metafile(referenceHdc: IntPtr, frameRect: Rectangle, frameUnit: MetafileFrameUnit, type: EmfType, desc: str)
    Metafile(fileName: str, referenceHdc: IntPtr)
    Metafile(fileName: str, referenceHdc: IntPtr, type: EmfType)
    Metafile(fileName: str, referenceHdc: IntPtr, type: EmfType, description: str)
    Metafile(fileName: str, referenceHdc: IntPtr, frameRect: RectangleF)
    Metafile(fileName: str, referenceHdc: IntPtr, frameRect: RectangleF, frameUnit: MetafileFrameUnit)
    Metafile(fileName: str, referenceHdc: IntPtr, frameRect: RectangleF, frameUnit: MetafileFrameUnit, type: EmfType)
    Metafile(fileName: str, referenceHdc: IntPtr, frameRect: RectangleF, frameUnit: MetafileFrameUnit, desc: str)
    Metafile(fileName: str, referenceHdc: IntPtr, frameRect: RectangleF, frameUnit: MetafileFrameUnit, type: EmfType, description: str)
    Metafile(fileName: str, referenceHdc: IntPtr, frameRect: Rectangle)
    Metafile(fileName: str, referenceHdc: IntPtr, frameRect: Rectangle, frameUnit: MetafileFrameUnit)
    Metafile(fileName: str, referenceHdc: IntPtr, frameRect: Rectangle, frameUnit: MetafileFrameUnit, type: EmfType)
    Metafile(fileName: str, referenceHdc: IntPtr, frameRect: Rectangle, frameUnit: MetafileFrameUnit, description: str)
    Metafile(fileName: str, referenceHdc: IntPtr, frameRect: Rectangle, frameUnit: MetafileFrameUnit, type: EmfType, description: str)
    Metafile(stream: Stream, referenceHdc: IntPtr)
    Metafile(stream: Stream, referenceHdc: IntPtr, type: EmfType)
    Metafile(stream: Stream, referenceHdc: IntPtr, type: EmfType, description: str)
    Metafile(stream: Stream, referenceHdc: IntPtr, frameRect: RectangleF)
    Metafile(stream: Stream, referenceHdc: IntPtr, frameRect: RectangleF, frameUnit: MetafileFrameUnit)
    Metafile(stream: Stream, referenceHdc: IntPtr, frameRect: RectangleF, frameUnit: MetafileFrameUnit, type: EmfType)
    Metafile(stream: Stream, referenceHdc: IntPtr, frameRect: RectangleF, frameUnit: MetafileFrameUnit, type: EmfType, description: str)
    Metafile(stream: Stream, referenceHdc: IntPtr, frameRect: Rectangle)
    Metafile(stream: Stream, referenceHdc: IntPtr, frameRect: Rectangle, frameUnit: MetafileFrameUnit)
    Metafile(stream: Stream, referenceHdc: IntPtr, frameRect: Rectangle, frameUnit: MetafileFrameUnit, type: EmfType)
    Metafile(stream: Stream, referenceHdc: IntPtr, frameRect: Rectangle, frameUnit: MetafileFrameUnit, type: EmfType, description: str)
    """
    def Dispose(self):
        """
        Dispose(self: Image, disposing: bool)
            Releases the unmanaged resources used by the System.Drawing.Image and optionally releases the 
             managed resources.
        
        
            disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
        """
        pass

    def GetHenhmetafile(self):
        """
        GetHenhmetafile(self: Metafile) -> IntPtr
        
            Returns a Windows handle to an enhanced System.Drawing.Imaging.Metafile.
            Returns: A Windows handle to this enhanced System.Drawing.Imaging.Metafile.
        """
        pass

    @staticmethod
    def GetMetafileHeader(*__args):
        """
        GetMetafileHeader(stream: Stream) -> MetafileHeader
        
            Returns the System.Drawing.Imaging.MetafileHeader associated with the specified 
             System.Drawing.Imaging.Metafile.
        
        
            stream: A System.IO.Stream containing the System.Drawing.Imaging.Metafile for which a header is 
             retrieved.
        
            Returns: The System.Drawing.Imaging.MetafileHeader associated with the specified 
             System.Drawing.Imaging.Metafile.
        
        GetMetafileHeader(self: Metafile) -> MetafileHeader
        
            Returns the System.Drawing.Imaging.MetafileHeader associated with this 
             System.Drawing.Imaging.Metafile.
        
            Returns: The System.Drawing.Imaging.MetafileHeader associated with this System.Drawing.Imaging.Metafile.
        GetMetafileHeader(fileName: str) -> MetafileHeader
        
            Returns the System.Drawing.Imaging.MetafileHeader associated with the specified 
             System.Drawing.Imaging.Metafile.
        
        
            fileName: A System.String containing the name of the System.Drawing.Imaging.Metafile for which a header is 
             retrieved.
        
            Returns: The System.Drawing.Imaging.MetafileHeader associated with the specified 
             System.Drawing.Imaging.Metafile.
        
        GetMetafileHeader(hmetafile: IntPtr, wmfHeader: WmfPlaceableFileHeader) -> MetafileHeader
        
            Returns the System.Drawing.Imaging.MetafileHeader associated with the specified 
             System.Drawing.Imaging.Metafile.
        
        
            hmetafile: The handle to the System.Drawing.Imaging.Metafile for which to return a header.
            wmfHeader: A System.Drawing.Imaging.WmfPlaceableFileHeader.
            Returns: The System.Drawing.Imaging.MetafileHeader associated with the specified 
             System.Drawing.Imaging.Metafile.
        
        GetMetafileHeader(henhmetafile: IntPtr) -> MetafileHeader
        
            Returns the System.Drawing.Imaging.MetafileHeader associated with the specified 
             System.Drawing.Imaging.Metafile.
        
        
            henhmetafile: The handle to the enhanced System.Drawing.Imaging.Metafile for which a header is returned.
            Returns: The System.Drawing.Imaging.MetafileHeader associated with the specified 
             System.Drawing.Imaging.Metafile.
        """
        pass

    def MemberwiseClone(self, *args): #cannot find CLR method
        """
        MemberwiseClone(self: MarshalByRefObject, cloneIdentity: bool) -> MarshalByRefObject
        
            Creates a shallow copy of the current System.MarshalByRefObject object.
        
            cloneIdentity: false to delete the current System.MarshalByRefObject object's identity, which will cause the 
             object to be assigned a new identity when it is marshaled across a remoting boundary. A value of 
             false is usually appropriate. true to copy the current System.MarshalByRefObject object's 
             identity to its clone, which will cause remoting client calls to be routed to the remote server 
             object.
        
            Returns: A shallow copy of the current System.MarshalByRefObject object.
        MemberwiseClone(self: object) -> object
        
            Creates a shallow copy of the current System.Object.
            Returns: A shallow copy of the current System.Object.
        """
        pass

    def PlayRecord(self, recordType, flags, dataSize, data):
        """
        PlayRecord(self: Metafile, recordType: EmfPlusRecordType, flags: int, dataSize: int, data: Array[Byte])
            Plays an individual metafile record.
        
            recordType: Element of the System.Drawing.Imaging.EmfPlusRecordType that specifies the type of metafile 
             record being played.
        
            flags: A set of flags that specify attributes of the record.
            dataSize: The number of bytes in the record data.
            data: An array of bytes that contains the record data.
        """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """
        __enter__(self: IDisposable) -> object
        
            Provides the implementation of __enter__ for objects which implement IDisposable.
        """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """
        __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object)
            Provides the implementation of __exit__ for objects which implement IDisposable.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type, hmetafile: IntPtr, wmfHeader: WmfPlaceableFileHeader)
        __new__(cls: type, hmetafile: IntPtr, wmfHeader: WmfPlaceableFileHeader, deleteWmf: bool)
        __new__(cls: type, henhmetafile: IntPtr, deleteEmf: bool)
        __new__(cls: type, filename: str)
        __new__(cls: type, stream: Stream)
        __new__(cls: type, referenceHdc: IntPtr, emfType: EmfType)
        __new__(cls: type, referenceHdc: IntPtr, emfType: EmfType, description: str)
        __new__(cls: type, referenceHdc: IntPtr, frameRect: RectangleF)
        __new__(cls: type, referenceHdc: IntPtr, frameRect: RectangleF, frameUnit: MetafileFrameUnit)
        __new__(cls: type, referenceHdc: IntPtr, frameRect: RectangleF, frameUnit: MetafileFrameUnit, type: EmfType)
        __new__(cls: type, referenceHdc: IntPtr, frameRect: RectangleF, frameUnit: MetafileFrameUnit, type: EmfType, description: str)
        __new__(cls: type, referenceHdc: IntPtr, frameRect: Rectangle)
        __new__(cls: type, referenceHdc: IntPtr, frameRect: Rectangle, frameUnit: MetafileFrameUnit)
        __new__(cls: type, referenceHdc: IntPtr, frameRect: Rectangle, frameUnit: MetafileFrameUnit, type: EmfType)
        __new__(cls: type, referenceHdc: IntPtr, frameRect: Rectangle, frameUnit: MetafileFrameUnit, type: EmfType, desc: str)
        __new__(cls: type, fileName: str, referenceHdc: IntPtr)
        __new__(cls: type, fileName: str, referenceHdc: IntPtr, type: EmfType)
        __new__(cls: type, fileName: str, referenceHdc: IntPtr, type: EmfType, description: str)
        __new__(cls: type, fileName: str, referenceHdc: IntPtr, frameRect: RectangleF)
        __new__(cls: type, fileName: str, referenceHdc: IntPtr, frameRect: RectangleF, frameUnit: MetafileFrameUnit)
        __new__(cls: type, fileName: str, referenceHdc: IntPtr, frameRect: RectangleF, frameUnit: MetafileFrameUnit, type: EmfType)
        __new__(cls: type, fileName: str, referenceHdc: IntPtr, frameRect: RectangleF, frameUnit: MetafileFrameUnit, desc: str)
        __new__(cls: type, fileName: str, referenceHdc: IntPtr, frameRect: RectangleF, frameUnit: MetafileFrameUnit, type: EmfType, description: str)
        __new__(cls: type, fileName: str, referenceHdc: IntPtr, frameRect: Rectangle)
        __new__(cls: type, fileName: str, referenceHdc: IntPtr, frameRect: Rectangle, frameUnit: MetafileFrameUnit)
        __new__(cls: type, fileName: str, referenceHdc: IntPtr, frameRect: Rectangle, frameUnit: MetafileFrameUnit, type: EmfType)
        __new__(cls: type, fileName: str, referenceHdc: IntPtr, frameRect: Rectangle, frameUnit: MetafileFrameUnit, description: str)
        __new__(cls: type, fileName: str, referenceHdc: IntPtr, frameRect: Rectangle, frameUnit: MetafileFrameUnit, type: EmfType, description: str)
        __new__(cls: type, stream: Stream, referenceHdc: IntPtr)
        __new__(cls: type, stream: Stream, referenceHdc: IntPtr, type: EmfType)
        __new__(cls: type, stream: Stream, referenceHdc: IntPtr, type: EmfType, description: str)
        __new__(cls: type, stream: Stream, referenceHdc: IntPtr, frameRect: RectangleF)
        __new__(cls: type, stream: Stream, referenceHdc: IntPtr, frameRect: RectangleF, frameUnit: MetafileFrameUnit)
        __new__(cls: type, stream: Stream, referenceHdc: IntPtr, frameRect: RectangleF, frameUnit: MetafileFrameUnit, type: EmfType)
        __new__(cls: type, stream: Stream, referenceHdc: IntPtr, frameRect: RectangleF, frameUnit: MetafileFrameUnit, type: EmfType, description: str)
        __new__(cls: type, stream: Stream, referenceHdc: IntPtr, frameRect: Rectangle)
        __new__(cls: type, stream: Stream, referenceHdc: IntPtr, frameRect: Rectangle, frameUnit: MetafileFrameUnit)
        __new__(cls: type, stream: Stream, referenceHdc: IntPtr, frameRect: Rectangle, frameUnit: MetafileFrameUnit, type: EmfType)
        __new__(cls: type, stream: Stream, referenceHdc: IntPtr, frameRect: Rectangle, frameUnit: MetafileFrameUnit, type: EmfType, description: str)
        """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class MetafileFrameUnit(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the unit of measurement for the rectangle used to size and position a metafile. This is specified during the creation of the System.Drawing.Imaging.Metafile object.
    
    enum MetafileFrameUnit, values: Document (5), GdiCompatible (7), Inch (4), Millimeter (6), Pixel (2), Point (3)
    """
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

    Document = None
    GdiCompatible = None
    Inch = None
    Millimeter = None
    Pixel = None
    Point = None
    value__ = None


class MetafileHeader(object):
    """ Contains attributes of an associated System.Drawing.Imaging.Metafile. Not inheritable. """
    def IsDisplay(self):
        """
        IsDisplay(self: MetafileHeader) -> bool
        
            Returns a value that indicates whether the associated System.Drawing.Imaging.Metafile is device 
             dependent.
        
            Returns: true if the associated System.Drawing.Imaging.Metafile is device dependent; otherwise, false.
        """
        pass

    def IsEmf(self):
        """
        IsEmf(self: MetafileHeader) -> bool
        
            Returns a value that indicates whether the associated System.Drawing.Imaging.Metafile is in the 
             Windows enhanced metafile format.
        
            Returns: true if the associated System.Drawing.Imaging.Metafile is in the Windows enhanced metafile 
             format; otherwise, false.
        """
        pass

    def IsEmfOrEmfPlus(self):
        """
        IsEmfOrEmfPlus(self: MetafileHeader) -> bool
        
            Returns a value that indicates whether the associated System.Drawing.Imaging.Metafile is in the 
             Windows enhanced metafile format or the Windows enhanced metafile plus format.
        
            Returns: true if the associated System.Drawing.Imaging.Metafile is in the Windows enhanced metafile 
             format or the Windows enhanced metafile plus format; otherwise, false.
        """
        pass

    def IsEmfPlus(self):
        """
        IsEmfPlus(self: MetafileHeader) -> bool
        
            Returns a value that indicates whether the associated System.Drawing.Imaging.Metafile is in the 
             Windows enhanced metafile plus format.
        
            Returns: true if the associated System.Drawing.Imaging.Metafile is in the Windows enhanced metafile plus 
             format; otherwise, false.
        """
        pass

    def IsEmfPlusDual(self):
        """
        IsEmfPlusDual(self: MetafileHeader) -> bool
        
            Returns a value that indicates whether the associated System.Drawing.Imaging.Metafile is in the 
             Dual enhanced metafile format. This format supports both the enhanced and the enhanced plus 
             format.
        
            Returns: true if the associated System.Drawing.Imaging.Metafile is in the Dual enhanced metafile format; 
             otherwise, false.
        """
        pass

    def IsEmfPlusOnly(self):
        """
        IsEmfPlusOnly(self: MetafileHeader) -> bool
        
            Returns a value that indicates whether the associated System.Drawing.Imaging.Metafile supports 
             only the Windows enhanced metafile plus format.
        
            Returns: true if the associated System.Drawing.Imaging.Metafile supports only the Windows enhanced 
             metafile plus format; otherwise, false.
        """
        pass

    def IsWmf(self):
        """
        IsWmf(self: MetafileHeader) -> bool
        
            Returns a value that indicates whether the associated System.Drawing.Imaging.Metafile is in the 
             Windows metafile format.
        
            Returns: true if the associated System.Drawing.Imaging.Metafile is in the Windows metafile format; 
             otherwise, false.
        """
        pass

    def IsWmfPlaceable(self):
        """
        IsWmfPlaceable(self: MetafileHeader) -> bool
        
            Returns a value that indicates whether the associated System.Drawing.Imaging.Metafile is in the 
             Windows placeable metafile format.
        
            Returns: true if the associated System.Drawing.Imaging.Metafile is in the Windows placeable metafile 
             format; otherwise, false.
        """
        pass

    Bounds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets a System.Drawing.Rectangle that bounds the associated System.Drawing.Imaging.Metafile.

Get: Bounds(self: MetafileHeader) -> Rectangle

"""

    DpiX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the horizontal resolution, in dots per inch, of the associated System.Drawing.Imaging.Metafile.

Get: DpiX(self: MetafileHeader) -> Single

"""

    DpiY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the vertical resolution, in dots per inch, of the associated System.Drawing.Imaging.Metafile.

Get: DpiY(self: MetafileHeader) -> Single

"""

    EmfPlusHeaderSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the size, in bytes, of the enhanced metafile plus header file.

Get: EmfPlusHeaderSize(self: MetafileHeader) -> int

"""

    LogicalDpiX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the logical horizontal resolution, in dots per inch, of the associated System.Drawing.Imaging.Metafile.

Get: LogicalDpiX(self: MetafileHeader) -> int

"""

    LogicalDpiY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the logical vertical resolution, in dots per inch, of the associated System.Drawing.Imaging.Metafile.

Get: LogicalDpiY(self: MetafileHeader) -> int

"""

    MetafileSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the size, in bytes, of the associated System.Drawing.Imaging.Metafile.

Get: MetafileSize(self: MetafileHeader) -> int

"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the type of the associated System.Drawing.Imaging.Metafile.

Get: Type(self: MetafileHeader) -> MetafileType

"""

    Version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the version number of the associated System.Drawing.Imaging.Metafile.

Get: Version(self: MetafileHeader) -> int

"""

    WmfHeader = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the Windows metafile (WMF) header file for the associated System.Drawing.Imaging.Metafile.

Get: WmfHeader(self: MetafileHeader) -> MetaHeader

"""



class MetafileType(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies types of metafiles. The System.Drawing.Imaging.MetafileHeader.Type property returns a member of this enumeration.
    
    enum MetafileType, values: Emf (3), EmfPlusDual (5), EmfPlusOnly (4), Invalid (0), Wmf (1), WmfPlaceable (2)
    """
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

    Emf = None
    EmfPlusDual = None
    EmfPlusOnly = None
    Invalid = None
    value__ = None
    Wmf = None
    WmfPlaceable = None


class MetaHeader(object):
    """
    Contains information about a windows-format (WMF) metafile.
    
    MetaHeader()
    """
    HeaderSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the size, in bytes, of the header file.

Get: HeaderSize(self: MetaHeader) -> Int16

Set: HeaderSize(self: MetaHeader) = value
"""

    MaxRecord = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the size, in bytes, of the largest record in the associated System.Drawing.Imaging.Metafile object.

Get: MaxRecord(self: MetaHeader) -> int

Set: MaxRecord(self: MetaHeader) = value
"""

    NoObjects = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the maximum number of objects that exist in the System.Drawing.Imaging.Metafile object at the same time.

Get: NoObjects(self: MetaHeader) -> Int16

Set: NoObjects(self: MetaHeader) = value
"""

    NoParameters = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Not used. Always returns 0.

Get: NoParameters(self: MetaHeader) -> Int16

Set: NoParameters(self: MetaHeader) = value
"""

    Size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the size, in bytes, of the associated System.Drawing.Imaging.Metafile object.

Get: Size(self: MetaHeader) -> int

Set: Size(self: MetaHeader) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the type of the associated System.Drawing.Imaging.Metafile object.

Get: Type(self: MetaHeader) -> Int16

Set: Type(self: MetaHeader) = value
"""

    Version = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the version number of the header format.

Get: Version(self: MetaHeader) -> Int16

Set: Version(self: MetaHeader) = value
"""



class PaletteFlags(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the type of color data in the system palette. The data can be color data with alpha, grayscale data only, or halftone data.
    
    enum (flags) PaletteFlags, values: GrayScale (2), Halftone (4), HasAlpha (1)
    """
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

    GrayScale = None
    Halftone = None
    HasAlpha = None
    value__ = None


class PixelFormat(Enum, IComparable, IFormattable, IConvertible):
    """
    Specifies the format of the color data for each pixel in the image.
    
    enum PixelFormat, values: Alpha (262144), Canonical (2097152), DontCare (0), Extended (1048576), Format16bppArgb1555 (397319), Format16bppGrayScale (1052676), Format16bppRgb555 (135173), Format16bppRgb565 (135174), Format1bppIndexed (196865), Format24bppRgb (137224), Format32bppArgb (2498570), Format32bppPArgb (925707), Format32bppRgb (139273), Format48bppRgb (1060876), Format4bppIndexed (197634), Format64bppArgb (3424269), Format64bppPArgb (1851406), Format8bppIndexed (198659), Gdi (131072), Indexed (65536), Max (15), PAlpha (524288), Undefined (0)
    """
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

    Alpha = None
    Canonical = None
    DontCare = None
    Extended = None
    Format16bppArgb1555 = None
    Format16bppGrayScale = None
    Format16bppRgb555 = None
    Format16bppRgb565 = None
    Format1bppIndexed = None
    Format24bppRgb = None
    Format32bppArgb = None
    Format32bppPArgb = None
    Format32bppRgb = None
    Format48bppRgb = None
    Format4bppIndexed = None
    Format64bppArgb = None
    Format64bppPArgb = None
    Format8bppIndexed = None
    Gdi = None
    Indexed = None
    Max = None
    PAlpha = None
    Undefined = None
    value__ = None


class PlayRecordCallback(MulticastDelegate, ICloneable, ISerializable):
    """
    This delegate is not used. For an example of enumerating the records of a metafile, see System.Drawing.Graphics.EnumerateMetafile(System.Drawing.Imaging.Metafile,System.Drawing.Point,System.Drawing.Graphics.EnumerateMetafileProc).
    
    PlayRecordCallback(object: object, method: IntPtr)
    """
    def BeginInvoke(self, recordType, flags, dataSize, recordData, callback, object):
        """ BeginInvoke(self: PlayRecordCallback, recordType: EmfPlusRecordType, flags: int, dataSize: int, recordData: IntPtr, callback: AsyncCallback, object: object) -> IAsyncResult """
        pass

    def CombineImpl(self, *args): #cannot find CLR method
        """
        CombineImpl(self: MulticastDelegate, follow: Delegate) -> Delegate
        
            Combines this System.Delegate with the specified System.Delegate to form a new delegate.
        
            follow: The delegate to combine with this delegate.
            Returns: A delegate that is the new root of the System.MulticastDelegate invocation list.
        """
        pass

    def DynamicInvokeImpl(self, *args): #cannot find CLR method
        """
        DynamicInvokeImpl(self: Delegate, args: Array[object]) -> object
        
            Dynamically invokes (late-bound) the method represented by the current delegate.
        
            args: An array of objects that are the arguments to pass to the method represented by the current 
             delegate.-or- null, if the method represented by the current delegate does not require 
             arguments.
        
            Returns: The object returned by the method represented by the delegate.
        """
        pass

    def EndInvoke(self, result):
        """ EndInvoke(self: PlayRecordCallback, result: IAsyncResult) """
        pass

    def GetMethodImpl(self, *args): #cannot find CLR method
        """
        GetMethodImpl(self: MulticastDelegate) -> MethodInfo
        
            Returns a static method represented by the current System.MulticastDelegate.
            Returns: A static method represented by the current System.MulticastDelegate.
        """
        pass

    def Invoke(self, recordType, flags, dataSize, recordData):
        """ Invoke(self: PlayRecordCallback, recordType: EmfPlusRecordType, flags: int, dataSize: int, recordData: IntPtr) """
        pass

    def RemoveImpl(self, *args): #cannot find CLR method
        """
        RemoveImpl(self: MulticastDelegate, value: Delegate) -> Delegate
        
            Removes an element from the invocation list of this System.MulticastDelegate that is equal to 
             the specified delegate.
        
        
            value: The delegate to search for in the invocation list.
            Returns: If value is found in the invocation list for this instance, then a new System.Delegate without 
             value in its invocation list; otherwise, this instance with its original invocation list.
        """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, object, method):
        """ __new__(cls: type, object: object, method: IntPtr) """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass


class PropertyItem(object):
    """ Encapsulates a metadata property to be included in an image file. Not inheritable. """
    Id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the ID of the property.

Get: Id(self: PropertyItem) -> int

Set: Id(self: PropertyItem) = value
"""

    Len = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the length (in bytes) of the System.Drawing.Imaging.PropertyItem.Value property.

Get: Len(self: PropertyItem) -> int

Set: Len(self: PropertyItem) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets an integer that defines the type of data contained in the System.Drawing.Imaging.PropertyItem.Value property.

Get: Type(self: PropertyItem) -> Int16

Set: Type(self: PropertyItem) = value
"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the value of the property item.

Get: Value(self: PropertyItem) -> Array[Byte]

Set: Value(self: PropertyItem) = value
"""



class WmfPlaceableFileHeader(object):
    """
    Defines a placeable metafile. Not inheritable.
    
    WmfPlaceableFileHeader()
    """
    BboxBottom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the y-coordinate of the lower-right corner of the bounding rectangle of the metafile image on the output device.

Get: BboxBottom(self: WmfPlaceableFileHeader) -> Int16

Set: BboxBottom(self: WmfPlaceableFileHeader) = value
"""

    BboxLeft = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the x-coordinate of the upper-left corner of the bounding rectangle of the metafile image on the output device.

Get: BboxLeft(self: WmfPlaceableFileHeader) -> Int16

Set: BboxLeft(self: WmfPlaceableFileHeader) = value
"""

    BboxRight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the x-coordinate of the lower-right corner of the bounding rectangle of the metafile image on the output device.

Get: BboxRight(self: WmfPlaceableFileHeader) -> Int16

Set: BboxRight(self: WmfPlaceableFileHeader) = value
"""

    BboxTop = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the y-coordinate of the upper-left corner of the bounding rectangle of the metafile image on the output device.

Get: BboxTop(self: WmfPlaceableFileHeader) -> Int16

Set: BboxTop(self: WmfPlaceableFileHeader) = value
"""

    Checksum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the checksum value for the previous ten WORD s in the header.

Get: Checksum(self: WmfPlaceableFileHeader) -> Int16

Set: Checksum(self: WmfPlaceableFileHeader) = value
"""

    Hmf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the handle of the metafile in memory.

Get: Hmf(self: WmfPlaceableFileHeader) -> Int16

Set: Hmf(self: WmfPlaceableFileHeader) = value
"""

    Inch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the number of twips per inch.

Get: Inch(self: WmfPlaceableFileHeader) -> Int16

Set: Inch(self: WmfPlaceableFileHeader) = value
"""

    Key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets a value indicating the presence of a placeable metafile header.

Get: Key(self: WmfPlaceableFileHeader) -> int

Set: Key(self: WmfPlaceableFileHeader) = value
"""

    Reserved = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reserved. Do not use.

Get: Reserved(self: WmfPlaceableFileHeader) -> int

Set: Reserved(self: WmfPlaceableFileHeader) = value
"""



