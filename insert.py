def ins(lst,data,pos):

    #changing datatype from int to list
    data=[data]

    #slicing original list from 0 to the position given
    list1=lst[:pos]

    #slicing original list from position given to last 
    list2=lst[pos:]

    #concatenating list 1 and data to be inserted
    list1=list1+data

    #concatenating list 1 and list 2 
    final=list1+list2

    #return final list after insertion
    return final
