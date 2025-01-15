#### 7 of the short stories are generated using random text generator - https://www.editpad.org/tool/story-generator
#### 3 of the stories(8, 9, 10) are actually whole books from Project Gutenberg - https://www.gutenberg.org

#### I'm running the search engine and the tests using my base Python 3.11.6 with no env.

#### cd into the project dir before running any commands.

#### To run the program - `python simplesearch.py ./samples`

#### To run the tests - `python -m unittest tests.py`

#### Few examples:

```
apple@Apples-MacBook-Air simple_search % python simplesearch.py ./samples


search> to be or not to be
File name: story-8-Hamlet-Prince-of-Denmark.txt
    -- Percent found in the file: 100.0%
    -- Words found: ['to', 'or', 'not', 'be']
File name: story-10-Twenty-years-after.txt
    -- Percent found in the file: 100.0%
    -- Words found: ['to', 'or', 'not', 'be']
File name: story-9-Alices-Adventures-in-Wonderland.txt
    -- Percent found in the file: 100.0%
    -- Words found: ['to', 'or', 'not', 'be']
File name: story-6-Oh-my-dear-Lizzy.txt
    -- Percent found in the file: 75.0%
    -- Words found: ['to', 'or', 'be']
File name: story-3-Greedy-Dog.txt
    -- Percent found in the file: 75.0%
    -- Words found: ['to', 'not', 'be']
File name: story-2-Thirsty-Crow.txt
    -- Percent found in the file: 50.0%
    -- Words found: ['to', 'not']
File name: story-1-Jack.txt
    -- Percent found in the file: 50.0%
    -- Words found: ['to', 'not']
File name: story-7-big-white-armoured-bear.txt
    -- Percent found in the file: 50.0%
    -- Words found: ['to', 'not']
File name: story-4-Mort-and-Keli.txt
    -- Percent found in the file: 25.0%
    -- Words found: ['to']
File name: story-5-A-Little-Rhosgobel-Rabbits.txt
    -- Percent found in the file: 25.0%
    -- Words found: ['to']


search> try with quite longer text
File name: story-8-Hamlet-Prince-of-Denmark.txt
    -- Percent found in the file: 80.0%
    -- Words found: ['with', 'try', 'quite', 'longer']
File name: story-10-Twenty-years-after.txt
    -- Percent found in the file: 80.0%
    -- Words found: ['with', 'try', 'quite', 'longer']
File name: story-9-Alices-Adventures-in-Wonderland.txt
    -- Percent found in the file: 80.0%
    -- Words found: ['with', 'try', 'quite', 'longer']
File name: story-4-Mort-and-Keli.txt
    -- Percent found in the file: 40.0%
    -- Words found: ['with', 'longer']
File name: story-2-Thirsty-Crow.txt
    -- Percent found in the file: 20.0%
    -- Words found: ['with']
File name: story-3-Greedy-Dog.txt
    -- Percent found in the file: 20.0%
    -- Words found: ['with']
File name: story-1-Jack.txt
    -- Percent found in the file: 20.0%
    -- Words found: ['with']
File name: story-7-big-white-armoured-bear.txt
    -- Percent found in the file: 20.0%
    -- Words found: ['with']
File name: story-6-Oh-my-dear-Lizzy.txt
    -- Percent found in the file: 20.0%
    -- Words found: ['with']
File name: story-5-A-Little-Rhosgobel-Rabbits.txt
    -- Percent found in the file: 20.0%
    -- Words found: ['with']


search> Teleportation
File name: story-3-Greedy-Dog.txt
    -- Percent found in the file: 100.0%
    -- Words found: ['teleportation']
File name: story-2-Thirsty-Crow.txt
    -- Percent found in the file: 0%
    -- Words found: []
File name: story-1-Jack.txt
    -- Percent found in the file: 0%
    -- Words found: []
File name: story-8-Hamlet-Prince-of-Denmark.txt
    -- Percent found in the file: 0%
    -- Words found: []
File name: story-7-big-white-armoured-bear.txt
    -- Percent found in the file: 0%
    -- Words found: []
File name: story-10-Twenty-years-after.txt
    -- Percent found in the file: 0%
    -- Words found: []
File name: story-4-Mort-and-Keli.txt
    -- Percent found in the file: 0%
    -- Words found: []
File name: story-6-Oh-my-dear-Lizzy.txt
    -- Percent found in the file: 0%
    -- Words found: []
File name: story-5-A-Little-Rhosgobel-Rabbits.txt
    -- Percent found in the file: 0%
    -- Words found: []
File name: story-9-Alices-Adventures-in-Wonderland.txt
    -- Percent found in the file: 0%
    -- Words found: []


search>      
No valid search terms.
search>
```
