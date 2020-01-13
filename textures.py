def load_texture(file):
    texture = []
    with open(file) as f:
        for i in f.readlines():
            row = []
            for j in i[:-1]:
                row.append(j)
            texture.append(row)
    return texture


jety_right = load_texture("textures/jety_right.txt")
jety_left = load_texture("textures/jety_left.txt")
jety_sheild = load_texture("textures/jety_sheild.txt")
cloud = load_texture("textures/cloud.txt")
broken_wall = load_texture("textures/broken_wall.txt")
dragon = load_texture("textures/dragon.txt")
firebeam_vert = load_texture("textures/firebeam_vert.txt")
firebram_slant_right = load_texture("textures/firebeam_slant_right.txt")
firebram_slant_left = load_texture("textures/firebeam_slant_left.txt")
firebeam_hor = load_texture("textures/firebeam_hor.txt")
magnet = load_texture("textures/magnet.txt")
coins_hor = load_texture("textures/coins_hor.txt")
coins_vert = load_texture("textures/coins_vert.txt")
coins_slant_right = load_texture("textures/coins_slant_right.txt")
coins_slant_left = load_texture("textures/coins_slant_left.txt")
coins_square = load_texture("textures/coins_square.txt")
coins_trap = load_texture("textures/coins_trap.txt")