from typing import List
import heapq


class Solution:
    def busiestServers(self,
                       k: int,
                       arrival: List[int],
                       load: List[int],
                       ) -> List[int]:
        busy = [0 for _ in range(k)]
        req_handled = [0 for _ in range(k)]

        for i in range(len(arrival)):
            arr, loa = arrival[i], load[i]

            index = i % k
            if busy[index] <= arr:
                busy[index] = arr + loa
                req_handled[index] += 1
            else:
                shifter = 1
                while (i + shifter) % k != index:
                    shifted = (i + shifter) % k
                    if busy[shifted] <= arr:
                        busy[shifted] = arr + loa
                        req_handled[shifted] += 1
                        break
                    shifter += 1

            print(f'busy: {busy}')
            print(f'req_: {req_handled}')

        print(req_handled)

        return [i for i, x in enumerate(req_handled) if x == max(req_handled)]

    def busiestServers2(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        # heap (job_end_time, node) to free up the nodes quickly
        busy_jobs = []
        after = []  # heap (nodes) free after current server
        before = list(range(k))  # heap (nodes) to use for loopback
        requests_handled = [0] * k

        for i, (arrvl, ld) in enumerate(zip(arrival, load)):
            server_id = i % k
            if server_id == 0:  # loopback
                after = before
                before = []

            print(f'after: {after}')
            print(f'before: {before}')

            while busy_jobs and busy_jobs[0][0] <= arrvl:
                freed_node = heapq.heappop(busy_jobs)[1]
                if freed_node < server_id:
                    heapq.heappush(before, freed_node)
                else:
                    heapq.heappush(after, freed_node)

            use_queue = after if after else before
            if not use_queue:
                continue  # request dropped
            using_node = heapq.heappop(use_queue)
            requests_handled[using_node] += 1
            heapq.heappush(busy_jobs, (arrvl + ld, using_node))

            print(busy_jobs)

        maxreqs = max(requests_handled)
        return [i for i, handled in enumerate(requests_handled) if handled == maxreqs]


sol = Solution()
print(sol.busiestServers2(k=3, arrival=[
      1, 2, 3, 4, 8, 9, 10], load=[5, 2, 10, 3, 1, 2, 2]))
