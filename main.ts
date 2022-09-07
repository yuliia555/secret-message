input.onButtonPressed(Button.A, function on_button_pressed_a() {
    music.playMelody("G B A G C5 B A B ", 120)
})
radio.onReceivedString(function on_received_string(receivedString: string) {
    basic.showString(receivedString)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    radio.sendString("Hey")
})
basic.showIcon(IconNames.Heart)
//  how're you
radio.setGroup(444)
basic.forever(function on_forever() {
    
})
