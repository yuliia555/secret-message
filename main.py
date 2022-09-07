def on_button_pressed_a():
    music.play_melody("G B A G C5 B A B ", 120)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_string(receivedString):
    basic.show_string(receivedString)
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    radio.send_string("Hey")
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_icon(IconNames.HEART)
# how're you
radio.set_group(444)

def on_forever():
    pass
basic.forever(on_forever)
