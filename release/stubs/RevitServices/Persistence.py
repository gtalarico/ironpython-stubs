# encoding: utf-8
# module RevitServices.Persistence calls itself Persistence
# from RevitServices, Version=1.2.1.3083, Culture=neutral, PublicKeyToken=null
# by generator 1.145
# no doc
# no imports

# no functions
# classes

class DocumentManager(object):
    # no doc
    def DeleteElement(self, element):
        """ DeleteElement(self: DocumentManager, element: ElementUUID) """
        pass

    def ElementExistsInDocument(self, id):
        """ ElementExistsInDocument(self: DocumentManager, id: ElementUUID) -> bool """
        pass

    def ElementsOfCategory(self, category):
        """ ElementsOfCategory(self: DocumentManager, category: BuiltInCategory) -> IEnumerable[Element] """
        pass

    def ElementsOfType(self):
        """ ElementsOfType[T](self: DocumentManager) -> IEnumerable[T] """
        pass

    def HandleDocumentActivation(self, revitView):
        """ HandleDocumentActivation(self: DocumentManager, revitView: View) """
        pass

    @staticmethod
    def Regenerate():
        """ Regenerate() """
        pass

    ActiveDocumentHashCode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: ActiveDocumentHashCode(self: DocumentManager) -> int

"""

    CurrentDBDocument = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentDBDocument(self: DocumentManager) -> Document

"""

    CurrentUIApplication = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentUIApplication(self: DocumentManager) -> UIApplication

Set: CurrentUIApplication(self: DocumentManager) = value
"""

    CurrentUIDocument = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: CurrentUIDocument(self: DocumentManager) -> UIDocument

Set: CurrentUIDocument(self: DocumentManager) = value
"""


    Instance = None
    OnLogError = None


class ElementBinder(object):
    """ ElementBinder() """
    @staticmethod
    def CleanupAndSetElementForTrace(document, newElement):
        """ CleanupAndSetElementForTrace(document: Document, newElement: Element) """
        pass

    @staticmethod
    def GetElementAndTraceData(document):
        """ GetElementAndTraceData[(TElement, TId)](document: Document) -> Tuple[TElement, TId] """
        pass

    @staticmethod
    def GetElementFromTrace(document):
# Error generating skeleton for function GetElementFromTrace: Method must be called on a Type for which Type.IsGenericParameter is false.

    @staticmethod
    def GetElementIdFromTrace(document):
        """ GetElementIdFromTrace(document: Document) -> ElementId """
        pass

    @staticmethod
    def GetElementsFromTrace(document):
        """ GetElementsFromTrace[T](document: Document) -> IEnumerable[T] """
        pass

    @staticmethod
    def GetElementUUIDFromTrace(document):
        """ GetElementUUIDFromTrace(document: Document) -> ElementUUID """
        pass

    @staticmethod
    def GetElementUUIDsFromTrace(document):
        """ GetElementUUIDsFromTrace(document: Document) -> List[ElementUUID] """
        pass

    @staticmethod
    def GetIdForUUID(document, uuid):
        """ GetIdForUUID(document: Document, uuid: ElementUUID) -> ElementId """
        pass

    @staticmethod
    def GetNodesFromElementIds(ids, workspace, engine):
        """ GetNodesFromElementIds(ids: IEnumerable[ElementId], workspace: WorkspaceModel, engine: EngineController) -> IEnumerable[NodeModel] """
        pass

    @staticmethod
    def GetRawDataFromTrace():
        """ GetRawDataFromTrace() -> ISerializable """
        pass

    @staticmethod
    def SetElementForTrace(*__args):
        """ SetElementForTrace(elementId: ElementId, elementUUID: ElementUUID)SetElementForTrace(element: Element) """
        pass

    @staticmethod
    def SetElementFreezeState(workspace, node, engine):
        """ SetElementFreezeState(workspace: WorkspaceModel, node: NodeModel, engine: EngineController) """
        pass

    @staticmethod
    def SetElementsForTrace(elements):
        """ SetElementsForTrace(elements: IEnumerable[Element]) """
        pass

    @staticmethod
    def SetRawDataForTrace(data):
        """ SetRawDataForTrace(data: ISerializable) """
        pass

    IsEnabled = False


