

def question1(s, t):
    '''Given two strings s and t, determine whether some anagram of t
    is a substring of s. For example: if s = "udacity" and t = "ad",
    then the function returns True. Your function definition should
    look like: question1(s, t) and return a boolean True or False.'''
    
    # If s does not exist, we can find our answer immediately
    if (not s): 
        if(t):
            return False
        else:
            return True
            
    # Loop through the letters in t
    while(t):
        index = s.find(t[0])
        # If a letter in t can not be found, we know the answer is False
        if (index == -1):
            return False
        else:
            # Found a matching letter, remove from t and s and keep looking
            t = t[1:]
            s = s[:index]+s[index+1:]
                
    # All the letters in t have been accounted for, so the answer is True
    return True
    
def question2(a):
    '''Given a string a, find the longest palindromic substring
    contained in a. Your function definition should look like
    question2(a), and return a string.'''
    # If a does not exist, we can exit immediatly
    if(not a):
        return ""
        
    # Since a exists, the smallest palindrome is 1
    longest_string = 1 
    longest_palindrome = a[0] # start with the first letter as smallest palindrome (any letter would do)
    
    palindrome_check_len = len(a)
    while(palindrome_check_len > 0):
        # check for palindrome at current len
        for i in range(len(a) - palindrome_check_len + 1):
            to_check = a[i:palindrome_check_len+i]
            if(is_palindrome(to_check)):
                return to_check
            
        # decrement the size you are checking for
        palindrome_check_len -= 1
        
        
    # Didn't find any
    return ""
    
def is_palindrome(s):
    '''check if a string is a palindrome'''
    for i in range(len(s)):
        if(not(s[i] == s[len(s) - 1 - i])):
            return False
        if(i >= (len(s) - i)): 
            # Exit if your counters meet in the middle
            return True
    return True
    
def question3(G):
    '''Given an undirected graph G, find the minimum spanning tree
    within G. A minimum spanning tree connects all vertices in a graph
    with the smallest possible total weight of edges. Your function
    should take in and return an adjacency list structured like this:
        {'A': [('B', 2)],
        'B': [('A', 2), ('C', 5)], 
        'C': [('B', 5)]}
    Vertices are represented as unique strings. 
    The function definition should be question3(G)'''
    pass
    
def question4(T, r, n1, n2):
    '''Find the least common ancestor between two nodes on a binary
    search tree. The least common ancestor is the farthest node from the
    root that is an ancestor of both nodes. For example, the root is a
    common ancestor of all nodes on the tree, but if both nodes are
    descendents of the root's left child, then that left child might be
    the lowest common ancestor. You can assume that both nodes are in
    the tree, and the tree itself adheres to all BST properties. The
    function definition should look like question4(T, r, n1, n2), 
    where T is the tree represented as a matrix, where the index of the
    list is equal to the integer stored in that node and a 1 represents
    a child node, r is a non-negative integer representing the root,
    and n1 and n2 are non-negative integers representing the two nodes
    in no particular order. For example, one test case might be
        question4([[0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [1, 0, 0, 0, 1],
                [0, 0, 0, 0, 0]],
                3,
                1,
                4)
    and the answer would be 3.'''
    pass
    
    
def question5(ll, m):
    '''Find the element in a singly linked list that's m elements from
    the end. For example, if a linked list has 5 elements, the 3rd
    element from the end is the 3rd element. The function definition
    should look like question5(ll, m), where ll is the first node of a
    linked list and m is the "mth number from the end". You should
    copy/paste the Node class below to use as a representation of a
    node in the linked list. Return the value of the node at that position.
        class Node(object):
            def __init__(self, data):
                self.data = data
                self.next = None'''
    if (not ll):
        return None
    
    nodes_in_ll = []
    current_node = ll
    
    # Add all the nodes to a stack
    while(current_node):
        nodes_in_ll.append(current_node)
        current_node = current_node.next
    
    # See if we have enough nodes
    if(len(nodes_in_ll) < m):
        return None
    else:
        node = None
        # Pop off m nodes and return the value of the mth
        for i in range(m):
            node = nodes_in_ll.pop(0)
        return node.data
    pass
    
class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None
    
## Test Cases ##
print("Question 1:")
print("s: udacity", "t: ad", question1("udacity", "ad"))
print("s: udacity", "t: ada", question1("udacity", "ada"))
print("s: udacity", "t:", question1("udacity", ""))
print("s:", "t: ad", question1("", "ad"))
print("s: None", "t: ad", question1(None, "ad"))
print("s: udacity", "t: None", question1("udacity", None))
print("s: None", "t: None", question1(None, None))

print("")

print("Question 2:")
print("cheese", question2("cheese"))
print("ooooo", question2("ooooo"))
print("None", question2(None))
print("(Empty string)", question2(""))
print("abcdeffed", question2("abcdeffed"))
print("abcdefed", question2("abcdefed"))

print("")

print("Question 3:")
print("Question 4:")
print("Question 5:")
Node1 = Node(1)
Node2 = Node(2)
Node3 = Node(3)
Node4 = Node(4)
Node5 = Node(5)
# LL1
Node1.next = Node2
Node2.next = Node3
Node3.next = Node4
Node4.next = Node5
print("Size of LL: 5", "m: 3", question5(Node1, 3))

Node1_1 = Node(1)
Node2_1 = Node(2)
Node3_1 = Node(3)
# LL2
Node1_1.next = Node2_1
Node2_1.next = Node3_1
print("Size of LL: 3", "m: 5", question5(Node1_1, 5))

# LL3
Node1_3 = Node(1)
print("Size of LL: 1", "m: 1", question5(Node1_3, 1))

# Empty LL
print("Size of LL: None", "m: 2", question5(None, 2))
