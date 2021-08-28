def on_button_pressed_a():
    basic.show_number(grove.measure_in_centimeters(DigitalPin.P1))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.show_number(pins.analog_read_pin(AnalogPin.P0))
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_number(Hitung_Mundur)
input.on_button_pressed(Button.B, on_button_pressed_b)

detik = 0
Hitung_Mundur = 0
led.set_brightness(10)
music.set_volume(100)
Hitung_Mundur = 1200

def on_every_interval():
    global Hitung_Mundur
    Hitung_Mundur += -1
loops.every_interval(1000, on_every_interval)

def on_forever():
    if grove.measure_in_centimeters(DigitalPin.P1) < 60:
        for index in range(4):
            music.play_tone(988, music.beat(BeatFraction.WHOLE))
        basic.show_icon(IconNames.NO)
    else:
        basic.show_icon(IconNames.YES)
basic.forever(on_forever)

def on_forever2():
    global detik, Hitung_Mundur
    if Hitung_Mundur < 10:
        detik = 10
        for index2 in range(10):
            detik += -1
            basic.show_number(detik)
            basic.pause(1000)
        Hitung_Mundur = 1200
        for index3 in range(4):
            basic.show_icon(IconNames.NO)
            music.play_melody("A B C5 A B C5 - - ", 180)
            basic.pause(1000)
        basic.clear_screen()
basic.forever(on_forever2)

def on_forever3():
    if pins.analog_read_pin(AnalogPin.P0) > 200:
        for index4 in range(4):
            music.play_melody("C5 B A B C5 B A B ", 180)
            basic.pause(1000)
            basic.show_leds("""
                # . # . #
                                . # # # .
                                # # # # #
                                . # # # .
                                # . # . #
            """)
    else:
        basic.show_icon(IconNames.HAPPY)
basic.forever(on_forever3)
