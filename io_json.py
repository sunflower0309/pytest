import io
from io import StringIO
import json
from io import BytesIO
import pickle
str1='soboy always there'
temp=pickle.dumps(str1)
f=BytesIO()
f.write(temp)

#print(f.read())
temp1=f.getvalue()
#print(type(temp1))
#print(pickle.loads(temp1))

d = dict(name='Bob', age=20, score=88)
l=(1,2,3)
temp2=json.dumps(l)
#print(temp2)
#print(json.loads(temp2))
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def student2dict(stu):
    return {'name':stu.name,
            'age':stu.age,
            'score':stu.score}

def dict2student(dic):
    return Student(dic['name'],dic['age'],dic['score'])

stu=Student('bob',22,88)
#print(json.dumps(stu,default=(lambda obj:obj.__dict__)))
js1=json.dumps(stu,default=(lambda obj:obj.__dict__))

stuback=json.loads(js1,object_hook=dict2student)
#print(stuback,type(stuback))

import re
def is_valid_email(addr):
    if re.match(r'^[\w\d]+\.?[\w\d]*@[\w\d]+\.[\w\d]+',addr):
        print('true')
    else:
        print('false')

# is_valid_email('someone@gmail.com')
# is_valid_email('bill.gates@microsoft.com')
# is_valid_email('bob#example.com')
# is_valid_email('mr-bob@example.com')

def name_of_email(addr):
    return re.match(r'.*?([\w\s\.]+)',addr).group(1)

assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
assert name_of_email('bill.gates@microsoft.com') == 'bill.gates'
print('ok')