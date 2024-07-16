import os
from langchain_openai import ChatOpenAI

# Rank recommendations based on similarity to reference book

model = ChatOpenAI(model='gpt-3.5-turbo', max_retries=1, api_key=os.environ['OPENAI_API_KEY'])

class RankingAgent():
    def __init__(self):
        pass

    # Order the books from the Search agent according to similarity to the reference
    def rank(self, reference: str, books: str):
        print('Generating your list...')
        prompt = f"Your task is to take a list of books and rank them in order of how similar they are to a given book. Here is a list of books that you will analyze and rank: {books}. Do NOT include any other books in your list. Here is the book you will be comparing them to: {reference}. Do NOT include {reference} in your rankings. You will compare each book in the former list to this latter book on subject matter, genre, tone, book length, and reading level, and then generate a string that lists the books in order of most to least similar. Use only the tokens you need to list the book title, author, and series, if it is a part of one."
        response = model.invoke(prompt).content

        book_list = response.split('\n')
        print(book_list)

        # Send a list of books to the Summary agent
        return {'books': book_list, 'find_recs': True}

    def run(self, input):
        return self.rank(input['reference'], input['book_list'])
