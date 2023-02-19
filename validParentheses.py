
class Solution:
    def isValid(self, s: str) -> bool:
        #Use push() and pop() function that works like the stack's push n pop
        #**edit: revised push() to append() bc python doesn't have built-in push()
        #instead of pop() in conditional, can use stack[-1]
        #Declare a list variable to store each characters in string
        #For loop to iterate the string 
        #Conditional statements to append the character if it is an opening tag (, {, [
        #Conditional statements for closing tags
            #nested conditional to stop the For loop (return False)if the string didn't have opening tags 
            #OR the last character appended doesn't match the current closing tag.
            #If above condition isn't met, the brackeets were matched, 
            #and pop() in conditional already removes the opening tag 
        #When the entire string was looped through,
        #check the length of the remaining list of the string to be 0 
        #If the length is 0, the input string is valid, return True 
        
    
        stack = []
        
        for c in s:
            if(c =="{"):
                stack.append(c)
            if(c =="["):
                stack.append(c)
            if(c =="("):
                stack.append(c)
            if(c =="}"):
                #if(len(stack)== 0 or stack.pop() != "{" ):
                #    return False
                if(stack[-1] != "{"):
                    return False
                else:
                    stack.pop()    
            if(c ==")"):
                #if(len(stack)== 0 or stack.pop() != "(" ):
                #    return False
                if(stack[-1] != "("):
                    return False
                else:
                    stack.pop()    
            if(c =="]"):
                #if(len(stack)== 0 or stack.pop() != "[" ):
                #    return False
                if(stack[-1] != "["):
                    return False
                else:
                    stack.pop()    
        if(len(stack) == 0):
            return True

