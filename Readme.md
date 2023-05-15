The Island's Legacy: Golden Mouse

A puzzle/game website project


Table of Contents:
1. Project Overview
2. Features
3. Soft Skills Assessment
4. Puzzle Solutions
5. Setup
6. Checklist of Implemented Features
7. Additional Features
8. Contributing


Project Overview:
This is a puzzle/game website made from python and django framework.


Features:
1. Anyone with an email address can create an Id and password to participate in the game
2. The puzzle contains
    i.    5 clues
    ii.   2 dead-ends
    iii.  1 solution
3. All the progress / user data (eg - time taken by each user for every step, etc.) is stored for every user.
4. On refreshing, from either browser or website, the puzzle starts from the same step and gives the user an option to restart.
5. A dashboard for the admin where the progress of all the users is tracked & analyzed.


Soft Skills Assessment:
A treasure hunting game can assess various soft skills depending on its design and mechanics. Here are some common soft skills that can be assessed:

1. Problem-solving: The ability to analyze clues, decipher puzzles, and find solutions to progress through the game.
2. Critical thinking: Evaluating information, making logical connections, and making informed decisions during the treasure hunt.
3. Time management: Balancing time constraints, prioritizing tasks, and optimizing efficiency to complete the treasure hunt within a given timeframe.
4. Attention to detail: Observing and analyzing the environment, clues, and objects carefully to discover hidden information or paths.
5. Creativity: Encouraging players to think outside the box, come up with innovative solutions, and use their imagination to tackle challenges.
6. Adaptability: Being flexible and open-minded when faced with unexpected situations or changes in the game's dynamics.


Puzzle Solutions
Clue 1: can be solved by putting the values 1, 2, 4, 2, 6, 5 in the same order in the holes.
This will lead to two options one is the riddle which is a deadend and has no correct option and other is the map.
Clue 2: can be solved by two strings 'achj' and 'afj'.
Clue 3: can be solved by using ceasar's cipher (shift of 3), the correct answer is 'PIRATE KING'.
Clue 4: can be solved only by moving queen to e4.
This will lead to two options one is upstairs, which is a deadend and other is downstairs which is the solution.


Setup
To setup a local development environment just clone this project from the git repository inside a virtual env and install django in that environment and the project will work.
