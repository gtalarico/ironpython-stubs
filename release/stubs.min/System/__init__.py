# encoding: utf-8
# module System
# from mscorlib,Version=4.0.0.0,Culture=neutral,PublicKeyToken=b77a5c561934e089,System,Version=4.0.0.0,Culture=neutral,PublicKeyToken=b77a5c561934e089
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# functions

def Action(p_object,method): # real signature unknown; restored from __doc__
 """
 Encapsulates a method that has no parameters and does not return a value.

 

 Action(object: object,method: IntPtr)
 """
 pass
def EventHandler(p_object,method): # real signature unknown; restored from __doc__
 """
 Represents the method that will handle an event that has no event data.

 

 EventHandler(object: object,method: IntPtr)
 """
 pass
def Func(*args,**kwargs): # real signature unknown
 """
 A TypeCollision is used when we have a collision between

    two types with the same name.  Currently this is only possible w/ generic

    methods that should logically have arity as a portion of their name. For eg:

      System.EventHandler and System.EventHandler[T]

      System.Nullable and System.Nullable[T]

      System.IComparable and System.IComparable[T]

    

    The TypeCollision provides an indexer but also is a real type.  When used

    as a real type it is the non-generic form of the type.

    

    The indexer allows the user to disambiguate between the generic and

    non-generic versions.  Therefore users must always provide additional

    information to get the generic version.
 """
 pass
def IComparable(*args,**kwargs): # real signature unknown
 """ Defines a generalized type-specific comparison method that a value type or class implements to order or sort its instances. """
 pass
def Nullable(*args,**kwargs): # real signature unknown
 """ Supports a value type that can be assigned null like a reference type. This class cannot be inherited. """
 pass
def Tuple(*args,**kwargs): # real signature unknown
 """ Provides static methods for creating tuple objects. """
 pass
def ValueTuple(*args,**kwargs): # real signature unknown
 """  """
 pass
def WeakReference(target): # real signature unknown; restored from __doc__
 """
 Represents a weak reference,which references an object while still allowing that object to be reclaimed by garbage collection.

 

 WeakReference(target: object)

 WeakReference(target: object,trackResurrection: bool)
 """
 pass
