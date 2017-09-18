class SolidSolidCutUtils(object):
 """ Exposes utilities which can cause one solid to cut another. """
 @staticmethod
 def AddCutBetweenSolids(document,solidToBeCut,cuttingSolid,splitFacesOfCuttingSolid=None):
  """
  AddCutBetweenSolids(document: Document,solidToBeCut: Element,cuttingSolid: Element)

   Adds a solid-solid cut for the two elements.

  

   document: The document containing the two elements.

   solidToBeCut: The solid to be cut.

   cuttingSolid: The cutting solid.

  AddCutBetweenSolids(document: Document,solidToBeCut: Element,cuttingSolid: Element,splitFacesOfCuttingSolid: bool)

   Adds a solid-solid cut for the two elements with the option to control 

    splitting of faces of the cutting solid.

  

  

   document: The document containing the two elements.

   solidToBeCut: The solid to be cut.

   cuttingSolid: The cutting solid.

   splitFacesOfCuttingSolid: True to split faces of cutting solid where it intersects the solid to be cut,

    false otherwise.
  """
  pass
 @staticmethod
 def CanElementCutElement(cuttingElement,cutElement,reason):
  """
  CanElementCutElement(cuttingElement: Element,cutElement: Element) -> (bool,CutFailureReason)

  

   Verifies if the cutting element can add a solid cut to the target element.

  

   cuttingElement: The cutting element.

   cutElement: The element to be cut.

   Returns: True if the cutting element can add a solid cut to the target element,false 

    otherwise.
  """
  pass
 @staticmethod
 def CutExistsBetweenElements(first,second,firstCutsSecond):
  """
  CutExistsBetweenElements(first: Element,second: Element) -> (bool,bool)

  

   Checks that if there is a solid-solid cut between two elements.

  

   first: The solid being cut or the cutting solid.

   second: The solid being cut or the cutting solid.

   Returns: True if there is a solid-solid cut between the input elements,false otherwise.
  """
  pass
 @staticmethod
 def GetCuttingSolids(element):
  """
  GetCuttingSolids(element: Element) -> ICollection[ElementId]

  

   Gets all the solids which cut the input element.

  

   element: The input element.

   Returns: The ids of the solids which cut the input element.
  """
  pass
 @staticmethod
 def GetSolidsBeingCut(element):
  """
  GetSolidsBeingCut(element: Element) -> ICollection[ElementId]

  

   Get all the solids which are cut by the input element.

  

   element: The input element.

   Returns: The ids of the solids which are cut by the input element.
  """
  pass
 @staticmethod
 def IsAllowedForSolidCut(element):
  """
  IsAllowedForSolidCut(element: Element) -> bool

  

   Validates that the element is eligible for a solid-solid cut.

  

   element: The solid to be cut or the cutting solid.

   Returns: True if the input element can participate in a solid-solid cut.  False 

    otherwise.
  """
  pass
 @staticmethod
 def IsElementFromAppropriateContext(element):
  """
  IsElementFromAppropriateContext(element: Element) -> bool

  

   Validates that the element is from an appropriate document.

  

   element: The solid to be cut or the cutting solid.

   Returns: True if the element is from an appropriate document for solid-solid cuts,false 

    otherwise.
  """
  pass
 @staticmethod
 def RemoveCutBetweenSolids(document,first,second):
  """
  RemoveCutBetweenSolids(document: Document,first: Element,second: Element)

   Removes the solid-solid cut between the two elements if it exists.

  

   document: The document containing the two elements

   first: The solid being cut or the cutting solid.

   second: The solid being cut or the cutting solid.
  """
  pass
 @staticmethod
 def SplitFacesOfCuttingSolid(first,second,split):
  """
  SplitFacesOfCuttingSolid(first: Element,second: Element,split: bool)

   Causes the faces of the cutting element where it intersects the element it is 

    cutting to be split or unsplit.

  

  

   first: The solid being cut or the cutting solid

   second: The solid being cut or the cutting solid

   split: True to split the faces of intersection,false to unsplit them.
  """
  pass
 __all__=[
  'AddCutBetweenSolids',
  'CanElementCutElement',
  'CutExistsBetweenElements',
  'GetCuttingSolids',
  'GetSolidsBeingCut',
  'IsAllowedForSolidCut',
  'IsElementFromAppropriateContext',
  'RemoveCutBetweenSolids',
  'SplitFacesOfCuttingSolid',
 ]

