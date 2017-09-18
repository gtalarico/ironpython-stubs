# encoding: utf-8
# module Rhino.Render.Fields calls itself Fields
# from RhinoCommon, Version=5.1.30000.16, Culture=neutral, PublicKeyToken=552281e97c755530
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class Field(object):
    """
    Generic data fields used to add publicly accessible properties to
                RenderContent.FieldDictionary.  These should be created by calling a
                FieldDictaionary.Add() method on a Render content object.  These are
                allocated after the RenderContent object's C++ object is created and
                added to the underlying C++ objects content dictionary, who ever
                allocates a field is responsible for deleting it so these objects clean
                up the C++ pointers when they are disposed of.
    """
    def CreateCppPointer(self, *args): #cannot find CLR method
        """
        CreateCppPointer(self: Field, content: RenderContent, attachToPointer: IntPtr)
            Create the RDK C++ field object and set its initial value, fields are
                    added to a 
             RenderContent.FieldDictionary in the RenderContent
                    constructor before the 
             RenderContent C++ pointer is created, the
                    RenderContent C++ pointer is required 
             when creating a field in order
                    for the field to get added to the RenderContent C++ 
             Field list so this
                    method is called by RenderContent when it is safe to create the 
             Field
                    C++ pointers.
        
        
            content: RenderContent.FiledDictionary that owns this Field.
            attachToPointer: Existing C++ pointer to attach to.
        """
        pass

    def ValueAsBool(self, *args): #cannot find CLR method
        """
        ValueAsBool(self: Field) -> bool
        
            Return field value as a bool.
            Returns: Returns field value as a bool.
        """
        pass

    def ValueAsByteArray(self, *args): #cannot find CLR method
        """
        ValueAsByteArray(self: Field) -> Array[Byte]
        
            Return field as a byte array.
            Returns: Return field as a byte array.
        """
        pass

    def ValueAsColor4f(self, *args): #cannot find CLR method
        """
        ValueAsColor4f(self: Field) -> Color4f
        
            Return field as a Rhino.Display.Color4f color value.
            Returns: Return field as a Rhino.Display.Color4f color value.
        """
        pass

    def ValueAsDateTime(self, *args): #cannot find CLR method
        """
        ValueAsDateTime(self: Field) -> DateTime
        
            Return field as a DateTime value.
            Returns: Return field as a DateTime value.
        """
        pass

    def ValueAsDouble(self, *args): #cannot find CLR method
        """
        ValueAsDouble(self: Field) -> float
        
            Return field value as a double precision number.
            Returns: Return the field value as a double precision number.
        """
        pass

    def ValueAsFloat(self, *args): #cannot find CLR method
        """
        ValueAsFloat(self: Field) -> Single
        
            Return field value as floating point number.
            Returns: Return the field value as an floating point number.
        """
        pass

    def ValueAsGuid(self, *args): #cannot find CLR method
        """
        ValueAsGuid(self: Field) -> Guid
        
            Return field value as Guid.
            Returns: Return the field value as an Guid.
        """
        pass

    def ValueAsInt(self, *args): #cannot find CLR method
        """
        ValueAsInt(self: Field) -> int
        
            Return field value as integer.
            Returns: Return the field value as an integer.
        """
        pass

    def ValueAsObject(self):
        """ ValueAsObject(self: Field) -> object """
        pass

    def ValueAsPoint2d(self, *args): #cannot find CLR method
        """
        ValueAsPoint2d(self: Field) -> Point2d
        
            Return field as a Rhino.Geometry.Point2d color value.
            Returns: Return field as a Rhino.Geometry.Point2d color value.
        """
        pass

    def ValueAsPoint3d(self, *args): #cannot find CLR method
        """
        ValueAsPoint3d(self: Field) -> Point3d
        
            Return field as a Rhino.Geometry.Point3d color value.
            Returns: Return field as a Rhino.Geometry.Point3d color value.
        """
        pass

    def ValueAsPoint4d(self, *args): #cannot find CLR method
        """
        ValueAsPoint4d(self: Field) -> Point4d
        
            Return field as a Rhino.Geometry.Point4d color value.
            Returns: Return field as a Rhino.Geometry.Point4d color value.
        """
        pass

    def ValueAsString(self, *args): #cannot find CLR method
        """
        ValueAsString(self: Field) -> str
        
            Get field value as a string.
            Returns: Returns the field value as a string if possible.
        """
        pass

    def ValueAsTransform(self, *args): #cannot find CLR method
        """
        ValueAsTransform(self: Field) -> Transform
        
            Return field as a Rhino.Geometry.Transform color value.
            Returns: Return field as a Rhino.Geometry.Transform color value.
        """
        pass

    def ValueAsVector2d(self, *args): #cannot find CLR method
        """
        ValueAsVector2d(self: Field) -> Vector2d
        
            Return field as a Rhino.Geometry.Vector2d color value.
            Returns: Return field as a Rhino.Geometry.Vector2d color value.
        """
        pass

    def ValueAsVector3d(self, *args): #cannot find CLR method
        """
        ValueAsVector3d(self: Field) -> Vector3d
        
            Return field as a Rhino.Geometry.Vector3d color value.
            Returns: Return field as a Rhino.Geometry.Vector3d color value.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(self, *args): #cannot find CLR constructor
        """ __new__(cls: type, renderContent: RenderContent, attachToPointer: IntPtr, key: str, prompt: str, initialValue: object, isTextured: bool) """
        pass

    IsTextured = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get: IsTextured(self: Field) -> bool

"""

    Key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Field key value string set by constructor

