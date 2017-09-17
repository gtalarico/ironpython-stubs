class JoinGeometryUtils(object):
 """ Utilities for joining and unjoining elements,and for managing the order in which elements are joined. """
 @staticmethod
 def AreElementsJoined(document,firstElement,secondElement):
  """
  AreElementsJoined(document: Document,firstElement: Element,secondElement: Element) -> bool
  
   Determines whether two elements are joined.
  
   document: The document containing the two elements.
   firstElement: The first element.
   secondElement: The second element.
   Returns: True if the two elements are joined.
  """
  pass
 @staticmethod
 def GetJoinedElements(document,element):
  """
  GetJoinedElements(document: Document,element: Element) -> ICollection[ElementId]
  
   Returns all elements joined to given element.
  
   document: The document containing the element.
   element: The element.
   Returns: The set of elements that are joined to the given element.
  """
  pass
 @staticmethod
 def IsCuttingElementInJoin(document,firstElement,secondElement):
  """
  IsCuttingElementInJoin(document: Document,firstElement: Element,secondElement: Element) -> bool
  
   Determines whether the first of two joined elements is cutting the second 
    element.
  
  
   document: The document containing the two elements.
   firstElement: The first element.
   secondElement: The second element.
   Returns: True if the secondElement is cut by the firstElement,false if the 
    secondElement is cut by the firstElement.
  """
  pass
 @staticmethod
 def JoinGeometry(document,firstElement,secondElement):
  """
  JoinGeometry(document: Document,firstElement: Element,secondElement: Element)
   Creates clean joins between two elements that share a common face.
  
   document: The document containing the two elements.
   firstElement: The first element to be joined.
   secondElement: The second element to be joined. This element must not be joined to the first 
    element.
  """
  pass
 @staticmethod
 def SwitchJoinOrder(document,firstElement,secondElement):
  """
  SwitchJoinOrder(document: Document,firstElement: Element,secondElement: Element)
   Reverses the order in which two elements are joined.
  
   document: The document containing the two elements.
   firstElement: The first element.
   secondElement: The second element. This element must be joined to the first element.
  """
  pass
 @staticmethod
 def UnjoinGeometry(document,firstElement,secondElement):
  """
  UnjoinGeometry(document: Document,firstElement: Element,secondElement: Element)
   Removes a join between two elements.
  
   document: The document containing the two elements.
   firstElement: The first element to be unjoined.
   secondElement: The second element to be unjoined. This element must be joined to the fist 
    element.
  """
  pass
 __all__=[
  'AreElementsJoined',
  'GetJoinedElements',
  'IsCuttingElementInJoin',
  'JoinGeometry',
  'SwitchJoinOrder',
  'UnjoinGeometry',
 ]

