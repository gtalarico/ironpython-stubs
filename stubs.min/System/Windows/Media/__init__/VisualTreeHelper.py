class VisualTreeHelper(object):
    """ Provides utility methods that perform common tasks involving nodes in a visual tree. """
    @staticmethod
    def GetBitmapEffect(reference):
        """
        GetBitmapEffect(reference: Visual) -> BitmapEffect
        
            Returns the System.Windows.Media.Effects.BitmapEffect value for the specified System.Windows.Media.Visual.
        
            reference: The System.Windows.Media.Visual that contains the bitmap effect.
            Returns: The System.Windows.Media.Effects.BitmapEffect for this System.Windows.Media.Visual.
        """
        pass

    @staticmethod
    def GetBitmapEffectInput(reference):
        """
        GetBitmapEffectInput(reference: Visual) -> BitmapEffectInput
        
            Returns the System.Windows.Media.Effects.BitmapEffectInput value for the specified System.Windows.Media.Visual.
        
            reference: The System.Windows.Media.Visual that contains the bitmap effect input value.
            Returns: The System.Windows.Media.Effects.BitmapEffectInput for this System.Windows.Media.Visual.
        """
        pass

    @staticmethod
    def GetCacheMode(reference):
        """
        GetCacheMode(reference: Visual) -> CacheMode
        
            Retrieves the cached representation of the specified System.Windows.Media.Visual.
        
            reference: The System.Windows.Media.Visual to get the System.Windows.Media.CacheMode for.
            Returns: The System.Windows.Media.CacheMode for reference.
        """
        pass

    @staticmethod
    def GetChild(reference, childIndex):
        """
        GetChild(reference: DependencyObject, childIndex: int) -> DependencyObject
        
            Returns the child visual object from the specified collection index within a specified parent.
        
            reference: The parent visual, referenced as a System.Windows.DependencyObject.
            childIndex: The index that represents the child visual that is contained by reference.
            Returns: The index value of the child visual object.
        """
        pass

    @staticmethod
    def GetChildrenCount(reference):
        """
        GetChildrenCount(reference: DependencyObject) -> int
        
            Returns the number of children that the specified visual object contains.
        
            reference: The parent visual that is referenced as a System.Windows.DependencyObject.
            Returns: The number of child visuals that the parent visual contains.
        """
        pass

    @staticmethod
    def GetClip(reference):
        """
        GetClip(reference: Visual) -> Geometry
        
            Return the clip region of the specified System.Windows.Media.Visual as a System.Windows.Media.Geometry value.
        
            reference: The System.Windows.Media.Visual whose clip region value is returned.
            Returns: The clip region value of the System.Windows.Media.Visual returned as a System.Windows.Media.Geometry type.
        """
        pass

    @staticmethod
    def GetContentBounds(reference):
        """
        GetContentBounds(reference: Visual3D) -> Rect3D
        
            Returns the cached bounding box rectangle for the specified System.Windows.Media.Media3D.Visual3D.
        
            reference: The 3D visual whose bounding box value is computed.
            Returns: The bounding box 3D rectangle for the System.Windows.Media.Media3D.Visual3D.
        GetContentBounds(reference: Visual) -> Rect
        
            Returns the cached bounding box rectangle for the specified System.Windows.Media.Visual.
        
            reference: The System.Windows.Media.Visual whose bounding box value is computed.
            Returns: The bounding box rectangle for the System.Windows.Media.Visual.
        """
        pass

    @staticmethod
    def GetDescendantBounds(reference):
        """
        GetDescendantBounds(reference: Visual3D) -> Rect3D
        
            Returns the union of all the content bounding boxes for all the descendants of the specified System.Windows.Media.Media3D.Visual3D, which includes the content bounding box of the 
             System.Windows.Media.Media3D.Visual3D.
        
        
            reference: The 3D visual whose bounding box value for all descendants is computed.
            Returns: Returns the bounding box 3D rectangle for the 3D visual.
        GetDescendantBounds(reference: Visual) -> Rect
        
            Returns the union of all the content bounding boxes for all the descendants of the System.Windows.Media.Visual, which includes the content bounding box of the System.Windows.Media.Visual.
        
            reference: The System.Windows.Media.Visual whose bounding box value for all descendants is computed.
            Returns: The bounding box rectangle for the specified System.Windows.Media.Visual.
        """
        pass

    @staticmethod
    def GetDpi(visual):
        """ GetDpi(visual: Visual) -> DpiScale """
        pass

    @staticmethod
    def GetDrawing(reference):
        """
        GetDrawing(reference: Visual) -> DrawingGroup
        
            Returns the drawing content of the specified System.Windows.Media.Visual.
        
            reference: The System.Windows.Media.Visual whose drawing content is returned.
            Returns: The drawing content of the System.Windows.Media.Visual returned as a System.Windows.Media.DrawingGroup type.
        """
        pass

    @staticmethod
    def GetEdgeMode(reference):
        """
        GetEdgeMode(reference: Visual) -> EdgeMode
        
            Returns the edge mode of the specified System.Windows.Media.Visual as an System.Windows.Media.EdgeMode value.
        
            reference: The System.Windows.Media.Visual whose edge mode value is returned.
            Returns: The System.Windows.Media.EdgeMode value of the System.Windows.Media.Visual.
        """
        pass

    @staticmethod
    def GetEffect(reference):
        """
        GetEffect(reference: Visual) -> Effect
        
            Gets the bitmap effect for the specified System.Windows.Media.Visual.
        
            reference: The System.Windows.Media.Visual to get the bitmap effect for.
            Returns: The System.Windows.Media.Effects.Effect applied to reference.
        """
        pass

    @staticmethod
    def GetOffset(reference):
        """
        GetOffset(reference: Visual) -> Vector
        
            Returns the offset of the System.Windows.Media.Visual.
        
            reference: The System.Windows.Media.Visual whose offset is returned.
            Returns: A System.Windows.Vector that represents the offset value of the System.Windows.Media.Visual.
        """
        pass

    @staticmethod
    def GetOpacity(reference):
        """
        GetOpacity(reference: Visual) -> float
        
            Returns the opacity of the System.Windows.Media.Visual.
        
            reference: The System.Windows.Media.Visual whose opacity value is returned.
            Returns: A value of type System.Double that represents the opacity value of the System.Windows.Media.Visual.
        """
        pass

    @staticmethod
    def GetOpacityMask(reference):
        """
        GetOpacityMask(reference: Visual) -> Brush
        
            Returns a System.Windows.Media.Brush value that represents the opacity mask of the System.Windows.Media.Visual.
        
            reference: The System.Windows.Media.Visual whose opacity mask value is returned.
            Returns: A value of type System.Windows.Media.Brush that represents the opacity mask value of the System.Windows.Media.Visual.
        """
        pass

    @staticmethod
    def GetParent(reference):
        """
        GetParent(reference: DependencyObject) -> DependencyObject
        
            Returns a System.Windows.DependencyObject value that represents the parent of the visual object.
        
            reference: The visual whose parent is returned.
            Returns: The parent of the visual.
        """
        pass

    @staticmethod
    def GetTransform(reference):
        """
        GetTransform(reference: Visual) -> Transform
        
            Returns a System.Windows.Media.Transform value for the System.Windows.Media.Visual.
        
            reference: The System.Windows.Media.Visual whose transform value is returned.
            Returns: The transform value of the System.Windows.Media.Visual, or null if reference does not have a transform defined.
        """
        pass

    @staticmethod
    def GetXSnappingGuidelines(reference):
        """
        GetXSnappingGuidelines(reference: Visual) -> DoubleCollection
        
            Returns an X-coordinate (vertical) guideline collection.
        
            reference: The System.Windows.Media.Visual whose X-coordinate guideline collection is returned.
            Returns: The X-coordinate guideline collection of the System.Windows.Media.Visual.
        """
        pass

    @staticmethod
    def GetYSnappingGuidelines(reference):
        """
        GetYSnappingGuidelines(reference: Visual) -> DoubleCollection
        
            Returns a Y-coordinate (horizontal) guideline collection.
        
            reference: The System.Windows.Media.Visual whose Y-coordinate guideline collection is returned.
            Returns: The Y-coordinate guideline collection of the System.Windows.Media.Visual.
        """
        pass

    @staticmethod
    def HitTest(reference, *__args):
        """
        HitTest(reference: Visual3D, filterCallback: HitTestFilterCallback, resultCallback: HitTestResultCallback, hitTestParameters: HitTestParameters3D)
            Initiates a hit test on the specified System.Windows.Media.Media3D.Visual3D, with caller-defined System.Windows.Media.HitTestFilterCallback and System.Windows.Media.HitTestResultCallback methods.
        
            reference: The System.Windows.Media.Media3D.Visual3D to hit test.
            filterCallback: The method that represents the hit test filter callback value.
            resultCallback: The method that represents the hit test result callback value.
            hitTestParameters: The 3D parameter value to hit test against.
        HitTest(reference: Visual, filterCallback: HitTestFilterCallback, resultCallback: HitTestResultCallback, hitTestParameters: HitTestParameters)
            Initiates a hit test on the specified System.Windows.Media.Visual, with caller-defined System.Windows.Media.HitTestFilterCallback and System.Windows.Media.HitTestResultCallback methods.
        
            reference: The System.Windows.Media.Visual to hit test.
            filterCallback: The method that represents the hit test filter callback value.
            resultCallback: The method that represents the hit test result callback value.
            hitTestParameters: The parameter value to hit test against.
        HitTest(reference: Visual, point: Point) -> HitTestResult
        
            Returns the topmost System.Windows.Media.Visual object of a hit test by specifying a System.Windows.Point.
        
            reference: The System.Windows.Media.Visual to hit test.
            point: The point value to hit test against.
            Returns: The hit test result of the System.Windows.Media.Visual, returned as a System.Windows.Media.HitTestResult type.
        """
        pass

    @staticmethod
    def SetRootDpi(visual, dpiInfo):
        """ SetRootDpi(visual: Visual, dpiInfo: DpiScale) """
        pass

    __all__ = [
        'GetBitmapEffect',
        'GetBitmapEffectInput',
        'GetCacheMode',
        'GetChild',
        'GetChildrenCount',
        'GetClip',
        'GetContentBounds',
        'GetDescendantBounds',
        'GetDpi',
        'GetDrawing',
        'GetEdgeMode',
        'GetEffect',
        'GetOffset',
        'GetOpacity',
        'GetOpacityMask',
        'GetParent',
        'GetTransform',
        'GetXSnappingGuidelines',
        'GetYSnappingGuidelines',
        'HitTest',
        'SetRootDpi',
    ]


# variables with complex values

