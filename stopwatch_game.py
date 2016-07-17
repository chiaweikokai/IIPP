# "Stopwatch: The Game"
import simpleguitk as simplegui
# define global variables
current_raw_time = 0
total_try = 0
success_try = 0


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def convert_time_format(raw_time):
    last_digit = raw_time % 10
    seconds = (raw_time // 10) % 60
    minutes = (raw_time // 10) // 60
    if seconds < 10:
        time_str = "%d:0%d.%d" % (minutes, seconds, last_digit)
    else:
        time_str = "%d:%d.%d" % (minutes, seconds, last_digit)

    return time_str


# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    # タイマーはすでに開始した場合に何もしないこと
    if timer.is_running():
        return
    timer.start()


def stop_handler():
    global total_try, success_try

    # タイマーがすでに停止されている場合は何もしないこと
    if not timer.is_running():
        return

    timer.stop()
    if current_raw_time % 10 == 0:
        success_try += 1
    total_try += 1


def reset_handler():
    global current_raw_time, total_try, success_try

    if timer.is_running():
        timer.stop()
    current_raw_time = 0
    total_try = 0
    success_try = 0


# define event handler for timer with 0.1 sec interval
def timer_tick():
    global current_raw_time
    current_raw_time += 1


# define draw handler
def draw_handler(canvas):
    canvas.draw_text(convert_time_format(current_raw_time), [100, 220], 40, 'White')
    canvas.draw_text("%d/%d" % (success_try, total_try), [300, 40], 28, 'Green')


# create frame
frame = simplegui.create_frame("Stopwatch", 400, 400)
timer = simplegui.create_timer(100, timer_tick)

# register event handlers
frame.add_button("Start", start_handler, 100)
frame.add_button("Stop", stop_handler, 100)
frame.add_button("Reset", reset_handler, 100)
frame.set_draw_handler(draw_handler)


# start frame
frame.start()

