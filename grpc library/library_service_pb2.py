# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: library_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='library_service.proto',
  package='library',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x15library_service.proto\x12\x07library\"\xf3\x01\n\x04\x42ook\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x61uthors\x18\x02 \x03(\t\x12\x11\n\tpublisher\x18\x03 \x01(\t\x12\x17\n\x0f\x64\x61te_of_release\x18\x04 \x01(\t\x12\"\n\x05genre\x18\x05 \x01(\x0e\x32\x13.library.Book.Genre\x12\x13\n\x0b\x64\x65scription\x18\x06 \x01(\t\"g\n\x05Genre\x12\n\n\x06\x41\x43TION\x10\x00\x12\x13\n\x0fSCIENCE_FICTION\x10\x01\x12\x0b\n\x07ROMANCE\x10\x02\x12\t\n\x05\x44RAMA\x10\x03\x12\n\n\x06\x43OMEDY\x10\x04\x12\n\n\x06HORROR\x10\x05\x12\r\n\tADVENTURE\x10\x06\"\x1a\n\x07Message\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x18\n\x08\x42ookName\x12\x0c\n\x04name\x18\x01 \x01(\t2\xc8\x01\n\x07Library\x12+\n\x08\x61\x64\x64_book\x12\r.library.Book\x1a\x10.library.Message\x12\x32\n\x0b\x64\x65lete_book\x12\x11.library.BookName\x1a\x10.library.Message\x12.\n\x0bupdate_book\x12\r.library.Book\x1a\x10.library.Message\x12,\n\x08get_book\x12\x11.library.BookName\x1a\r.library.Bookb\x06proto3'
)



_BOOK_GENRE = _descriptor.EnumDescriptor(
  name='Genre',
  full_name='library.Book.Genre',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ACTION', index=0, number=0,
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
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=175,
  serialized_end=278,
)
_sym_db.RegisterEnumDescriptor(_BOOK_GENRE)


_BOOK = _descriptor.Descriptor(
  name='Book',
  full_name='library.Book',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='library.Book.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='authors', full_name='library.Book.authors', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='publisher', full_name='library.Book.publisher', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='date_of_release', full_name='library.Book.date_of_release', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='genre', full_name='library.Book.genre', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='library.Book.description', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _BOOK_GENRE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=35,
  serialized_end=278,
)


_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='library.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='library.Message.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=280,
  serialized_end=306,
)


_BOOKNAME = _descriptor.Descriptor(
  name='BookName',
  full_name='library.BookName',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='library.BookName.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=308,
  serialized_end=332,
)

_BOOK.fields_by_name['genre'].enum_type = _BOOK_GENRE
_BOOK_GENRE.containing_type = _BOOK
DESCRIPTOR.message_types_by_name['Book'] = _BOOK
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
DESCRIPTOR.message_types_by_name['BookName'] = _BOOKNAME
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Book = _reflection.GeneratedProtocolMessageType('Book', (_message.Message,), {
  'DESCRIPTOR' : _BOOK,
  '__module__' : 'library_service_pb2'
  # @@protoc_insertion_point(class_scope:library.Book)
  })
_sym_db.RegisterMessage(Book)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGE,
  '__module__' : 'library_service_pb2'
  # @@protoc_insertion_point(class_scope:library.Message)
  })
_sym_db.RegisterMessage(Message)

BookName = _reflection.GeneratedProtocolMessageType('BookName', (_message.Message,), {
  'DESCRIPTOR' : _BOOKNAME,
  '__module__' : 'library_service_pb2'
  # @@protoc_insertion_point(class_scope:library.BookName)
  })
_sym_db.RegisterMessage(BookName)



_LIBRARY = _descriptor.ServiceDescriptor(
  name='Library',
  full_name='library.Library',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=335,
  serialized_end=535,
  methods=[
  _descriptor.MethodDescriptor(
    name='add_book',
    full_name='library.Library.add_book',
    index=0,
    containing_service=None,
    input_type=_BOOK,
    output_type=_MESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='delete_book',
    full_name='library.Library.delete_book',
    index=1,
    containing_service=None,
    input_type=_BOOKNAME,
    output_type=_MESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='update_book',
    full_name='library.Library.update_book',
    index=2,
    containing_service=None,
    input_type=_BOOK,
    output_type=_MESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='get_book',
    full_name='library.Library.get_book',
    index=3,
    containing_service=None,
    input_type=_BOOKNAME,
    output_type=_BOOK,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_LIBRARY)

DESCRIPTOR.services_by_name['Library'] = _LIBRARY

# @@protoc_insertion_point(module_scope)