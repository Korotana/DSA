def findString(self, N, K):
    # code here
    from collections import defaultdict

    if N == 1:
        return ''.join(str(i) for i in range(K))

    graph = defaultdict(list)

    for i in range(K ** (N - 1)):
        prefix = ''
        temp = i
        for _ in range(N - 1):
            prefix = str(temp % K) + prefix
            temp //= K
        for j in range(K):
            graph[prefix].append(str(j))

    start = '0' * (N - 1)
    stack = [start]
    result = []

    while stack:
        node = stack[-1]
        if graph[node]:
            next_digit = graph[node].pop()
            next_node = node[1:] + next_digit
            stack.append(next_node)
        else:
            stack.pop()
            if stack:  # Only append if stack still has elements
                result.append(stack[-1][-1])  # Safe now

    return start + ''.join(reversed(result))