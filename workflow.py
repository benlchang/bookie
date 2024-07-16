import os
from langgraph.graph import Graph
from agents import ranking, search, summary

# Master workflow
class Master():
    def __init__(self):
        pass

    def run(self):
        # Assemble the AI agents
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
            lambda x: 'find_recs' if x['find_recs'] else 'no_recs',
            {'find_recs':'ranking', 'no_recs':'summary'}
        )

        workflow.add_edge('ranking', 'summary')

        workflow.set_entry_point('search')
        workflow.set_finish_point('summary')

        chain = workflow.compile()

        # ASCII art for the name
        print(' ____________________________________________________\n',
        '|____________________________________________________|\n',
        '| __     __   ____   ___ ||  ____    ____     _  __  |\n',
        '||  |__ |--|_| || |_|   |||_|**|*|__|+|+||___| ||  | |\n',
        '||==|^^||--| |=||=| |=*=||| |~~|~|  |=|=|| | |~||==| |\n',
        '||  |##||  | | || | |JRO|||-|  | |==|+|+||-|-|~||__| |\n',
        '||__|__||__|_|_||_|_|___|||_|__|_|__|_|_||_|_|_||__|_|\n',
        '||_______________________||__________________________|\n',
        '| _____________________  ||      __   __  _  __    _ |\n',
        '||=|=|B|O|O|K|I|E|!|=|=| __..\/ |  |_|  ||#||==|  / /|\n',
        '|| | | | | | | | | | | |/\ \  \\|++|=|  || ||==| / / |\n',
        '||_|_|_|_|_|_|_|_|_|_|_/_/\_.___\__|_|__||_||__|/_/__|\n',
        '|____________________ /\~()/()~//\ __________________|\n',
        '| __   __    _  _     \_  (_ .  _/ _    ___     _____|\n',
        '||~~|_|..|__| || |_ _   \ //\\ /  |=|__|~|~|___| | | |\n',
        '||--|+|^^|==|1||2| | |__/\ __ /\__| |==|x|x|+|+|=|=|=|\n',
        '||__|_|__|__|_||_|_| /  \ \  / /  \_|__|_|_|_|_|_|_|_|\n',
        '|_________________ _/    \/\/\/    \_ _______________|\n',
        '| _____   _   __  |/      \../      \|  __   __   ___|\n',
        '||_____|_| |_|##|_||   |   \/ __|   ||_|==|_|++|_|-|||\n',
        '||______||=|#|--| |\   \   o    /   /| |  |~|  | | |||\n',
        '||______||_|_|__|_|_\   \  o   /   /_|_|__|_|__|_|_|||\n',
        '|_________ __________\___\____/___/___________ ______|\n',
        '|__    _  /    ________     ______           /| _ _ _|\n',
        '|\ \  |=|/   //    /| //   /  /  / |        / ||%|%|%|\n',
        '| \/\ |*/  .//____//.//   /__/__/ (_)      /  ||=|=|=|\n',
        '__|  \/\|/   /(____|/ //                    /  /||~|~|\n',
        '|___\_/   /________//   ________         /  / ||_|_|_|\n',
        '|___ /   (|________/   |\_______\       /  /| |______|\n',
        '    /                  \|________)     /  / | |')

      
        print("\nô¿ô : Hey, welcome back to Bookie! Can I help you with anything?\n")
        
        # Maintain context and remember rejected books
        context = set()

        # Run the application
        thread = {'configurable': {'thread_id': '1'}}
        while True:
            # Accept user input from command line
            find_recs = input('1) Analyze a book\n2) Find me recommendations based on this book\n3) Quit\n\n')
            if find_recs not in '12':
                break
            book = input('\n\nô¿ô : Alright! Which book should I use for you?\n\n')

            # Run the workflow with current user input, context, and thread
            print('\nô¿ô : Just a moment!')
            response = chain.invoke({'book': book, 'find_recs': find_recs == '2', 'rejected': context}, thread)
            for rejected in response['rejected']:
                context.add(rejected[3:])

            # Restart the chain until the user picks out a book
            while not response['exit'] and response['find_recs']:
                response = chain.invoke({'book': book, 'find_recs': find_recs == '2', 'rejected': context}, thread)
                
                print(response['find_recs'])
                for rejected in response['rejected']:
                    context.add(rejected[3:])


            
            print("ô¿ô : Got any more books for me?\n")
        

if __name__ == '__main__':
    init = Master()
    init.run()