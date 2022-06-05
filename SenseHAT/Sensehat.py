from SenseHAT import senseHat

sense = senseHat() 
X = [255, 0, 0] #Red
O = [255, 255, 255] #White

question_mark = [
O, O, O, X, X, O, O, O,
O, O, X, O, O, X, O, O,
O, O, O, O, O, X, O, O,
O, O, O, O, X, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, X, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, X, O, O, O, O
]

sense.set_pixels(question_mark)

sense.show_message("Hello World!", text_colour=[255, 0, 0])