# 各頂点の出次数が1の有向単純グラフにおいて、各頂点からK個先にある頂点を O(N√N)で求められる。
# K は大きくてOK。
class FunctionalGraph:
    # O(N√N)
    def __init__(self, n: int, next: list[int]) -> None:
        self.n = n
        self.sqrt_n = int(n**0.5)
        self.nexts = next
        self.prevs = [-1] * n
        for i, j in enumerate(next):
            self.prevs[j] = i
        self.jumps = [-1] * self.n
        self.visited = [False] * self.n
        self.cycles = [-1] * self.n
        self.dis_to_cycle = [-1] * self.n

        self.calc_cycles()
        self.calc_jumps()

    def calc_jumps(self) -> None:
        self.dis_to_cycle_sorted = [(j, i) for i, j in enumerate(self.dis_to_cycle)]
        self.dis_to_cycle_sorted.sort(key=lambda x: x[0], reverse=True)
        for _, s in self.dis_to_cycle_sorted:
            now = s
            if self.prevs[now] != -1 and self.jumps[self.prevs[now]] != -1:
                self.jumps[s] = self.nexts[self.jumps[self.prevs[now]]]
            else:
                for _ in range(self.sqrt_n):
                    now = next[now]
                self.jumps[s] = now

    def calc_cycles(self) -> None:
        for s in range(self.n):
            if not self.visited[s]:
                path, cycle = self.dfs(s)
                for i, v in enumerate(cycle):
                    self.cycles[v] = cycle
                    self.dis_to_cycle[v] = -i
                if cycle:
                    for i, v in enumerate(path[::-1], start=1):
                        self.cycles[v] = cycle
                        self.dis_to_cycle[v] = i
                else:
                    dis = self.dis_to_cycle[self.nexts[path[-1]]]
                    for i, v in enumerate(path[::-1], start=1):
                        self.cycles[v] = self.cycles[self.nexts[path[-1]]]
                        self.dis_to_cycle[v] = dis + i

    def dfs(self, s: int) -> tuple[list[int], list[int]]:
        stack = [s]
        path = [s]
        cycle = []
        self.visited[s] = True
        while stack:
            now = stack.pop()
            next = self.nexts[now]
            if not self.visited[next]:
                stack.append(next)
                self.visited[next] = True
                path.append(next)
        next = self.nexts[path[-1]]
        index = 0
        while index < len(path):
            if path[index] == next:
                path, cycle = path[:index], path[index:]
                break
            index += 1
        return path, cycle

    # 頂点sのk個先の頂点を返す O(√N)
    def get_next(self, s: int, k: int) -> int:
        if k == 0:
            return s
        now = s

        if k >= self.dis_to_cycle[now]:
            cycle_len = len(self.cycles[now])
            return self.cycles[now][(k - self.dis_to_cycle[now]) % cycle_len]

        while k > 0:
            if k >= self.sqrt_n:
                k -= self.sqrt_n
                now = self.jumps[now]
            else:
                k -= 1
                now = self.nexts[now]
        return now

    # 全ての頂点からのk個先の頂点のリストを返す O(N√N)
    def get_next_all(self, k: int) -> int:
        if k == 0:
            return list(range(self.n))
        result = [-1] * self.n
        for _, s in self.dis_to_cycle_sorted:
            now = s
            if self.prevs[now] != -1 and result[self.prevs[now]] != -1:
                result[s] = self.nexts[result[self.prevs[now]]]
                continue
            if k >= self.dis_to_cycle[now]:
                cycle_len = len(self.cycles[now])
                result[s] = self.cycles[now][(k - self.dis_to_cycle[now]) % cycle_len]
                continue

            while k > 0:
                if k >= self.sqrt_n:
                    k -= self.sqrt_n
                    now = self.jumps[now]
                else:
                    k -= 1
                    now = self.nexts[now]
            result[s] = now

        return result
