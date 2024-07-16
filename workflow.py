import os
from langgraph.graph import Graph
from agents import ranking, search, summary

# Master workflow

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

        # Skip the ranking if the user only wants to hear about one book
        workflow.add_conditional_edges(
            'search',
            lambda x: 'has_recs' if x['find_recs'] else 'no_recs',
            {'has_recs':'ranking', 'no_recs':'summary'}
        )

        # workflow.add_conditional_edges(
        #     'summary',
        #     lambda x: 'needs_recs' if x['exit'] == [] else 'done',
        #     {'needs_recs': 'search'}
        # )

        #conditional edge from summary to search?

        workflow.add_edge('ranking', 'summary')

        workflow.set_entry_point('search')
        workflow.set_finish_point('summary')

        chain = workflow.compile()

        # ASCII art for the name
        print("__________               __   .__         ._.\n\______   \ ____   ____ |  | _|__| ____   | |\n |    |  _//  _ \ /  _ \|  |/ /  |/ __ \  | |\n |    |   (  <_> |  <_> )    <|  \  ___/   \|\n |______  /\____/ \____/|__|_ \__|\___  >  __\n \/                   \/       \/   \/")
        print("\nHey, welcome back to Bookie! Can I help you with anything?\n")

        thread = {'configurable': {'thread_id': '1'}}
        
        # Maintain context and remember rejected books
        context = set()

        # Run the application
        while True:
            # Accept user input from command line
            find_recs = input('1) Analyze a book\n2) Find me recommendations based on this book\n3) Quit\n\n')
            if find_recs not in '12':
                break
            book = input('\n\nAlright! Which book should I use for you?\n\n')

            # Run the workflow with current user input, context, and thread
            print('\nJust a moment!\n')
            response = chain.invoke({'book': book, 'find_recs': find_recs == '2', 'rejected': context}, thread)
            for rejected in response['rejected']:
                context.add(rejected)

            # Restart the chain until the user picks out a book
            while not response['exit']:
                response = chain.invoke({'book': book, 'find_recs': find_recs == '2', 'rejected': context}, thread)
                for rejected in response['rejected']:
                    context.add(rejected)


            print("Great! Come back when you finish, I'll have some more recommendations for you :)")
            print("Got any more books for me?")
        

if __name__ == '__main__':
    init = Master()
    init.run()