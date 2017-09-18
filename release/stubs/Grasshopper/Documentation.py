# encoding: utf-8
# module Grasshopper.Documentation calls itself Documentation
# from Grasshopper, Version=1.0.0.20, Culture=neutral, PublicKeyToken=dda4f5ec2cd80803
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class GH_Audience(Enum, IComparable, IFormattable, IConvertible):
    """ enum GH_Audience, values: Beginner (0), Expert (2), Intermediate (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Beginner = None
    Expert = None
    Intermediate = None
    value__ = None


class GH_ContentCollection(object, IGH_Content):
    """ GH_ContentCollection() """
    def ToString(self):
        """ ToString(self: GH_ContentCollection) -> str """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Content = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Content(self: GH_ContentCollection) -> List[IGH_Content]

"""

    Count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Count(self: GH_ContentCollection) -> int

"""



class GH_Format(object, IGH_Content):
    # no doc
    @staticmethod
    def Create(content, style):
        """
        Create(content: IGH_Content, style: GH_Style) -> GH_Format
        Create(content: str, style: GH_Style) -> GH_Format
        """
        pass

    def ToString(self):
        """ ToString(self: GH_Format) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Content = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Content(self: GH_Format) -> IGH_Content

"""

    Style = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Style(self: GH_Format) -> GH_Style

"""



class GH_GlossaryItem(object):
    # no doc
    @staticmethod
    def ParseFile(path):
        """ ParseFile(path: str) -> GH_GlossaryItem """
        pass

    Author = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Author(self: GH_GlossaryItem) -> IGH_Content

"""

    Contact = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Contact(self: GH_GlossaryItem) -> IGH_Content

"""

    Descriptions = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Descriptions(self: GH_GlossaryItem) -> List[IGH_Content]

"""

    Path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Path(self: GH_GlossaryItem) -> str

"""

    Pronunciation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Pronunciation(self: GH_GlossaryItem) -> IGH_Content

"""

    Synonyms = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Synonyms(self: GH_GlossaryItem) -> ReadOnlyCollection[str]

"""

    Word = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Word(self: GH_GlossaryItem) -> str

"""



class GH_Link(object, IGH_Content):
    # no doc
    @staticmethod
    def CreateExternalLink(text, url, tooltip=None):
        """
        CreateExternalLink(text: str, url: str, tooltip: str) -> GH_Link
        CreateExternalLink(text: str, url: str) -> GH_Link
        """
        pass

    @staticmethod
    def CreateGlossaryLink(text, glossaryEntry=None):
        """
        CreateGlossaryLink(text: str, glossaryEntry: str) -> GH_Link
        CreateGlossaryLink(text: str) -> GH_Link
        """
        pass

    @staticmethod
    def CreateSharedLink(linkId, target, tooltip=None):
        """
        CreateSharedLink(linkId: str, target: str, tooltip: str) -> GH_Link
        CreateSharedLink(linkId: str, target: str) -> GH_Link
        """
        pass

    @staticmethod
    def CreateTopicLink(text, topicName, tooltip=None):
        """
        CreateTopicLink(text: str, topicName: str, tooltip: str) -> GH_Link
        CreateTopicLink(text: str, topicName: str) -> GH_Link
        """
        pass

    def ToString(self):
        """ ToString(self: GH_Link) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Destination = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Destination(self: GH_Link) -> str

"""

    IsSharedLink = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsSharedLink(self: GH_Link) -> bool

"""

    LinkId = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: LinkId(self: GH_Link) -> str

"""

    Target = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Target(self: GH_Link) -> GH_Target

"""

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Text(self: GH_Link) -> IGH_Content

"""

    Tooltip = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Tooltip(self: GH_Link) -> str

"""



class GH_List(object, IGH_Content):
    # no doc
    @staticmethod
    def Create(ordered, items=None):
        """
        Create(ordered: bool, items: IEnumerable[IGH_Content]) -> GH_List
        Create(ordered: bool) -> GH_List
        """
        pass

    def ToString(self):
        """ ToString(self: GH_List) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Items = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Items(self: GH_List) -> List[IGH_Content]

"""

    Ordered = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Ordered(self: GH_List) -> bool

"""



class GH_Paragraph(object, IGH_Content):
    # no doc
    @staticmethod
    def Create(content):
        """
        Create(content: Array[str]) -> GH_Paragraph
        Create(content: str) -> GH_Paragraph
        """
        pass

    def ToString(self):
        """ ToString(self: GH_Paragraph) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Content = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Content(self: GH_Paragraph) -> IGH_Content

