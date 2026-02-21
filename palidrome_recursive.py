def panlindrome(sentence):
    if len(sentence)<=1:
        return True 
    else:
        if sentence[0]!=sentence[-1]:
            a=False
        else:
            
            return panlindrome(sentence[1:-1])
    return a
sentence=input("Enter the para:")
output=panlindrome(sentence)
print(output)