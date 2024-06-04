# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        node = root
        col = 0
        que = deque([(node, col)])
        res_dict = defaultdict(list)
        res = []

        while que:
            curnode, curcol  = que.popleft()
            
            if curnode:
                res_dict[curcol].append(curnode.val)
                que.append((curnode.left, curcol-1))
                que.append((curnode.right, curcol+1))

        res = [res_dict[x] for x in sorted(res_dict.keys())]
        return res


