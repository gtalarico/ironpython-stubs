class DockablePaneId(GuidEnum):
    """
    Identifier for a pane that participates in the Revit docking window system.
    
    DockablePaneId(guid: Guid)
    """
    @staticmethod # known case of __new__
    def __new__(self, guid):
        """ __new__(cls: type, guid: Guid) """
        pass

