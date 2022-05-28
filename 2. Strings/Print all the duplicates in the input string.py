def Duplicates(string):

    check = {}
    for i in string:
        if i in check:
            check[i]+=1
        else:
            check[i] = 1
    
    for key,value in check.items():
        print(f'Count of "{key}" : {value}')

string = 'aaaaaaaaaa'
Duplicates(string)
