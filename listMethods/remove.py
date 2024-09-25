def remove(lst,data):

    #iterate on length of list
    for i in range(len(lst)):

        #if data is equal to element present in list
        if data==lst[i]:

            #slicing lst till the position of data 
            lst1=lst[:i]

            #slicing lst from the position of data plus one till end
            lst2=lst[i+1:]

            #concatenate lst1 and lst2
            final_list=lst1+lst2

            #return final_list after removal of element
            return final_list
        
    #else return error message
    else:
        return f"{data} is not in list."
    
