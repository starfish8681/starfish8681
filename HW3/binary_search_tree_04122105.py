class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def insert(self, root, val):
        if root.val:
            if root.val == val:
                pass   #已經有此數
            elif root.val < val:
                if root.right:
                    root = root.right
                    return self.insert(root, val)  
                else:
                    root.right = TreeNode(val)
            else:
                if root.left:
                    root = root.left
                    return self.insert(root, val)
                else:
                    root.left = TreeNode(val)
        else:
            root.val = TreeNode(val)
            
    def search(self, root, target):
        if root.val:
            if root.val == target:
                return True
            elif root.val < target:
                if root.right:
                    root = root.right
                    return self.search(root, target)  
                else:
                    return None
            else: 
                if root.left:
                    root = root.left
                    return self.search(root, target)
        else:
            return None
        
    def delete(self, root, target):
        if self.search(root,target) is True:   
            if root.val == target:
                if root.left is None and root.right is None:
                    root.val = None   
                elif root.left is None and root.right != None:
                    root.val = root.right   
                elif root.left != None and root.right is None:
                    root.val = root.left
                elif root.left and root.right:
                    replacednodeP = root
                    replacednode = root.right
                    while replacednode.left:
                        replacednodeP = replacednode
                        replacednode = replacednode.left
                    root.val = replacednode.val
                    if replacednode.right:
                        if replacednodeP.val < replacednode.val:
                            replacednodeP.right = replacednode.right
                        else:
                            replacednodeP.left = replacednode.right
                    else:    #replacednode本身就是最後一個左子節點，所以不會還有left
                        if replacednodeP.val < replacednode.val:
                            replacednodeP.right = None
                        else:
                            replacednodeP.left = None

                    
            elif root.val != target:
                parent = None
                currentnode = root
                while currentnode != target:
                    if currentnode.val < target:
                        parent = currentnode
                        currentnode = currentnode.left
                    elif currentnode.val > target:
                        parent = currentnode
                        currentnode = currentnode.right
                if currentnode.left is None and currentnode.right is None:
                    if parent.val < target:
                        parent.right = None
                    else:
                        parent.left = None
                elif currentnode.left is None and currentnode.right != None:
                    if parent.val < target:
                        parent.right = currentnode.right
                    else:
                        parent.left = currentnode.right  
                elif currentnode.left != None and currentnode.right is None:
                    if parent.val < target:
                        parent.right = currentnode.left
                    else:
                        parent.left = currentnode.left  
                elif currentnode.left and currentnode.right:
                    replacednodeP = currentnode
                    replacednode = currentnode.right
                    while replacednode.left:
                        replacednodeP = replacednode
                        replacednode = replacednode.left
                    currentnode.val = replacednode.val
                    if replacednode.right:
                        if replacednodeP.val < replacednode.val:
                            replacednodeP.right = replacednode.right
                        else:
                            replacednodeP.left = replacednode.right
                    else:       #replacednode本身就是最後一個左子節點，所以不會還有left
                        if replacednodeP.val < replacednode.val:
                            replacednodeP.right = None
                        else:
                            replacednodeP.left = None
     
        else:
            pass             
        return root.val             
    
    def modify(self, root, target, new_val):    
        if root == new_val:
            pass
        else:
            self.delete(root, target)
            self.insert(root, new_val)
        return root.val
