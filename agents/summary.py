import os
from langchain_openai import ChatOpenAI

# Use ChatGPT to summarize a given book

class SummaryAgent():
    def __init__(self):
        pass
    
    # Loop through the ranked list with the user OR provide the summary for the user's selection
    def run(self, params):
  
        index=0
        model = ChatOpenAI(model='gpt-3.5-turbo', api_key=os.environ['OPENAI_API_KEY'])

        bookpile = []

        # Continuously load in new books from the ranking until the list is exhausted
        while index < len(params['books']):
            print("Generating summary...") 
            book = params['books'][index]
            
            prompt=f"Provide an in-depth summary of {book}, including a few sentences about the story, one sentence about the author and their other work, and two sentences about the reception of the book by the public. This should be a short, five sentence paragraph."
      
            summary = model.invoke(prompt).content

            print(f"\nSummary generated! What do you think of {book[3:]}?\n")
            print(summary)

            user = input("\n1) I'll read it!\n2) Load another suggestion\n\n")

            if user != '2':
                print(bookpile)
                return {'exit': [book], 'rejected': bookpile}
            
            bookpile.append(book)
            index += 1

        return {'exit': [], 'rejected': params['books']}