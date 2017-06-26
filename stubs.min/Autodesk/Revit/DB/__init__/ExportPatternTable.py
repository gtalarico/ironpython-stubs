class ExportPatternTable(object, IEnumerable[KeyValuePair[ExportPatternKey, ExportPatternInfo]], IEnumerable, IDisposable):
    """
    A table supporting a mapping of FillPatterns in Revit to pattern names that will be set
       in the target export format.
    
    ExportPatternTable()
    """
    def Add(self, exportPatternKey, exportPatternInfo):
        """
        Add(self: ExportPatternTable, exportPatternKey: ExportPatternKey, exportPatternInfo: ExportPatternInfo)
            Inserts a (key,info) pair into Export pattern table.
        
            exportPatternKey: The export pattern key to be added.
            exportPatternInfo: The export pattern info to be added.
        """
        pass

    def Clear(self):
        """
        Clear(self: ExportPatternTable)
            Removes all contents stored in the table.
        """
        pass

    def ContainsKey(self, exportpatternKey):
        """
        ContainsKey(self: ExportPatternTable, exportpatternKey: ExportPatternKey) -> bool
        
            Checks whether a pattern key exists in the table.
        
            exportpatternKey: The export pattern Key.
            Returns: True if the pattern key exists in the table.
        """
        pass

    def Dispose(self):
        """ Dispose(self: ExportPatternTable) """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: ExportPatternTable) -> IEnumerator[KeyValuePair[ExportPatternKey, ExportPatternInfo]]
        
            Returns an enumerator that iterates through a collection.
            Returns: An IEnumerator object that can be used to iterate through the collection.
        """
        pass

    def GetExportPatternInfo(self, exportPatternKey):
        """
        GetExportPatternInfo(self: ExportPatternTable, exportPatternKey: ExportPatternKey) -> ExportPatternInfo
        
            Gets a copy of the pattern info associated to the input pattern key.
        
            exportPatternKey: The export pattern Key.
            Returns: Return the patternInfo for this key.
        """
        pass

    def GetKeys(self):
        """
        GetKeys(self: ExportPatternTable) -> IList[ExportPatternKey]
        
            Gets all the keys stored in the map.
            Returns: Return the key array.
        """
        pass

    def GetPatternTableIterator(self):
        """
        GetPatternTableIterator(self: ExportPatternTable) -> ExportPatternTableIterator
        
            Returns a PatternTableIterator that iterates through the collection.
            Returns: A PatternTableIterator object that can be used to iterate through key-value 
             pairs in the collection.
        """
        pass

    def GetValues(self):
        """
        GetValues(self: ExportPatternTable) -> IList[ExportPatternInfo]
        
            Returns all the values stored in the map.
            Returns: Return the info array.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ExportPatternTable, disposing: bool) """
        pass

    def Remove(self, exportPatternKey):
        """
        Remove(self: ExportPatternTable, exportPatternKey: ExportPatternKey)
            Removes the pair (key, info) by pattern key.
        
            exportPatternKey: The export pattern key.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[KeyValuePair[ExportPatternKey, ExportPatternInfo]](enumerable: IEnumerable[KeyValuePair[ExportPatternKey, ExportPatternInfo]], value: KeyValuePair[ExportPatternKey, ExportPatternInfo]) -> bool """
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

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Count of the items contained in the collection.

Get: Count(self: ExportPatternTable) -> int

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: ExportPatternTable) -> bool

"""


