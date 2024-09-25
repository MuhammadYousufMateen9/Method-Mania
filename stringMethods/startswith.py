class String:
    def __init__(self,string):
        self.string=string

    def startswith(self,element):

        #if length of string is 0 return False
        if len(self.string)==0:
            return False

        #checking if string first element is equal to searching element
        elif self.string[0]==element:
            return True
        
        #else return False
        else:
            return False
        

