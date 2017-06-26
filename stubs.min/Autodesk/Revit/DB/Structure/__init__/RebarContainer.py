class RebarContainer(Element, IDisposable, IEnumerable[RebarContainerItem], IEnumerable):
    """ An object that represents an Rebar Container Element within the Autodesk Revit project. """
    def AppendItemFromCurves(self, style, barType, startHook, endHook, normal, curves, startHookOrient, endHookOrient, useExistingShapeIfPossible, createNewShape):
        """ AppendItemFromCurves(self: RebarContainer, style: RebarStyle, barType: RebarBarType, startHook: RebarHookType, endHook: RebarHookType, normal: XYZ, curves: IList[Curve], startHookOrient: RebarHookOrientation, endHookOrient: RebarHookOrientation, useExistingShapeIfPossible: bool, createNewShape: bool) -> RebarContainerItem """
        pass

    def AppendItemFromCurvesAndShape(self, rebarShape, barType, startHook, endHook, normal, curves, startHookOrient, endHookOrient):
        """ AppendItemFromCurvesAndShape(self: RebarContainer, rebarShape: RebarShape, barType: RebarBarType, startHook: RebarHookType, endHook: RebarHookType, normal: XYZ, curves: IList[Curve], startHookOrient: RebarHookOrientation, endHookOrient: RebarHookOrientation) -> RebarContainerItem """
        pass

    def AppendItemFromRebar(self, rebar):
        """
        AppendItemFromRebar(self: RebarContainer, rebar: Rebar) -> RebarContainerItem
        
            Appends an Item to the RebarContainer. Fills its data on base of the Rebar.
        
            rebar: The Rebar.
            Returns: The Rebar Container Item.
        """
        pass

    def AppendItemFromRebarShape(self, rebarShape, barType, origin, xVector, yVector):
        """
        AppendItemFromRebarShape(self: RebarContainer, rebarShape: RebarShape, barType: RebarBarType, origin: XYZ, xVector: XYZ, yVector: XYZ) -> RebarContainerItem
        
            Appends an Item to the RebarContainer. Fills its data on base of the Rebar.
        
            rebarShape: A RebarShape element that defines the shape of the rebar.
            barType: A RebarBarType element that defines bar diameter, bend radius and material of 
             the rebar.
        
            origin: The lower-left corner of the shape's bounding box will be placed at this point 
             in the project.
        
            xVector: The x-axis in the shape definition will be mapped to this direction in the 
             project.
        
            yVector: The y-axis in the shape definition will be mapped to this direction in the 
             project.
        
            Returns: The Rebar Container Item.
        """
        pass

    def CanApplyPresentationMode(self, dBView):
        """
        CanApplyPresentationMode(self: RebarContainer, dBView: View) -> bool
        
            Checks if a presentation mode can be applied for this RebarContainer in the 
             given view.
        
        
            dBView: The view in which presentation mode will be applied.
            Returns: True if presentation mode can be applied for this view, false otherwise.
        """
        pass

    def ClearItems(self):
        """
        ClearItems(self: RebarContainer)
            Clears all the Items stored in this Rebar Container element.
        """
        pass

    def Contains(self, pItem):
        """
        Contains(self: RebarContainer, pItem: RebarContainerItem) -> bool
        
            Checks if the RebarContainer has this item as one of its members.
        
            pItem: The item to be checked if RebarContainer has it as one of its members
            Returns: True if RebarContainer has this item as one of its members, false otherwise.
        """
        pass

    @staticmethod
    def Create(aDoc, hostElement, rebarContainerTypeId):
        """
        Create(aDoc: Document, hostElement: Element, rebarContainerTypeId: ElementId) -> RebarContainer
        
            Creates a new instance of a Rebar Container element within the project.
        
            aDoc: A document.
            hostElement: The element that will host the RebarContainer.
            rebarContainerTypeId: The id of the RebarContainerType.
            Returns: The newly created Rebar Container instance.
        """
        pass

    def Dispose(self):
        """ Dispose(self: Element, A_0: bool) """
        pass

    def getBoundingBox(self, *args): #cannot find CLR method
        """ getBoundingBox(self: Element, view: View) -> BoundingBoxXYZ """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: RebarContainer) -> IEnumerator[RebarContainerItem]
        
            Returns an enumerator that iterates through a collection.
            Returns: An IEnumerator object that can be used to iterate through the collection.
        """
        pass

    def GetHostId(self):
        """
        GetHostId(self: RebarContainer) -> ElementId
        
            The element that contains the rebar.
            Returns: The element that the rebar object belongs to, such as a structural
           wall, 
             floor, foundation, beam, brace or column.
        """
        pass

    def GetItem(self, itemIndex):
        """
        GetItem(self: RebarContainer, itemIndex: int) -> RebarContainerItem
        
            Gets the item stored in the RebarContainer at the associated index.
        
            itemIndex: Item index in the Rebar Container
            Returns: Rebar Container Item
        """
        pass

    def GetParametersManager(self):
        """
        GetParametersManager(self: RebarContainer) -> RebarContainerParameterManager
        
            Returns an object used to manage parameters of the Rebar Container.
            Returns: The parameters manager.
        """
        pass

    def GetRebarContainerIterator(self):
        """
        GetRebarContainerIterator(self: RebarContainer) -> RebarContainerIterator
        
            Returns a Rebar Container Iterator that iterates through the Rebar Container 
             Items.
        
            Returns: A Rebar Container Iterator object that can be used to iterate through Rebar 
             Container Items in the collection.
        """
        pass

    def GetReinforcementRoundingManager(self):
        """
        GetReinforcementRoundingManager(self: RebarContainer) -> RebarRoundingManager
        
            Returns an object for managing reinforcement rounding override settings.
            Returns: The rounding manager.
        """
        pass

    def HasPresentationOverrides(self, dBView):
        """
        HasPresentationOverrides(self: RebarContainer, dBView: View) -> bool
        
            Identifies if any RebarContainerItem of this RebarContainer has overridden 
             default presentation settings for the given view.
        
        
            dBView: The view.
            Returns: True if if any RebarContainerItem of this RebarContainer has overridden default 
             presentation settings, false otherwise.
        """
        pass

    def IsItemHidden(self, view, itemIndex):
        """
        IsItemHidden(self: RebarContainer, view: View, itemIndex: int) -> bool
        
            Identifies if a given RebarContainerItem is hidden in this view.
        
            view: The view.
            itemIndex: Item index in the Rebar Container.
            Returns: True if the RebarContainerItem is hidden in this view, false otherwise.
        """
        pass

    def IsSolidInView(self, view):
        """
        IsSolidInView(self: RebarContainer, view: View3D) -> bool
        
            Checks if this RebarContainer element is shown as solid in the given 3D view.
        
            view: The 3D view element
            Returns: True this RebarContainer element is shown as solid in the given 3D view, false 
             otherwise.
        """
        pass

    def IsUnobscuredInView(self, view):
        """
        IsUnobscuredInView(self: RebarContainer, view: View) -> bool
        
            Checks if this rebar container element is shown unobscured in a view.
        
            view: The view element
            Returns: True if rebar is shown unobscured, false otherwise.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: Element, disposing: bool) """
        pass

    def RemoveItem(self, pItem):
        """
        RemoveItem(self: RebarContainer, pItem: RebarContainerItem)
            Removes Item from the Rebar Container.
        
            pItem: Item to be removed from this Rebar Container
        """
        pass

    def setElementType(self, *args): #cannot find CLR method
        """ setElementType(self: Element, type: ElementType, incompatibleExceptionMessage: str) """
        pass

    def SetHostId(self, doc, hostId):
        """
        SetHostId(self: RebarContainer, doc: Document, hostId: ElementId)
            The element that contains the rebar.
        
            doc: The document containing both this element and the host element.
            hostId: The element that the rebar object belongs to, such as a structural
           wall, 
             floor, foundation, beam, brace or column. The rebar does not need
           to be 
             strictly inside the host, but it must be assigned to one host
           element.
        """
        pass

    def SetItemHiddenStatus(self, view, itemIndex, hide):
        """
        SetItemHiddenStatus(self: RebarContainer, view: View, itemIndex: int, hide: bool)
            Sets the RebarContainerItem to be hidden or unhidden in the given view.
        
            view: The view.
            itemIndex: Item index in the Rebar Container.
            hide: True to hide this RebarContainerItem in the view, false to unhide the item.
        """
        pass

    def SetSolidInView(self, view, solid):
        """
        SetSolidInView(self: RebarContainer, view: View3D, solid: bool)
            Sets this RebarContainer element is shown as solid in the given 3D view.
        
            view: The 3D view element
            solid: True if this RebarContainer element is shown as solid in the given 3D view, 
             false otherwise.
        """
        pass

    def SetUnobscuredInView(self, view, unobscured):
        """
        SetUnobscuredInView(self: RebarContainer, view: View, unobscured: bool)
            Sets this rebar container element to be shown unobscured in a view.
        
            view: The view element
            unobscured: True if rebar is shown unobscured, false otherwise.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[RebarContainerItem](enumerable: IEnumerable[RebarContainerItem], value: RebarContainerItem) -> bool """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    ItemsCount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The count of Items in this Rebar Container.

Get: ItemsCount(self: RebarContainer) -> int

"""

    PresentItemsAsSubelements = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Identifies if Items should be presented in schedules and tags as separate subelements.

Get: PresentItemsAsSubelements(self: RebarContainer) -> bool

Set: PresentItemsAsSubelements(self: RebarContainer) = value
"""

    ScheduleMark = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Schedule Mark parameter. On creation, the Schedule Mark is set
   to a value that is unique to the host, but it can be set to
   any value.

Get: ScheduleMark(self: RebarContainer) -> str

Set: ScheduleMark(self: RebarContainer) = value
"""


