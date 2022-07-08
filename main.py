basic.show_icon(IconNames.NO)
ESP8266_IoT.init_wifi(SerialPin.P8, SerialPin.P12, BaudRate.BAUD_RATE115200)
ESP8266_IoT.connect_wifi("TP-Link_BBC6", "47170100")
if ESP8266_IoT.wifi_state(True):
    basic.show_icon(IconNames.YES)
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    OLED.init(128, 64)

def on_forever():
    OLED.clear()
    OLED.write_string("Temperature C")
    OLED.write_num(Environment.octopus_BME280(Environment.BME280_state.BME280_TEMPERATURE_C))
    OLED.new_line()
    OLED.write_string("humidity")
    OLED.write_num(Environment.octopus_BME280(Environment.BME280_state.BME280_HUMIDITY))
    OLED.new_line()
    OLED.write_string("Dust")
    OLED.write_num(Environment.read_dust(DigitalPin.P13, AnalogPin.P1))
    OLED.new_line()
    OLED.write_string("light")
    OLED.write_num(Environment.read_light_intensity(AnalogPin.P3))
    OLED.new_line()
    OLED.write_string("noise")
    OLED.write_num(Environment.read_noise(AnalogPin.P2))
    ESP8266_IoT.connect_thing_speak()
    ESP8266_IoT.set_data("CEJ7SV7KXSHM3W03",
        Environment.octopus_BME280(Environment.BME280_state.BME280_TEMPERATURE_C),
        Environment.octopus_BME280(Environment.BME280_state.BME280_HUMIDITY),
        Environment.read_dust(DigitalPin.P13, AnalogPin.P1),
        Environment.read_light_intensity(AnalogPin.P3),
        Environment.read_noise(AnalogPin.P2))
    ESP8266_IoT.upload_data()
    basic.pause(10000)
basic.forever(on_forever)
