class AssemblyViewUtils(object):
 """ Utilities that provide capabilities related to assembly view creation and validation. """
 @staticmethod
 def AcquireAssemblyViews(document,sourceAssemblyInstanceId,targetAssemblyInstanceId):
  """
  AcquireAssemblyViews(document: Document,sourceAssemblyInstanceId: ElementId,targetAssemblyInstanceId: ElementId)
   Transfers the assembly views owned by a source assembly instance to a target 
    sibling assembly instance of the same assembly type.
  
  
   document: The document in which the assembly instances live.
   sourceAssemblyInstanceId: Id of the assembly instance that currently owns the assembly views.
   targetAssemblyInstanceId: Id of the assembly instance which will become the new owner of the assembly 
    views.
  """
  pass
 @staticmethod
 def Create3DOrthographic(document,assemblyInstanceId,viewTemplateId=None,isAssigned=None):
  """
  Create3DOrthographic(document: Document,assemblyInstanceId: ElementId) -> View3D
  
   Creates a new orthographic 3D assembly view for the assembly instance.
  
   document: The document to which the view will be added.
   assemblyInstanceId: Id of the assembly instance that owns the new view.
   Returns: A new orthographic 3D assembly view.
  Create3DOrthographic(document: Document,assemblyInstanceId: ElementId,viewTemplateId: ElementId,isAssigned: bool) -> View3D
  
   Creates a new orthographic 3D assembly view for the assembly instance.
     The 
    view will have the same orientation as the Default 3D view.
     The document 
    must be regenerated before using the 3D view.
  
  
   document: The document to which the view will be added.
   assemblyInstanceId: Id of the assembly instance that owns the new view.
   viewTemplateId: Id of the view template that is used to create the view;
     if 
    invalidElementId,the view will be created with the default settings.
  
   isAssigned: If true,the template will be assigned,if false,the template will be applied.
   Returns: A new orthographic 3D assembly view.
  """
  pass
 @staticmethod
 def CreateDetailSection(document,assemblyInstanceId,direction,viewTemplateId=None,isAssigned=None):
  """
  CreateDetailSection(document: Document,assemblyInstanceId: ElementId,direction: AssemblyDetailViewOrientation) -> ViewSection
  
   Creates a new detail section assembly view for the assembly instance.
  
   document: The document to which the view will be added.
   assemblyInstanceId: Id of the assembly instance that owns the new view.
   direction: The direction for the new view.
   Returns: A new detail section assembly view.
  CreateDetailSection(document: Document,assemblyInstanceId: ElementId,direction: AssemblyDetailViewOrientation,viewTemplateId: ElementId,isAssigned: bool) -> ViewSection
  
   Creates a new detail section assembly view for the assembly instance.
  
   document: The document to which the view will be added.
   assemblyInstanceId: Id of the assembly instance that owns the new view.
   direction: The direction for the new view.
   viewTemplateId: Id of the view template that is used to create the view; if invalidElementId,
    the view will be created with the default settings.
  
   isAssigned: If true,the template will be assigned; if false,the template will be applied.
   Returns: A new detail section assembly view.
  """
  pass
 @staticmethod
 def CreateMaterialTakeoff(document,assemblyInstanceId,viewTemplateId=None,isAssigned=None):
  """
  CreateMaterialTakeoff(document: Document,assemblyInstanceId: ElementId) -> ViewSchedule
  
   Creates a new material takeoff multicategory schedule assembly view for the 
    assembly instance.
  
  
   document: The document to which the view will be added.
   assemblyInstanceId: Id of the assembly instance that owns the new view.
   Returns: A new material takeoff multicategory schedule assembly view.
  CreateMaterialTakeoff(document: Document,assemblyInstanceId: ElementId,viewTemplateId: ElementId,isAssigned: bool) -> ViewSchedule
  
   Creates a new material takeoff multicategory schedule assembly view for the 
    assembly instance.
  
  
   document: The document to which the view will be added.
   assemblyInstanceId: Id of the assembly instance that owns the new view.
   viewTemplateId: Id of the view template that is used to create the view;
     if 
    invalidElementId,the view will be created with the default settings.
  
   isAssigned: If true,the template will be assigned,if false,the template will be applied.
   Returns: A new material takeoff multicategory schedule assembly view.
  """
  pass
 @staticmethod
 def CreatePartList(document,assemblyInstanceId,viewTemplateId=None,isAssigned=None):
  """
  CreatePartList(document: Document,assemblyInstanceId: ElementId) -> ViewSchedule
  
   Creates a new part list multicategory schedule assembly view for the assembly 
    instance.
  
  
   document: The document to which the view will be added.
   assemblyInstanceId: Id of the assembly instance that owns the new view.
   Returns: A new part list multicategory schedule assembly view.
  CreatePartList(document: Document,assemblyInstanceId: ElementId,viewTemplateId: ElementId,isAssigned: bool) -> ViewSchedule
  
   Creates a new part list multicategory schedule assembly view for the assembly 
    instance.
  
  
   document: The document to which the view will be added.
   assemblyInstanceId: Id of the assembly instance that owns the new view.
   viewTemplateId: Id of the view template that is used to create the view;
     if 
    invalidElementId,the view will be created with the default settings.
  
   isAssigned: If true,the template will be assigned,if false,the template will be applied.
   Returns: A new part list multicategory schedule assembly view.
  """
  pass
 @staticmethod
 def CreateSheet(document,assemblyInstanceId,titleBlockId):
  """
  CreateSheet(document: Document,assemblyInstanceId: ElementId,titleBlockId: ElementId) -> ViewSheet
  
   Creates a new sheet assembly view for the assembly instance.
  
   document: The document to which the view will be added.
   assemblyInstanceId: Id of the assembly instance that owns the new view.
   titleBlockId: Id of the titleblock family to use.  For no titleblock,pass invalidElementId.
   Returns: A new sheet assembly view.
  """
  pass
 @staticmethod
 def CreateSingleCategorySchedule(document,assemblyInstanceId,scheduleCategoryId,viewTemplateId=None,isAssigned=None):
  """
  CreateSingleCategorySchedule(document: Document,assemblyInstanceId: ElementId,scheduleCategoryId: ElementId) -> ViewSchedule
  
   Creates a new single-category schedule assembly view for the assembly instance.
  
   document: The document to which the view will be added.
   assemblyInstanceId: Id of the assembly instance that owns the new view.
   scheduleCategoryId: Id of the category for which the schedule will be created.
     Use 
    ViewSchedule.IsValidCategoryForSchedule() to check if a category can be 
    scheduled.
  
   Returns: A new single-category schedule assembly view.
  CreateSingleCategorySchedule(document: Document,assemblyInstanceId: ElementId,scheduleCategoryId: ElementId,viewTemplateId: ElementId,isAssigned: bool) -> ViewSchedule
  
   Creates a new single-category schedule assembly view for the assembly instance.
  
   document: The document to which the view will be added.
   assemblyInstanceId: Id of the assembly instance that owns the new view.
   scheduleCategoryId: Id of the category for which the schedule will be created.
     Use 
    ViewSchedule.IsValidCategoryForSchedule() to check if a category can be 
    scheduled.
  
   viewTemplateId: Id of the view template that is used to create the view;
     if 
    invalidElementId,the view will be created with the default settings.
  
   isAssigned: If true,the template will be assigned,if false,the template will be applied.
   Returns: A new single-category schedule assembly view.
  """
  pass
 __all__=[
  'AcquireAssemblyViews',
  'Create3DOrthographic',
  'CreateDetailSection',
  'CreateMaterialTakeoff',
  'CreatePartList',
  'CreateSheet',
  'CreateSingleCategorySchedule',
 ]

