import random
import curses

# Initialize the screen
s = curses.initscr()
# Set the cursor to invisible
curses.curs_set(0)
# Get the height and width of the screen
sh, sw = s.getmaxyx()
# Create a new window using screen height and width
w = curses.newwin(sh, sw, 0, 0)
# Enable the keypad for special keys
w.keypad(1)
# Set the screen refresh rate
w.timeout(100)

# Set the initial position of the snake
snk_x = sw//4
snk_y = sh//2
# Create the initial snake body parts
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]

# Create the initial food position
food = [sh//2, sw//2]
# Add the food to the screen
w.addch(int(food[0]), int(food[1]), curses.ACS_PI)

# Set the initial direction of the snake
key = curses.KEY_RIGHT

# Start the game loop
while True:
    # Get the next key pressed
    next_key = w.getch()
    # If no key is pressed, keep the current key
    key = key if next_key == -1 else next_key

    # If the snake runs over the screen or itself, or 'q' is pressed, quit
    if key in [ord('q'), curses.KEY_DOWN, curses.KEY_UP, curses.KEY_LEFT, curses.KEY_RIGHT]:
        if key == ord('q') or snake[0][0] in [0, sh] or \
            snake[0][1]  in [0, sw] or \
            snake[0] in snake[1:]:
            curses.endwin()
            quit()

        # Create a new head for the snake
        new_head = [snake[0][0], snake[0][1]]

        # Move the head in the direction of the key pressed
        if key == curses.KEY_DOWN:
            new_head[0] = min(sh-1, new_head[0] + 1)
        if key == curses.KEY_UP:
            new_head[0] = max(0, new_head[0] - 1)
        if key == curses.KEY_LEFT:
            new_head[1] = max(0, new_head[1] - 1)
        if key == curses.KEY_RIGHT:
            new_head[1] = min(sw-1, new_head[1] + 1)

        # Insert the new head into the snake
        snake.insert(0, new_head)

        # If the snake eats the food
        if snake[0] == food:
            # Remove the food
            food = None
            # Create new food
            while food is None:
                nf = [
                    random.randint(1, sh-1),
                    random.randint(1, sw-1)
                ]
                # If the new food position is not on the snake body, place it, else repeat
                food = nf if nf not in snake else None
            # Add the new food to the screen
            w.addch(food[0], food[1], curses.ACS_PI)
        else:
            # If the snake didn't eat the food, move the snake forward by removing the tail
            tail = snake.pop()
            # Remove the tail from the screen
            w.addch(int(tail[0]), int(tail[1]), ' ')

        # Add the new head to the screen
        w.addch(int(snake[0][0]), int(snake[0][1]), curses.ACS_CKBOARD)