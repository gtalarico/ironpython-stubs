class EditorInteraction(object):
 """
 Wraps the EditorInteractionType for the Pane to allow
    for clients to override their type dynamically if need
    be.
 
 EditorInteraction(interactionType: EditorInteractionType)
 EditorInteraction()
 """
 @staticmethod
 def __new__(self,interactionType=None):
  """
  __new__(cls: type,interactionType: EditorInteractionType)
  __new__(cls: type)
  """
  pass
 InteractionType=property(lambda self: object(),lambda self,v: None,lambda self: None)
 """The type of interaction.

Get: InteractionType(self: EditorInteraction) -> EditorInteractionType

Set: InteractionType(self: EditorInteraction)=value
"""


