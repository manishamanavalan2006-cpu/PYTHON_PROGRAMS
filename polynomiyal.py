def conditon_poly(poly_name):
    result=[]
    for exp in poly_name:
        if poly_name[exp]!=0:  #polynokiyal coefficent not equal to zero
            result.append(poly_name[exp],exp)
    result.sort(key=lambda x:x[1],reverse=True)   #exponent desc order write pannradhu
    return result 

def add_poly(p1,p2):
    poly_name={}
    for coeff,exp in p1:
        poly_name[exp]=poly_name.get(exp,0)+coeff  #first polynomiyal add pannradhu
    for coeff,exp in p2:
        poly_name[exp]=poly_name.get(exp,0)+coeff   #second polynomiyal add pannradhu
        return conditon_poly(poly_name)
    
def mul_poly(p1,p2):
    poly_name={}
    for coeff1,exp1 in p1:
        for coeff2,exp2 in p2:
            new_coff=coeff1*coeff2 #two polynomiyal coefficient add pannradhu
            new_exp=exp1*exp2     #two po;lynomiyal exponent add pannradhu

            poly_name[new_exp]=poly_name.get(new_exp,0)+new_exp
    return conditon_poly(poly_name)

n1=int(input("Enter the terms in first polynomiyal:"))
p1=[]
for i in range(n1):
    coefficent,exponent=map(int,input("Enter the coefficient and expontent:").split())
    p1.append((coefficent,exponent))

n2=int(input("Enter the terms in first polynomiyal:"))
p2=[]
for i in range(n2):
    coefficent,exponent=map(int,input("Enter the coefficient and expontent:").split())
    p2.append((coefficent,exponent))
sum_polynomiyal=add_poly(p1,p2)
multiple_polynomiyal=mul_poly(p1,p2)

print(sum_polynomiyal)
print(multiple_polynomiyal)
    
