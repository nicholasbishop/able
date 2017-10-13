import collections

import six


class Block(object):
    def __init__(self):
        self._output = ''
        self._indent_level = 0

    def open_value(self, text):
        pass

    def close_value(self, text):
        pass

    def simple_value(self, text):
        pass


class Serializer(object):
    def __init__(self):
        self._indent_level = 0
        self._output = ''
        self._needs_indent = False

    def put(self, line):
        if self._needs_indent:
            self._output += '  ' * self._indent_level
            self._needs_indent = False
        self._output += line

    def eol(self):
        self._output += '\n'
        self._needs_indent = True

    def is_valid_pair_key(self, key):
        # TODO
        return isinstance(key, str)

    def serialize_int(self, data):
        self.put(str(data))
        self.eol()

    def serialize_float(self, data):
        self.put(str(data))
        self.eol()

    def serialize_string(self, data):
        self.put("'{}'".format(data))
        self.eol()

    def serialize_pair(self, key, val):
        self.put(key)
        self.put(': ')
        self.serialize_any(val)

    def serialize_map_inner(self, val):
        # TODO
        for key in sorted(val):
            # TODO
            if not self.is_valid_pair_key(key):
                raise KeyError(key)
            self.serialize_pair(key, val[key])

    def serialize_map(self, val):
        self.put('[')
        self.eol()
        # TODO "with self.indent..."
        self._indent_level += 1
        self.serialize_map_inner(val)
        self._indent_level -= 1
        self.put(']')
        self.eol()

    def serialize_any(self, data):
        if isinstance(data, collections.Mapping):
            self.serialize_map(data)
        elif isinstance(data, six.string_types):
            self.serialize_string(data)
        elif isinstance(data, int):
            self.serialize_int(data)
        elif isinstance(data, float):
            self.serialize_float(data)

    def serialize(self, data):
        # TODO
        self._indent_level = 0
        self._output = ''

        # TODO
        self.serialize_map_inner(data)
        return self._output
