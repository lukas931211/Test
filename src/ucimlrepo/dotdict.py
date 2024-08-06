class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

    # requires as suggested here in order to allow for pickling the dotdict https://stackoverflow.com/a/2050357
    def __getstate__(self): return self.__dict__
    def __setstate__(self, d): self.__dict__.update(d)
