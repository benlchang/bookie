import os
from langchain_openai import ChatOpenAI

class SummaryAgent():
    def __init__(self):
        pass

    def run(self, input):
        book = input['books']
        if input['find_recs']:
            book = input['books'][input['index']]
        
        print(book)

        prompt=f'Provide an in-depth summary of {book}, including a few sentences about the story, one sentence about the author and their other work, and two sentences about the reception of the book by the public. This should be a short, five sentence paragraph.'
        model = ChatOpenAI(model='gpt-3.5-turbo', api_key=os.environ['OPENAI_API_KEY'])

        summary = model.invoke(prompt).content
        print(summary)
        return {'summary': summary}