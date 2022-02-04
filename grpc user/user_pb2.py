# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='user.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nuser.proto\"%\n\x08\x42ookName\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03num\x18\x02 \x01(\x05\" \n\x08\x61rrBooks\x12\x14\n\x05\x62ooks\x18\x01 \x03(\x0b\x32\x05.Book\"\x1a\n\tBookPrice\x12\r\n\x05price\x18\x01 \x01(\x04\"\x91\x01\n\x04\x42ook\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x61uthors\x18\x02 \x03(\t\x12\x11\n\tpublisher\x18\x03 \x01(\t\x12\x17\n\x0f\x64\x61te_of_release\x18\x04 \x01(\t\x12\x15\n\x05genre\x18\x05 \x01(\x0e\x32\x06.Genre\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\x12\x12\n\nextra_info\x18\x07 \x01(\t\"+\n\nPagination\x12\x0e\n\x06offset\x18\x01 \x01(\x05\x12\r\n\x05limit\x18\x02 \x01(\x05*q\n\x05Genre\x12\x08\n\x04NONE\x10\x00\x12\x13\n\x0fSCIENCE_FICTION\x10\x01\x12\x0b\n\x07ROMANCE\x10\x02\x12\t\n\x05\x44RAMA\x10\x03\x12\n\n\x06\x43OMEDY\x10\x04\x12\n\n\x06HORROR\x10\x05\x12\r\n\tADVENTURE\x10\x06\x12\n\n\x06\x41\x43TION\x10\x07\x32U\n\x04user\x12\'\n\x0eget_book_price\x12\t.BookName\x1a\n.BookPrice\x12$\n\nextra_info\x12\x0b.Pagination\x1a\t.arrBooksb\x06proto3'
)

_GENRE = _descriptor.EnumDescriptor(
  name='Genre',
  full_name='Genre',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SCIENCE_FICTION', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ROMANCE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DRAMA', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='COMEDY', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='HORROR', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ADVENTURE', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ACTION', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=308,
  serialized_end=421,
)
_sym_db.RegisterEnumDescriptor(_GENRE)

Genre = enum_type_wrapper.EnumTypeWrapper(_GENRE)
NONE = 0
SCIENCE_FICTION = 1
ROMANCE = 2
DRAMA = 3
COMEDY = 4
HORROR = 5
ADVENTURE = 6
ACTION = 7



_BOOKNAME = _descriptor.Descriptor(
  name='BookName',
  full_name='BookName',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='BookName.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='num', full_name='BookName.num', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=14,
  serialized_end=51,
)


_ARRBOOKS = _descriptor.Descriptor(
  name='arrBooks',
  full_name='arrBooks',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='books', full_name='arrBooks.books', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=53,
  serialized_end=85,
)


_BOOKPRICE = _descriptor.Descriptor(
  name='BookPrice',
  full_name='BookPrice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='price', full_name='BookPrice.price', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=87,
  serialized_end=113,
)


_BOOK = _descriptor.Descriptor(
  name='Book',
  full_name='Book',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Book.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='authors', full_name='Book.authors', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='publisher', full_name='Book.publisher', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='date_of_release', full_name='Book.date_of_release', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='genre', full_name='Book.genre', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='Book.description', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='extra_info', full_name='Book.extra_info', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=116,
  serialized_end=261,
)


_PAGINATION = _descriptor.Descriptor(
  name='Pagination',
  full_name='Pagination',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='offset', full_name='Pagination.offset', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='limit', full_name='Pagination.limit', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=263,
  serialized_end=306,
)

_ARRBOOKS.fields_by_name['books'].message_type = _BOOK
_BOOK.fields_by_name['genre'].enum_type = _GENRE
DESCRIPTOR.message_types_by_name['BookName'] = _BOOKNAME
DESCRIPTOR.message_types_by_name['arrBooks'] = _ARRBOOKS
DESCRIPTOR.message_types_by_name['BookPrice'] = _BOOKPRICE
DESCRIPTOR.message_types_by_name['Book'] = _BOOK
DESCRIPTOR.message_types_by_name['Pagination'] = _PAGINATION
DESCRIPTOR.enum_types_by_name['Genre'] = _GENRE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BookName = _reflection.GeneratedProtocolMessageType('BookName', (_message.Message,), {
  'DESCRIPTOR' : _BOOKNAME,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:BookName)
  })
_sym_db.RegisterMessage(BookName)

arrBooks = _reflection.GeneratedProtocolMessageType('arrBooks', (_message.Message,), {
  'DESCRIPTOR' : _ARRBOOKS,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:arrBooks)
  })
_sym_db.RegisterMessage(arrBooks)

BookPrice = _reflection.GeneratedProtocolMessageType('BookPrice', (_message.Message,), {
  'DESCRIPTOR' : _BOOKPRICE,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:BookPrice)
  })
_sym_db.RegisterMessage(BookPrice)

Book = _reflection.GeneratedProtocolMessageType('Book', (_message.Message,), {
  'DESCRIPTOR' : _BOOK,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:Book)
  })
_sym_db.RegisterMessage(Book)

Pagination = _reflection.GeneratedProtocolMessageType('Pagination', (_message.Message,), {
  'DESCRIPTOR' : _PAGINATION,
  '__module__' : 'user_pb2'
  # @@protoc_insertion_point(class_scope:Pagination)
  })
_sym_db.RegisterMessage(Pagination)



_USER = _descriptor.ServiceDescriptor(
  name='user',
  full_name='user',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=423,
  serialized_end=508,
  methods=[
  _descriptor.MethodDescriptor(
    name='get_book_price',
    full_name='user.get_book_price',
    index=0,
    containing_service=None,
    input_type=_BOOKNAME,
    output_type=_BOOKPRICE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='extra_info',
    full_name='user.extra_info',
    index=1,
    containing_service=None,
    input_type=_PAGINATION,
    output_type=_ARRBOOKS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_USER)

DESCRIPTOR.services_by_name['user'] = _USER

# @@protoc_insertion_point(module_scope)
