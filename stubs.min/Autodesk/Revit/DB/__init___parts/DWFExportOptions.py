class DWFExportOptions(CADExportOptions):
    """
    DWF Export options.
    
    DWFExportOptions()
    """
    CropBoxVisible = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether to export crop box.

Get: CropBoxVisible(self: DWFExportOptions) -> bool

Set: CropBoxVisible(self: DWFExportOptions) = value
"""

    ExportingAreas = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether to also export areas and rooms' geometry.

Get: ExportingAreas(self: DWFExportOptions) -> bool

Set: ExportingAreas(self: DWFExportOptions) = value
"""

    ExportObjectData = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether to include properties associated with elements.

Get: ExportObjectData(self: DWFExportOptions) -> bool

Set: ExportObjectData(self: DWFExportOptions) = value
"""

    ExportTexture = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether to export texture.

Get: ExportTexture(self: DWFExportOptions) -> bool

Set: ExportTexture(self: DWFExportOptions) = value
"""

    ImageFormat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Controls the compression level of images embedded.

Get: ImageFormat(self: DWFExportOptions) -> DWFImageFormat

Set: ImageFormat(self: DWFExportOptions) = value
"""

    ImageQuality = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Image quality level when compressed raster format(JPEG) is used.

Get: ImageQuality(self: DWFExportOptions) -> DWFImageQuality

Set: ImageQuality(self: DWFExportOptions) = value
"""

    MergedViews = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether to merge all views in one file.

Get: MergedViews(self: DWFExportOptions) -> bool

Set: MergedViews(self: DWFExportOptions) = value
"""

    PaperFormat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Standard paper format.

Get: PaperFormat(self: DWFExportOptions) -> ExportPaperFormat

Set: PaperFormat(self: DWFExportOptions) = value
"""

    PortraitLayout = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Paper orientation - Portrait/Landscape.

Get: PortraitLayout(self: DWFExportOptions) -> bool

Set: PortraitLayout(self: DWFExportOptions) = value
"""

    StopOnError = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether export process should stop when a view fails to export.

Get: StopOnError(self: DWFExportOptions) -> bool

Set: StopOnError(self: DWFExportOptions) = value
"""


