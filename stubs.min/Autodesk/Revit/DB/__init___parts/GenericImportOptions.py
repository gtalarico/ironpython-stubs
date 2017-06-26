class GenericImportOptions(object):
    """ Generic Import options. """
    RefPoint = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Reference point (in Revit) to which the image is going to be inserted.

Get: RefPoint(self: GenericImportOptions) -> XYZ

Set: RefPoint(self: GenericImportOptions) = value
"""


