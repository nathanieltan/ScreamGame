
## HAVE YOU EVER WANTED TO SCREAM?

Introducing ScreamGame. This interactive, voice-controlled, screaming game allows two players to compete against each other: one player controls the character in order to avoid the death traps, while the other player voice-activates the death traps.

**The story:**

_The player:_ It’s a nice day outside so you decide to take a walk for the first time in like thirty weeks (because let’s face it, you don’t get out much do you?). Unfortunately all of your suspicions are right: the outside world is trying to kill you. Get out alive so you can live, and more importantly, play more games on your laptop. Also you’re a cute lil’ hamster.

_The environment:_ Some nerd thought they could just take a walk? False. Try to kill them for lols. Even though they are a cute hamster. But since you aren’t a physical body, you got to scream.


**The gameplay**

_The player:_ Use the arrow keys in order to make the hamster jump, move forward, and move backwards until you reach the goal. Make sure to avoid items that will cause certain death.

_The environment:_ Scream at the laptop to activate the death traps.


## MEET THE TEAM

All four project students are part of the ENGR2510 Software Design, Fall 2017 class. As part of a final project project, we elected to create a voice-controlled 'scream' game, while also pursuing personal project goals.

**Camille Xue**

Camille is a first year engineering student at Franklin W. Olin College of Engineering, studying Engineering with Computing. Her project goals for this project included working with new libraries and integrating voice input with the game environment. For this project, Camille worked on the voice integration and the environment set-up.
[link to Github](https://github.com/camillexue)

**Minju Kang**

Minju is a first year engineering student at Franklin W. Olin College of Engineering, studying Electrical Engineering. Her project goals for this project were to learn how to use pygame and to be able to work in a group on a semi-large scale project. Minju's contributions for this projects were the general game structure design, environment set-up, and player set-up.
[link to Github](https://github.com/mindew)

**Nathaniel Tan**

Nathaniel is a first year engineering student at Franklin W. Olin College of Engineering, also studying Electrical Engineering. Project goals for this project included: learning how to integrate physics concepts into game design and learning more about game design. Nathaniel worked on the physics and collision detection engine and the level editor.
[link to Github](https://github.com/nathanieltan)

**Prava Dhulipalla**

Prava, like all of her project partners, is a first year engineering student at Franklin W. Olin College of Engineering, studying Electrical and Computer Engineering. Her project goals were to learn more about machine learning and voice integration with a project. As a result, she worked on the neural network and the voice integration aspects of the code.
[link to Github](https://github.com/prava-d)

## MOTIVATION

Our personal motivations, combined with the group motivation of creating a final product of which we were proud and about which we were excited.

Ultimately, all of us ended up not only engaging with our personal goals, but learning a lot about fields we wanted to explore. Thus, the culmination of this project was not only a success because it was a final product that worked and satisfied the requirements of our lovely Software Design professors, but because we ended up fulfilling our personal motivations.

This visual shows that the game included many components to help us engage with our personal goals.

## PLAYING THE GAME

![](https://github.com/prava-d/SCREAMgame/blob/master/Screenshot%20from%202017-04-27%2019-39-12.png?raw=true)

Please reference the [README.md](https://github.com/nathanieltan/ScreamGame/blob/newBranch/README.md) on our original repository in order to play our SCREAM game! Have fun!


![](https://github.com/prava-d/SCREAMgame/blob/master/implementation%20image.png?raw=true)



## IMPLEMENTATION

**Main Game**

Run this! Combines the player and the level for an A+ playing experience. It’s the head honcho of this group.

**Player**

Handles the keyboard input and the player movement. Also has collision detection and determines death.

**Level Editor**

It’s not fun if there is the same round every time. This allows a different level to be accessed every time.
![](https://github.com/prava-d/SCREAMgame/blob/master/Screenshot%20from%202017-04-30%2021-03-52.png?raw=true)


**Environment**

Just your basic pygame environmental set-up. Has all the fun stuff you’ll see in main.

**Voice Input**

Makes the scream scream do the work work. It processes the voice input and determines if the threshold is high enough (for the death traps).

**Neural Network**

12 fantastic nodes that theoretically train data (of vowel sound input) that was never utilized.

## IMPLEMENTATION

_Level Editor_
All individual levels are implemented in seperate files, all in one folder. The code specifies which level, which then finds the correct file in the level folder.

_Physics and Collision Detection Engine_
The physics work off of real life kinematic equations, with the except of the use of trial and error to determine friction and gravity coefficients. The collision detection was fairly basic, as it was two-dimensional and the detection focused on rectangular boxes.

_Environment Set-up_
The environment set-up included generating the sky, the ground, the boxes, and the death-traps.

_Player Set-up_
The player set-up included generating the character, and integrating keyboard commands with character movement.

_Voice Integration_
The game records the character for a small amount of time, and then processes that information to determine whether it was loud enough to make the death traps fall.

_Neural Network_
This trains on the 'a', 'e', and 'o' vowel sounds to differentiate using machine learning methods, specifically a neural network algorithm.

![](https://github.com/prava-d/SCREAMgame/blob/master/implementation%20image.png?raw=true)

## PROJECT HISTORY

As for actual code building, we built our code starting simple and making it more complex.


1 - Got voice input from the laptop and was able to quantify it. A basic level with the environment and a moving player (through keyboard, only could move back and forth) was created.


2 - The voice input was turned into one amplitude. Collision detection and physics was included in the environment and the game environment. Character can jump and interact with the environment.


3 - A threshold was set and a calibration period was introduced. Death traps were added.


4 - Death traps fall based on voice input. The player can die when coming in contact with interactive traps or land traps.


In terms of idea, our idea changed quite a bit.


1 - A three-dimensional game with volume and pitch controlling elevation of the landscape. Volume and pitch also control the path that the player has. The game would be played on separate laptops.


2 - A three-dimensional game, played on one laptop, with volume and pitch controlling elevation of the landscape but the arrow keys controlling the path of the player.


3 - A two-dimensional game, played on one laptop, with volume controlling elevation of the landscape and the arrow keys moving the player.


4 - A two-dimensional game, played on one laptop, with volume controlling death traps that kill a character. The player is controlled by the keyboard.


5 - A two-dimensional game, played on one laptop, with vowel sounds controlling the type of death trap that kills a character. The player is controlled by the keyboard.

![](https://github.com/prava-d/SCREAMgame/blob/master/timeline%20image.png?raw=true)

## RESULTS

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/jZsqoxcna8M/0.jpg)](https://www.youtube.com/watch?v=jZsqoxcna8M)
This is the screencapture of the gameplay

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/OdKVO05B4rI/0.jpg)](https://www.youtube.com/watch?v=OdKVO05B4rI)
This is the video of the gameplay

## ATTRIBUTIONS

_Voice control:_

<http://sharewebegin.blogspot.com/2013/07/record-from-mic-python.html>

<https://people.csail.mit.edu/hubert/pyaudio/docs/>

Initially, these links were used merely used as reference points in order to get audio from the microphone. However, debugging and troubleshooting issues made the code essentially very similar to snippets of code located within these two links.

_Neural network:_

http://www.wildml.com/2015/09/implementing-a-neural-network-from-scratch/

http://neuralnetworksanddeeplearning.com/chap1.html

These links were used as references and information sources in order to create an algorithm for a neural network. No code was directly copied from snippets of code located within these links.

## FUTURE STEPS

Although satisfied with the implementation of our vision, we realize there are multiple ways we could carry this project even further.

**Neural Network**

The neural network is trained on the vowel sounds of ‘a,’ ‘e,’ and ‘o,’ However, more options could be included if it were trained on all the vowel sounds. This would probably require more work on the neural network so that it will be more accurate (or possibly the existing one would be fine). More recognizable vowel sounds means more options in the game.

**Voice-control**

One idea that was discussed was having both elements of the play experience (controlling the player and controlling the environment) be voice-controlled. To do this, the game would have to be hosted on two different laptops (the reason that having the game able to be played across two different laptops wasn’t a significant next step is because we felt that being able to scream and use keyboard commands on one laptop by two people added to the gaming experience).

**Environment Build**

Although the environment is voice-controlled, another option we were considering (and this could go with implementing more vowel sounds) is being able to ‘build’ the environment. As in, when pitch or volume is raised, the environment builds up, and when pitch and volume is lowered, the environment goes deeper.

**Hosted online**

Using something like Flask, it would be interesting and more convenient if there was a way to host the game on the web instead of making players download a git repository and play it through the terminal window.
