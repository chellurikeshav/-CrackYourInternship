class Solution:
    def intToRoman(self, num: int) -> str:
        new_dict = {1: 'I',
                    4:'IV',
                    5:'V',
                    9:'IX',
                    10:'X',
                    40:'XL',
                    50:'L',
                    90:'XC',
                    100:'C',
                    400:'CD',
                    500:'D',
                    900:'CM',
                    1000:'M'}
        roman = []
        num = str(num)
        n = len(num)
        k = 0
        for i in reversed(range(n)):
            x = int(num[i])*(10**k)
            
            if x in new_dict:
                roman.insert(0,new_dict[x])
                k+=1
                continue
            
            keys = [5,50,500,5000]
            for j in range(4):
                
                if 1*(10**j)<=x<=3*(10**j):
                    roman.insert(0,new_dict[10**j]*int(x/10**j))
            

                if 6*(10**j)<=x<=8*(10**j):
                    roman.insert(0,new_dict[keys[j]]+new_dict[10**j]*int((x-keys[j])/10**j))
            k+=1
        return ''.join(roman)
        
        
        