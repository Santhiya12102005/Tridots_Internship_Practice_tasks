import json

details={
    "Name":"Santhiya B",
    "Skills_List":['Proramming(Python,Java)','Web development(HTML,CSS,JS)','Framework(Springboot,Flask)'],
    "Level":'Intermediate'
}
with open('profile.json',"w") as file:
    json.dump(details,file,indent=4)

with open('profile.json',"r") as file:
    data=json.load(file)

print(json.dumps(data,indent=4))