class InstanceDefinition(object):
 # no doc
 def CreatePreviewBitmap(self,definedViewportProjection,*__args):
  """
  CreatePreviewBitmap(self: InstanceDefinition,definedViewportProjection: DefinedViewportProjection,bitmapSize: Size) -> Bitmap

  CreatePreviewBitmap(self: InstanceDefinition,definedViewportProjection: DefinedViewportProjection,displayMode: DisplayMode,bitmapSize: Size) -> Bitmap
  """
  pass
 def GetContainers(self):
  """
  GetContainers(self: InstanceDefinition) -> Array[InstanceDefinition]

  

   Gets a list of all the InstanceDefinitions that contain a reference this InstanceDefinition.

   Returns: An array of instance definitions. The returned array can be empty,but not null.
  """
  pass
 def GetObjects(self):
  """
  GetObjects(self: InstanceDefinition) -> Array[RhinoObject]

  

   Gets an array with the objects that belong to this instance definition.

   Returns: An array of Rhino objects. The returned array can be empty,but not null.
  """
  pass
 def GetReferences(self,wheretoLook):
  """
  GetReferences(self: InstanceDefinition,wheretoLook: int) -> Array[InstanceObject]

  

   Gets a list of the CRhinoInstanceObjects (inserts) that contains

     a reference this 

    instance definition.

  

  

   wheretoLook: 0=get top level references in active document.1=get top level and nested references in 

    active document.2=check for references from other instance definitions.

  

   Returns: An array of instance objects. The returned array can be empty,but not null.
  """
  pass
 def InUse(self,wheretoLook):
  """
  InUse(self: InstanceDefinition,wheretoLook: int) -> bool

  

   Determines whether the instance definition is referenced.

  

   wheretoLook: 0=check for top level references in active document.1=check for top level and nested 

    references in active document.2=check for references in other instance definitions.

  

   Returns: true if the instance definition is used; otherwise false.
  """
  pass
 def Object(self,index):
  """
  Object(self: InstanceDefinition,index: int) -> RhinoObject

  

   returns an object used as part of this definition.

  

   index: 0 <= index < ObjectCount.

   Returns: Returns an object that is used to define the geometry.

     Does NOT return an object 

    that references this definition.count the number of references to this instance.
  """
  pass
 def UsesDefinition(self,otherIdefIndex):
  """
  UsesDefinition(self: InstanceDefinition,otherIdefIndex: int) -> int

  

   Determines if this instance definition contains a reference to another instance definition.

  

   otherIdefIndex: index of another instance definition.

   Returns: 0   no

       1   other_idef_index is the index of this instance definition

     

     >1   This InstanceDefinition uses the instance definition

        and 

    the returned value is the nesting depth.
  """
  pass
 ArchiveFileStatus=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Returns the archive file status of a linked instance definition.



Get: ArchiveFileStatus(self: InstanceDefinition) -> InstanceDefinitionArchiveFileStatus



"""

 Description=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Description(self: InstanceDefinition) -> str



"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Id(self: InstanceDefinition) -> Guid



"""

 Index=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Index of this instance definition in the index definition table.



Get: Index(self: InstanceDefinition) -> int



"""

 IsDeleted=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsDeleted(self: InstanceDefinition) -> bool



"""

 IsReference=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """An object from a work session reference model is reference a

   reference object and cannot be modified.  An object is a reference

   object if,and only if,it is on a reference layer.



Get: IsReference(self: InstanceDefinition) -> bool



"""

 IsTenuous=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IsTenuous(self: InstanceDefinition) -> bool



"""

 LayerStyle=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: LayerStyle(self: InstanceDefinition) -> InstanceDefinitionLayerStyle



"""

 Name=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: Name(self: InstanceDefinition) -> str



"""

 ObjectCount=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Number of objects this definition uses. This counts the objects that are used to define the geometry.

   This does NOT count the number of references to this instance definition.



Get: ObjectCount(self: InstanceDefinition) -> int



"""

 SkipNestedLinkedDefinitions=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Controls how much geometry is read when a linked InstanceDefinition is updated.



Get: SkipNestedLinkedDefinitions(self: InstanceDefinition) -> bool



"""

 SourceArchive=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SourceArchive(self: InstanceDefinition) -> str



"""

 UpdateType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: UpdateType(self: InstanceDefinition) -> InstanceDefinitionUpdateType



"""

 Url=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The hyperlink URL that is executed when the UrlDescription hyperlink is clicked on in the Insert and Block UI



Get: Url(self: InstanceDefinition) -> str



"""

 UrlDescription=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The URL description displayed as a hyperlink in the Insert and Block UI



Get: UrlDescription(self: InstanceDefinition) -> str



"""


