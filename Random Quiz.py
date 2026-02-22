import random
capitals={
    "Andhra Pradesh": "Amaravati",
    "Arunachal Pradesh": "Itanagar",
    "Assam": "Dispur",
    "Bihar": "Patna",
    "Chhattisgarh": "Raipur",
    "Goa": "Panaji",
    "Gujarat": "Gandhinagar",
    "Haryana": "Chandigarh",
    "Himachal Pradesh": "Shimla",
    "Jharkhand": "Ranchi",
    "Karnataka": "Bengaluru",
    "Kerala": "Thiruvananthapuram",
    "Madhya Pradesh": "Bhopal",
    "Maharashtra": "Mumbai",
    "Manipur": "Imphal",
    "Meghalaya": "Shillong",
    "Mizoram": "Aizawl",
    "Nagaland": "Kohima",
    "Odisha": "Bhubaneswar",
    "Punjab": "Chandigarh",
    "Rajasthan": "Jaipur",
    "Sikkim": "Gangtok",
    "Tamil Nadu": "Chennai",
    "Telangana": "Hyderabad",
    "Tripura": "Agartala",
    "Uttar Pradesh": "Lucknow",
    "Uttarakhand": "Dehradun",
    "West Bengal": "Kolkata"
}

#Create 35 different files
for i in range(35):
   quiz_file=open(f'capitalsquiz{i+1}.txt',"w",encoding='UTF-8')
   ans_file=open(f'capitalsquiz_ans{i+1}','w',encoding='UTF-8')
   quiz_file.write('Name:\n\n,date:\n\n,Period:\n\n')
   quiz_file.write((' '*20)+f'Quizzzz(Form{i+1})')
   quiz_file.write('\n\n')
   
   states=list(capitals.keys())
   random.shuffle(states)
                   
#Create 50 random questions
   for j in range(28):
       correct_ans=capitals[states[j]]
       wrong_ans=list(capitals.values())
       del wrong_ans[wrong_ans.index(correct_ans)]
       wrong_ans=random.sample(wrong_ans,3)
       answers=wrong_ans+[correct_ans]
       random.shuffle(answers)
    
#Creating each question with choices
       quiz_file.write(f'{j+1}.Capital of {states[j]}:\n')
       for k in range(4):
           quiz_file.write(f"   {'ABCD'[k]}.{answers[k]}\n")
       quiz_file.write('\n')
       ans_file.write(f"{j+1}.{'ABCD'[answers.index(correct_ans)]}")
ans_file.close()
quiz_file.close()
    
     


