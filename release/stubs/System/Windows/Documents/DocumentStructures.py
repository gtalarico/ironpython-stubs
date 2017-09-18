# encoding: utf-8
# module System.Windows.Documents.DocumentStructures calls itself DocumentStructures
# from PresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class BlockElement(object):
    """
    Do not use.
    
    BlockElement()
    """

class SemanticBasicElement(BlockElement):
    """ An XML element in the markup for XML Paper Specification (XPS) documents. """

class FigureStructure(SemanticBasicElement, IAddChild, IEnumerable[NamedElement], IEnumerable):
    """
    Represents a drawing, chart, or diagram in a document.
    
    FigureStructure()
    """
    def Add(self, element):
        """
        Add(self: FigureStructure, element: NamedElement)
            Add a named element to the figure.
        
            element: The element to add.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[NamedElement](enumerable: IEnumerable[NamedElement], value: NamedElement) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass


class ListItemStructure(SemanticBasicElement, IAddChild, IEnumerable[BlockElement], IEnumerable):
    """
    Represents an item in a list or outline.
    
    ListItemStructure()
    """
    def Add(self, element):
        """
        Add(self: ListItemStructure, element: BlockElement)
            Adds a block to a list item.
        
            element: The block to add.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[BlockElement](enumerable: IEnumerable[BlockElement], value: BlockElement) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    Marker = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the numeral, character, or bullet symbol for the list item as it appears in the formatting markup of the document.

Get: Marker(self: ListItemStructure) -> str

Set: Marker(self: ListItemStructure) = value
"""



class ListStructure(SemanticBasicElement, IAddChild, IEnumerable[ListItemStructure], IEnumerable):
    """
    Represents a list of items in a document.
    
    ListStructure()
    """
    def Add(self, listItem):
        """
        Add(self: ListStructure, listItem: ListItemStructure)
            Adds a list item to the list.
        
            listItem: The list item to add.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[ListItemStructure](enumerable: IEnumerable[ListItemStructure], value: ListItemStructure) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass


class NamedElement(BlockElement):
    """
    Identifies an element within the hierarchy of elements under a System.Windows.Documents.FixedPage.
    
    NamedElement()
    """
    NameReference = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the element in the System.Windows.Documents.FixedPage markup hierarchy that provides the content for the parent of the System.Windows.Documents.DocumentStructures.NamedElement.

Get: NameReference(self: NamedElement) -> str

Set: NameReference(self: NamedElement) = value
"""



class ParagraphStructure(SemanticBasicElement, IAddChild, IEnumerable[NamedElement], IEnumerable):
    """
    Represents a paragraph in a document.
    
    ParagraphStructure()
    """
    def Add(self, element):
        """
        Add(self: ParagraphStructure, element: NamedElement)
            Adds a named element to the paragraph.
        
            element: The element to add.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[NamedElement](enumerable: IEnumerable[NamedElement], value: NamedElement) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass


class SectionStructure(SemanticBasicElement, IAddChild, IEnumerable[BlockElement], IEnumerable):
    """
    Represents a section of content in a document.
    
    SectionStructure()
    """
    def Add(self, element):
        """
        Add(self: SectionStructure, element: BlockElement)
            Adds a block to the section.
        
            element: The block element to add.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[BlockElement](enumerable: IEnumerable[BlockElement], value: BlockElement) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass


class StoryBreak(BlockElement):
    """
    Identifies the start or end of story composed of one or more System.Windows.Documents.DocumentStructures.StoryFragment elements.
    
    StoryBreak()
    """

class StoryFragment(object, IAddChild, IEnumerable[BlockElement], IEnumerable):
    """
    Represents all or part of a story within an XPS document.
    
    StoryFragment()
    """
    def Add(self, element):
        """
        Add(self: StoryFragment, element: BlockElement)
            Add a block to the story fragment.
        
            element: The block to add.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[BlockElement](enumerable: IEnumerable[BlockElement], value: BlockElement) -> bool """
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

    FragmentName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the story fragment.

Get: FragmentName(self: StoryFragment) -> str

Set: FragmentName(self: StoryFragment) = value
"""

    FragmentType = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the type of fragment.

Get: FragmentType(self: StoryFragment) -> str

Set: FragmentType(self: StoryFragment) = value
"""

    StoryName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the name of the story.

Get: StoryName(self: StoryFragment) -> str

Set: StoryName(self: StoryFragment) = value
"""



class StoryFragments(object, IAddChild, IEnumerable[StoryFragment], IEnumerable):
    """
    Represents a set of one or more System.Windows.Documents.DocumentStructures.StoryFragment elements.
    
    StoryFragments()
    """
    def Add(self, storyFragment):
        """
        Add(self: StoryFragments, storyFragment: StoryFragment)
            Adds a System.Windows.Documents.DocumentStructures.StoryFragment to the 
             System.Windows.Documents.DocumentStructures.StoryFragments collection.
        
        
            storyFragment: The System.Windows.Documents.DocumentStructures.StoryFragment to add.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[StoryFragment](enumerable: IEnumerable[StoryFragment], value: StoryFragment) -> bool """
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


class TableCellStructure(SemanticBasicElement, IAddChild, IEnumerable[BlockElement], IEnumerable):
    """
    Represents a cell in a table.
    
    TableCellStructure()
    """
    def Add(self, element):
        """
        Add(self: TableCellStructure, element: BlockElement)
            Adds a block element to the table cell.
        
            element: The element to add.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[BlockElement](enumerable: IEnumerable[BlockElement], value: BlockElement) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    ColumnSpan = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the number of columns spanned by the cell.

Get: ColumnSpan(self: TableCellStructure) -> int

Set: ColumnSpan(self: TableCellStructure) = value
"""

    RowSpan = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the number of rows spanned by the cell.

Get: RowSpan(self: TableCellStructure) -> int

Set: RowSpan(self: TableCellStructure) = value
"""



class TableRowGroupStructure(SemanticBasicElement, IAddChild, IEnumerable[TableRowStructure], IEnumerable):
    """
    Represents a set of one or more rows in a table.
    
    TableRowGroupStructure()
    """
    def Add(self, tableRow):
        """
        Add(self: TableRowGroupStructure, tableRow: TableRowStructure)
            Adds a row to the table row group.
        
            tableRow: The row to add.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[TableRowStructure](enumerable: IEnumerable[TableRowStructure], value: TableRowStructure) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass


class TableRowStructure(SemanticBasicElement, IAddChild, IEnumerable[TableCellStructure], IEnumerable):
    """
    Represents a row of one or more cells in a table.
    
    TableRowStructure()
    """
    def Add(self, tableCell):
        """
        Add(self: TableRowStructure, tableCell: TableCellStructure)
            Adds a cell to a table row.
        
            tableCell: The cell to add.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[TableCellStructure](enumerable: IEnumerable[TableCellStructure], value: TableCellStructure) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass


class TableStructure(SemanticBasicElement, IAddChild, IEnumerable[TableRowGroupStructure], IEnumerable):
    """
    Represents a table in a document.
    
    TableStructure()
    """
    def Add(self, tableRowGroup):
        """
        Add(self: TableStructure, tableRowGroup: TableRowGroupStructure)
            Adds a group of rows to a table.
        
            tableRowGroup: The group of rows to add.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+y """
        pass

    def __contains__(self, *args): #cannot find CLR method
        """ __contains__[TableRowGroupStructure](enumerable: IEnumerable[TableRowGroupStructure], value: TableRowGroupStructure) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass


