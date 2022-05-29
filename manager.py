class Manager:
    def __init__(self, _class=None):
        self._class = _class

    def search(self, **kwargs):

        results = []
        for key, value in kwargs.items():
            if key.endswith('__min'):
                key = key[:-5]
                compare_key = 'min'
            elif key.endswith('__max'):
                key = key[:-5]
                compare_key = 'max'
            else:
                compare_key = 'equal'

            for var_item in self._class.object_list:
                if hasattr(var_item, key):
                    if compare_key == 'min':
                        result = getattr(var_item, key) >= value
                    elif compare_key == 'max':
                        result = getattr(var_item, key) <= value
                    else:
                        result = getattr(var_item, key) == value
                    if result:
                        results.append(var_item)
        return results

    def get_single(self, **kwargs):
        for key, value in kwargs.items():
            for var_item in self._class.object_list:
                if hasattr(var_item, key) and getattr(var_item, key) == value:
                    return var_item
        return None

    def count(self):
        return len(self._class.object_list)


