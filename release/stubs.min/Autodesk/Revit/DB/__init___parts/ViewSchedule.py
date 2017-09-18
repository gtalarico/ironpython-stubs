class ViewSchedule(TableView,IDisposable):
 """ A schedule view. """
 def CanGroupHeaders(self,top,left,bottom,right):
  """
  CanGroupHeaders(self: ViewSchedule,top: int,left: int,bottom: int,right: int) -> bool

  

   Indicates if selected headers can be grouped for this schedule.

  

   top: The index of the top row of the selected headers.

   left: The index of the left column of the selected headers.

   bottom: The index of the bottom row of the selected headers.

   right: The index of the right column of the selected headers.

   Returns: True if the selected headers can be grouped,false otherwise.
  """
  pass
 def CanUngroupHeaders(self,top,left,bottom,right):
  """
  CanUngroupHeaders(self: ViewSchedule,top: int,left: int,bottom: int,right: int) -> bool

  

   Indicates if selected headers can be ungrouped.

  

   top: The index of the top row of the selected headers.

   left: The index of the left column of the selected headers.

   bottom: The index of the bottom row of the selected headers.

   right: The index of the right column of the selected headers.

   Returns: True if the selected headers can be grouped,false otherwise.
  """
  pass
 @staticmethod
 def CreateKeynoteLegend(document):
  """
  CreateKeynoteLegend(document: Document) -> ViewSchedule

  

   Creates a keynote legend.

  

   document: The document to which the new schedule will be added.

   Returns: The newly created schedule.
  """
  pass
 @staticmethod
 def CreateKeySchedule(document,categoryId):
  """
  CreateKeySchedule(document: Document,categoryId: ElementId) -> ViewSchedule

  

   Create a key schedule.

  

   document: The document to which the new schedule will be added.

   categoryId: The ID of the category of elements that the schedule's keys will be associated 

    with.

  

   Returns: The newly created schedule.
  """
  pass
 @staticmethod
 def CreateMaterialTakeoff(document,categoryId):
  """
  CreateMaterialTakeoff(document: Document,categoryId: ElementId) -> ViewSchedule

  

   Creates a material takeoff.

  

   document: The document to which the new schedule will be added.

   categoryId: The ID of the category whose elements will be included in the schedule,

     or 

    InvalidElementId for a multi-category schedule.

  

   Returns: The newly created schedule.
  """
  pass
 @staticmethod
 def CreateNoteBlock(document,familyId):
  """
  CreateNoteBlock(document: Document,familyId: ElementId) -> ViewSchedule

  

   Creates a note block.

  

   document: The document to which the new schedule will be added.

   familyId: The ID of the family whose elements will be included in the schedule.

   Returns: The newly created schedule.
  """
  pass
 @staticmethod
 def CreateRevisionSchedule(document):
  """
  CreateRevisionSchedule(document: Document) -> ViewSchedule

  

   Creates a revision schedule.

  

   document: The titleblock family document to which the new schedule will be added.

   Returns: The newly created schedule.
  """
  pass
 @staticmethod
 def CreateSchedule(document,categoryId,areaSchemeId=None):
  """
  CreateSchedule(document: Document,categoryId: ElementId) -> ViewSchedule

  

   Creates a regular schedule.

  

   document: The document to which the new schedule will be added.

   categoryId: The ID of the category whose elements will be included in the schedule,or 

    InvalidElementId for a multi-category schedule.

  

   Returns: The newly created schedule.

  CreateSchedule(document: Document,categoryId: ElementId,areaSchemeId: ElementId) -> ViewSchedule

  

   Creates a regular schedule that can relate to a specific area scheme.

  

   document: The document to which the new schedule will be added.

   categoryId: The ID of the category whose elements will be included in the schedule,or 

    InvalidElementId for a multi-category schedule.

  

   areaSchemeId: The ID of an area scheme in an area schedule,InvalidElementId otherwise.

   Returns: The newly created schedule.
  """
  pass
 @staticmethod
 def CreateSheetList(document):
  """
  CreateSheetList(document: Document) -> ViewSchedule

  

   Creates a sheet list.

  

   document: The document to which the new schedule will be added.

   Returns: The newly created schedule.
  """
  pass
 @staticmethod
 def CreateViewList(document):
  """
  CreateViewList(document: Document) -> ViewSchedule

  

   Creates a view list.

  

   document: The document to which the new schedule will be added.

   Returns: The newly created schedule.
  """
  pass
 def Dispose(self):
  """ Dispose(self: Element,A_0: bool) """
  pass
 def Export(self,folder,name,options):
  """
  Export(self: ViewSchedule,folder: str,name: str,options: ViewScheduleExportOptions)

   Exports the schedule data to a text file.

  

   folder: Path to the location where the file will be saved.

   name: Name of file.

   options: Options that relate to schedule export.
  """
  pass
 def getBoundingBox(self,*args):
  """ getBoundingBox(self: View,view: View) -> BoundingBoxXYZ """
  pass
 @staticmethod
 def GetDefaultNameForKeynoteLegend(document):
  """
  GetDefaultNameForKeynoteLegend(document: Document) -> str

  

   Gets the default view name that will be used when creating a keynote legend.

  

   document: The document to which the new schedule will be added.

   Returns: The default view name.
  """
  pass
 @staticmethod
 def GetDefaultNameForKeySchedule(document,categoryId):
  """
  GetDefaultNameForKeySchedule(document: Document,categoryId: ElementId) -> str

  

   Gets the default view name that will be used when creating a key schedule.

  

   document: The document to which the new schedule will be added.

   categoryId: The ID of the category of elements that the schedule's keys will be associated 

    with.

  

   Returns: The default view name.
  """
  pass
 @staticmethod
 def GetDefaultNameForMaterialTakeoff(document,categoryId):
  """
  GetDefaultNameForMaterialTakeoff(document: Document,categoryId: ElementId) -> str

  

   Gets the default view name that will be used when creating a material takeoff.

  

   document: The document to which the new schedule will be added.

   categoryId: The ID of the category whose elements will be included in the schedule,or 

    InvalidElementId for a multi-category schedule.

  

   Returns: The default view name.
  """
  pass
 @staticmethod
 def GetDefaultNameForNoteBlock(document):
  """
  GetDefaultNameForNoteBlock(document: Document) -> str

  

   Gets the default view name that will be used when creating a note block.

  

   document: The document to which the new schedule will be added.

   Returns: The default view name.
  """
  pass
 @staticmethod
 def GetDefaultNameForRevisionSchedule(document):
  """
  GetDefaultNameForRevisionSchedule(document: Document) -> str

  

   Gets the default view name that will be used when creating a revision schedule.

  

   document: The titleblock family document to which the new schedule will be added.

   Returns: The default view name.
  """
  pass
 @staticmethod
 def GetDefaultNameForSchedule(document,categoryId,areaSchemeId=None):
  """
  GetDefaultNameForSchedule(document: Document,categoryId: ElementId) -> str

  

   Gets the default view name that will be used when creating a regular schedule.

  

   document: The document to which the new schedule will be added.

   categoryId: The ID of the category whose elements will be included in the schedule,or 

    InvalidElementId for a multi-category schedule.

  

   Returns: The default view name.

  GetDefaultNameForSchedule(document: Document,categoryId: ElementId,areaSchemeId: ElementId) -> str

  

   Gets the default view name that will be used when creating a schedule.

  

   document: The document to which the new schedule will be added.

   categoryId: The ID of the category whose elements will be included in the schedule,or 

    InvalidElementId for a multi-category schedule.

  

   areaSchemeId: The ID of an area scheme in an area schedule,InvalidElementId otherwise.

   Returns: The default view name.
  """
  pass
 @staticmethod
 def GetDefaultNameForSheetList(document):
  """
  GetDefaultNameForSheetList(document: Document) -> str

  

   Gets the default view name that will be used when creating a sheet list.

  

   document: The document to which the new schedule will be added.

   Returns: The default view name.
  """
  pass
 @staticmethod
 def GetDefaultNameForViewList(document):
  """
  GetDefaultNameForViewList(document: Document) -> str

  

   Gets the default view name that will be used when creating a view list.

  

   document: The document to which the new schedule will be added.

   Returns: The default view name.
  """
  pass
 @staticmethod
 def GetDefaultParameterNameForKeySchedule(document,categoryId):
  """
  GetDefaultParameterNameForKeySchedule(document: Document,categoryId: ElementId) -> str

  

   Gets the default parameter name that will be used when creating a key schedule.

  

   document: The document to which the new schedule will be added.

   categoryId: The ID of the category of elements that the schedule's keys will be associated 

    with.

  

   Returns: The default parameter name.
  """
  pass
 def GetTableData(self):
  """
  GetTableData(self: ViewSchedule) -> TableData

  

   Gets the writable table data object.

   Returns: The schedule data object.
  """
  pass
 @staticmethod
 def GetValidCategoriesForKeySchedule():
  """
  GetValidCategoriesForKeySchedule() -> ICollection[ElementId]

  

   Gets a list of categories that can be used for a key schedule.

   Returns: The IDs of all valid categories.
  """
  pass
 @staticmethod
 def GetValidCategoriesForMaterialTakeoff():
  """
  GetValidCategoriesForMaterialTakeoff() -> ICollection[ElementId]

  

   Gets a list of categories that can be used for a material takeoff.

   Returns: The IDs of all valid categories.
  """
  pass
 @staticmethod
 def GetValidCategoriesForSchedule():
  """
  GetValidCategoriesForSchedule() -> ICollection[ElementId]

  

   Gets a list of categories that can be used for a regular schedule.

   Returns: The IDs of all valid categories.
  """
  pass
 @staticmethod
 def GetValidFamiliesForNoteBlock(document):
  """
  GetValidFamiliesForNoteBlock(document: Document) -> ICollection[ElementId]

  

   Gets a list of families that can be used for a note block.

  

   document: The document.

   Returns: The IDs of all valid families.
  """
  pass
 def GroupHeaders(self,top,left,bottom,right,caption=None):
  """
  GroupHeaders(self: ViewSchedule,top: int,left: int,bottom: int,right: int)

   Groups schedule header cells.

  

   top: The index of the top row of the selected headers.

   left: The index of the left column of the selected headers.

   bottom: The index of the bottom row of the selected headers.

   right: The index of the right column of the selected headers.

  GroupHeaders(self: ViewSchedule,top: int,left: int,bottom: int,right: int,caption: str)

   Groups schedule header cells.

  

   top: The index of the top row of the selected headers.

   left: The index of the left column of the selected headers.

   bottom: The index of the bottom row of the selected headers.

   right: The index of the right column of the selected headers.

   caption: The header caption.
  """
  pass
 def HasImageField(self):
  """
  HasImageField(self: ViewSchedule) -> bool

  

   Checks whether the schedule definition includes any image-related fields and if 

    any elements in the schedule actually have images in those fields.

  

   Returns: True if the schedule has at least one image field showing at least one image,

    false otherwise.
  """
  pass
 def IsDataOutOfDate(self):
  """
  IsDataOutOfDate(self: ViewSchedule) -> bool

  

   Indicates whether the schedule data is out of date.

   Returns: True if the schedule data is out of date,false otherwise.
  """
  pass
 @staticmethod
 def IsValidCategoryForKeySchedule(categoryId):
  """
  IsValidCategoryForKeySchedule(categoryId: ElementId) -> bool

  

   Checks whether a category can be used for a key schedule.

  

   categoryId: The category ID to check.

   Returns: True if the category can be used for a key schedule,

     false otherwise.
  """
  pass
 @staticmethod
 def IsValidCategoryForMaterialTakeoff(categoryId):
  """
  IsValidCategoryForMaterialTakeoff(categoryId: ElementId) -> bool

  

   Checks whether a category can be used for a material takeoff.

  

   categoryId: The category ID to check.

   Returns: True if the category can be used for a material takeoff,

     false otherwise.
  """
  pass
 @staticmethod
 def IsValidCategoryForSchedule(categoryId):
  """
  IsValidCategoryForSchedule(categoryId: ElementId) -> bool

  

   Checks whether a category can be used for a regular schedule.

  

   categoryId: The category ID to check.

   Returns: True if the category can be used for a regular schedule,

     false otherwise.
  """
  pass
 @staticmethod
 def IsValidFamilyForNoteBlock(document,familyId):
  """
  IsValidFamilyForNoteBlock(document: Document,familyId: ElementId) -> bool

  

   Checks whether a family can be used for a note block.

  

   document: The document.

   familyId: The family ID to check.

   Returns: True if the family can be used for a note block,

     false otherwise.
  """
  pass
 def IsValidTextTypeId(self,textTypeId):
  """
  IsValidTextTypeId(self: ViewSchedule,textTypeId: ElementId) -> bool

  

   Identifies if the input id represents a valid text type id for use in the 

    schedule properties.

  

  

   textTypeId: The element id of the text type.
  """
  pass
 def RefreshData(self):
  """
  RefreshData(self: ViewSchedule) -> bool

  

   Rebuilds the schedule data if it is out of date.

   Returns: True if the data is up to date after the refresh.
  """
  pass
 def ReleaseUnmanagedResources(self,*args):
  """ ReleaseUnmanagedResources(self: Element,disposing: bool) """
  pass
 def RestoreImageSize(self):
  """
  RestoreImageSize(self: ViewSchedule)

   Restores all images to their original sizes.
  """
  pass
 def setElementType(self,*args):
  """ setElementType(self: Element,type: ElementType,incompatibleExceptionMessage: str) """
  pass
 def UngroupHeaders(self,top,left,bottom,right):
  """
  UngroupHeaders(self: ViewSchedule,top: int,left: int,bottom: int,right: int)

   Ungroups selected headers of schedule.

  

   top: The index of the top row of the selected headers.

   left: The index of the left column of the selected headers.

   bottom: The index of the bottom row of the selected headers.

   right: The index of the right column of the selected headers.
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
 BodyTextTypeId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Defines the default text style used for the data section of the schedule.



Get: BodyTextTypeId(self: ViewSchedule) -> ElementId



Set: BodyTextTypeId(self: ViewSchedule)=value

"""

 Definition=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The primary ScheduleDefinition.



