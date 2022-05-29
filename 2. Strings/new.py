
string = input()
n = len(string)
palindrome = ''

def isPalindrome(s):
    s = list(s)
    s = list(filter(lambda x:x.isalnum(),s))
    s = list(map(lambda x:x.lower(),s))
    
    n = len(s)
    start = 0
    end = n-1
    mid = (n//2)
    for k in range(mid):
        if s[start+k]!=s[end-k]:
            return False
    return True

for i in range(n):
    for j in range(i+1,n):

        if isPalindrome(string[i:j]):
            if len(string[i:j])>len(palindrome):
                palindrome = string[i:j]




