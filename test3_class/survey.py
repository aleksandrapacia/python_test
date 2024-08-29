class AnonymousSurvey():
    """manages anonymous survey """

    def __init__(self, question):
        """saves the answers collected from survey"""
        self.question = question
        self.responses = [] # list where responses will be stored

    def show_question(self):
        """shows a question from survey"""
        print(self.question)

    def store_response(self, new_response):
        """stores single answer to the question"""
        self.responses.append(new_response)

    def show_results(self):
        """shows all answeres that have been answered"""
        print("Survey results: ")
        for response in self.responses:
            print(f" - {response}")

    
