import random


states = [
{
    "name": "Alabama",
    "capital": "Montgomery"
}, {
    "name": "Alaska",
    "capital": "Juneau"
}, {
    "name": "Arizona",
    "capital": "Phoenix"
}, {
    "name": "Arkansas",
    "capital": "Little Rock"
}]#, {
#     "name": "California",
#     "capital": "Sacramento"
# }, {
#     "name": "Colorado",
#     "capital": "Denver"
# }, {
#     "name": "Connecticut",
#     "capital": "Hartford"
# }, {
#     "name": "Delaware",
#     "capital": "Dover"
# }, {
#     "name": "Florida",
#     "capital": "Tallahassee"
# }, {
#     "name": "Georgia",
#     "capital": "Atlanta"
# }, {
#     "name": "Hawaii",
#     "capital": "Honolulu"
# }, {
#     "name": "Idaho",
#     "capital": "Boise"
# }, {
#     "name": "Illinois",
#     "capital": "Springfield"
# }, {
#     "name": "Indiana",
#     "capital": "Indianapolis"
# }, {
#     "name": "Iowa",
#     "capital": "Des Moines"
# }, {
#     "name": "Kansas",
#     "capital": "Topeka"
# }, {
#     "name": "Kentucky",
#     "capital": "Frankfort"
# }, {
#     "name": "Louisiana",
#     "capital": "Baton Rouge"
# }, {
#     "name": "Maine",
#     "capital": "Augusta"
# }, {
#     "name": "Maryland",
#     "capital": "Annapolis"
# }, {
#     "name": "Massachusetts",
#     "capital": "Boston"
# }, {
#     "name": "Michigan",
#     "capital": "Lansing"
# }, {
#     "name": "Minnesota",
#     "capital": "St. Paul"
# }, {
#     "name": "Mississippi",
#     "capital": "Jackson"
# }, {
#     "name": "Missouri",
#     "capital": "Jefferson City"
# }, {
#     "name": "Montana",
#     "capital": "Helena"
# }, {
#     "name": "Nebraska",
#     "capital": "Lincoln"
# }, {
#     "name": "Nevada",
#     "capital": "Carson City"
# }, {
#     "name": "New Hampshire",
#     "capital": "Concord"
# }, {
#     "name": "New Jersey",
#     "capital": "Trenton"
# }, {
#     "name": "New Mexico",
#     "capital": "Santa Fe"
# }, {
#     "name": "New York",
#     "capital": "Albany"
# }, {
#     "name": "North Carolina",
#     "capital": "Raleigh"
# }, {
#     "name": "North Dakota",
#     "capital": "Bismarck"
# }, {
#     "name": "Ohio",
#     "capital": "Columbus"
# }, {
#     "name": "Oklahoma",
#     "capital": "Oklahoma City"
# }, {
#     "name": "Oregon",
#     "capital": "Salem"
# }, {
#     "name": "Pennsylvania",
#     "capital": "Harrisburg"
# }, {
#     "name": "Rhode Island",
#     "capital": "Providence"
# }, {
#     "name": "South Carolina",
#     "capital": "Columbia"
# }, {
#     "name": "South Dakota",
#     "capital": "Pierre"
# }, {
#     "name": "Tennessee",
#     "capital": "Nashville"
# }, {
#     "name": "Texas",
#     "capital": "Austin"
# }, {
#     "name": "Utah",
#     "capital": "Salt Lake City"
# }, {
#     "name": "Vermont",
#     "capital": "Montpelier"
# }, {
#     "name": "Virginia",
#     "capital": "Richmond"
# }, {
#     "name": "Washington",
#     "capital": "Olympia"
# }, {
#     "name": "West Virginia",
#     "capital": "Charleston"
# }, {
#     "name": "Wisconsin",
#     "capital": "Madison"
# }, {
#     "name": "Wyoming",
#     "capital": "Cheyenne"
# }]



def quiz():
    
## Greeting / Game Start
    print("Hello Player!")
    play = input("Would you like to play a game about USA's capitals? (y/n) ")

    if play == "n":
        print("Ok, maybe next time.")
        return
    elif play == "y":
        print("Ok, here we go!")
        quiz()

# State Shuffle
    random.shuffle(states)
    score = {}
    score['correct'] = 0
    score['wrong'] = 0
    for i in range(4):
        capital = states[i]['capital']
        q = ('What is the capital of ' + states[i]['name'] + '?')
        print(q)
        a = input().lower()
        if (a == states[i]['capital'].lower()):
            score['correct'] += 1
            print('Correct!')
            print(f"Score: {score['correct']} correct and {score['wrong']} wrong. ")
        else:
            score['wrong'] += 1
            print('Not Quite...')
            print(f"Score: {score['correct']} correct and {score['wrong']} wrong. ")

quiz()

restart = input('Want to play again? (y/n): ')
if(restart == 'y'):
    quiz()
else:
    print('See you space cowgirl...')

################################
# A previous attempt
################################
    # incorrect_answers=[]

    # print("Hello Player!")
    # play = input("Would you like to play a quiz game about USA's capitals? (y/n)")

    # if play == "n":
    #     print("Ok, maybe next time.")
    # elif play == "y":
    #     print("Ok, here we go!")

#     while len(states)>0:
#     # for i in range(51):
#         choice=random.choice(states('name'))
#         correct_answer=states.get(choice)

#         print('Please name the capitals of the following states:')
#         print(choice)
#         answer = input("# ")
#         if answer.lower() == correct_answer.lower():
#             print('Correct!')
#             del states[choice]
#         else:
#             print('Not quite...')
#             print('The correct answer is', correct_answer)
#             incorrect_answers.append(choice)

#     print('You missed', len(incorrect_answers), 'states. ')

#     if incorrect_answers:
#         print('Time to study up for: ')
#         for each in incorrect_answers:
#             print(each)
#     else:
#         print("You're a genius!")

#     response=''
#     while response!='n':
#         game()
#         response=input('Want to play again?(y/n)#')

# game()