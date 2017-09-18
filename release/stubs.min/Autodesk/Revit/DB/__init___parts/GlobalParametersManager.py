class GlobalParametersManager(object,IDisposable):
 """ A class to access and query information about global parameters in Revit models. """
 @staticmethod
 def AreGlobalParametersAllowed(document):
  """
  AreGlobalParametersAllowed(document: Document) -> bool

  

   Tests whether global parameters are allowed in the given document.

  

   document: A revit document of interest.
  """
  pass
 def Dispose(self):
  """ Dispose(self: GlobalParametersManager) """
  pass
 @staticmethod
 def FindByName(document,name):
  """
  FindByName(document: Document,name: str) -> ElementId

  

   Finds whether a global parameter with the given name exists in the input 

    document.

  

  

   document: The document expected to contain the global parameter.

   name: Name of the global parameter

   Returns: ElementId of the parameter element,or InvalidElementId if it was not found.
  """
  pass
 @staticmethod
 def GetAllGlobalParameters(document):
  """
  GetAllGlobalParameters(document: Document) -> ISet[ElementId]

  

   Returns all global parameters available in the given document.

  

   document: The document containing the global parameters

   Returns: A collection of Element Ids of global parameter elements.
  """
  pass
 @staticmethod
 def GetGlobalParametersOrdered(document):
  """
  GetGlobalParametersOrdered(document: Document) -> IList[ElementId]

  

   Returns all global paramters in an ordered array.

  

   document: Document containing the requested global parameters

   Returns: An array of Element Ids of all Global Parameters in the document.
  """
  pass
 @staticmethod
 def IsUniqueName(document,name):
  """
  IsUniqueName(document: Document,name: str) -> bool

  

   Tests whether a name is unique among existing global parameters of a given 

    document.

  

  

   document: Document in which a new parameter is to be added.

   name: A name of a parameter being added.

   Returns: True if the given %name% does not exist yet among existing global parameters 

    nof the document; False otherwise.
  """
  pass
 @staticmethod
 def IsValidGlobalParameter(document,parameterId):
  """
  IsValidGlobalParameter(document: Document,parameterId: ElementId) -> bool

  

   Tests whether an ElementId is of a global parameter in the given document.

  

   document: The document containing the global parameter.

   parameterId: Id of a global parameter

   Returns: Returns True if the Id is of a valid global parameter; False otherwise.
  """
  pass
 @staticmethod
 def MoveParameterDownOrder(document,parameterId):
  """
  MoveParameterDownOrder(document: Document,parameterId: ElementId) -> bool

  

   Moves given paramerer Down in the current order.

  

   document: Document containing the give global parameter

   parameterId: The parameter to move Down

   Returns: Indicates whether the parameter could be moved Down in order or not.
  """
  pass
 @staticmethod
 def MoveParameterUpOrder(document,parameterId):
  """
  MoveParameterUpOrder(document: Document,parameterId: ElementId) -> bool

  

   Moves given paramerer Up in the current order.

  

   document: Document containing the give global parameter

   parameterId: The parameter to move up

   Returns: Indicates whether the parameter could be moved Up in order or not.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: GlobalParametersManager,disposing: bool) """
  pass
 @staticmethod
 def SortParameters(document,order):
  """
  SortParameters(document: Document,order: ParametersOrder)

   Sorts global parameters in the desired order.

  

   document: Document containing the global parameters to be sorted

   order: Desired sorting order
  """
  pass
 def __enter__(self,*args):
  """ __enter__(self: IDisposable) -> object """
  pass
 def __exit__(self,*args):
  """ __exit__(self: IDisposable,exc_type: object,exc_value: object,exc_back: object) """
  pass
 def __init__(self,*args):
  """ x.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signaturex.__init__(...) initializes x; see x.__class__.__doc__ for signature """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: GlobalParametersManager) -> bool



"""


