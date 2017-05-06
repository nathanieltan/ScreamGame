
**Background and Context**
Our project is a 2D platformer that involves two players. One person plays the character that must complete the levels, while the second player controls environment elements with their voice in order to kill the character. We will primarily be focusing on using the PyGame library for the platformer aspect, and microphone for the voice control aspect. 

![Imgur](http://i.imgur.com/hTFmp1Z.png)

Voice controllers: takes the sound input from the microphone and  ‘transfers’ it into quantifiable data

Controllable environment: builds on the general environment using the data from the microphone input (e.g. a loud noise will build the environment one block)

General environment:  static environment; serves as a background for the game

Character actions: controls the way the character moves based on keyboard input

Keyboard controllers: takes in input from user through keyboard

Game instance: the overall game; controls frame-rate and is responsible for updating the player and environment elements

Player: everything that the player controls

Class Structure
Player
Character (pygame sprite)
Environment
Class Level
Class Level 1
Class Level 2
Class Ground (pygame sprite)
Class Blocks (pygame sprite)
Class Falling object (pygame sprite)
Class Spikes (pygame sprite) 
Class Fan (pygame sprite) 

**Key Questions**

We would like feedback on our software architectural structure: What improvements could we make to the software structure in order to optimize the code?

Although our idea is semi-fleshed out, we would appreciate any ideas about how we can improve the player’s experience with the game: What other features can we add into the game?

Our team did research on libraries, but obviously we probably missed a few that could be useful: Are there any libraries we should check out?

One of our potential is problems is not having immediate feedback from the voice input, are there any ways we could potentially solve this?

In terms of the user interface, what would you want to see with keyboard controls in a game? 
What would you want to see with volume-based voice control?

What should we variate for levels? What’s the goal level for keyboard player? How long our game should take?

**Agenda for technical review session**

Present/Go Over Software Architecture (Drawing on Whiteboard)
General Structure
Class Structure
Get Feedback about Software Architecture
Present Current Progress (Partial Prototypes)
Feedback on Current Progress 
Ask Key Questions
Final Feedback
