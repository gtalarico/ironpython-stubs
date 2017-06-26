class BuildingSiteExportOptions(object):
    """
    Building Site Export options.
    
    BuildingSiteExportOptions()
    """
    AreaPerPerson = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Custom value for Area Per Person value.

Get: AreaPerPerson(self: BuildingSiteExportOptions) -> float

Set: AreaPerPerson(self: BuildingSiteExportOptions) = value
"""

    PropertyLine = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Optional property Line to export; it may be ll.

Get: PropertyLine(self: BuildingSiteExportOptions) -> PropertyLine

Set: PropertyLine(self: BuildingSiteExportOptions) = value
"""

    PropertyLineOffset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Property Line Offset. Default is 0.0.

Get: PropertyLineOffset(self: BuildingSiteExportOptions) -> float

Set: PropertyLineOffset(self: BuildingSiteExportOptions) = value
"""

    TotalGrossArea = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Custom value for the total area.

Get: TotalGrossArea(self: BuildingSiteExportOptions) -> float

Set: TotalGrossArea(self: BuildingSiteExportOptions) = value
"""

    TotalOccupancy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Custom value for the total occupancy.

Get: TotalOccupancy(self: BuildingSiteExportOptions) -> int

Set: TotalOccupancy(self: BuildingSiteExportOptions) = value
"""


