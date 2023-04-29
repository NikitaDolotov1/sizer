def sizer(cls):
    class Sized(cls):
        @property
        def size(self):
            try:
                return len(self)
            except:

                try:
                    return abs(self)
                except:
                    return 0

    return Sized

@sizer
class Val:
    def __init__(self, val):
        self.val = val

    def __abs__(self):
        return abs(self.val)

    def __len__(self):
        return len(self.val)

val1 = Val([1, 2, 3, 5])
print(val1.size)

val2 = Val(24)
print(val2.size)

val3 = Val(None)
print(val3.size)