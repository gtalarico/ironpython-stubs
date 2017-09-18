class SplitButton(PulldownButton):
 """ The SplitButton object represents a button with a clickable button appearing above a pulldown. """
 CurrentButton=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Gets or sets the current PushButton of the SplitButton.



Get: CurrentButton(self: SplitButton) -> PushButton



Set: CurrentButton(self: SplitButton)=value

"""

 IsSynchronizedWithCurrentItem=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """Indicates whether the top PushButton on the SplitButton changes based on the CurrentButton property.



Get: IsSynchronizedWithCurrentItem(self: SplitButton) -> bool



Set: IsSynchronizedWithCurrentItem(self: SplitButton)=value

"""


 m_ItemType=None