"""



class GH_Parser(object):
    # no doc
    @staticmethod
    def IsChapterHeaderLine(line):
        """ IsChapterHeaderLine(line: str) -> bool """
        pass

    @staticmethod
    def IsCommentLine(line):
        """ IsCommentLine(line: str) -> bool """
        pass

    @staticmethod
    def IsLinkLine(line, linkId=None, linkTarget=None, linkTooltip=None):
        """
        IsLinkLine(line: str) -> (bool, str, str, str)
        IsLinkLine(line: str) -> bool
        """
        pass

    @staticmethod
    def IsListLine(line):
        """ IsListLine(line: str) -> bool """
        pass

    @staticmethod
    def IsParagraphHeaderLine(line):
        """ IsParagraphHeaderLine(line: str) -> bool """
        pass

    @staticmethod
    def IsQuoteLine(line):
        """ IsQuoteLine(line: str) -> bool """
        pass

    @staticmethod
    def StringToFragment(text):
        """ StringToFragment(text: str) -> IGH_Content """
        pass

    Whitespace = None


class GH_RuntimeFile(object):
    # no doc
    def ContainsKey(self, key):
        """ ContainsKey(self: GH_RuntimeFile, key: str) -> bool """
        pass

    @staticmethod
    def IsTag(text):
        """ IsTag(text: str) -> bool """
        pass

    @staticmethod
    def IsTagLine(line, keyword, remainder):
        """ IsTagLine(line: str) -> (bool, str, str) """
        pass

    @staticmethod
    def ParseFile(path):
        """ ParseFile(path: str) -> GH_RuntimeFile """
        pass

    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    Keys = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Keys(self: GH_RuntimeFile) -> List[str]

"""

    Path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Path(self: GH_RuntimeFile) -> str

"""


    TagAuthor = 'AUTHOR'
    TagAutoLink = 'AUTOLINK'
    TagBeginner = 'BEGINNER'
    TagCategory = 'CATEGORY'
    TagComponent = 'COMPONENT'
    TagContact = 'CONTACT'
    TagDescription = 'DESCRIPTION'
    TagErranyms = 'DONTCONFUSE'
    TagExpert = 'EXPERT'
    TagInclude = 'INCLUDE'
    TagIntermediate = 'INTERMEDIATE'
    TagKeywords = 'KEYWORDS'
    TagPronunciation = 'PRONUNCIATION'
    TagRhinoCommand = 'RHINOCOMMAND'
    Tags = None
    TagSeeAlso = 'SEEALSO'
    TagSynonyms = 'SYNONYMS'
    TagTitle = 'TITLE'


class GH_Style(Enum, IComparable, IFormattable, IConvertible):
    """ enum GH_Style, values: Boxed (4), ChapterHeader (5), Monospaced (3), None (0), ParagraphHeader (6), StrongEmphasis (2), WeakEmphasis (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Boxed = None
    ChapterHeader = None
    Monospaced = None
    None = None
    ParagraphHeader = None
    StrongEmphasis = None
    value__ = None
    WeakEmphasis = None


class GH_Target(Enum, IComparable, IFormattable, IConvertible):
    """ enum GH_Target, values: External (2), Glossary (0), Topic (1) """
    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==yx.__eq__(y) <==> x==yx.__eq__(y) <==> x==y """
        pass

    def __format__(self, *args): #cannot find CLR method
        """ __format__(formattable: IFormattable, format: str) -> str """
        pass

    def __ge__(self, *args): #cannot find CLR method
        pass

    def __gt__(self, *args): #cannot find CLR method
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __le__(self, *args): #cannot find CLR method
        pass

    def __lt__(self, *args): #cannot find CLR method
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    External = None
    Glossary = None
    Topic = None
    value__ = None


class GH_Text(object, IGH_Content):
    # no doc
    @staticmethod
    def Create(text):
        """ Create(text: str) -> GH_Text """
        pass

    def ToString(self):
        """ ToString(self: GH_Text) -> str """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    def __str__(self, *args): #cannot find CLR method
        pass

    Text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: Text(self: GH_Text) -> str

"""



class GH_Topic(object):
    # no doc
    @staticmethod
    def ParseFile(path):
        """ ParseFile(path: str) -> GH_Topic """
        pass


class IGH_Content:
    # no doc
    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass


