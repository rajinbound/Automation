import json

courses = '{"name": "RajMishra","languages": [ "JavaScript", "Python"]}'

#Loads method parse json string and it returns dictionary
dict_courses = json.loads(courses)
print(type(dict_courses))
print(dict_courses)
print(dict_courses['name'])
#get me the first language taught by trainer
# list_language = dict_courses['languages']
# print(type(list_language))
# print(list_language[])
print(dict_courses['languages'])
print(dict_courses['languages'][0])
print(dict_courses['languages'][1])

#****** Parse content present in Json file
with open('course.json') as f:
    data = json.load(f)
    print(data)
    print(type(data))
    print(data['quiz']['sport']["q1"]['question'])

#    print(data['dashboard']['website'])
#    print(type(data['dashboard']))
#price of course 'RPA'
    for team in data['quiz']['sport']["q1"]['options']:
        #print(team)
        if team == "Huston Rocket":
            print(team,"is Correct Answer")
            break
with open('course.json') as f:
    data = json.load(f)
    print(data['quiz']['maths']["q1"]['question'], "\n")
    for i in data['quiz']['maths']["q1"]['options']:
        print(i, "\n")
        if i == "12":
            print(i, "answer is correct""\n","\n","\n")
            break

#comparing file



with open('course1.json') as fi:
    data2 = json.load(fi)
    assert (data == data2)


















