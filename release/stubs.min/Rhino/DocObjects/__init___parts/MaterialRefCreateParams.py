class MaterialRefCreateParams(object):
 """
 Options passed to MaterialRefs.Create

 

 MaterialRefCreateParams()
 """
 BackFaceMaterialId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The Id of the Material used to render the back of an object.



Get: BackFaceMaterialId(self: MaterialRefCreateParams) -> Guid



Set: BackFaceMaterialId(self: MaterialRefCreateParams)=value

"""

 BackFaceMaterialIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The index of the material used to render the back of an object



Get: BackFaceMaterialIndex(self: MaterialRefCreateParams) -> int



Set: BackFaceMaterialIndex(self: MaterialRefCreateParams)=value

"""

 FrontFaceMaterialId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The Id of the Material used to render the front of an object.



Get: FrontFaceMaterialId(self: MaterialRefCreateParams) -> Guid



Set: FrontFaceMaterialId(self: MaterialRefCreateParams)=value

"""

 FrontFaceMaterialIndex=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The index of the material used to render the front of an object



Get: FrontFaceMaterialIndex(self: MaterialRefCreateParams) -> int



Set: FrontFaceMaterialIndex(self: MaterialRefCreateParams)=value

"""

 MaterialSource=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Determines if the simple material should come from the object or from

   it's layer.



Get: MaterialSource(self: MaterialRefCreateParams) -> ObjectMaterialSource



Set: MaterialSource(self: MaterialRefCreateParams)=value

"""

 PlugInId=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Identifies a rendering plug-in



Get: PlugInId(self: MaterialRefCreateParams) -> Guid



Set: PlugInId(self: MaterialRefCreateParams)=value

"""


