{
  "version": 1,
  "author": "Anonymous maker",
  "editor": "wokwi",
  "parts": [
    { "type": "board-esp32-devkit-c-v4", "id": "esp", "top": 57.6, "left": -119.96, "attrs": {} },
    {
      "type": "wokwi-dht22",
      "id": "dht1",
      "top": -86.1,
      "left": -24.6,
      "attrs": { "temperature": "46" }
    },
    { "type": "wokwi-led", "id": "led1", "top": -3.6, "left": 157.4, "attrs": { "color": "red" } },
    {
      "type": "wokwi-resistor",
      "id": "r1",
      "top": 80.75,
      "left": 96,
      "attrs": { "value": "220" }
    }
  ],
  "connections": [
    [ "esp:TX", "$serialMonitor:RX", "", [] ],
    [ "esp:RX", "$serialMonitor:TX", "", [] ],
    [ "dht1:VCC", "esp:3V3", "red", [ "v0" ] ],
    [ "dht1:GND", "esp:GND.2", "black", [ "v0" ] ],
    [ "dht1:SDA", "esp:15", "green", [ "v0" ] ],
    [ "led1:A", "r1:2", "green", [ "v0" ] ],
    [ "r1:1", "esp:4", "green", [ "v0" ] ],
    [ "led1:C", "esp:GND.3", "green", [ "v0" ] ]
  ],
  "dependencies": {}
}