# encoding: utf-8
# module Grasshopper.Kernel.Undo.Actions calls itself Actions
# from Grasshopper, Version=1.0.0.20, Culture=neutral, PublicKeyToken=dda4f5ec2cd80803
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class GH_AddObjectAction(GH_UndoAction, IGH_UndoAction, GH_ISerializable):
    """ GH_AddObjectAction(obj: IGH_DocumentObject) """
    def Internal_Redo(self, *args): #cannot find CLR method
        """ Internal_Redo(self: GH_AddObjectAction, doc: GH_Document) """
        pass

    def Internal_Undo(self, *args): #cannot find CLR method
        """ Internal_Undo(self: GH_AddObjectAction, doc: GH_Document) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, obj):
        """ __new__(cls: type, obj: IGH_DocumentObject) """
        pass

    ExpiresSolution = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExpiresSolution(self: GH_AddObjectAction) -> bool

"""



class GH_AddStateAction(GH_ArchivedUndoAction, IGH_UndoAction, GH_ISerializable):
    """ GH_AddStateAction(index: int, state: GH_State) """
    def Deserialize(self, *args): #cannot find CLR method
        """ Deserialize(self: GH_ArchivedUndoAction, obj: GH_ISerializable) """
        pass

    def Internal_Redo(self, *args): #cannot find CLR method
        """ Internal_Redo(self: GH_AddStateAction, doc: GH_Document) """
        pass

    def Internal_Undo(self, *args): #cannot find CLR method
        """ Internal_Undo(self: GH_AddStateAction, doc: GH_Document) """
        pass

    def Read(self, reader):
        """ Read(self: GH_AddStateAction, reader: GH_IReader) -> bool """
        pass

    def Serialize(self, *args): #cannot find CLR method
        """ Serialize(self: GH_ArchivedUndoAction, obj: GH_ISerializable) """
        pass

    def SerializeToByteArray(self, *args): #cannot find CLR method
        """ SerializeToByteArray(self: GH_ArchivedUndoAction, obj: GH_ISerializable) -> Array[Byte] """
        pass

    def Write(self, writer):
        """ Write(self: GH_AddStateAction, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, index, state):
        """ __new__(cls: type, index: int, state: GH_State) """
        pass

    m_data = None


class GH_DataMatchingAction(GH_ObjectUndoAction, IGH_UndoAction, GH_ISerializable):
    """ GH_DataMatchingAction(obj: IGH_Component) """
    def Internal_Redo(self, *args): #cannot find CLR method
        """ Internal_Redo(self: GH_ObjectUndoAction, doc: GH_Document) """
        pass

    def Internal_Undo(self, *args): #cannot find CLR method
        """ Internal_Undo(self: GH_ObjectUndoAction, doc: GH_Document) """
        pass

    def Object_Redo(self, *args): #cannot find CLR method
        """ Object_Redo(self: GH_DataMatchingAction, doc: GH_Document, obj: IGH_DocumentObject) """
        pass

    def Object_Undo(self, *args): #cannot find CLR method
        """ Object_Undo(self: GH_DataMatchingAction, doc: GH_Document, obj: IGH_DocumentObject) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, obj):
        """ __new__(cls: type, obj: IGH_Component) """
        pass

    ExpiresSolution = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExpiresSolution(self: GH_DataMatchingAction) -> bool

"""



class GH_DataModificationAction(GH_ObjectUndoAction, IGH_UndoAction, GH_ISerializable):
    """ GH_DataModificationAction(obj: IGH_Param) """
    def Internal_Redo(self, *args): #cannot find CLR method
        """ Internal_Redo(self: GH_ObjectUndoAction, doc: GH_Document) """
        pass

    def Internal_Undo(self, *args): #cannot find CLR method
        """ Internal_Undo(self: GH_ObjectUndoAction, doc: GH_Document) """
        pass

    def Object_Redo(self, *args): #cannot find CLR method
        """ Object_Redo(self: GH_DataModificationAction, doc: GH_Document, obj: IGH_DocumentObject) """
        pass

    def Object_Undo(self, *args): #cannot find CLR method
        """ Object_Undo(self: GH_DataModificationAction, doc: GH_Document, obj: IGH_DocumentObject) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, obj):
        """ __new__(cls: type, obj: IGH_Param) """
        pass

    ExpiresSolution = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExpiresSolution(self: GH_DataModificationAction) -> bool

