from typing import List
from collections import defaultdict

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        # Build the folder tree
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.to_delete = False
        
        root = TrieNode()
        
        # Build the trie from all paths
        for path in paths:
            node = root
            for folder in path:
                if folder not in node.children:
                    node.children[folder] = TrieNode()
                node = node.children[folder]
        
        # Generate subtree signatures and mark duplicates
        def get_signature(node):
            """
            Returns a tuple representing the structure of this subtree.
            Also marks nodes for deletion if they have duplicates.
            """
            if not node.children:
                # Leaf node - empty signature
                return tuple()
            
            # Get signatures of all children
            child_signatures = []
            for folder_name in sorted(node.children.keys()):
                child_node = node.children[folder_name]
                child_sig = get_signature(child_node)
                child_signatures.append((folder_name, child_sig))
            
            # Current node's signature is tuple of sorted (name, signature) pairs
            signature = tuple(child_signatures)
            
            # Track signatures to find duplicates
            if not hasattr(get_signature, 'signature_count'):
                get_signature.signature_count = defaultdict(int)
                get_signature.signature_to_nodes = defaultdict(list)
            
            get_signature.signature_count[signature] += 1
            get_signature.signature_to_nodes[signature].append(node)
            
            return signature
        
        # Generate signatures for all nodes
        get_signature(root)
        
        # Mark nodes with duplicate signatures for deletion
        for signature, count in get_signature.signature_count.items():
            if count > 1 and signature:  # signature is empty for leaf nodes, don't delete those
                for node in get_signature.signature_to_nodes[signature]:
                    node.to_delete = True
        
        # Mark all descendants of deleted nodes for deletion
        def mark_descendants(node):
            if node.to_delete:
                for child in node.children.values():
                    child.to_delete = True
                    mark_descendants(child)
            else:
                for child in node.children.values():
                    mark_descendants(child)
        
        mark_descendants(root)
        
        # Collect remaining paths
        result = []
        
        def dfs(node, current_path):
            if node.to_delete:
                return
            
            # If this is not root and not marked for deletion, it's a valid folder
            if current_path:  # not root
                result.append(current_path[:])
            
            # Continue to children
            for folder_name, child_node in node.children.items():
                current_path.append(folder_name)
                dfs(child_node, current_path)
                current_path.pop()
        
        dfs(root, [])
        return result

# Test cases
def test_solution():
    sol = Solution()
    
    # Test case 1
    paths1 = [["a"],["c"],["d"],["a","b"],["c","b"],["d","a"]]
    result1 = sol.deleteDuplicateFolder(paths1)
    print("Test 1:", result1)
    # Expected: [["d"],["d","a"]] (folders /a and /c are identical)
    
    # Test case 2  
    paths2 = [["a"],["c"],["a","b"],["c","b"],["a","b","x"],["a","b","x","y"],["w"],["w","y"]]
    result2 = sol.deleteDuplicateFolder(paths2)
    print("Test 2:", result2)
    # Expected: [["w"],["w","y"]] (folders /a and /c are identical)
    
    # Test case 3
    paths3 = [["a","b"],["c","d"],["c"],["a"]]
    result3 = sol.deleteDuplicateFolder(paths3)
    print("Test 3:", result3)
    # Expected: [["a","b"],["c","d"],["c"],["a"]] (no identical folders)

if __name__ == "__main__":
    test_solution()