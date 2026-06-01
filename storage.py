class History:
    def __init__(self, size=10):
        self.size = size
        self.inside_t = []
        self.inside_h = []
        self.outside_t = []
        self.outside_h = []

    def _trim(self, arr):
        if len(arr) > self.size:
            del arr[0]

    def add(self, in_t, in_h, out_t, out_h):
        self.inside_t.append(in_t)
        self.inside_h.append(in_h)
        self.outside_t.append(out_t)
        self.outside_h.append(out_h)

        self._trim(self.inside_t)
        self._trim(self.inside_h)
        self._trim(self.outside_t)
        self._trim(self.outside_h)