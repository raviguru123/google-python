import sys

def hello(name):
    if name=='ravi' or name=='guru':
        print 'mode=',name;
    else:
        doeodod('else part');
    name=name+'!!!!';
    print 'hello',name;

def main():
    hello(sys.argv[1]);

if __name__=='__main__':
    main();

dir(sys)