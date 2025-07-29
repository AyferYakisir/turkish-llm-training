gokyuzunde_pos = [-0.5065,  0.0998, -0.6540,  0.7317]
bulutlar_pos = [ 0.7295, -0.3170,  1.5783,  1.3409]

dot_product = (
    gokyuzunde_pos[0] * bulutlar_pos[0] +
    gokyuzunde_pos[1] * bulutlar_pos[1] +
    gokyuzunde_pos[2] * bulutlar_pos[2] +
    gokyuzunde_pos[3] * bulutlar_pos[3]
)
print(dot_product)