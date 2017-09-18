class ImageAnimator(object):
 """ Animates an image that has time-based frames. """
 @staticmethod
 def Animate(image,onFrameChangedHandler):
  """
  Animate(image: Image,onFrameChangedHandler: EventHandler)

   Displays a multiple-frame image as an animation.

  

   image: The System.Drawing.Image object to animate.

   onFrameChangedHandler: An EventHandler object that specifies the method that is called when the animation frame changes.
  """
  pass
 @staticmethod
 def CanAnimate(image):
  """
  CanAnimate(image: Image) -> bool

  

   Returns a Boolean value indicating whether the specified image contains time-based frames.

  

   image: The System.Drawing.Image object to test.

   Returns: This method returns true if the specified image contains time-based frames; otherwise,false.
  """
  pass
 @staticmethod
 def StopAnimate(image,onFrameChangedHandler):
  """
  StopAnimate(image: Image,onFrameChangedHandler: EventHandler)

   Terminates a running animation.

  

   image: The System.Drawing.Image object to stop animating.

   onFrameChangedHandler: An EventHandler object that specifies the method that is called when the animation frame changes.
  """
  pass
 @staticmethod
 def UpdateFrames(image=None):
  """
  UpdateFrames()

   Advances the frame in all images currently being animated. The new frame is drawn the next time 

    the image is rendered.

  

  UpdateFrames(image: Image)

   Advances the frame in the specified image. The new frame is drawn the next time the image is 

    rendered. This method applies only to images with time-based frames.

  

  

   image: The System.Drawing.Image object for which to update frames.
  """
  pass