# classes
from __init___parts.Object import Object
from __init___parts.Exception import Exception
from __init___parts.SystemException import SystemException
from __init___parts.AccessViolationException import AccessViolationException
from __init___parts.IDisposable import IDisposable
from __init___parts.ActivationContext import ActivationContext
from __init___parts.Activator import Activator
from __init___parts.AggregateException import AggregateException
from __init___parts.AppContext import AppContext
from __init___parts.MarshalByRefObject import MarshalByRefObject
from __init___parts._AppDomain import _AppDomain
from __init___parts.AppDomain import AppDomain
from __init___parts.Delegate import Delegate
from __init___parts.MulticastDelegate import MulticastDelegate
from __init___parts.AppDomainInitializer import AppDomainInitializer
from __init___parts.AppDomainManager import AppDomainManager
from __init___parts.IConvertible import IConvertible
from __init___parts.IFormattable import IFormattable
from __init___parts.Enum import Enum
from __init___parts.AppDomainManagerInitializationOptions import AppDomainManagerInitializationOptions
from __init___parts.AppDomainSetup import AppDomainSetup
from __init___parts.AppDomainUnloadedException import AppDomainUnloadedException
from __init___parts.ApplicationException import ApplicationException
from __init___parts.ApplicationId import ApplicationId
from __init___parts.ApplicationIdentity import ApplicationIdentity
from __init___parts.ArgIterator import ArgIterator
from __init___parts.ArgumentException import ArgumentException
from __init___parts.ArgumentNullException import ArgumentNullException
from __init___parts.ArgumentOutOfRangeException import ArgumentOutOfRangeException
from __init___parts.ArithmeticException import ArithmeticException
from __init___parts.ICloneable import ICloneable
from __init___parts.Array import Array
from __init___parts.ArraySegment import ArraySegment
from __init___parts.ArrayTypeMismatchException import ArrayTypeMismatchException
from __init___parts.EventArgs import EventArgs
from __init___parts.AssemblyLoadEventArgs import AssemblyLoadEventArgs
from __init___parts.AssemblyLoadEventHandler import AssemblyLoadEventHandler
from __init___parts.AsyncCallback import AsyncCallback
from __init___parts.Attribute import Attribute
from __init___parts.AttributeTargets import AttributeTargets
from __init___parts.AttributeUsageAttribute import AttributeUsageAttribute
from __init___parts.BadImageFormatException import BadImageFormatException
from __init___parts.Base64FormattingOptions import Base64FormattingOptions
from __init___parts.BitConverter import BitConverter
from __init___parts.Int32 import Int32
from __init___parts.Boolean import Boolean
from __init___parts.Buffer import Buffer
from __init___parts.Byte import Byte
from __init___parts.CannotUnloadAppDomainException import CannotUnloadAppDomainException
from __init___parts.Char import Char
from __init___parts.CharEnumerator import CharEnumerator
from __init___parts.CLSCompliantAttribute import CLSCompliantAttribute
from __init___parts.Comparison import Comparison
from __init___parts.Console import Console
from __init___parts.ConsoleCancelEventArgs import ConsoleCancelEventArgs
from __init___parts.ConsoleCancelEventHandler import ConsoleCancelEventHandler
from __init___parts.ConsoleColor import ConsoleColor
from __init___parts.ConsoleKey import ConsoleKey
from __init___parts.ConsoleKeyInfo import ConsoleKeyInfo
from __init___parts.ConsoleModifiers import ConsoleModifiers
from __init___parts.ConsoleSpecialKey import ConsoleSpecialKey
from __init___parts.ContextBoundObject import ContextBoundObject
from __init___parts.ContextMarshalException import ContextMarshalException
from __init___parts.ContextStaticAttribute import ContextStaticAttribute
from __init___parts.Convert import Convert
from __init___parts.Converter import Converter
from __init___parts.CrossAppDomainDelegate import CrossAppDomainDelegate
from __init___parts.DataMisalignedException import DataMisalignedException
from __init___parts.DateTime import DateTime
from __init___parts.DateTimeKind import DateTimeKind
from __init___parts.DateTimeOffset import DateTimeOffset
from __init___parts.DayOfWeek import DayOfWeek
from __init___parts.DBNull import DBNull
from __init___parts.Decimal import Decimal
from __init___parts.DivideByZeroException import DivideByZeroException
from __init___parts.TypeLoadException import TypeLoadException
from __init___parts.DllNotFoundException import DllNotFoundException
from __init___parts.Double import Double
from __init___parts.DuplicateWaitObjectException import DuplicateWaitObjectException
from __init___parts.EntryPointNotFoundException import EntryPointNotFoundException
from __init___parts.Environment import Environment
from __init___parts.EnvironmentVariableTarget import EnvironmentVariableTarget
from __init___parts.ExecutionEngineException import ExecutionEngineException
from __init___parts.MemberAccessException import MemberAccessException
from __init___parts.FieldAccessException import FieldAccessException
from __init___parts.UriParser import UriParser
from __init___parts.FileStyleUriParser import FileStyleUriParser
from __init___parts.FlagsAttribute import FlagsAttribute
from __init___parts.FormatException import FormatException
from __init___parts.FormattableString import FormattableString
from __init___parts.FtpStyleUriParser import FtpStyleUriParser
from __init___parts.GC import GC
from __init___parts.GCCollectionMode import GCCollectionMode
from __init___parts.GCNotificationStatus import GCNotificationStatus
from __init___parts.GenericUriParser import GenericUriParser
from __init___parts.GenericUriParserOptions import GenericUriParserOptions
from __init___parts.GopherStyleUriParser import GopherStyleUriParser
from __init___parts.Guid import Guid
from __init___parts.HttpStyleUriParser import HttpStyleUriParser
from __init___parts.IAppDomainSetup import IAppDomainSetup
from __init___parts.IAsyncResult import IAsyncResult
from __init___parts.ICustomFormatter import ICustomFormatter
from __init___parts.IEquatable import IEquatable
from __init___parts.IFormatProvider import IFormatProvider
from __init___parts.IndexOutOfRangeException import IndexOutOfRangeException
from __init___parts.InsufficientExecutionStackException import InsufficientExecutionStackException
from __init___parts.OutOfMemoryException import OutOfMemoryException
from __init___parts.InsufficientMemoryException import InsufficientMemoryException
from __init___parts.Int16 import Int16
from __init___parts.Int64 import Int64
from __init___parts.IntPtr import IntPtr
from __init___parts.InvalidCastException import InvalidCastException
from __init___parts.InvalidOperationException import InvalidOperationException
from __init___parts.InvalidProgramException import InvalidProgramException
from __init___parts.InvalidTimeZoneException import InvalidTimeZoneException
from __init___parts.IObservable import IObservable
from __init___parts.IObserver import IObserver
from __init___parts.IProgress import IProgress
from __init___parts.IServiceProvider import IServiceProvider
from __init___parts.Lazy import Lazy
from __init___parts.LdapStyleUriParser import LdapStyleUriParser
from __init___parts.LoaderOptimization import LoaderOptimization
from __init___parts.LoaderOptimizationAttribute import LoaderOptimizationAttribute
from __init___parts.LocalDataStoreSlot import LocalDataStoreSlot
from __init___parts.Math import Math
from __init___parts.MethodAccessException import MethodAccessException
from __init___parts.MidpointRounding import MidpointRounding
from __init___parts.MissingMemberException import MissingMemberException
from __init___parts.MissingFieldException import MissingFieldException
from __init___parts.MissingMethodException import MissingMethodException
from __init___parts.ModuleHandle import ModuleHandle
from __init___parts.MTAThreadAttribute import MTAThreadAttribute
from __init___parts.MulticastNotSupportedException import MulticastNotSupportedException
from __init___parts.NetPipeStyleUriParser import NetPipeStyleUriParser
from __init___parts.NetTcpStyleUriParser import NetTcpStyleUriParser
from __init___parts.NewsStyleUriParser import NewsStyleUriParser
from __init___parts.NonSerializedAttribute import NonSerializedAttribute
from __init___parts.NotFiniteNumberException import NotFiniteNumberException
from __init___parts.NotImplementedException import NotImplementedException
from __init___parts.NotSupportedException import NotSupportedException
from __init___parts.NullReferenceException import NullReferenceException
from __init___parts.ObjectDisposedException import ObjectDisposedException
from __init___parts.ObsoleteAttribute import ObsoleteAttribute
from __init___parts.OperatingSystem import OperatingSystem
from __init___parts.OperationCanceledException import OperationCanceledException
from __init___parts.OverflowException import OverflowException
from __init___parts.ParamArrayAttribute import ParamArrayAttribute
from __init___parts.PlatformID import PlatformID
from __init___parts.PlatformNotSupportedException import PlatformNotSupportedException
from __init___parts.Predicate import Predicate
from __init___parts.Progress import Progress
from __init___parts.Random import Random
from __init___parts.RankException import RankException
from __init___parts.ResolveEventArgs import ResolveEventArgs
from __init___parts.ResolveEventHandler import ResolveEventHandler
from __init___parts.RuntimeArgumentHandle import RuntimeArgumentHandle
from __init___parts.RuntimeFieldHandle import RuntimeFieldHandle
from __init___parts.RuntimeMethodHandle import RuntimeMethodHandle
from __init___parts.RuntimeTypeHandle import RuntimeTypeHandle
from __init___parts.SByte import SByte
from __init___parts.SerializableAttribute import SerializableAttribute
from __init___parts.Single import Single
from __init___parts.StackOverflowException import StackOverflowException
from __init___parts.STAThreadAttribute import STAThreadAttribute
from __init___parts.String import String
from __init___parts.StringComparer import StringComparer
from __init___parts.StringComparison import StringComparison
from __init___parts.StringSplitOptions import StringSplitOptions
from __init___parts.ThreadStaticAttribute import ThreadStaticAttribute
from __init___parts.TimeoutException import TimeoutException
from __init___parts.TimeSpan import TimeSpan
from __init___parts.TimeZone import TimeZone
from __init___parts.TimeZoneInfo import TimeZoneInfo
from __init___parts.TimeZoneNotFoundException import TimeZoneNotFoundException
from __init___parts.TupleExtensions import TupleExtensions
from __init___parts.Type import Type
from __init___parts.TypeAccessException import TypeAccessException
from __init___parts.TypeCode import TypeCode
from __init___parts.TypedReference import TypedReference
from __init___parts.TypeInitializationException import TypeInitializationException
from __init___parts.TypeUnloadedException import TypeUnloadedException
from __init___parts.UInt16 import UInt16
from __init___parts.UInt32 import UInt32
from __init___parts.UInt64 import UInt64
from __init___parts.UIntPtr import UIntPtr
from __init___parts.UnauthorizedAccessException import UnauthorizedAccessException
from __init___parts.UnhandledExceptionEventArgs import UnhandledExceptionEventArgs
from __init___parts.UnhandledExceptionEventHandler import UnhandledExceptionEventHandler
from __init___parts.Uri import Uri
from __init___parts.UriBuilder import UriBuilder
from __init___parts.UriComponents import UriComponents
from __init___parts.UriFormat import UriFormat
from __init___parts.UriFormatException import UriFormatException
from __init___parts.UriHostNameType import UriHostNameType
from __init___parts.UriIdnScope import UriIdnScope
from __init___parts.UriKind import UriKind
from __init___parts.UriPartial import UriPartial
from __init___parts.UriTypeConverter import UriTypeConverter
from __init___parts.ValueType import ValueType
from __init___parts.Version import Version
from __init___parts.Void import Void
