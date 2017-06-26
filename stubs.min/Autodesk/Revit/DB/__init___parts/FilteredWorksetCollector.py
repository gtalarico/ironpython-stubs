class FilteredWorksetCollector(object, IEnumerable[Workset], IEnumerable, IDisposable):
    """
    This class is used to search, filter and iterate through a set of worksets.
    
    FilteredWorksetCollector(document: Document)
    """
    def Dispose(self):
        """ Dispose(self: FilteredWorksetCollector) """
        pass

    def FirstWorkset(self):
        """
        FirstWorkset(self: FilteredWorksetCollector) -> Workset
        
            Returns the first workset to pass the filter(s).
            Returns: The first workset.
        """
        pass

    def FirstWorksetId(self):
        """
        FirstWorksetId(self: FilteredWorksetCollector) -> WorksetId
        
            Returns the id of the first workset to pass the filter(s).
            Returns: The first workset id.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: FilteredWorksetCollector) -> IEnumerator[Workset]
        
            Returns an enumerator that iterates through a collection.
            Returns: An IEnumerator object that can be used to iterate through the collection.
        """
        pass

    def GetWorksetIdIterator(self):
        """
        GetWorksetIdIterator(self: FilteredWorksetCollector) -> FilteredWorksetIdIterator
        
            Returns a FilteredWorksetIdIterator to the worksets passing the current filter.
        """
        pass

    def GetWorksetIterator(self):
        """
        GetWorksetIterator(self: FilteredWorksetCollector) -> FilteredWorksetIterator
        
            Returns a FilteredWorksetIterator to the worksets passing the current filter.
        """
        pass

    def OfKind(self, worksetKind):
        """
        OfKind(self: FilteredWorksetCollector, worksetKind: WorksetKind) -> FilteredWorksetCollector
        
            Applies a WorksetKindFilter to the collector.
        
            worksetKind: The WorksetKind of the workset.
            Returns: A handle to this collector.  This is the same collector that has just been 
             modified, returned
           so you can chain multiple calls together in one line.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: FilteredWorksetCollector, disposing: bool) """
        pass

    def ToWorksetIds(self):
        """
        ToWorksetIds(self: FilteredWorksetCollector) -> ICollection[WorksetId]
        
            Returns the complete set of workset ids that pass the filter(s).
            Returns: The complete set of workset ids.
        """
        pass

    def ToWorksets(self):
        """
        ToWorksets(self: FilteredWorksetCollector) -> IList[Workset]
        
            Returns the complete set of worksets that pass the filter(s).
            Returns: The complete array of worksets.
        """
        pass

    def WherePasses(self, filter):
        """
        WherePasses(self: FilteredWorksetCollector, filter: WorksetFilter) -> FilteredWorksetCollector
        
            Applies a workset filter to the collector.
        
            filter: The workset filter.
            Returns: A handle to this collector.  This is the same collector that has just been 
             modified, returned
           so you can chain multiple calls together in one line.
        """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[Workset](enumerable: IEnumerable[Workset], value: Workset) -> bool """
        pass

    def __enter__(self, *args): #cannot find CLR method
        """ __enter__(self: IDisposable) -> object """
        pass

    def __exit__(self, *args): #cannot find CLR method
        """ __exit__(self: IDisposable, exc_type: object, exc_value: object, exc_back: object) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    @staticmethod # known case of __new__
    def __new__(self, document):
        """ __new__(cls: type, document: Document) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: FilteredWorksetCollector) -> bool

"""


