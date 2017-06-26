class NumberingSchemaType(GuidEnum):
    """
    A type for identifying a Autodesk.Revit.DB.NumberingSchema of a particular kind.
    
    NumberingSchemaType(guid: Guid)
    """
    @staticmethod # known case of __new__
    def __new__(self, guid):
        """ __new__(cls: type, guid: Guid) """
        pass

