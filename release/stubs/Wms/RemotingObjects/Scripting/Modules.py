from Wms.RemotingObjects import *
# encoding: utf-8
# module Wms.RemotingObjects.Scripting.Modules calls itself Modules
# from Wms.RemotingObjects, Version=1.23.1.0, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class AddModuleArgs():
    """ AddModuleArgs() """
    Content = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Content(self: AddModuleArgs) -> Array[Byte]

Set: Content(self: AddModuleArgs) = value
"""

    FileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: FileName(self: AddModuleArgs) -> str

Set: FileName(self: AddModuleArgs) = value
"""

    Path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Path(self: AddModuleArgs) -> str

Set: Path(self: AddModuleArgs) = value
"""


    def Instance(self):
        """hardcoded/mock instance of the class"""
        return AddModuleArgs()

class GetLibArgs():
    """ GetLibArgs() """
    Path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Path(self: GetLibArgs) -> str

Set: Path(self: GetLibArgs) = value
"""


    def Instance(self):
        """hardcoded/mock instance of the class"""
        return GetLibArgs()

class LibContent():
    """ LibContent() """
    Directory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Directory(self: LibContent) -> str

Set: Directory(self: LibContent) = value
"""

    Name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Name(self: LibContent) -> str

Set: Name(self: LibContent) = value
"""

    ReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: ReadOnly(self: LibContent) -> bool

Set: ReadOnly(self: LibContent) = value
"""

    SubContent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: SubContent(self: LibContent) -> LibContents

Set: SubContent(self: LibContent) = value
"""

    Type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Type(self: LibContent) -> LibContentType

Set: Type(self: LibContent) = value
"""


    def Instance(self):
        """hardcoded/mock instance of the class"""
        return LibContent()

class LibContents(FindableList):
    """ LibContents() """
    def __getitem__(self, *args): #cannot find CLR method
        """ x.__getitem__(y) <==> x[y] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    def __iter__(self, *args): #cannot find CLR method
        """ __iter__(self: IEnumerable) -> object """
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __setitem__(self, *args): #cannot find CLR method
        """ x.__setitem__(i, y) <==> x[i]= """
        pass

    Path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Directory to retrieve the contents. An empty path will retrieve the root content.

Get: Path(self: LibContents) -> str

Set: Path(self: LibContents) = value
"""


    def Instance(self):
        """hardcoded/mock instance of the class"""
        return LibContents()

class LibContentType:
    """ enum LibContentType, values: File (1), Folder (0) """
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

    File = None
    Folder = None
    value__ = None

    def Instance(self):
        """hardcoded/mock instance of the class"""
        return LibContentType()

class ModuleArgs():
    """ ModuleArgs() """
    Directory = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Directory(self: ModuleArgs) -> str

Set: Directory(self: ModuleArgs) = value
"""

    FileName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: FileName(self: ModuleArgs) -> str

Set: FileName(self: ModuleArgs) = value
"""

    Overwrite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Overwrite(self: ModuleArgs) -> bool

Set: Overwrite(self: ModuleArgs) = value
"""

    Script = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Script(self: ModuleArgs) -> Array[Byte]

Set: Script(self: ModuleArgs) = value
"""


    def Instance(self):
        """hardcoded/mock instance of the class"""
        return ModuleArgs()

class PythonModule():
    """ PythonModule() """
    Content = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Content(self: PythonModule) -> str

Set: Content(self: PythonModule) = value
"""

    IsReadOnly = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: IsReadOnly(self: PythonModule) -> bool

Set: IsReadOnly(self: PythonModule) = value
"""

    Path = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """

Get: Path(self: PythonModule) -> str

Set: Path(self: PythonModule) = value
"""


    def Instance(self):
        """hardcoded/mock instance of the class"""
        return PythonModule()