Get: Key(self: Field) -> str

"""

    Prompt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Optional UI prompt string set by constructor

Get: Prompt(self: Field) -> str

"""

    Tag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets an object that contains data to associate with the field.

Get: Tag(self: Field) -> object

Set: Tag(self: Field) = value
"""



class BoolField(Field):
    """ bool field value class """
    def ValueAsObject(self):
        """ ValueAsObject(self: BoolField) -> object """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the field value

Get: Value(self: BoolField) -> bool

Set: Value(self: BoolField) = value
"""



class ByteArrayField(Field):
    """ ByteArray field value class """
    def ValueAsObject(self):
        """ ValueAsObject(self: ByteArrayField) -> object """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the field value

Get: Value(self: ByteArrayField) -> Array[Byte]

Set: Value(self: ByteArrayField) = value
"""



class Color4fField(Field):
    """ Color4f field value class """
    def ValueAsObject(self):
        """ ValueAsObject(self: Color4fField) -> object """
        pass

    SystemColorValue = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the field value

Get: SystemColorValue(self: Color4fField) -> Color

Set: SystemColorValue(self: Color4fField) = value
"""

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the field value

Get: Value(self: Color4fField) -> Color4f

Set: Value(self: Color4fField) = value
"""



class DateTimeField(Field):
    """ DateTime field value class """
    def ValueAsObject(self):
        """ ValueAsObject(self: DateTimeField) -> object """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the field value

Get: Value(self: DateTimeField) -> DateTime

Set: Value(self: DateTimeField) = value
"""



class DoubleField(Field):
    """ double field value class """
    def ValueAsObject(self):
        """ ValueAsObject(self: DoubleField) -> object """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the field value

Get: Value(self: DoubleField) -> float