"""



class GH_GenericObjectAction(GH_ArchivedUndoAction, IGH_UndoAction, GH_ISerializable):
    """ GH_GenericObjectAction(obj: IGH_DocumentObject) """
    def Deserialize(self, *args): #cannot find CLR method
        """ Deserialize(self: GH_ArchivedUndoAction, obj: GH_ISerializable) """
        pass

    def Internal_Redo(self, *args): #cannot find CLR method
        """ Internal_Redo(self: GH_GenericObjectAction, doc: GH_Document) """
        pass

    def Internal_Undo(self, *args): #cannot find CLR method
        """ Internal_Undo(self: GH_GenericObjectAction, doc: GH_Document) """
        pass

    def Serialize(self, *args): #cannot find CLR method
        """ Serialize(self: GH_ArchivedUndoAction, obj: GH_ISerializable) """
        pass

    def SerializeToByteArray(self, *args): #cannot find CLR method
        """ SerializeToByteArray(self: GH_ArchivedUndoAction, obj: GH_ISerializable) -> Array[Byte] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, obj):
        """ __new__(cls: type, obj: IGH_DocumentObject) """
        pass

    ExpiresSolution = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExpiresSolution(self: GH_GenericObjectAction) -> bool

"""


    m_data = None


class GH_HiddenAction(GH_ObjectUndoAction, IGH_UndoAction, GH_ISerializable):
    """ GH_HiddenAction(obj: IGH_ActiveObject) """
    def Internal_Redo(self, *args): #cannot find CLR method
        """ Internal_Redo(self: GH_ObjectUndoAction, doc: GH_Document) """
        pass

    def Internal_Undo(self, *args): #cannot find CLR method
        """ Internal_Undo(self: GH_ObjectUndoAction, doc: GH_Document) """
        pass

    def Object_Redo(self, *args): #cannot find CLR method
        """ Object_Redo(self: GH_HiddenAction, doc: GH_Document, obj: IGH_DocumentObject) """
        pass

    def Object_Undo(self, *args): #cannot find CLR method
        """ Object_Undo(self: GH_HiddenAction, doc: GH_Document, obj: IGH_DocumentObject) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, obj):
        """ __new__(cls: type, obj: IGH_ActiveObject) """
        pass

    ExpiresDisplay = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExpiresDisplay(self: GH_HiddenAction) -> bool

"""



class GH_IconDisplayAction(GH_ObjectUndoAction, IGH_UndoAction, GH_ISerializable):
    """ GH_IconDisplayAction(obj: IGH_DocumentObject) """
    def Internal_Redo(self, *args): #cannot find CLR method
        """ Internal_Redo(self: GH_ObjectUndoAction, doc: GH_Document) """
        pass

    def Internal_Undo(self, *args): #cannot find CLR method
        """ Internal_Undo(self: GH_ObjectUndoAction, doc: GH_Document) """
        pass

    def Object_Redo(self, *args): #cannot find CLR method
        """ Object_Redo(self: GH_IconDisplayAction, doc: GH_Document, obj: IGH_DocumentObject) """
        pass

    def Object_Undo(self, *args): #cannot find CLR method
        """ Object_Undo(self: GH_IconDisplayAction, doc: GH_Document, obj: IGH_DocumentObject) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, obj):
        """ __new__(cls: type, obj: IGH_DocumentObject) """
        pass


class GH_IconOverrideAction(GH_ObjectUndoAction, IGH_UndoAction, GH_ISerializable):
    """ GH_IconOverrideAction(obj: IGH_DocumentObject) """
    def Internal_Redo(self, *args): #cannot find CLR method
        """ Internal_Redo(self: GH_ObjectUndoAction, doc: GH_Document) """
        pass

    def Internal_Undo(self, *args): #cannot find CLR method
        """ Internal_Undo(self: GH_ObjectUndoAction, doc: GH_Document) """
        pass

    def Object_Redo(self, *args): #cannot find CLR method
        """ Object_Redo(self: GH_IconOverrideAction, doc: GH_Document, obj: IGH_DocumentObject) """
        pass

    def Object_Undo(self, *args): #cannot find CLR method
        """ Object_Undo(self: GH_IconOverrideAction, doc: GH_Document, obj: IGH_DocumentObject) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, obj):
        """ __new__(cls: type, obj: IGH_DocumentObject) """
        pass


class GH_LayoutAction(GH_ObjectUndoAction, IGH_UndoAction, GH_ISerializable):
    """ GH_LayoutAction(obj: IGH_DocumentObject) """
    def Internal_Redo(self, *args): #cannot find CLR method
        """ Internal_Redo(self: GH_ObjectUndoAction, doc: GH_Document) """
        pass

    def Internal_Undo(self, *args): #cannot find CLR method
        """ Internal_Undo(self: GH_ObjectUndoAction, doc: GH_Document) """
        pass

    def Object_Redo(self, *args): #cannot find CLR method
        """ Object_Redo(self: GH_LayoutAction, doc: GH_Document, obj: IGH_DocumentObject) """
        pass

    def Object_Undo(self, *args): #cannot find CLR method
        """ Object_Undo(self: GH_LayoutAction, doc: GH_Document, obj: IGH_DocumentObject) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, obj):
        """ __new__(cls: type, obj: IGH_DocumentObject) """
        pass


