# Tree is data structure for hirerical and organize data
# tree traversal = pre order=  # root,left,right.  in order= left,root,right. post order=  left,right,root

class TreeNode:
  def __init__(self,val):
     self.val = val
     self.left, self.right = None, None


def traverse(root):
  if root:
    print(root.val)
    traverse(root.left)
    traverse(root.right)

def main():
    root = TreeNode(50)

    root.left = TreeNode(10)
    root.right = TreeNode(20)

    root.left.left = TreeNode(5)
    root.left.right = TreeNode(15)

    root.right.left = TreeNode(23)
    root.right.right = TreeNode(25)
    traverse(root)
main()
   
