# Able: a simple configuration format

A quick example:

    key: 'value'
    'a multiline
    string'
    # A comment
    myList: [  # a trailing comment
      1
      'item 2'
      item3: 'the end'
    ]
    
The top-level of an Able file is an implicit list, meaning it isn't
surrounded by square braces.

## Encoding

UTF-8, always.

## Data types

- Numbers: integers and floats. Integers can be prefixed with `0x` for
  hex or `0b` for binary. Case does not matter; `0xabc` is the same as
  `0XABC`. In addition to normal numeric floats the special names
  `nan` and `inf` can be used. `inf` can also be spelled
  `infinity`. Again, case does not matter. Examples:

        42
        3.14
        0xff
        0b11001001
        -inf
        infinity
        +INFINITY
        nan

- Strings: denoted by either a single quote or a double quote. Forward
  slash (`\`) is used for escaping special characters. Regular
  newlines (unescaped) are allowed in strings. Examples:

        'a string'
        "also a string"
        "a
        multiline
        string"
        'a "silly" string\'\t\n'

- Pair: a key and its value separated by a colon (`:`). The key cannot
  contain spaces or escape characters. The value can be any data
  type. Examples:

        key: 'value'
        another_key: 22
        
- List: a whitespace-separated sequence of values of any type,
  surrounded by square brackets. Mixed types are allowed. Note that
  any whitespace can be used to separate items and commas are not used
  to separate items. The order of items in a list is significant. If
  the list contains pairs with duplicate keys, the later pair
  overrides the earlier pair. Client libraries should allow numeric
  indexing into the list as well as string lookup. The latter only
  applies to pair elements. Examples:
  
        []
        ['a' "b" 3]
        ['a' ['nested'] 'list]
        [key: 'value' 3.14]
        [key: 'value' key: 'this overrides the previous value]

## Rationale

Why another configuration format? I wasn't able to find an existing
one that seemed quite right to me. I probably missed something; let me
know if so!

Why not JSON? Overall I like JSON, but it often doesn't "read" well
for human editing. It tends to use a lot of indentation, long strings
must be forced onto a single line, and comments aren't
allowed. Treating trailing commas as an error is also very annoying.

Why not YAML? In my opinion YAML is just way too complicated.

Why not TOML? TOML's attempts to make nested data structures appear
more flat end up just being confusing to me.

Why not INI? Not well specified, doesn't have a consistent way to
represent lists / objects.

Why is the top level of an Able file an implicit list? To reduce
unnecessary indentation. Almost every configuration file is going to
be a list anyway.

Why a list type but no map/hash/object type? To keep things simple and
reduce unnecessary nesting.
