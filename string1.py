#this is first function for returning number of donuts;
def donuts(count):
    value="Number of donuts:";
    if(count<10):
        value+=' '+str(count);
    else:
        value+=' many';
    return value;

#print donuts(10);
#print donuts(9);

#this is second exercise for returning both end string;
def both_ends(str):
    if(len(str)<2):
        return "";
    else:
        return str[0:2]+str[len(str)-2:];

#print both_ends('sp');

#replace all occurance of it's first character

def fix_start(str,rep='*'):
    str1=str[0];
    return str[0]+str[1:].replace(str1,rep);

#print fix_start('babble','*');

# mixup program

def mix_up(str1,str2):
    return str2[0:2]+str1[2:]+'  '+ str1[0:2]+str2[2:];

# print mix_up('dog', 'dinner');
# print mix_up('mix', 'pod');


def test(got,expected):
    if(got==expected):
        prefix=' Ok';
    else:
        prefix='Wrong';
    print '%s got:%s expected: %s'%(prefix,got,expected);

def main():
    test(donuts(10),'Number of donuts: many');
    test(donuts(9),'Number of donuts: 9');
    test(fix_start('babble'), 'ba**le')
    test(fix_start('aardvark'), 'a*rdv*rk')
    test(fix_start('google'), 'goo*le')
    test(fix_start('donut'), 'donut')
    
if __name__=='__main__':
    main();