from sys import stdin

readline = stdin.readline

n, m = map(int, readline().split())
stations = list(map(int, readline().split()))

MAX = 1000000
prev = [0] * (MAX + 1)
nxt = [0] * (MAX + 1)
answer = []

for i in range(n):
    prev[stations[i]] = stations[i - 1]
    nxt[stations[i]] = stations[(i + 1) % n]

for _ in range(m):
    cmd = readline().split()

    if cmd[0] == "BN":
        i = int(cmd[1])
        j = int(cmd[2])
        # BN 4줄
        r = nxt[i]
        answer.append(str(r))
        nxt[i] = j
        prev[j] = i
        nxt[j] = r
        prev[r] = j

    elif cmd[0] == "BP":
        i = int(cmd[1])
        j = int(cmd[2])
        # BP 4줄
        l = prev[i]
        answer.append(str(l))
        nxt[l] = j
        prev[j] = l
        nxt[j] = i
        prev[i] = j

    elif cmd[0] == "CN":
        i = int(cmd[1])
        # CN 4줄
        target = nxt[i]
        answer.append(str(target))
        r = nxt[target]
        nxt[i] = r
        prev[r] = i

    else:
        i = int(cmd[1])
        # CP 4줄
        target = prev[i]
        answer.append(str(target))
        l = prev[target]
        prev[i] = l
        nxt[l] = i

print("\n".join(answer))
