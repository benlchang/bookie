import os
from tavily import TavilyClient


# Use Tavily search to retrieve 10 similar books from the web

class SearchAgent:
    def __init__(self):
        pass

    def gather_books(self, context: set, book: str, find_recs: bool = True):

        # If we're not finding recommendations, then the user just wants a summary of this book...
        # Send the book to the Summary agent
        if not find_recs:
            return {'books': book, 'find_recs': find_recs}
        
        # Otherwise, let's find recommendations!
        # Use Tavily search to find similar books
        print('Searching for books...')
        client = TavilyClient(api_key=os.environ['TAVILY_API_KEY'])

        print(context)

        query = f"Find me at least 10 different books similar in genre and subject matter to {book}, using only enough tokens to list the book titles. Do NOT return any of the following books: {context}."
        results = client.search(
                    query=query,
                    max_results=10,
                    include_answer=True
                )
        
        books = results['answer']
        
        # Send a list of books to the Ranking agent
        return {'reference': book, 'book_list': books, 'find_recs': find_recs}
    
    def run(self, input: dict):
        return self.gather_books(input['rejected'], input['book'], input['find_recs'])