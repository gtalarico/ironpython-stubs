class ObjectEnumeratorSettings(object):
 """
 Settings used for getting an enumerator of objects in a document

    See Rhino.Collections.ObjectTable.GetEnumerator()

 

 ObjectEnumeratorSettings()
 """
 ActiveObjects=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ActiveObjects(self: ObjectEnumeratorSettings) -> bool



Set: ActiveObjects(self: ObjectEnumeratorSettings)=value

"""

 ClassTypeFilter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ClassTypeFilter(self: ObjectEnumeratorSettings) -> Type



Set: ClassTypeFilter(self: ObjectEnumeratorSettings)=value

"""

 DeletedObjects=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: DeletedObjects(self: ObjectEnumeratorSettings) -> bool



Set: DeletedObjects(self: ObjectEnumeratorSettings)=value

"""

 HiddenObjects=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: HiddenObjects(self: ObjectEnumeratorSettings) -> bool



Set: HiddenObjects(self: ObjectEnumeratorSettings)=value

"""

 IdefObjects=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """When true,ONLY Instance Definitions will be returned



Get: IdefObjects(self: ObjectEnumeratorSettings) -> bool



Set: IdefObjects(self: ObjectEnumeratorSettings)=value

"""

 IncludeGrips=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IncludeGrips(self: ObjectEnumeratorSettings) -> bool



Set: IncludeGrips(self: ObjectEnumeratorSettings)=value

"""

 IncludeLights=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IncludeLights(self: ObjectEnumeratorSettings) -> bool



Set: IncludeLights(self: ObjectEnumeratorSettings)=value

"""

 IncludePhantoms=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: IncludePhantoms(self: ObjectEnumeratorSettings) -> bool



Set: IncludePhantoms(self: ObjectEnumeratorSettings)=value

"""

 LayerIndexFilter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: LayerIndexFilter(self: ObjectEnumeratorSettings) -> int



Set: LayerIndexFilter(self: ObjectEnumeratorSettings)=value

"""

 LockedObjects=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: LockedObjects(self: ObjectEnumeratorSettings) -> bool



Set: LockedObjects(self: ObjectEnumeratorSettings)=value

"""

 NameFilter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: NameFilter(self: ObjectEnumeratorSettings) -> str



Set: NameFilter(self: ObjectEnumeratorSettings)=value

"""

 NormalObjects=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: NormalObjects(self: ObjectEnumeratorSettings) -> bool



Set: NormalObjects(self: ObjectEnumeratorSettings)=value

"""

 ObjectTypeFilter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ObjectTypeFilter(self: ObjectEnumeratorSettings) -> ObjectType



Set: ObjectTypeFilter(self: ObjectEnumeratorSettings)=value

"""

 ReferenceObjects=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: ReferenceObjects(self: ObjectEnumeratorSettings) -> bool



Set: ReferenceObjects(self: ObjectEnumeratorSettings)=value

"""

 SelectedObjectsFilter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: SelectedObjectsFilter(self: ObjectEnumeratorSettings) -> bool



Set: SelectedObjectsFilter(self: ObjectEnumeratorSettings)=value

"""

 ViewportFilter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Filter on value of object->IsActiveInViewport()



Get: ViewportFilter(self: ObjectEnumeratorSettings) -> RhinoViewport



Set: ViewportFilter(self: ObjectEnumeratorSettings)=value

"""

 VisibleFilter=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Get: VisibleFilter(self: ObjectEnumeratorSettings) -> bool



Set: VisibleFilter(self: ObjectEnumeratorSettings)=value

"""


