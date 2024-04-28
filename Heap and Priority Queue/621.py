class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        ls = {}
        for task in tasks:
            if task in ls:
                ls[task] += 1
            else:
                ls[task] = 1

        m = 0
        f = 1
        for i in ls.values():
            if i > m:
                m = i
                f = 1
            elif i == m:
                f += 1

        print(n, m, f, len(tasks))
        return max(((n + 1) * (m - 1)) + f, len(tasks))
