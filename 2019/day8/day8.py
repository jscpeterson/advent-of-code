def get_layers(width, height, data):
    layers = []
    layer_area = width*height
    data = [pixel for pixel in str(data)]
    data.remove('\n')
    while len(data) > 0:
        layers.append(data[:layer_area])
        data = data[layer_area:]
    return layers

WIDTH = 25
HEIGHT = 6

layers = get_layers(WIDTH, HEIGHT, open('input').read())
fewest_zero_layer = min(layers, key=lambda layer: layer.count('0'))
print('Part 1 solution: %i' % (fewest_zero_layer.count('1') * fewest_zero_layer.count('2')))

BLACK = '0'
WHITE = '1'
TRANS = '2'

COLORS = {
    WHITE: u'\u2588',
    BLACK: ' ',
    TRANS: None,
}

imagedata = []
for index, pixel in enumerate(layers[0]):
    depth = 0
    while pixel == TRANS:
        depth += 1
        pixel = layers[depth][index]
    imagedata.append(pixel)

def get_image(width, height, imagedata):
    output = ''
    for i, pixel in enumerate(imagedata):
        if i > 0 and i % width == 0:
            output += '\n'
        output += COLORS[pixel]
    return output

print(get_image(WIDTH, HEIGHT, imagedata))
