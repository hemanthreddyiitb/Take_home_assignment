from typing import List, Optional

# defining a node 
class Node:
    def __init__(self, val=None, children=None):
        if children is None:
            children = []
            # empty list when no children are provided
        self.val = val
        self.children = children

class Solution:
    def createTree(self, input: List[Optional[int]]) -> Optional[Node]:
        # if  input list is empty, return no tree
        if not input:
            return None

        nodes = []  
        root = None  # to keep track of  root node

        # Creating nodes for all non-None values in the input list
        for val in input:
            if val is not None:
                new_node = Node(val)
                nodes.append(new_node)  
                # appending the new node to the list
                if root is None:
                    root = new_node  
                    # settinf the root node if it's not already set
            else:
                nodes.append(None)  # Keep a None placeholder for children

        # Build the tree structure using a stack
        stack = []
        for i in range(len(input)):
            if input[i] is not None:
                current_node = nodes[i]  # get  current node
                # attach children to  current node
                while stack and input[stack[-1]] is None:
                    stack.pop()  # remove none placeholders from  stack

                if stack:
                    parent_idx = stack[-1]  # get  index of the parent node
                    nodes[parent_idx].children.append(current_node)  # add current node as a child

                stack.append(i)  # push index of the current node onto the stack

        return root  

    def postorder(self, root: Node) -> List[int]:
        
        if not root:
            return []

        result = []  # To store  result of postorder traversal
        stack = [(root, False)]  # Stack holds tuples of (node, visited status)
        
        while stack:
            node, visited = stack.pop()  # Pop the top item from the stack
            if visited:
                # If the node has been visited, add its value to the result
                result.append(node.val)
            else:
                # If the node has not been visited, push it back as visited
                stack.append((node, True))
                # Push all children to the stack in reversed order
                for child in reversed(node.children):
                    stack.append((child, False))  # Mark children as not visited

        return result  # Return the postorder traversal result

# Example 
solution = Solution()
tree_root = solution.createTree([1, None, 3, 2, 4, None, 5, 6])
postorder_result = solution.postorder(tree_root)
print(postorder_result)  

tree_root2 = solution.createTree([1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10, None, None, 11, None, 12, None, 13, None, None, 14])
postorder_result2 = solution.postorder(tree_root2)
print(postorder_result2)  
