from survey import AnonymousSurvey

# define a question
question = "What is your native language?"

#create a survey
my_survey = AnonymousSurvey(question)

# show question
my_survey.show_question()
# store answer
print("Enter 'q' if you want to quit program running")
while True:
    response = input('Language: ')
    if response == 'q':
        break  
    my_survey.store_response(response)

print("\nThank you for taking part in a survey!")
my_survey.show_results()