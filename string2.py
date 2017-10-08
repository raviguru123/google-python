def verbing(str):
    if(len(str)>2):
        if(str[-3:]=='ing'):
            return str+'ly';
        else:
            return str+'ing';
    return str;

def not_bad(str):
    if(str.find('not')>-1 and str.find('bad')>-1 and str.find('bad')>str.find('not')):
        badc=str.find('bad');
        notc=str.find('not');
        return str[0:notc]+'good'+ str[badc+3:];
    return str;

# print not_bad('This dinner is not that bad!');

def front_back(a,b):
    if(len(a)%2==0):
        indexa=len(a)/2;
    else:
        (len(a)/2)+1;

    if(len(b)%2==0):
        indexb=len(b)/2;
    else:
        (len(b)/2)+1;
    
    return a[0:indexa]+b[0:indexb]+a[indexa:]+b[indexb:];

# print front_back('abcd', 'xy');


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
  print 'verbing'
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')

  print
  print 'not_bad'
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")

  print
  print 'front_back'
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  main()
        

    

