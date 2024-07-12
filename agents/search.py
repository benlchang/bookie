import os
from tavily import TavilyClient

class SearchAgent:
    def __init__(self):
        pass

    def gather_books(self, book: str, find_recs: bool = True):
        if not find_recs:
            return {'books': book, 'find_recs': find_recs}
        
        
        client = TavilyClient(api_key=os.environ['TAVILY_API_KEY'])

        query = f'Find me at least 10 different books similar in genre and subject matter to {book}, using only enough tokens to list the book titles.'
        results = client.search(
                    query=query,
                    max_results=5,
                    include_answer=True
                )
        
        books = results['answer']
        print(books)
        return {'reference': book, 'book_list': books, 'find_recs': find_recs}    ##needs to output books as a list of just the book names
    
    def run(self, input: dict):
        print(input)
        return self.gather_books(input['book'], input['find_recs'])


# test_agent = SearchAgent()
# test_agent.run({'book': 'Champion by Marie Lu', 
#                 'find_recs': True})