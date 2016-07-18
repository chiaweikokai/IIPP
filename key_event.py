import simpleguitk as simplegui

result = 5


def key_down(key):
    global result
    if key == simplegui.KEY_MAP['X']:
        result *= 2


def key_up(key):
    global result
    if key == simplegui.KEY_MAP['X']:
        result -= 3


def draw_handler(canvas):
    canvas.draw_text(result, [50, 50], 20, 'White')

frame = simplegui.create_frame("Key event test", 200, 200)

frame.set_keydown_handler(key_down)
frame.set_keyup_handler(key_up)
frame.set_draw_handler(draw_handler)

frame.start()

