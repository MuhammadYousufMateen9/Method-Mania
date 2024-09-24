def delete(lst,data):
    for i in range(len(lst)):
        if data==lst[i]:
            lst1=lst[:i]
            lst2=lst[i+1:]
            final_list=lst1+lst2
            return final_list
    else:
        return f"{data} is not in list."
