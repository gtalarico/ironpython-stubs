class RTreeEventArgs(EventArgs):
 """
 Represents event data that is passed when when an item that meets certain 

    criteria is found and the passed RTree event is raised.
 """
 Cancel=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets a value that determines if the search should be conducted farther.



Get: Cancel(self: RTreeEventArgs) -> bool



Set: Cancel(self: RTreeEventArgs)=value

"""

 Id=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the identifier of the found item.



Get: Id(self: RTreeEventArgs) -> int



"""

 IdB=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """If search is using two r-trees,IdB is element b in the search.



Get: IdB(self: RTreeEventArgs) -> int



"""

 IdBPtr=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """If search is using two r-trees,IdB is the element b pointer in the search.



Get: IdBPtr(self: RTreeEventArgs) -> IntPtr



"""

 IdPtr=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the identifier pointer of the found item.



Get: IdPtr(self: RTreeEventArgs) -> IntPtr



"""

 SearchBoundingBox=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Bounding box bounds used during a search. You may modify the box in a search callback

   to help reduce the bounds to search.



Get: SearchBoundingBox(self: RTreeEventArgs) -> BoundingBox



Set: SearchBoundingBox(self: RTreeEventArgs)=value

"""

 SearchSphere=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Sphere bounds used during a search. You can modify the sphere in a search callback to

   help reduce the bounds to search.



Get: SearchSphere(self: RTreeEventArgs) -> Sphere



Set: SearchSphere(self: RTreeEventArgs)=value

"""

 Tag=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets an arbitrary object that can be attached to this event args.

   This object will "stick" through a single search and can represent user-defined state.



Get: Tag(self: RTreeEventArgs) -> object



Set: Tag(self: RTreeEventArgs)=value

"""


