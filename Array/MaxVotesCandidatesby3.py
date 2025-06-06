
def findMajority(self, arr):
    # Your Code goes here.

    person1 = person2 = None
    votecount1 = votecount2 = 0
    size = 0

    for candidate in arr:

        size += 1
        if person1 == candidate:
            votecount1 += 1
        elif person2 == candidate:
            votecount2 += 1
        elif votecount1 == 0:
            person1, votecount1 = candidate, 1
        elif votecount2 == 0:
            person2, votecount2 = candidate, 1
        else:
            votecount1 -= 1
            votecount2 -= 1

    votecount1 = votecount2 = 0

    for candidate in arr:
        if candidate == person1:
            votecount1 += 1
        elif candidate == person2:
            votecount2 += 1

    result = []
    if votecount1 > size // 3:
        result.append(person1)
    if votecount2 > size // 3:
        result.append(person2)

    return sorted(result)