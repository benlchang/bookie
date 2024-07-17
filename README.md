# Bookie
Book recommendation system powered by Tavily, OpenAI, and LangGraph

## Table of Contents
* [Installation](#installation)
* [Workflow Architecture](#workflow-architecture)
* [Usage](#usage)
* [Background & Goals](#background-and-goals)
* [Credits](#credits)

## Installation
To get started, you can clone this repository and install all requirements.

```
$ git clone https://github.com/benlchang/bookie.git
$ cd bookie
$ pip install -r requirements.txt
```

Bookie will need to make calls to both the Tavily Search API and OpenAI's ChatGPT 3.5 model. You'll have to define a 'TAVILY_API_KEY' and 'OPENAI_API_KEY' from the command line like this.  
You can export these keys to your global environment variables:

```
Windows:
$ export TAVILY_API_KEY = <your Tavily API key>
$ export OPENAI_API_KEY = <your OpenAI API key>
```

Or, if you're running a Python virtual environment, add these lines to your activate.bat file under env\scripts\:

```
set TAVILY_API_KEY = <your Tavily API key>
set OPENAI_API_KEY = <your OpenAI API key>
```

After exporting your API keys, make sure you're in the root directory before starting the Usage section to ensure everything's working properly.



## Usage
Bookie runs completely on the command line. From the root directory, run the following command to start things up.

```
$ python workflow.py
```

The user interface relies on user input in the form of numbered options to interact with Bookie.
![image](https://github.com/user-attachments/assets/742df625-d051-452b-96a1-a99ca155cf68)


To get a summary of a book, type '1' and hit enter, then provide the title and author of the book and hit enter again.

The workflow will run, summarizing your book and asking about your thoughts. After responding, you'll return to the main screen.

To get recommendations based on a book, type '2' and hit enter, then provide the title and author of the 
book and hit enter again.

![image](https://github.com/user-attachments/assets/e8af572a-ebd5-4ead-a86a-26ccca7f2bcb)

The workflow will run, first searching for 10 similar books, then ranking them based on similarity to the book you entered. Bookie will then start summarizing each book in the list one by one, asking you 
each time about your thoughts. 

![image](https://github.com/user-attachments/assets/5bade702-d6da-4b76-bc3d-7d2d610382ad)

If you like one of the books, type '1' and hit enter. You'll be sent back to the title screen to a happy Bookie!

If you don't like the book, type '2' and hit enter. Bookie will pick out new books from the list of 10 from search.  
If you exhaust the first list of 10, the workflow will restart, trying not to recommend any books you've already rejected.

![image](https://github.com/user-attachments/assets/1c63305c-6fb4-4d69-8e18-1da643ad0243)  

Once you're all done, type '3' (or anything that isn't '1' or '2') and hit enter to exit. Don't forget to say bye to Bookie!






## Workflow Architecture
Bookie only employs three AI agents: a **Searcher agent** that looks for similar books to the user's input using Tavily Search, a **Ranking agent** that arranges this list in order of similarity to the user's input, and finally a **Summarizer agent** that provides the user with summaries of each result one book at a time using ChatGPT.   

If the user entered '1' and asks for a summary of one particular book, the Searcher agent will pass that book title straight to the Summarizer agent. If the user entered '2' and asks for recommendations similar to a book, the workflow will operate in its entirety: searching for similar books, ranking them, and offering summaries to the user in a loop.  

## Background and Goals
We all know a reader, don't we? I'm not much of a reader myself, but lately my girlfriend's been burning through a book a day, and her reading list
is wearing quite thin. She's pretty busy, so I figured I'd use this challenge from Tavily as an opportunity to build something avid readers like her
could use to find quick relevant book recommendations easily! 

The fundamental goal of this project was to utilize AI agents to allow users to find new books to read based on ones they liked before. However, it is always possible to develop projects like these to cover more options for the user's book search. A few next steps would include:

* Make this project into a full-stack application with a Flask/Django server and a prettier UI
* Optimizing context to improve the workflow's ability to ignore books that the user has already rejected in subsequent searches
* Implement user-specific threads and database entries for use across multiple instances of the program

Overall, I'm proud of how quickly I was able to 1) learn how to interact with AI API's, 2) construct and interact with AI agents and workflows, and 3) deliver a product that is at least somewhat useful. Hopefully I'll have some time to flesh this out a bit more this semester!  



## Credits
Title screen bookshelf image is from https://www.asciiart.eu/books/books  
Looking face lineart is from https://1lineart.kulaone.com/#/  