Set: Value(self: DoubleField) = value
"""



class FieldDictionary(object):
    """
    Dictionary containing RenderContent data fields, add fields to this
                dictionary in your derived RenderContent classes constructor.  Get field
                values using the TryGet[data type]() methods and set them using the Set()
                method.
    """
    def Add(self, key, value, prompt=None):
        """
        Add(self: FieldDictionary, key: str, value: Point3d) -> Point3dField
        
            Add a new Point3dField to the dictionary. This will be a data only
                    field and not 
             show up in the content browsers.
        
        
            key: Key name for the field value to change.
            value: Initial value for this field.
        Add(self: FieldDictionary, key: str, value: Point3d, prompt: str) -> Point3dField
        
            Add a new Point3dField to the dictionary.
        
            key: Key name for the field value to change.
            value: Initial value for this field.
            prompt: Prompt to display in the user interface (Content Browsers) if this
                    is null or an 
             empty string the this field is a data only field and will
                    not appear in the user 
             interface.
        
        Add(self: FieldDictionary, key: str, value: Point4d) -> Point4dField
        
            Add a new Point4dField to the dictionary. This will be a data only
                    field and not 
             show up in the content browsers.
        
        
            key: Key name for the field value to change.
            value: Initial value for this field.
        Add(self: FieldDictionary, key: str, value: Point2d, prompt: str) -> Point2dField
        
            Add a new Point2dField to the dictionary.
        
            key: Key name for the field value to change.
            value: Initial value for this field.
            prompt: Prompt to display in the user interface (Content Browsers) if this
                    is null or an 
             empty string the this field is a data only field and will
                    not appear in the user 
             interface.
        
        Add(self: FieldDictionary, key: str, value: Vector3d) -> Vector3dField
        
            Add a new Vector3dField to the dictionary. This will be a data only
                    field and not 
             show up in the content browsers.
        
        
            key: Key name for the field value to change.
            value: Initial value for this field.
        Add(self: FieldDictionary, key: str, value: Vector3d, prompt: str) -> Vector3dField
        
            Add a new Vector3dField to the dictionary.
        
            key: Key name for the field value to change.
            value: Initial value for this field.
            prompt: Prompt to display in the user interface (Content Browsers) if this
                    is null or an 
             empty string the this field is a data only field and will
                    not appear in the user 
             interface.
        
        Add(self: FieldDictionary, key: str, value: Point2d) -> Point2dField
        
            Add a new Point2dField to the dictionary. This will be a data only
                    field and not 
             show up in the content browsers.
        
        
            key: Key name for the field value to change.
            value: Initial value for this field.
        Add(self: FieldDictionary, key: str, value: Point4d, prompt: str) -> Point4dField
        
            Add a new Point4dField to the dictionary.
        
            key: Key name for the field value to change.
            value: Initial value for this field.
            prompt: Prompt to display in the user interface (Content Browsers) if this
                    is null or an 
             empty string the this field is a data only field and will
                    not appear in the user 
             interface.
        
        Add(self: FieldDictionary, key: str, value: DateTime) -> DateTimeField
        
            Add a new DateTimeField to the dictionary. This will be a data only
                    field and not 
             show up in the content browsers.
        
        
            key: Key name for the field value to change.
            value: Initial value for this field.
        Add(self: FieldDictionary, key: str, value: DateTime, prompt: str) -> DateTimeField
        
            Add a new DateTimeField to the dictionary.
        
            key: Key name for the field value to change.
            value: Initial value for this field.
            prompt: Prompt to display in the user interface (Content Browsers) if this
                    is null or an 
             empty string the this field is a data only field and will
                    not appear in the user 
             interface.
        
        Add(self: FieldDictionary, key: str, value: Array[Byte]) -> ByteArrayField
        
            AddField a new ByteArrayField to the dictionary. This will be a data
                    only field and 
             not show up in the content browsers.
        
        
            key: Key name for the field value to change.
            value: Initial value for this field.
        Add(self: FieldDictionary, key: str, value: Transform, prompt: str) -> TransformField
        
            Add a new TransformField to the dictionary.
        
            key: Key name for the field value to change.
            value: Initial value for this field.
            prompt: Prompt to display in the user interface (Content Browsers) if this
                    is null or an 
             empty string the this field is a data only field and will
                    not appear in the user 
             interface.
        
        Add(self: FieldDictionary, key: str, value: Guid) -> GuidField
        
            Add a new GuidField to the dictionary. This will be a data only field
                    and not show 
             up in the content browsers.
        
        
            key: Key name for the field value to change.
            value: Initial value for this field.
        Add(self: FieldDictionary, key: str, value: Guid, prompt: str) -> GuidField
        
            Add a new GuidField to the dictionary.
        
            key: Key name for the field value to change.
            value: Initial value for this field.
            prompt: Prompt to display in the user interface (Content Browsers) if this
                    is null or an 
             empty string the this field is a data only field and will
                    not appear in the user 
             interface.
        
        Add(self: FieldDictionary, key: str, value: Transform) -> TransformField
        
            Add a new TransformField to the dictionary. This will be a data only
                    field and not 
             show up in the content browsers.
        
        
            key: Key name for the field value to change.
            value: Initial value for this field.
        Add(self: FieldDictionary, key: str, value: Vector2d, prompt: str) -> Vector2dField
        
            Add a new Vector2dField to the dictionary.
        
            key: Key name for the field value to change.
            value: Initial value for this field.
            prompt: Prompt to display in the user interface (Content Browsers) if this
                    is null or an 
             empty string the this field is a data only field and will
                    not appear in the user 
             interface.
        
        Add(self: FieldDictionary, key: str, value: int) -> IntField
        
            Add a new IntField to the dictionary. This will be a data only field
                    and not show 
             up in the content browsers.
        
        
            key: Key name for the field value to change.
            value: Initial value for this field.
        Add(self: FieldDictionary, key: str, value: int, prompt: str) -> IntField
        
            Add a new IntField to the dictionary.
        
            key: Key name for the field value to change.
            value: Initial value for this field.
            prompt: Prompt to display in the user interface (Content Browsers) if this
                    is null or an 
             empty string the this field is a data only field and will
                    not appear in the user 
             interface.
        
        Add(self: FieldDictionary, key: str, value: Single) -> FloatField
        
            Add a new FloatField to the dictionary. This will be a data only field
                    and not show 
             up in the content browsers.
        
        
            key: Key name for the field value to change.
            value: Initial value for this field.
        Add(self: FieldDictionary, key: str, value: bool, prompt: str) -> BoolField
        
            Add a new BoolField to the dictionary.
        
            key: Key name for the field value to change.
            value: Initial value for this field.
            prompt: Prompt to display in the user interface (Content Browsers) if this
                    is null or an 
             empty string the this field is a data only field and will
                    not appear in the user 
             interface.
        
        Add(self: FieldDictionary, key: str, value: str) -> StringField
        
            Add a new StringField to the dictionary.  This will be a data only
                    field and not 
             show up in the content browsers.
        
        
            key: Key name for the field value to change.
            value: Initial value for this field.
        Add(self: FieldDictionary, key: str, value: str, prompt: str) -> StringField
        
            Add a new StringField to the dictionary.
        
            key: Key name for the field value to change.
            value: Initial value for this field.
            prompt: Prompt to display in the user interface (Content Browsers) if this
                    is null or an 
             empty string the this field is a data only field and will
                    not appear in the user 
             interface.
        
        Add(self: FieldDictionary, key: str, value: bool) -> BoolField
        
            Add a new BoolField to the dictionary. This will be a data only field
                    and not show 
             up in the content browsers.
        
        
            key: Key name for the field value to change.
            value: Initial value for this field.
        Add(self: FieldDictionary, key: str, value: Single, prompt: str) -> FloatField
        
            AddField a new FloatField to the dictionary.
        
            key: Key name for the field value to change.
            value: Initial value for this field.
            prompt: Prompt to display in the user interface (Content Browsers) if this
                    is null or an 
             empty string the this field is a data only field and will
                    not appear in the user 
             interface.
        
        Add(self: FieldDictionary, key: str, value: Color) -> Color4fField
        
            Add a new Color4fField to the dictionary. This will be a data only
                    field and not 
             show up in the content browsers.
        
        
            key: Key name for the field value to change.
            value: Initial value for this field.
        Add(self: FieldDictionary, key: str, value: Color, prompt: str) -> Color4fField
        
            Add a new Color4fField to the dictionary.
        
            key: Key name for the field value to change.
            value: Initial value for this field.
            prompt: Prompt to display in the user interface (Content Browsers) if this
                    is null or an 
             empty string the this field is a data only field and will
                    not appear in the user 
             interface.
        
        Add(self: FieldDictionary, key: str, value: Vector2d) -> Vector2dField
        
            Add a new Vector2dField to the dictionary. This will be a data only
                    field and not 
             show up in the content browsers.
        
        
            key: Key name for the field value to change.
            value: Initial value for this field.
        Add(self: FieldDictionary, key: str, value: Color4f, prompt: str) -> Color4fField
        
            Add a new Color4fField to the dictionary.
        
            key: Key name for the field value to change.
            value: Initial value for this field.
            prompt: Prompt to display in the user interface (Content Browsers) if this
                    is null or an 
             empty string the this field is a data only field and will
                    not appear in the user 
             interface.
        
        Add(self: FieldDictionary, key: str, value: float) -> DoubleField
        
            AddField a new DoubleField to the dictionary. This will be a data only
                    field and 
             not show up in the content browsers.
        
        
            key: Key name for the field value to change.
            value: Initial value for this field.
        Add(self: FieldDictionary, key: str, value: float, prompt: str) -> DoubleField
        
            Add a new DoubleField to the dictionary.
        
            key: Key name for the field value to change.
            value: Initial value for this field.
            prompt: Prompt to display in the user interface (Content Browsers) if this
                    is null or an 
             empty string the this field is a data only field and will
                    not appear in the user 
             interface.
        
        Add(self: FieldDictionary, key: str, value: Color4f) -> Color4fField
        
            Add a new Color4fField to the dictionary. This will be a data only
                    field and not 
             show up in the content browsers.
        
        
            key: Key name for the field value to change.
            value: Initial value for this field.
        """
        pass

    def AddTextured(self, key, value, prompt):
        """
        AddTextured(self: FieldDictionary, key: str, value: Point3d, prompt: str) -> Point3dField
        
            Add a new Point3dField to the dictionary. This overload will cause the
                    field to be 
             tagged as "textured" so that the texturing UI will appear
                    in automatic UIs.
        
        
            key: Key name for the field value to change.
            value: Initial value for this field.
            prompt: Prompt to display in the user interface (Content Browsers) if this
                    is null or an 
             empty string the this field is a data only field and will
                    not appear in the user 
             interface.
        
        AddTextured(self: FieldDictionary, key: str, value: Point2d, prompt: str) -> Point2dField
        
            Add a new Point2dField to the dictionary. This overload will cause the
                    field to be 
             tagged as "textured" so that the texturing UI will appear
                    in automatic UIs.
        
        
            key: Key name for the field value to change.
            value: Initial value for this field.
            prompt: Prompt to display in the user interface (Content Browsers) if this
                    is null or an 
             empty string the this field is a data only field and will
                    not appear in the user 
             interface.
        
        AddTextured(self: FieldDictionary, key: str, value: Vector3d, prompt: str) -> Vector3dField
        
            Add a new Vector3dField to the dictionary. This overload will cause the
                    field to be 
             tagged as "textured" so that the texturing UI will appear
                    in automatic UIs.
        
        
            key: Key name for the field value to change.
            value: Initial value for this field.
            prompt: Prompt to display in the user interface (Content Browsers) if this
                    is null or an 
             empty string the this field is a data only field and will
                    not appear in the user 
             interface.
        
        AddTextured(self: FieldDictionary, key: str, value: Point4d, prompt: str) -> Point4dField
        
            Add a new Point4dField to the dictionary. This overload will cause the
                    field to be 
             tagged as "textured" so that the texturing UI will appear
                    in automatic UIs.
        
        
            key: Key name for the field value to change.
            value: Initial value for this field.
            prompt: Prompt to display in the user interface (Content Browsers) if this
                    is null or an 
             empty string the this field is a data only field and will
                    not appear in the user 
             interface.
        
        AddTextured(self: FieldDictionary, key: str, value: DateTime, prompt: str) -> DateTimeField
        
            Add a new DateTimeField to the dictionary. This overload will cause the
                    field to be 
             tagged as "textured" so that the texturing UI will appear
                    in automatic UIs.
        
        
            key: Key name for the field value to change.
            value: Initial value for this field.
            prompt: Prompt to display in the user interface (Content Browsers) if this
                    is null or an 
             empty string the this field is a data only field and will
                    not appear in the user 
             interface.
        
        AddTextured(self: FieldDictionary, key: str, value: Transform, prompt: str) -> TransformField
        
            Add a new TransformField to the dictionary. This overload will cause
                    the field to 
             be tagged as "textured" so that the texturing UI will
                    appear in automatic UIs.
        
        
            key: Key name for the field value to change.
            value: Initial value for this field.
            prompt: Prompt to display in the user interface (Content Browsers) if this
                    is null or an 
             empty string the this field is a data only field and will
                    not appear in the user 
             interface.
        
        AddTextured(self: FieldDictionary, key: str, value: Guid, prompt: str) -> GuidField
        
            Add a new GuidField to the dictionary. This overload will cause the
                    field to be 
             tagged as "textured" so that the texturing UI will appear
                    in automatic UIs.
        
        
            key: Key name for the field value to change.
            value: Initial value for this field.
            prompt: Prompt to display in the user interface (Content Browsers) if this
                    is null or an 
             empty string the this field is a data only field and will
                    not appear in the user 
             interface.
        
        AddTextured(self: FieldDictionary, key: str, value: Vector2d, prompt: str) -> Vector2dField
        
            Add a new Vector2dField to the dictionary. This overload will cause the
                    field to be 
             tagged as "textured" so that the texturing UI will appear
                    in automatic UIs.
        
        
            key: Key name for the field value to change.
            value: Initial value for this field.
            prompt: Prompt to display in the user interface (Content Browsers) if this
                    is null or an 
             empty string the this field is a data only field and will
                    not appear in the user 
             interface.
        
        AddTextured(self: FieldDictionary, key: str, value: int, prompt: str) -> IntField
        
            Add a new IntField to the dictionary. This overload will cause the
                    field to be 
             tagged as "textured" so that the texturing UI will appear
                    in automatic UIs.
        
        
            key: Key name for the field value to change.
            value: Initial value for this field.
            prompt: Prompt to display in the user interface (Content Browsers) if this
                    is null or an 
             empty string the this field is a data only field and will
                    not appear in the user 
             interface.
        
        AddTextured(self: FieldDictionary, key: str, value: bool, prompt: str) -> BoolField
        
            Add a new BoolField to the dictionary. This overload will cause the
                    field to be 
             tagged as "textured" so that the texturing UI will appear
                    in automatic UIs.
        
        
            key: Key name for the field value to change.
            value: Initial value for this field.
            prompt: Prompt to display in the user interface (Content Browsers) if this
                    is null or an 
             empty string the this field is a data only field and will
                    not appear in the user 
             interface.
        
        AddTextured(self: FieldDictionary, key: str, value: str, prompt: str) -> StringField
        
            Add a new StringField to the dictionary. This overload will cause the
                    field to be 
             tagged as "textured" so that the texturing UI will appear
                    in automatic UIs.
        
        
            key: Key name for the field value to change.
            value: Initial value for this field.
            prompt: Prompt to display in the user interface (Content Browsers) if this
                    is null or an 
             empty string the this field is a data only field and will
                    not appear in the user 
             interface.
        
        AddTextured(self: FieldDictionary, key: str, value: Single, prompt: str) -> FloatField
        
            Add a new FloatField to the dictionary. This overload will cause the
                    field to be 
             tagged as "textured" so that the texturing UI will appear
                    in automatic UIs.
        
        
            key: Key name for the field value to change.
            value: Initial value for this field.
            prompt: Prompt to display in the user interface (Content Browsers) if this
                    is null or an 
             empty string the this field is a data only field and will
                    not appear in the user 
             interface.
        
        AddTextured(self: FieldDictionary, key: str, value: Color, prompt: str) -> Color4fField
        
            Add a new Color4fField to the dictionary. This overload will cause the
                    field to be 
             tagged as "textured" so that the texturing UI will appear
                    in automatic UIs.
        
        
            key: Key name for the field value to change.
            value: Initial value for this field.
            prompt: Prompt to display in the user interface (Content Browsers) if this
                    is null or an 
             empty string the this field is a data only field and will
                    not appear in the user 
             interface.
        
        AddTextured(self: FieldDictionary, key: str, value: Color4f, prompt: str) -> Color4fField
        
            Add a new Color4fField to the dictionary. This overload will cause the
                    field to be 
             tagged as "textured" so that the texturing UI will appear
                    in automatic UIs.
        
        
            key: Key name for the field value to change.
            value: Initial value for this field.
            prompt: Prompt to display in the user interface (Content Browsers) if this
                    is null or an 
             empty string the this field is a data only field and will
                    not appear in the user 
             interface.
        
        AddTextured(self: FieldDictionary, key: str, value: float, prompt: str) -> DoubleField
        
            Add a new DoubleField to the dictionary. This overload will cause the
                    field to be 
             tagged as "textured" so that the texturing UI will appear
                    in automatic UIs.
        
        
            key: Key name for the field value to change.
            value: Initial value for this field.
            prompt: Prompt to display in the user interface (Content Browsers) if this
                    is null or an 
             empty string the this field is a data only field and will
                    not appear in the user 
             interface.
        """
        pass

    def ContainsField(self, fieldName):
        """
        ContainsField(self: FieldDictionary, fieldName: str) -> bool
        
            Call this method to determine if a this FieldsList contains a field
                    with the 
             specified field name.
        
        
            fieldName: Field to search for
            Returns: Returns true if a field with that matches fieldName is found or false
                    if it is not 
             found.
        """
        pass

    def GetField(self, fieldName):
        """
        GetField(self: FieldDictionary, fieldName: str) -> Field
        
            Call this method to get the field with the matching name.
        
            fieldName: Field name to search for.
            Returns: If the field exists in the Fields dictionary then the field is returned
                    otherwise; 
             null is returned.
        """
        pass

    def Set(self, key, value, changeContext=None):
        """
        Set(self: FieldDictionary, key: str, value: Point2d)
            Set the field value and send the appropriate change notification to the
                    render SDK. 
              Will throw a InvalidOperationException exception if the key
                    name is not valid.
        
        
            key: Key name for the field value to change.
            value: New value for this field.
        Set(self: FieldDictionary, key: str, value: Vector3d, changeContext: ChangeContexts)Set(self: FieldDictionary, key: str, value: Point3d)
            Set the field value and send the appropriate change notification to the
                    render SDK. 
              Will throw a InvalidOperationException exception if the key
                    name is not valid.
        
        
            key: Key name for the field value to change.
            value: New value for this field.
        Set(self: FieldDictionary, key: str, value: Point2d, changeContext: ChangeContexts)Set(self: FieldDictionary, key: str, value: Vector2d)
            Set the field value and send the appropriate change notification to the
                    render SDK. 
              Will throw a InvalidOperationException exception if the key
                    name is not valid.
        
        
            key: Key name for the field value to change.
            value: New value for this field.
        Set(self: FieldDictionary, key: str, value: Color, changeContext: ChangeContexts)Set(self: FieldDictionary, key: str, value: Vector3d)
            Set the field value and send the appropriate change notification to the
                    render SDK. 
              Will throw a InvalidOperationException exception if the key
                    name is not valid.
        
        
            key: Key name for the field value to change.
            value: New value for this field.
        Set(self: FieldDictionary, key: str, value: Vector2d, changeContext: ChangeContexts)Set(self: FieldDictionary, key: str, value: Transform)
            Set the field value and send the appropriate change notification to the
                    render SDK. 
              Will throw a InvalidOperationException exception if the key
                    name is not valid.
        
        
            key: Key name for the field value to change.
            value: New value for this field.
        Set(self: FieldDictionary, key: str, value: Guid, changeContext: ChangeContexts)Set(self: FieldDictionary, key: str, value: DateTime)
            Set the field value and send the appropriate change notification to the
                    render SDK. 
              Will throw a InvalidOperationException exception if the key
                    name is not valid.
        
        
            key: Key name for the field value to change.
            value: New value for this field.
        Set(self: FieldDictionary, key: str, value: Transform, changeContext: ChangeContexts)Set(self: FieldDictionary, key: str, value: Point4d)
            Set the field value and send the appropriate change notification to the
                    render SDK. 
              Will throw a InvalidOperationException exception if the key
                    name is not valid.
        
        
            key: Key name for the field value to change.
            value: New value for this field.
        Set(self: FieldDictionary, key: str, value: Point3d, changeContext: ChangeContexts)Set(self: FieldDictionary, key: str, value: Guid)
            Set the field value and send the appropriate change notification to the
                    render SDK. 
              Will throw a InvalidOperationException exception if the key
                    name is not valid.
        
        
            key: Key name for the field value to change.
            value: New value for this field.
        Set(self: FieldDictionary, key: str, value: Point4d, changeContext: ChangeContexts)Set(self: FieldDictionary, key: str, value: bool)
            Set the field value and send the appropriate change notification to the
                    render SDK. 
              Will throw a InvalidOperationException exception if the key
                    name is not valid.
        
        
            key: Key name for the field value to change.
            value: New value for this field.
        Set(self: FieldDictionary, key: str, value: str, changeContext: ChangeContexts)Set(self: FieldDictionary, key: str, value: int)
            Set the field value and send the appropriate change notification to the
                    render SDK. 
              Will throw a InvalidOperationException exception if the key
                    name is not valid.
        
        
            key: Key name for the field value to change.
            value: New value for this field.
        Set(self: FieldDictionary, key: str, value: bool, changeContext: ChangeContexts)Set(self: FieldDictionary, key: str, value: Array[Byte])
            Set the field value and send the appropriate change notification to the
                    render SDK. 
              Will throw a InvalidOperationException exception if the key
                    name is not valid.
        
        
            key: Key name for the field value to change.
            value: New value for this field.
        Set(self: FieldDictionary, key: str, value: DateTime, changeContext: ChangeContexts)Set(self: FieldDictionary, key: str, value: str)
            Set the field value and send the appropriate change notification to the
                    render SDK. 
              Will throw a InvalidOperationException exception if the key
                    name is not valid.
        
        
            key: Key name for the field value to change.
            value: New value for this field.
        Set(self: FieldDictionary, key: str, value: Array[Byte], changeContext: ChangeContexts)Set(self: FieldDictionary, key: str, value: Color4f)
            Set the field value and send the appropriate change notification to the
                    render SDK. 
              Will throw a InvalidOperationException exception if the key
                    name is not valid.
        
        
            key: Key name for the field value to change.
            value: New value for this field.
        Set(self: FieldDictionary, key: str, value: float, changeContext: ChangeContexts)Set(self: FieldDictionary, key: str, value: Color)
            Set the field value and send the appropriate change notification to the
                    render SDK. 
              Will throw a InvalidOperationException exception if the key
                    name is not valid.
        
        
            key: Key name for the field value to change.
            value: New value for this field.
        Set(self: FieldDictionary, key: str, value: Color4f, changeContext: ChangeContexts)Set(self: FieldDictionary, key: str, value: Single)
            Set the field value and send the appropriate change notification to the
                    render SDK. 
              Will throw a InvalidOperationException exception if the key
                    name is not valid.
        
        
            key: Key name for the field value to change.
            value: New value for this field.
        Set(self: FieldDictionary, key: str, value: int, changeContext: ChangeContexts)Set(self: FieldDictionary, key: str, value: float)
            Set the field value and send the appropriate change notification to the
                    render SDK. 
              Will throw a InvalidOperationException exception if the key
                    name is not valid.
        
        
            key: Key name for the field value to change.
            value: New value for this field.
        Set(self: FieldDictionary, key: str, value: Single, changeContext: ChangeContexts)
        """
        pass

    def SetTag(self, key, tag):
        """
        SetTag(self: FieldDictionary, key: str, tag: object) -> bool
        
            Sets an object that contains data to associate with the field.
        
            key: Key name for the field to tag.
            tag: Data to associate with the field.
            Returns: True if the field is found and the tag was set otherwise false is returned.
        """
        pass

    def TryGetTag(self, key, tag):
        """
        TryGetTag(self: FieldDictionary, key: str) -> (bool, object)
        
            Gets object that contains data associate with a field.
        
            key: Key name of the field to get.
            Returns: Returns true if the field is found and its tag was retrieved otherwise;
                    returns 
             false.
        """
        pass

    def TryGetValue(self, key, value):
        """
        TryGetValue(self: FieldDictionary, key: str) -> (bool, Point3d)
        
            Find a field with the specified key and get its value if found.
        
            key: Key name of the field to get a value for.
            Returns: Returns true if the key is found and the value parameter is set to the
                    field value. 
              Returns false if the field was not found.
        
        TryGetValue(self: FieldDictionary, key: str) -> (bool, Point4d)
        
            Find a field with the specified key and get its value if found.
        
            key: Key name of the field to get a value for.
            Returns: Returns true if the key is found and the value parameter is set to the
                    field value. 
              Returns false if the field was not found.
        
        TryGetValue(self: FieldDictionary, key: str) -> (bool, Vector3d)
        
            Find a field with the specified key and get its value if found.
        
            key: Key name of the field to get a value for.
            Returns: Returns true if the key is found and the value parameter is set to the
                    field value. 
              Returns false if the field was not found.
        
        TryGetValue(self: FieldDictionary, key: str) -> (bool, Point2d)
        
            Find a field with the specified key and get its value if found.
        
            key: Key name of the field to get a value for.
            Returns: Returns true if the key is found and the value parameter is set to the
                    field value. 
              Returns false if the field was not found.
        
        TryGetValue(self: FieldDictionary, key: str) -> (bool, DateTime)
        
            Find a field with the specified key and get its value if found.
        
            key: Key name of the field to get a value for.
            Returns: Returns true if the key is found and the value parameter is set to the
                    field value. 
              Returns false if the field was not found.
        
        TryGetValue(self: FieldDictionary, key: str) -> (bool, Array[Byte])
        
            Find a field with the specified key and get its value if found.
        
            key: Key name of the field to get a value for.
            Returns: Returns true if the key is found and the value parameter is set to the
                    field value. 
              Returns false if the field was not found.
        
        TryGetValue(self: FieldDictionary, key: str) -> (bool, Guid)
        
            Find a field with the specified key and get its value if found.
        
            key: Key name of the field to get a value for.
            Returns: Returns true if the key is found and the value parameter is set to the
                    field value. 
              Returns false if the field was not found.
        
        TryGetValue(self: FieldDictionary, key: str) -> (bool, Transform)
        
            Find a field with the specified key and get its value if found.
        
            key: Key name of the field to get a value for.
            Returns: Returns true if the key is found and the value parameter is set to the
                    field value. 
              Returns false if the field was not found.
        
        TryGetValue(self: FieldDictionary, key: str) -> (bool, int)
        
            Find a field with the specified key and get its value if found.
        
            key: Key name of the field to get a value for.
            Returns: Returns true if the key is found and the value parameter is set to the
                    field value. 
              Returns false if the field was not found.
        
        TryGetValue(self: FieldDictionary, key: str) -> (bool, float)
        
            Find a field with the specified key and get its value if found.
        
            key: Key name of the field to get a value for.
            Returns: Returns true if the key is found and the value parameter is set to the
                    field value. 
              Returns false if the field was not found.
        
        TryGetValue(self: FieldDictionary, key: str) -> (bool, str)
        
            Find a field with the specified key and get its value if found.
        
            key: Key name of the field to get a value for.
            Returns: Returns true if the key is found and the value parameter is set to the
                    field value. 
              Returns false if the field was not found.
        
        TryGetValue(self: FieldDictionary, key: str) -> (bool, bool)
        
            Find a field with the specified key and get its value if found.
        
            key: Key name of the field to get a value for.
            Returns: Returns true if the key is found and the value parameter is set to the
                    field value. 
              Returns false if the field was not found.
        
        TryGetValue(self: FieldDictionary, key: str) -> (bool, Color)
        
            Find a field with the specified key and get its value if found.
        
            key: Key name of the field to get a value for.
            Returns: Returns true if the key is found and the value parameter is set to the
                    field value. 
              Returns false if the field was not found.
        
        TryGetValue(self: FieldDictionary, key: str) -> (bool, Vector2d)
        
            Find a field with the specified key and get its value if found.
        
            key: Key name of the field to get a value for.
            Returns: Returns true if the key is found and the value parameter is set to the
                    field value. 
              Returns false if the field was not found.
        
        TryGetValue(self: FieldDictionary, key: str) -> (bool, Single)
        
            Find a field with the specified key and get its value if found.
        
            key: Key name of the field to get a value for.
            Returns: Returns true if the key is found and the value parameter is set to the
                    field value. 
              Returns false if the field was not found.
        
        TryGetValue(self: FieldDictionary, key: str) -> (bool, Color4f)
        
            Find a field with the specified key and get its value if found.
        
            key: Key name of the field to get a value for.
            Returns: Returns true if the key is found and the value parameter is set to the
                    field value. 
              Returns false if the field was not found.
        """
        pass

    def __add__(self, *args): #cannot find CLR method
        """ x.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+yx.__add__(y) <==> x+y """
        pass


class FloatField(Field):
    """ float field value class """
    def ValueAsObject(self):
        """ ValueAsObject(self: FloatField) -> object """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the field value

Get: Value(self: FloatField) -> Single

Set: Value(self: FloatField) = value
"""



