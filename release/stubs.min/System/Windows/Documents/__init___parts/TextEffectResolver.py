class TextEffectResolver(object):
 """ A helper class that sets text effects in a text container """
 @staticmethod
 def Resolve(startPosition,endPosition,effect):
  """
  Resolve(startPosition: TextPointer,endPosition: TextPointer,effect: TextEffect) -> Array[TextEffectTarget]
  
   Resolves text effect on a text range to a list of text effect targets.
  
   startPosition: The starting text pointer
   endPosition: The end text pointer
   effect: The effect to apply on the text
   Returns: Collection of System.Windows.Documents.TextEffectTarget objects corresponding 
    to the text range.
  """
  pass
 __all__=[
  'Resolve',
 ]

