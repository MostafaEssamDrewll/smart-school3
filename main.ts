basic.showIcon(IconNames.No)
ESP8266_IoT.initWIFI(SerialPin.P8, SerialPin.P12, BaudRate.BaudRate115200)
ESP8266_IoT.connectWifi("TP-Link_BBC6", "47170100")
if (ESP8266_IoT.wifiState(true)) {
    basic.showIcon(IconNames.Yes)
    music.playTone(262, music.beat(BeatFraction.Whole))
    OLED.init(128, 64)
}
basic.forever(function () {
    OLED.clear()
    OLED.writeString("Temperature C")
    OLED.writeNum(Environment.octopus_BME280(Environment.BME280_state.BME280_temperature_C))
    OLED.newLine()
    OLED.writeString("humidity")
    OLED.writeNum(Environment.octopus_BME280(Environment.BME280_state.BME280_humidity))
    OLED.newLine()
    OLED.writeString("Dust")
    OLED.writeNum(Environment.ReadDust(DigitalPin.P13, AnalogPin.P1))
    OLED.newLine()
    OLED.writeString("light")
    OLED.writeNum(Environment.ReadLightIntensity(AnalogPin.P3))
    OLED.newLine()
    OLED.writeString("noise")
    OLED.writeNum(Environment.ReadNoise(AnalogPin.P2))
    ESP8266_IoT.connectThingSpeak()
    ESP8266_IoT.setData(
    "CEJ7SV7KXSHM3W03",
    Environment.octopus_BME280(Environment.BME280_state.BME280_temperature_C),
    Environment.octopus_BME280(Environment.BME280_state.BME280_humidity),
    Environment.ReadDust(DigitalPin.P13, AnalogPin.P1),
    Environment.ReadLightIntensity(AnalogPin.P3),
    Environment.ReadNoise(AnalogPin.P2)
    )
    ESP8266_IoT.uploadData()
    basic.pause(10000)
})
