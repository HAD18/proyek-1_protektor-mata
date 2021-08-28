input.onButtonPressed(Button.A, function () {
    basic.showNumber(grove.measureInCentimeters(DigitalPin.P1))
})
input.onButtonPressed(Button.AB, function () {
    basic.showNumber(pins.analogReadPin(AnalogPin.P0))
})
input.onButtonPressed(Button.B, function () {
    basic.showNumber(Hitung_Mundur)
})
let detik = 0
let Hitung_Mundur = 0
led.setBrightness(10)
music.setVolume(100)
Hitung_Mundur = 1200
loops.everyInterval(1000, function () {
    Hitung_Mundur += -1
})
basic.forever(function () {
    if (grove.measureInCentimeters(DigitalPin.P1) < 60) {
        for (let index = 0; index < 4; index++) {
            music.playTone(988, music.beat(BeatFraction.Whole))
        }
        basic.showIcon(IconNames.No)
    } else {
        basic.showIcon(IconNames.Yes)
    }
})
basic.forever(function () {
    if (Hitung_Mundur < 10) {
        detik = 10
        for (let index = 0; index < 10; index++) {
            detik += -1
            basic.showNumber(detik)
            basic.pause(1000)
        }
        Hitung_Mundur = 1200
        for (let index = 0; index < 4; index++) {
            basic.showIcon(IconNames.No)
            music.playMelody("A B C5 A B C5 - - ", 180)
            basic.pause(1000)
        }
        basic.clearScreen()
    }
})
basic.forever(function () {
    if (pins.analogReadPin(AnalogPin.P0) > 200) {
        for (let index = 0; index < 4; index++) {
            music.playMelody("C5 B A B C5 B A B ", 180)
            basic.pause(1000)
            basic.showLeds(`
                # . # . #
                . # # # .
                # # # # #
                . # # # .
                # . # . #
                `)
        }
    } else {
        basic.showIcon(IconNames.Happy)
    }
})
