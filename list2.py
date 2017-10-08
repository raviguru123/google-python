def remove_adjacent(list1):
    prev="";
    list2=[];
    for el in list1:
        if(prev!=el):
            list2.append(el);
        prev=el;
    return list2;


# print(remove_adjacent([1, 2, 2, 3]));


def linear_merge(list1,list2):
    index1=0;
    index2=0;
    list3=[];
    while len(list1)!=0 and len(list2)!=0:
        if(list1[index1]<list2[index2]):
            list3.append(list1.pop(index1));
        else:
            list3.append(list2.pop(index2));
    if(len(list1)>0):
        for i in list1:
            list3.append(i);  
    else:
        for i in list2:
            list3.append(i);  
    return list3;


# print (linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']));


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))

def main():
    print 'remove_adjacent'
    test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    test(remove_adjacent([]), [])

    print
    print 'linear_merge'
    test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
        ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
        ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
        ['aa', 'aa', 'aa', 'bb', 'bb'])


if __name__ == '__main__':
  main()
