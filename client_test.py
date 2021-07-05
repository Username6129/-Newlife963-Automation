import requests

BASE = "http://127.0.0.1:5000/"

data = [{"uid": "Ali"},
        {"uid": "Abu"},
        {"uid": "AAA"}]

response = requests.post(BASE + "status/2", data={"uid": "ABC"})
print(response.json())
input()

response = requests.get(BASE + "status/2")
print(response.json())

# for i in range(len(data)):
# response = requests.put(BASE + "status/" + "a" + str(i), data[i])
# print(response.json())
# input()
# response = requests.delete(BASE + "status/a0")
# print(response)
# input()
# response = requests.get(BASE + "status/a0")
# print(response.json())
