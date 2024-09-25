def index(lst,data):

    #iterate on length of list
    for i in range(len(lst)):

        #if element is equal to data
        if lst[i] == data:

            #return index of that element
            return i
    
    #else return none
    return None