class GuidField(Field):
    """ Guid field value class """
    def ValueAsObject(self):
        """ ValueAsObject(self: GuidField) -> object """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the field value

Get: Value(self: GuidField) -> Guid

Set: Value(self: GuidField) = value
"""



class IntField(Field):
    """ Integer field value class """
    def ValueAsObject(self):
        """ ValueAsObject(self: IntField) -> object """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the field value

Get: Value(self: IntField) -> int

Set: Value(self: IntField) = value
"""



class Point2dField(Field):
    """ Point2d field value class """
    def ValueAsObject(self):
        """ ValueAsObject(self: Point2dField) -> object """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the field value

Get: Value(self: Point2dField) -> Point2d

Set: Value(self: Point2dField) = value
"""



class Point3dField(Field):
    """ Point3d field value class """
    def ValueAsObject(self):
        """ ValueAsObject(self: Point3dField) -> object """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the field value

Get: Value(self: Point3dField) -> Point3d

Set: Value(self: Point3dField) = value
"""



class Point4dField(Field):
    """ Point4d field value class """
    def ValueAsObject(self):
        """ ValueAsObject(self: Point4dField) -> object """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the field value

Get: Value(self: Point4dField) -> Point4d

Set: Value(self: Point4dField) = value
"""



class StringField(Field):
    """ String field value class """
    def ValueAsObject(self):
        """ ValueAsObject(self: StringField) -> object """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the field value

Get: Value(self: StringField) -> str

Set: Value(self: StringField) = value
"""



class TransformField(Field):
    """ Transform field value class """
    def ValueAsObject(self):
        """ ValueAsObject(self: TransformField) -> object """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the field value

Get: Value(self: TransformField) -> Transform

Set: Value(self: TransformField) = value
"""



class Vector2dField(Field):
    """ Vector2d field value class """
    def ValueAsObject(self):
        """ ValueAsObject(self: Vector2dField) -> object """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the field value

Get: Value(self: Vector2dField) -> Vector2d

Set: Value(self: Vector2dField) = value
"""



class Vector3dField(Field):
    """ Vector3d field value class """
    def ValueAsObject(self):
        """ ValueAsObject(self: Vector3dField) -> object """
        pass

    Value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Gets or sets the field value

Get: Value(self: Vector3dField) -> Vector3d

Set: Value(self: Vector3dField) = value
"""



