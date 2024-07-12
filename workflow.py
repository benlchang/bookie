import os
from langgraph.graph import Graph
from bookie.agents import ranking, search, summary

class Master():
    def __init__(self):
        pass

    def run(self):
        searcher = search.SearchAgent()
        ranker = ranking.RankingAgent()
        summarizer = summary.SummaryAgent()

        workflow = Graph() 

        workflow.add_node('search', searcher.run)
        workflow.add_node('ranking', ranker.run)
        workflow.add_node('summary', summarizer.run)

        workflow.add_conditional_edges(
            'search',
            lambda x: 'has_recs' if x['find_recs'] else 'no_recs',
            {'has_recs':'ranking', 'no_recs':'summary'}
        )

        workflow.add_edge('ranking', 'summary')

        workflow.set_entry_point('search')

        chain = workflow.compile()

        while True:
            find_recs = input('1) Analyze a book\n2) Find me recommendations based on this book\n3) Quit\n\n')
            if find_recs == '3':
                break
            book = input('Which book shall I fetch for ya?')

            response = chain.invoke({'book': book, 'find_recs': find_recs == '2'})
            print(response)
        

if __name__ == '__main__':
    init = Master()
    init.run()