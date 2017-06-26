class DetailElementOrderUtils(object):
 """ A utility class that arranges the draw order of the detail objects. """
 @staticmethod
 def AreDetailElements(pDocument,pDBView,detailElementIds):
  """ AreDetailElements(pDocument: Document,pDBView: View,detailElementIds: ICollection[ElementId]) -> bool """
  pass
 @staticmethod
 def BringForward(pDocument,pDBView,*__args):
  """
  BringForward(pDocument: Document,pDBView: View,detailElementId: ElementId)
   Moves the given detail instance one step closer to the front of all other 
    detail instances in the view.
  
  
   pDocument: The document.
   pDBView: The view.
   detailElementId: The detail elementId to bring forward.
  BringForward(pDocument: Document,pDBView: View,detailElementIds: ICollection[ElementId])
  """
  pass
 @staticmethod
 def BringToFront(pDocument,pDBView,*__args):
  """
  BringToFront(pDocument: Document,pDBView: View,detailElementId: ElementId)
   Places the given detail instance in the front of all other detail instances in 
    the view.
  
  
   pDocument: The document.
   pDBView: The view.
   detailElementId: The detail elementId
  BringToFront(pDocument: Document,pDBView: View,detailElementIds: ICollection[ElementId])
  """
  pass
 @staticmethod
 def IsDetailElement(pDocument,pDBView,detailElementId):
  """
  IsDetailElement(pDocument: Document,pDBView: View,detailElementId: ElementId) -> bool
  
   Indicates if the given element is a detail element.
  
   pDocument: The document.
   pDBView: The view.
   detailElementId: The detail elementId
   Returns: True if it is a detail element,false otherwise.
  """
  pass
 @staticmethod
 def SendBackward(pDocument,pDBView,*__args):
  """
  SendBackward(pDocument: Document,pDBView: View,detailElementId: ElementId)
   Moves the given detail instance one step closer to the back of all other detail 
    instances in the view.
  
  
   pDocument: The document.
   pDBView: The view.
   detailElementId: The detail elementId to move backward.
  SendBackward(pDocument: Document,pDBView: View,detailElementIds: ICollection[ElementId])
  """
  pass
 @staticmethod
 def SendToBack(pDocument,pDBView,*__args):
  """
  SendToBack(pDocument: Document,pDBView: View,detailElementId: ElementId)
   Places the given detail instance behind all detail instances in the view.
  
   pDocument: The document.
   pDBView: The view.
   detailElementId: The detail elementId to send to back.
  SendToBack(pDocument: Document,pDBView: View,detailElementIds: ICollection[ElementId])
  """
  pass
 __all__=[
  'AreDetailElements',
  'BringForward',
  'BringToFront',
  'IsDetailElement',
  'SendBackward',
  'SendToBack',
 ]

