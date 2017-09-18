class UIDocument(object,IDisposable):
 """
 An object that represents an Autodesk Revit project opened in the Revit user interface.

 

 UIDocument(document: Document)
 """
 def CanPlaceElementType(self,elementType):
  """
  CanPlaceElementType(self: UIDocument,elementType: ElementType) -> bool

  

   Verifies that the user can be prompted to place the input element type on the 

    current active view.

  

  

   elementType: The ElementType.

   Returns: True if the user can be prompted to place the input element type on the active 

    view,false otherwise.
  """
  pass
 def Dispose(self):
  """ Dispose(self: UIDocument) """
  pass
 def GetOpenUIViews(self):
  """
  GetOpenUIViews(self: UIDocument) -> IList[UIView]

  

   Get a list of all open view windows in the Revit user interface.
  """
  pass
 def GetPlacementTypes(self,familySymbol,pDBView):
  """
  GetPlacementTypes(self: UIDocument,familySymbol: FamilySymbol,pDBView: View) -> IList[FaceBasedPlacementType]

  

   Get a collection of valid placement types for input family symbol.

  

   familySymbol: The family symbol.

   pDBView: The view in which the family instance will be placed in.
  """
  pass
 @staticmethod
 def GetRevitUIFamilyLoadOptions():
  """
  GetRevitUIFamilyLoadOptions() -> IFamilyLoadOptions

  

   Return the option object that allows you to use Revit's dialog boxes to let the 

    user respond to questions that arise during loading of families.
  """
  pass
 def GetSketchGalleryOptions(self,familySymbol):
  """
  GetSketchGalleryOptions(self: UIDocument,familySymbol: FamilySymbol) -> IList[SketchGalleryOptions]

  

   Gets the valid sketch gallery options of a family symbol.

  

   familySymbol: The family symbol.

   Returns: The valid list of SketchGalleryOptions.
  """
  pass
 def PostRequestForElementTypePlacement(self,elementType):
  """
  PostRequestForElementTypePlacement(self: UIDocument,elementType: ElementType)

   Places a request on Revit's command queue for the user to place instances of 

    the specified ElementType.  This does not execute immediately,

     but instead 

    when control returns to Revit from the current API context.

  

  

   elementType: The ElementType of which instances are to be placed.
  """
  pass
 def PromptForFamilyInstancePlacement(self,familySymbol,options=None):
  """
  PromptForFamilyInstancePlacement(self: UIDocument,familySymbol: FamilySymbol)

   Prompts the user to place instances of the specified FamilySymbol.

  

   familySymbol: The FamilySymbol.

  PromptForFamilyInstancePlacement(self: UIDocument,familySymbol: FamilySymbol,options: PromptForFamilyInstancePlacementOptions)

   Prompts the user to place instances of the specified FamilySymbol.

  

   familySymbol: The FamilySymbol.

   options: The PromptForFamilyInstancePlacementOptions,to place the family instance 

    according to the options.
  """
  pass
 def PromptToMatchElementType(self,elementType):
  """
  PromptToMatchElementType(self: UIDocument,elementType: ElementType)

   Prompts the user to select elements to change them to the input type.

  

   elementType: The ElementType applied to selected instances.
  """
  pass
 def PromptToPlaceElementTypeOnLegendView(self,elementType):
  """
  PromptToPlaceElementTypeOnLegendView(self: UIDocument,elementType: ElementType)

   Prompts the user to place an element type onto a legend view.

  

   elementType: The ElementType of which instances are to be placed.
  """
  pass
 def PromptToPlaceViewOnSheet(self,view,allowReplaceExistingSheetViewport):
  """
  PromptToPlaceViewOnSheet(self: UIDocument,view: View,allowReplaceExistingSheetViewport: bool)

   Prompts the user to place a specified view onto a sheet.

  

   view: The view to insert onto a sheet.

   allowReplaceExistingSheetViewport: A indicator which allows the user to replace the existing viewport.

     If 

    true,the viewport representing this view will be replaced by the new viewport 

    created during placement.

     If the view is allowed only to be on one sheet,

    this will remove the viewport from the old sheet.

     If the view is allowed to 

    be on multiple sheets,and the view is currently placed on the active sheet,

    

     the old viewport on this sheet will be replaced. 

     If false,if the view is 

    only allowed to be on one sheet,

     or if the view is allowed to be on 

    multiple sheets but is already on the active sheet,an exception will be 

    thrown.
  """
  pass
 def RefreshActiveView(self):
  """
  RefreshActiveView(self: UIDocument)

   Refresh the display of the active view in the active document.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: UIDocument,disposing: bool) """
  pass
 def RequestViewChange(self,view):
  """
  RequestViewChange(self: UIDocument,view: View)

   Requests an asynchronous change of the active view in the currently active 

    document.

  

  

   view: The View.
  """
  pass
 def SaveAndClose(self):
  """
  SaveAndClose(self: UIDocument) -> bool

  

   Close the document,prompting the user for saving it when necessary.

   Returns: False if closing procedure fails or if saving of a modified document was 

    requested but failed. 

  Also returns False if closing is cancelled by an 

    external application during 'DocumentClosing' event. 

  When function succeeds,

    True is returned.
  """
  pass
 def SaveAs(self,options=None):
  """
  SaveAs(self: UIDocument)

   Saves the document to a file name obtained from the Revit user without 

    prompting the user to overwrite file if it exists.

  

  SaveAs(self: UIDocument,options: UISaveAsOptions)

   Saves the document to a file name obtained from the Revit user optionally 

    prompting the user to overwrite file if it exists.

  

  

   options: UI options for the SaveAs operation.
  """
  pass
 def setUIDocument(self,*args):
  """ setUIDocument(self: UIDocument,pUIDocument: UIDocument*) """
  pass
 def ShowElements(self,*__args):
  """
  ShowElements(self: UIDocument,element: Element)

   Shows the element by zoom to fit.

  

   element: Element that will be shown.

  ShowElements(self: UIDocument,elementId: ElementId)

   Shows the element by zoom to fit.

  

   elementId: Element id that will be shown.

  ShowElements(self: UIDocument,elementIds: ICollection[ElementId])ShowElements(self: UIDocument,elements: ElementSet)

   Shows the elements by zoom to fit.

  

   elements: The set of elements that will be shown.
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
 @staticmethod
 def __new__(self,document):
  """ __new__(cls: type,document: Document) """
  pass
 def __repr__(self,*args):
  """ __repr__(self: object) -> str """
  pass
 ActiveGraphicalView=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The currently active graphical view of the currently active document.



Get: ActiveGraphicalView(self: UIDocument) -> View



"""

 ActiveView=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The currently active view of the currently active document.



Get: ActiveView(self: UIDocument) -> View



Set: ActiveView(self: UIDocument)=value

"""

 Application=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Retrieves an object that represents the current Application.



Get: Application(self: UIDocument) -> UIApplication



"""

 Document=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the database level document represented by this UI-level document.



Get: Document(self: UIDocument) -> Document



"""

 IsValidObject=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Specifies whether the .NET object represents a valid Revit entity.



Get: IsValidObject(self: UIDocument) -> bool



"""

 Selection=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Retrieve the currently selected Elements in Autodesk Revit.



Get: Selection(self: UIDocument) -> Selection



"""


