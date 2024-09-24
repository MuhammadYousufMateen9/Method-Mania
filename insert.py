class MethodMania:
    def ins(lst,data,pos):
        data=[data]
        list1=lst[:pos]
        list2=lst[pos:]
        list1=list1+data
        final=list1+list2
        return final