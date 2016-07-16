import simpleguitk as simplegui

# global state

max_number = 0


# helper functions
def init(start):
    """Initializes n."""
    global n
    n = start
    print("Input is", n)


def get_next(current):
    """??? Part of mystery computation."""
    global max_number
    if current > max_number:
        max_number = current

    if current % 2 == 0:
        return current / 2
    return current * 3 + 1


# timer callback
def update():
    """??? Part of mystery computation."""
    global max_number, n

    # next_number = get_next(next_number)
    # Stop iterating after max_iterations
    if n == 1:
        timer.stop()
        print("Output is", max_number)
    else:
        n = get_next(n)

# register event handlers

timer = simplegui.create_timer(1, update)

# start program

init(217)
timer.start()

