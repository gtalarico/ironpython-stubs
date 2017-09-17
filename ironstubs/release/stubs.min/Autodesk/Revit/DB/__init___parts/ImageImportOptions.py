class ImageImportOptions(GenericImportOptions):
 """
 Options used to import specific image formats and place an instance of them on a view or sheet.
 
 ImageImportOptions()
 """
 Placement=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies which point of the image will be aligned to the placement point Autodesk.Revit.DB.GenericImportOptions.RefPoint.

Get: Placement(self: ImageImportOptions) -> BoxPlacement

Set: Placement(self: ImageImportOptions)=value
"""

 Resolution=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Resolution to use (in dpi) for the image to be imported.

Get: Resolution(self: ImageImportOptions) -> UInt16

Set: Resolution(self: ImageImportOptions)=value
"""


