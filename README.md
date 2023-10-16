# Naval Battle

Welcome to Naval Battle, an engaging card matching game with a naval warfare theme. Test your  strategy skills as you aim to sink all the battleships!

![mockup](./readme-images/mockup.png)

## Table of Contents
- [Naval Battle](#naval-battle)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Game Features](#game-features)
    - [Player Name](#player-name)
    - [Guesses on the grid](#attempts-marked-on-the-grid)
    - [Play Again](#play-again)
  - [How to Play](#how-to-play)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Wireframe](#wireframe)
  - [Bugs](#bugs)
    - [Bug 1: Columns Number Without Spacing](#columns-number-without-spacing)
    - [Bug 2: Press Any Key](#press-any-key)
  - [Goals](#goals)
    - [Grid](#random-elements)
    - [Input](#input)
    - [Random Elements](#random-elements)
    - [If](#event-listeners)
  - [Credits](#credits)
  - [License](#license)

  

## Introduction

Welcome to the Naval Battle game! This is a simple Python-based game where you try to sink the computer's battleship by guessing its location on a 5x5 grid. This readme provides an overview of the game, its rules, and how to play.

## Game Features

**Naval Battle** offer's a couple of simple features that enhance and simplify your gaming experience:

### Player Name

- Allow players to input their names at the start of the game. The game recalls the name, creating a more engaging and personalized experience, with this feature we can enhanced player engagement and a personal touch to the gaming experience.

### Guesses on the grid

- The game utilizes a grid to mark player guesses. Correct guesses result in a "hit," while incorrect guesses are marked with an "X" on the grid. Duplicate guesses are also tracked. It provides a visual feedback to the player about their guesses, enhancing the gameplay experience and preventing redundant guesses.

### Play Again

- After a game ends, players are given the option to play again. If they choose to do so, the game can be replayed with the same name and without showing the rules again. Allows for quick and convenient game replay without the need to re-enter the player's name or view the rules repeatedly. Enhances the overall user experience.


## How to Play

1. Objective: The objective of the game is to sink the computer's battleship by correctly guessing its location on a 5x5 grid.

2. Attempts: You have a total of 6 attempts to guess the battleship's location.

3. Grid: The game is played on a 5x5 grid, and you will guess both the row and column where you think the battleship is located. The rows and columns are numbered from 1 to 5.

4. Winning Condition: If you guess the correct row and column where the battleship is positioned, you win the game.

5. Missed Guesses: If your guess is incorrect, the grid will mark the location with an 'X' to indicate a missed guess.

6. Repeated Guesses: If you guess a location that you've already guessed in a previous turn, it won't count as a valid guess, and you won't be penalized for repeating the same guess.

7. Losing Condition: If you use up all 6 attempts and don't successfully guess the battleship's location, you lose the game. The game will reveal the battleship's location at this point.

## Installation

1. Clone this repository to your local machine.
2. Open the project folder in your preferred code editor.