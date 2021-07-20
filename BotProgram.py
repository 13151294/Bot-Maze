class array:
    def __init__(self, arr):
        self.arr = arr

    def reshape(self, l, r):
        arr = []
        if (len(self.arr) != l * r):
            raise ValueError
        for i in range(l):
            arr.append([])
            for j in self.arr[i*r:(i*r)+r]:
                arr[i].append(j)
        return arr