#kth smallest element
class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.right = None 
        self.left = None  
 
 
def insertIntoBST(root, ele):
    if root == None:
        newBlock = TreeNode(ele)
        return newBlock 
 
    if root.data < ele:
        root.right = insertIntoBST(root.right, ele)
    else:
        root.left = insertIntoBST(root.left, ele)
    return root
 
def printInorderTraversal(root):
    if root == None:
        return 
 
    printInorderTraversal(root.left)
    print(root.data, end = " ")
    printInorderTraversal(root.right)
n=int(input())
nums = list(map(int,input().split()))
k=int(input())

root = None 
for ele in nums:
    root = insertIntoBST(root, ele)

def fillInorder(inorder,root):
    if root==None:
        return
    fillInorder(inorder,root.left)
    inorder.append(root.data)
    fillInorder(inorder,root.right)
    
def insertIntoBST(root,ele):
    if root==None:
        new=TreeNode(ele)
        return new
    if root.data<ele:
        root.right=insertIntoBST(root.right,ele)
    else:
        root.left=insertIntoBST(root.left,ele)
    return root

root=None
for ele in nums:
    root=insertIntoBST(root,ele)
    
inorder=[]
fillInorder(inorder,root)
print(inorder[k-1])
