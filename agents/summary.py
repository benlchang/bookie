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
            print("ô¿ô : Generating summary...") 
            book = params['books'][index]
            
            # Invoke ChatGPT to generate summary
            prompt=f"Provide an in-depth summary of {book}, including a few sentences about the story, one sentence about the author and their other work, and two sentences about the reception of the book by the public. This should be a short, five sentence paragraph."
            summary = model.invoke(prompt).content

            print(f"\nô¿ô : Summary generated! What do you think of {book[3:]}?\n")
            print(summary)
            user = input("\n1) I'll read it!\n2) Eh...\n\n")

            # If the user doesn't say no to it, we're done!
            if user != '2':
                print("\nô¿ô : Great! Come back when you finish, I'll have some more recommendations for you :)")
                return {'exit': [book], 'rejected': bookpile, 'find_recs': False}
            
            # Otherwise, keep track of the rejected books and keep going
            bookpile.append(book)
            index += 1

        # If the user said no to every book offered, 
        if not params['find_recs']:
            print("\nô¿ô : Ah, no worries! I'll put this one back on the shelf...")

        return {'exit': [], 'rejected': params['books'], 'find_recs': params['find_recs']}