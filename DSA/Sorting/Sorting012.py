def sort012(self, arr):
        res = sorted(arr)
        for i in range(len(arr)):
            arr[i] = res[i]
        return arr