class ReferenceableViewUtils(object):
 """ Utilities related to reference views such as reference sections and reference callouts. """
 @staticmethod
 def ChangeReferencedView(document,referenceId,desiredViewId):
  """
  ChangeReferencedView(document: Document,referenceId: ElementId,desiredViewId: ElementId)

   Changes a particular reference view (such as a reference section or reference 

    callout) to refer to a different View.

  

  

   document: The document containing the elements.

   referenceId: The reference view that will be changed to refer to a different View.

   desiredViewId: The id of the View that the reference section or callout will refer to.
  """
  pass
 @staticmethod
 def GetReferencedViewId(document,referenceId):
  """
  GetReferencedViewId(document: Document,referenceId: ElementId) -> ElementId

  

   Gets the id of the view referenced by a reference view (such as a reference 

    section or reference callout).

  

  

   document: The document containing the elements.

   referenceId: The reference view that will be changed to refer to a different View.

   Returns: The id of the referenced view.
  """
  pass
 __all__=[
  'ChangeReferencedView',
  'GetReferencedViewId',
 ]

