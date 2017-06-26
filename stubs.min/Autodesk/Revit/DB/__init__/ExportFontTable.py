class ExportFontTable(object, IEnumerable[KeyValuePair[ExportFontKey, ExportFontInfo]], IEnumerable, IDisposable):
    """
    A table supporting a mapping of Revit font names to font names that will be set
       in the target export format.
    
    ExportFontTable()
    """
    def Add(self, exportFontKey, exportFontInfo):
        """
        Add(self: ExportFontTable, exportFontKey: ExportFontKey, exportFontInfo: ExportFontInfo)
            Inserts a (key,info) pair into Export font table.
        
            exportFontKey: The export font key to be added.
            exportFontInfo: The export font info to be added.
        """
        pass

    def Clear(self):
        """
        Clear(self: ExportFontTable)
            Removes all contents stored in the table.
        """
        pass

    def ContainsKey(self, exportfontKey):
        """
        ContainsKey(self: ExportFontTable, exportfontKey: ExportFontKey) -> bool
        
            Checks whether a font key exists in the table.
        
            exportfontKey: The export font Key.
            Returns: True if the font key exists in the table.
        """
        pass

    def Dispose(self):
        """ Dispose(self: ExportFontTable) """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: ExportFontTable) -> IEnumerator[KeyValuePair[ExportFontKey, ExportFontInfo]]
        
            Returns an enumerator that iterates through a collection.
            Returns: An IEnumerator object that can be used to iterate through the collection.
        """
        pass

    def GetExportFontInfo(self, exportFontKey):
        """
        GetExportFontInfo(self: ExportFontTable, exportFontKey: ExportFontKey) -> ExportFontInfo
        
            Gets a copy of the font info associated to the input font key.
        
            exportFontKey: The export font Key.
            Returns: Returns the fontInfo for this key.
        """
        pass

    def GetFontTableIterator(self):
        """
        GetFontTableIterator(self: ExportFontTable) -> ExportFontTableIterator
        
            Returns a FontTableIterator that iterates through the collection.
            Returns: A FontTableIterator object that can be used to iterate through key-value pairs 
             in the collection.
        """
        pass

    def GetKeys(self):
        """
        GetKeys(self: ExportFontTable) -> IList[ExportFontKey]
        
            Returns a collection of the keys stored in this table.
            Returns: The collection of keys.
        """
        pass

    def GetValues(self):
        """
        GetValues(self: ExportFontTable) -> IList[ExportFontInfo]
        
            Returns a collection of the values stored in this table.
            Returns: The collection of values.
        """
        pass

    def ReleaseUnmanagedResources(self, *args): #cannot find CLR method
        """ ReleaseUnmanagedResources(self: ExportFontTable, disposing: bool) """
        pass

    def Remove(self, exportFontKey):
        """
        Remove(self: ExportFontTable, exportFontKey: ExportFontKey)
            Removes the pair (key, info) by font key.
        
            exportFontKey: The export font key.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[KeyValuePair[ExportFontKey, ExportFontInfo]](enumerable: IEnumerable[KeyValuePair[ExportFontKey, ExportFontInfo]], value: KeyValuePair[ExportFontKey, ExportFontInfo]) -> bool """
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

Get: Count(self: ExportFontTable) -> int

"""

    IsValidObject = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Specifies whether the .NET object represents a valid Revit entity.

Get: IsValidObject(self: ExportFontTable) -> bool

"""


