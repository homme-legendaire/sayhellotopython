from email import message


money=True
if money:
    print("택시를 타고 가라")
else:
    print("걸어가라")

money=2000
if money>=3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")

money=2000
card=True
if money >=3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")

pocket=['knife','money','cellphone']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")

pocket=['knife','money','cellphone']
if 'money' in pocket:
    pass
else:
    print("걸어가라")

pocket=['knife','cellphone']
card =True
if 'money' in pocket:
    print("택시를 타고 가라")
elif card:
    print("택시를 타고 가라")
else:
    print("걸어가라")
    
score=70
if score>=60:
    message = "success"
else:
    message = "failure"
print(score,message)