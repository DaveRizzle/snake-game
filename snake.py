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
# Add a border to the window
w.box()
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
food = [random.randint(2, sh-3), random.randint(2, sw-3)]
# Add the food to the screen
w.addch(int(food[0]), int(food[1]), curses.ACS_PI)

# Set the initial direction of the snake
key = curses.KEY_RIGHT

# Initialize food counter
food_counter = 0

# Start the game loop
while True:
    # Redraw the border
    w.box()
    # Get the next key pressed
    next_key = w.getch()
    # If no key is pressed, keep the current key
    # If the next key is opposite to the current key, ignore it
    if next_key == -1 or (next_key == curses.KEY_DOWN and key == curses.KEY_UP) or \
       (next_key == curses.KEY_UP and key == curses.KEY_DOWN) or \
       (next_key == curses.KEY_LEFT and key == curses.KEY_RIGHT) or \
       (next_key == curses.KEY_RIGHT and key == curses.KEY_LEFT):
        pass
    else:
        key = next_key

    # If the snake runs over itself, or 'q' is pressed, quit
    if snake[0] in snake[1:] or key == ord('q'):
        print(f"Congratulations! You ate {food_counter} pieces of food!")
        curses.endwin()
        quit()

    # Create a new head for the snake
    new_head = [snake[0][0], snake[0][1]]

    # Move the head in the direction of the key pressed
    if key == curses.KEY_DOWN:
        new_head[0] = new_head[0] + 1 if new_head[0] < sh-3 else 2
    if key == curses.KEY_UP:
        new_head[0] = new_head[0] - 1 if new_head[0] > 2 else sh-3
    if key == curses.KEY_LEFT:
        new_head[1] = new_head[1] - 1 if new_head[1] > 2 else sw-3
    if key == curses.KEY_RIGHT:
        new_head[1] = new_head[1] + 1 if new_head[1] < sw-3 else 2

    # Insert the new head into the snake
    snake.insert(0, new_head)

    # If the snake eats the food
    if snake[0] == food:
        # Increment food counter
        food_counter += 1
        # Remove the food
        food = None
        # Create new food
        while food is None:
            nf = [
                random.randint(2, sh-3),
                random.randint(2, sw-3)
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