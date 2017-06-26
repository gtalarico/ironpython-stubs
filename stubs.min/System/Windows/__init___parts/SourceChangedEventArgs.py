class SourceChangedEventArgs(RoutedEventArgs):
 """
 Provides data for the SourceChanged event,used for interoperation. This class cannot be inherited.
 
 SourceChangedEventArgs(oldSource: PresentationSource,newSource: PresentationSource)
 SourceChangedEventArgs(oldSource: PresentationSource,newSource: PresentationSource,element: IInputElement,oldParent: IInputElement)
 """
 @staticmethod
 def __new__(self,oldSource,newSource,element=None,oldParent=None):
  """
  __new__(cls: type,oldSource: PresentationSource,newSource: PresentationSource)
  __new__(cls: type,oldSource: PresentationSource,newSource: PresentationSource,element: IInputElement,oldParent: IInputElement)
  """
  pass
 Element=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the element whose parent change causing the presentation source information to change.

Get: Element(self: SourceChangedEventArgs) -> IInputElement

"""

 NewSource=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the new source involved in this source change.

Get: NewSource(self: SourceChangedEventArgs) -> PresentationSource

"""

 OldParent=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the previous parent of the element whose parent change causing the presentation source information to change.

Get: OldParent(self: SourceChangedEventArgs) -> IInputElement

"""

 OldSource=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets the old source involved in this source change.

Get: OldSource(self: SourceChangedEventArgs) -> PresentationSource

"""


