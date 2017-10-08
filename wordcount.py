import sys

def cat(filename):
    dict={};
    f=open(filename,'rU');
    for line in f:
        arr=line.split();
        for w in arr:
             word=w.lower();
             if(word in dict):
                 dict[word]+=1;
             else:
                 dict[word]=1;
    for w in sorted(dict.keys()):
        print w,' ',dict[w];    


def Last(touple):
    return touple[1];


def print_top(filename):
    dict={};
    f=open(filename,'rU');
    for line in f:
        arr=line.split();
        for w in arr:
             word=w.lower();
             if(word in dict):
                 dict[word]+=1;
             else:
                 dict[word]=1;
    arr=dict.items(); 
    arr=sorted(arr,key=Last);
    print arr;
   

def main():
    print_top(sys.argv[1]);

if __name__=='__main__':
    main();