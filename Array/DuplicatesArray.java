lass Solution:
    def duplicates(self, arr, n):
        # code here
        a = []
        dup = {}
        for i in arr:
           if i in dup:
                dup[i] += 1
           else:
                dup[i] = 1

        for i in dup:
            if dup[i] > 1:
                a.append(i)
        if len(a) == 0:
            a.append(-1)

        a.sort()
        return a