class GH_LockedAction(GH_ObjectUndoAction, IGH_UndoAction, GH_ISerializable):
    """ GH_LockedAction(obj: IGH_ActiveObject) """
    def Internal_Redo(self, *args): #cannot find CLR method
        """ Internal_Redo(self: GH_ObjectUndoAction, doc: GH_Document) """
        pass

    def Internal_Undo(self, *args): #cannot find CLR method
        """ Internal_Undo(self: GH_ObjectUndoAction, doc: GH_Document) """
        pass

    def Object_Redo(self, *args): #cannot find CLR method
        """ Object_Redo(self: GH_LockedAction, doc: GH_Document, obj: IGH_DocumentObject) """
        pass

    def Object_Undo(self, *args): #cannot find CLR method
        """ Object_Undo(self: GH_LockedAction, doc: GH_Document, obj: IGH_DocumentObject) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, obj):
        """ __new__(cls: type, obj: IGH_ActiveObject) """
        pass

    ExpiresSolution = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExpiresSolution(self: GH_LockedAction) -> bool

"""



class GH_NickNameAction(GH_ObjectUndoAction, IGH_UndoAction, GH_ISerializable):
    """ GH_NickNameAction(obj: IGH_DocumentObject) """
    def Internal_Redo(self, *args): #cannot find CLR method
        """ Internal_Redo(self: GH_ObjectUndoAction, doc: GH_Document) """
        pass

    def Internal_Undo(self, *args): #cannot find CLR method
        """ Internal_Undo(self: GH_ObjectUndoAction, doc: GH_Document) """
        pass

    def Object_Redo(self, *args): #cannot find CLR method
        """ Object_Redo(self: GH_NickNameAction, doc: GH_Document, obj: IGH_DocumentObject) """
        pass

    def Object_Undo(self, *args): #cannot find CLR method
        """ Object_Undo(self: GH_NickNameAction, doc: GH_Document, obj: IGH_DocumentObject) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, obj):
        """ __new__(cls: type, obj: IGH_DocumentObject) """
        pass


class GH_PersistentDataAction(GH_ObjectUndoAction, IGH_UndoAction, GH_ISerializable):
    """ GH_PersistentDataAction[T](obj: GH_PersistentParam[T]) """
    def Internal_Redo(self, *args): #cannot find CLR method
        """ Internal_Redo(self: GH_ObjectUndoAction, doc: GH_Document) """
        pass

    def Internal_Undo(self, *args): #cannot find CLR method
        """ Internal_Undo(self: GH_ObjectUndoAction, doc: GH_Document) """
        pass

    def Object_Redo(self, *args): #cannot find CLR method
        """ Object_Redo(self: GH_PersistentDataAction[T], doc: GH_Document, obj: IGH_DocumentObject) """
        pass

    def Object_Undo(self, *args): #cannot find CLR method
        """ Object_Undo(self: GH_PersistentDataAction[T], doc: GH_Document, obj: IGH_DocumentObject) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, obj):
        """ __new__(cls: type, obj: GH_PersistentParam[T]) """
        pass

    ExpiresSolution = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExpiresSolution(self: GH_PersistentDataAction[T]) -> bool

"""



class GH_PivotAction(GH_ObjectUndoAction, IGH_UndoAction, GH_ISerializable):
    """ GH_PivotAction(obj: IGH_DocumentObject) """
    def Internal_Redo(self, *args): #cannot find CLR method
        """ Internal_Redo(self: GH_ObjectUndoAction, doc: GH_Document) """
        pass

    def Internal_Undo(self, *args): #cannot find CLR method
        """ Internal_Undo(self: GH_ObjectUndoAction, doc: GH_Document) """
        pass

    def Object_Redo(self, *args): #cannot find CLR method
        """ Object_Redo(self: GH_PivotAction, doc: GH_Document, obj: IGH_DocumentObject) """
        pass

    def Object_Undo(self, *args): #cannot find CLR method
        """ Object_Undo(self: GH_PivotAction, doc: GH_Document, obj: IGH_DocumentObject) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, obj):
        """ __new__(cls: type, obj: IGH_DocumentObject) """
        pass


