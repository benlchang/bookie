import os
from tavily import TavilyClient


# Use Tavily search to retrieve 10 similar books from the web

class SearchAgent:
    def __init__(self):
        pass

    def gather_books(self, book: str, find_recs: bool = True):

        # If we're not finding recommendations, then the user just wants a summary of this book...
        if not find_recs:
            return {'books': book, 'find_recs': find_recs}
        
        # Otherwise, let's find recommendations!
        # Use Tavily search to find similar books
        print('Searching for books...')
        client = TavilyClient(api_key=os.environ['TAVILY_API_KEY'])

        query = f"Find me at least 10 different books similar in genre and subject matter to {book}, using only enough tokens to list the book titles. Do NOT return any books you've found for me before."
        results = client.search(
                    query=query,
                    max_results=5,
                    include_answer=True
                )
        
        books = results['answer']
        
        return {'reference': book, 'book_list': books, 'find_recs': find_recs}    ##needs to output books as a list of just the book names
    
    def run(self, input: dict):
        return self.gather_books(input['book'], input['find_recs'])