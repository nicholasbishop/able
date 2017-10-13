import collections

class Serializer(object):
    def __init__(self):
        self._indent_level = 0
        self._output = ''

    def put(self, line):
        self._output += '  ' * self._indent_level + line + '\n'

    def is_valid_pair_key(self, key):
        # TODO
        return isinstance(key, str)

    def serialize_int(self, val):
        self.put(str(val))

    def serialize_pair(self, key, val):
        self.put('{}: {}'.format(key, val))

    def serialize_map_inner(self, val):
        for key in val:
            # TODO
            if not self.is_valid_pair_key(key):
                raise KeyError(key)
            self.serialize_pair(key, val[key])

    def serialize_map(self, val):
        self.put('[')
        # TODO "with self.indent..."
        self._indent_level += 1
        self.serialize_map_inner(val)
        self._indent_level -= 1
        self.put(']')

    def serialize_any(self, data):
        if isinstance(data, collections.Mapping):
            self.serialize_map(data)

    def serialize(self, data):
        # TODO
        self._indent_level = 0
        self._output = ''

        # TODO
        data['able'] = 1

        # TODO
        self.serialize_map_inner(data)
        return self._output