Get: Definition(self: ViewSchedule) -> ScheduleDefinition



"""

 EmbeddedDefinition=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The embedded ScheduleDefinition.



Get: EmbeddedDefinition(self: ViewSchedule) -> ScheduleDefinition



"""

 HeaderTextTypeId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Defines the default text style used in the column headers in the body section of the schedule.



Get: HeaderTextTypeId(self: ViewSchedule) -> ElementId



Set: HeaderTextTypeId(self: ViewSchedule)=value

"""

 ImageRowHeight=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Defines the image row height in the schedule.



Get: ImageRowHeight(self: ViewSchedule) -> float



Set: ImageRowHeight(self: ViewSchedule)=value

"""

 IsInternalKeynoteSchedule=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies if this ViewSchedule is an internal schedule used when keynotes are filtered based on the elements that are shown on a sheet.



Get: IsInternalKeynoteSchedule(self: ViewSchedule) -> bool



"""

 IsTitleblockRevisionSchedule=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies if this ViewSchedule is an internal schedule used to display revision schedules as part of a titleblock.



Get: IsTitleblockRevisionSchedule(self: ViewSchedule) -> bool



"""

 KeyScheduleParameterName=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """In a key schedule,the name of the parameter for choosing one of the keys.



Get: KeyScheduleParameterName(self: ViewSchedule) -> str



Set: KeyScheduleParameterName(self: ViewSchedule)=value

"""

 TitleTextTypeId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Defines the default text style used in the header section of the schedule.



Get: TitleTextTypeId(self: ViewSchedule) -> ElementId



Set: TitleTextTypeId(self: ViewSchedule)=value

"""


