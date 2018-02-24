import random
import itertools as it

def drop(a):
    flat_a = [i for j in a for i in j]
    new_a = [reversed(list(k)) for v,k in it.groupby(
        sorted(flat_a,key=lambda x:x[1]),lambda x:x[1])]
    return [list(filter(None,i)) for i in it.zip_longest(*new_a)][::-1]
def drop2(a):
    result = []
    nums = sorted({i[1] for j in a for i in j})
    new_a = sorted([i for j in a for i in j],key=lambda x:x[1])[::-1]

    while new_a:
        temp=[]
        for i in nums:
            for j in range(len(new_a)):
                if i in new_a[j]:
                    temp.append(new_a.pop(j))
                    break
        result.insert(0,temp)
    return result


def drop3(list1):
   list2=[0 for i in range(len(list1))]
   list3=[]
   j = 0
   for i in list1:
      list2[j]=len(i)
      j+=1
   while(len(list2)):
     a=list1.pop(list2.index(min(list2)))
     list3.append(a)
     list2.pop(list2.index(min(list2)))
   return list3

def drop4(a):
    b = sorted(a,key = lambda s:len(s))
    return b

def drop5(ls):
    ls_len = []
    for each in ls:
        ls_len.append(len(each))

    if ls_len == sorted(ls_len):
        return ls

    for i in range(len(ls)-1,0,-1):
        if len(ls[i]) < len(ls[i-1]):
            j = len(ls[i-1])-len(ls[i])
            ls[i] += ls[i-1][-j:]
            ls[i-1] = ls[i-1][:-j]
    return drop5(ls)


def drop6(list1):
    maxlen = max([len(i) for i in list1])
    for i in range(10):
        list1[i] += ['' for j in range(len(list1[i]), maxlen)]
    lst = [list(i) for i in zip(*list1)]
    for i in lst:
        i.sort()
    lst = [list(i) for i in zip(*lst)]
    for i in range(10):
        while '' in lst[i]:
            lst[i].remove('')
    return lst

list1 = [[] for i in range(10)]
for i in range(10):
    for j in range(random.randint(1,9)):
        list1[i].append(chr(65+i) + str(j))

for i in drop6(list1):
    print(i)