class GH_RemoveObjectAction(GH_ArchivedUndoAction, IGH_UndoAction, GH_ISerializable):
    """ GH_RemoveObjectAction(obj: IGH_DocumentObject) """
    def Deserialize(self, *args): #cannot find CLR method
        """ Deserialize(self: GH_ArchivedUndoAction, obj: GH_ISerializable) """
        pass

    def Internal_Redo(self, *args): #cannot find CLR method
        """ Internal_Redo(self: GH_RemoveObjectAction, doc: GH_Document) """
        pass

    def Internal_Undo(self, *args): #cannot find CLR method
        """ Internal_Undo(self: GH_RemoveObjectAction, doc: GH_Document) """
        pass

    def Serialize(self, *args): #cannot find CLR method
        """ Serialize(self: GH_ArchivedUndoAction, obj: GH_ISerializable) """
        pass

    def SerializeToByteArray(self, *args): #cannot find CLR method
        """ SerializeToByteArray(self: GH_ArchivedUndoAction, obj: GH_ISerializable) -> Array[Byte] """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, obj):
        """ __new__(cls: type, obj: IGH_DocumentObject) """
        pass

    ExpiresSolution = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExpiresSolution(self: GH_RemoveObjectAction) -> bool

"""


    m_data = None


class GH_RemoveStateAction(GH_ArchivedUndoAction, IGH_UndoAction, GH_ISerializable):
    """ GH_RemoveStateAction(index: int, state: GH_State) """
    def Deserialize(self, *args): #cannot find CLR method
        """ Deserialize(self: GH_ArchivedUndoAction, obj: GH_ISerializable) """
        pass

    def Internal_Redo(self, *args): #cannot find CLR method
        """ Internal_Redo(self: GH_RemoveStateAction, doc: GH_Document) """
        pass

    def Internal_Undo(self, *args): #cannot find CLR method
        """ Internal_Undo(self: GH_RemoveStateAction, doc: GH_Document) """
        pass

    def Read(self, reader):
        """ Read(self: GH_RemoveStateAction, reader: GH_IReader) -> bool """
        pass

    def Serialize(self, *args): #cannot find CLR method
        """ Serialize(self: GH_ArchivedUndoAction, obj: GH_ISerializable) """
        pass

    def SerializeToByteArray(self, *args): #cannot find CLR method
        """ SerializeToByteArray(self: GH_ArchivedUndoAction, obj: GH_ISerializable) -> Array[Byte] """
        pass

    def Write(self, writer):
        """ Write(self: GH_RemoveStateAction, writer: GH_IWriter) -> bool """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, index, state):
        """ __new__(cls: type, index: int, state: GH_State) """
        pass

    m_data = None


class GH_WireAction(GH_UndoAction, IGH_UndoAction, GH_ISerializable):
    """ GH_WireAction(param: IGH_Param) """
    def Internal_Redo(self, *args): #cannot find CLR method
        """ Internal_Redo(self: GH_WireAction, doc: GH_Document) """
        pass

    def Internal_Undo(self, *args): #cannot find CLR method
        """ Internal_Undo(self: GH_WireAction, doc: GH_Document) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, param):
        """ __new__(cls: type, param: IGH_Param) """
        pass

    ExpiresSolution = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ExpiresSolution(self: GH_WireAction) -> bool

"""



class GH_WireDisplayAction(GH_ObjectUndoAction, IGH_UndoAction, GH_ISerializable):
    """ GH_WireDisplayAction(obj: IGH_Param) """
    def Internal_Redo(self, *args): #cannot find CLR method
        """ Internal_Redo(self: GH_ObjectUndoAction, doc: GH_Document) """
        pass

    def Internal_Undo(self, *args): #cannot find CLR method
        """ Internal_Undo(self: GH_ObjectUndoAction, doc: GH_Document) """
        pass

    def Object_Redo(self, *args): #cannot find CLR method
        """ Object_Redo(self: GH_WireDisplayAction, doc: GH_Document, obj: IGH_DocumentObject) """
        pass

    def Object_Undo(self, *args): #cannot find CLR method
        """ Object_Undo(self: GH_WireDisplayAction, doc: GH_Document, obj: IGH_DocumentObject) """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, obj):
        """ __new__(cls: type, obj: IGH_Param) """
        pass


