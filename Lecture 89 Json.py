import json

def readJson():
    # ข้อมูล JSON ที่เราต้องการอ่าน
    x =  '{ "name":"John", "age":30, "city":"New York"}'
    # แปลงข้อมูลให้กลายเป็นรูปที่เราสามารถใช้ได้
    y = json.loads(x)
    # ทำการเรียกข้อมูล age ออกมาแสดง
    print(y["name"])

def writeJson():

# a Python object (dict):

     x = {
  "name": "John",
  "age": 30,
  "city": "New York"
    }

# convert into JSON:
     y = json.dumps(x)

# the result is a JSON string:
     print(y)

writeJson()
readJson()

