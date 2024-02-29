# Snake Game

This is a simple implementation of the classic Snake game in Python using the curses library.

## Game Description

The game starts with a small snake moving in a bordered window. The snake can move in any direction (up, down, left, or right) using the arrow keys. A piece of food is randomly placed in the window. The goal of the game is to eat as much food as possible. Each time the snake eats food, it grows longer and the player's score increases. The game ends when the snake runs into the border or into itself.

## How to Run

To run the game, you need Python installed on your machine. You can run the game using the following command:

## Game Controls

- Use the arrow keys to control the direction of the snake.
- Press 'q' to quit the game.

## Game Features

- The game keeps track of the number of pieces of food the snake has eaten. This count is displayed when the game ends.
- The game prevents the snake from moving in the opposite direction instantly to avoid the snake running into itself.
- The game ensures that the new food is not placed on the snake's body.

## Dependencies

- Python
- curses library

## Future Enhancements

- Add a score display during the game.
- Increase the speed of the snake as the score increases.
- Add different levels with different obstacles.

Enjoy the game!
