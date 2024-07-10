import os
from tavily import TavilyClient

client = TavilyClient(api_key=os.environ['TAVILY_API_KEY'])

class SearchAgent:
    def __init__(self):
        pass

    def gather_books(self, book: str, find_recs: bool = True):
        if not find_recs:
            return book
        
        query = f'Find me at least 4 different books similar in genre and subject matter to {book}, using only enough tokens to list the book titles'
        results = client.search(
                    query=query,
                    max_results=5,
                    include_answer=True
                )
        
        books = results['answer']
        print(books)
        return books    ##needs to output books as a list of just the book names
    
    def run(self, input: dict):
        return self.gather_books(input['book'], input['find_recs'])


# test_agent = SearchAgent()
# test_agent.run({'book': 'Champion by Marie Lu', 
#                 'find_recs': True})