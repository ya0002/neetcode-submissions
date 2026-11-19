class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res =[]

        def dfs(i,cur,total):
            if total==target:
                res.append(cur.copy())
                return
            if total>target or i>len(nums)-1:
                return

            
            cur.append(nums[i])
            dfs(i,cur,total+nums[i])
            cur.pop()
            dfs(i+1,cur,total)

        dfs(0,[],0)
        return res

# class Solution:
#     def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
#         res = []
#         # Each item on the stack: (start_index, current_combination, current_total)
#         stack = [(0, [], 0)]

#         while stack:
#             idx, cur, total = stack.pop()

#             if total == target:
#                 res.append(cur)
#                 continue

#             # Try picking any number from idx onward
#             for i in range(idx, len(nums)):
#                 new_total = total + nums[i]
#                 if new_total <= target:
#                     # nums[i] can be reused, so pass index 'i' instead of 'i + 1'
#                     stack.append((i, cur + [nums[i]], new_total))

#         return res