class ElementIDLifecycleManager(object):
    # no doc
    @staticmethod
    def DisposeInstance():
        """ DisposeInstance() """
        pass

    def GetFirstWrapper(self, id):
        """ GetFirstWrapper(self: ElementIDLifecycleManager[T], id: T) -> object """
        pass

    @staticmethod
    def GetInstance():
        """ GetInstance() -> ElementIDLifecycleManager[T] """
        pass

    def GetRegisteredCount(self, id):
        """ GetRegisteredCount(self: ElementIDLifecycleManager[T], id: T) -> int """
        pass

    def IsRevitDeleted(self, id):
        """ IsRevitDeleted(self: ElementIDLifecycleManager[T], id: T) -> bool """
        pass

    def NotifyOfRevitDeletion(self, id):
        """ NotifyOfRevitDeletion(self: ElementIDLifecycleManager[T], id: T) """
        pass

    def RegisterAsssociation(self, elementID, wrapper):
        """ RegisterAsssociation(self: ElementIDLifecycleManager[T], elementID: T, wrapper: object) """
        pass

    def ToString(self):
        """ ToString(self: ElementIDLifecycleManager[T]) -> str """
        pass

    def UnRegisterAssociation(self, elementID, wrapper):
        """ UnRegisterAssociation(self: ElementIDLifecycleManager[T], elementID: T, wrapper: object) -> int """
        pass


class ElementUUID(object):
    """
    ElementUUID()
    ElementUUID(uuid: str)
    """
    @staticmethod # known case of __new__
    def __new__(self, uuid=None):
        """
        __new__(cls: type)
        __new__(cls: type, uuid: str)
        """
        pass

    UUID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: UUID(self: ElementUUID) -> str

Set: UUID(self: ElementUUID) = value
"""



class MultipleSerializableId(object, ISerializable):
    """
    MultipleSerializableId()
    MultipleSerializableId(elements: IEnumerable[Element])
    MultipleSerializableId(info: SerializationInfo, context: StreamingContext)
    """
    def Equals(self, other):
        """ Equals(self: MultipleSerializableId, other: object) -> bool """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: MultipleSerializableId) -> int """
        pass

    def GetObjectData(self, info, context):
        """ GetObjectData(self: MultipleSerializableId, info: SerializationInfo, context: StreamingContext) """
        pass

    def isSubset(self, other):
        """ isSubset(self: MultipleSerializableId, other: MultipleSerializableId) -> bool """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *__args):
        """
        __new__(cls: type)
        __new__(cls: type, elements: IEnumerable[Element])
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IntIDs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IntIDs(self: MultipleSerializableId) -> List[int]

Set: IntIDs(self: MultipleSerializableId) = value
"""

    StringIDs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StringIDs(self: MultipleSerializableId) -> List[str]

Set: StringIDs(self: MultipleSerializableId) = value
"""



class SerializableId(object, ISerializable):
    """
    SerializableId()
    SerializableId(info: SerializationInfo, context: StreamingContext)
    """
    def Equals(self, other):
        """ Equals(self: SerializableId, other: object) -> bool """
        pass

    def GetHashCode(self):
        """ GetHashCode(self: SerializableId) -> int """
        pass

    def GetObjectData(self, info, context):
        """ GetObjectData(self: SerializableId, info: SerializationInfo, context: StreamingContext) """
        pass

    def __eq__(self, *args): #cannot find CLR method
        """ x.__eq__(y) <==> x==y """
        pass

    def __init__(self, *args): #cannot find CLR method
        """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
        pass

    @staticmethod # known case of __new__
    def __new__(self, info=None, context=None):
        """
        __new__(cls: type)
        __new__(cls: type, info: SerializationInfo, context: StreamingContext)
        """
        pass

    def __ne__(self, *args): #cannot find CLR method
        pass

    def __reduce_ex__(self, *args): #cannot find CLR method
        pass

    def __repr__(self, *args): #cannot find CLR method
        """ __repr__(self: object) -> str """
        pass

    IntID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IntID(self: SerializableId) -> int

Set: IntID(self: SerializableId) = value
"""

    StringID = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: StringID(self: SerializableId) -> str

Set: StringID(self: SerializableId) = value
"""



