class HtmlElementCollection(object, ICollection, IEnumerable):
    """ Defines a collection of System.Windows.Forms.HtmlElement objects. """
    def GetElementsByName(self, name):
        """
        GetElementsByName(self: HtmlElementCollection, name: str) -> HtmlElementCollection
        
            Gets a collection of elements by their name.
        
            name: The name or ID of the element.
            Returns: An System.Windows.Forms.HtmlElementCollection containing the elements whose System.Windows.Forms.HtmlElement.Name property match name.
        """
        pass

    def GetEnumerator(self):
        """
        GetEnumerator(self: HtmlElementCollection) -> IEnumerator
        
            Returns an enumerator that iterates through a collection.
            Returns: An System.Collections.IEnumerator that can be used to iterate through the collection.
        """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y]x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __len__(self, *args): #cannot find CLR method
        """ x.__len__() <==> len(x) """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets the number of elements in the collection.

Get: Count(self: HtmlElementCollection) -> int

"""


