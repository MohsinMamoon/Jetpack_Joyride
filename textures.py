from colorama import Fore


def load_texture(file, foreground):
    texture = []
    with open(file) as f:
        for i in f.readlines():
            row = []
            for j in i[:-1]:
                if j != ' ':
                    row.append(foreground + j)
                else:
                    row.append(j)
            texture.append(row)
    return texture


jety_right = load_texture("textures/jety_right.txt", Fore.LIGHTWHITE_EX)
jety_left = load_texture("textures/jety_left.txt", Fore.LIGHTWHITE_EX)
jety_sheild = load_texture("textures/jety_sheild.txt", Fore.LIGHTWHITE_EX)
cloud = load_texture("textures/cloud.txt", Fore.LIGHTWHITE_EX)
broken_wall = load_texture("textures/broken_wall.txt", Fore.RED)
dragon = load_texture("textures/dragon.txt", Fore.BLACK)
firebeam_vert = load_texture("textures/firebeam_vert.txt", Fore.LIGHTRED_EX)
firebram_slant_right = load_texture("textures/firebeam_slant_right.txt", Fore.LIGHTRED_EX)
firebram_slant_left = load_texture("textures/firebeam_slant_left.txt", Fore.LIGHTRED_EX)
firebeam_hor = load_texture("textures/firebeam_hor.txt", Fore.LIGHTRED_EX)
magnet = load_texture("textures/magnet.txt", Fore.LIGHTGREEN_EX)
coins_hor = load_texture("textures/coins_hor.txt", Fore.LIGHTYELLOW_EX)
coins_vert = load_texture("textures/coins_vert.txt", Fore.LIGHTYELLOW_EX)
coins_slant_right = load_texture("textures/coins_slant_right.txt", Fore.LIGHTYELLOW_EX)
coins_slant_left = load_texture("textures/coins_slant_left.txt", Fore.LIGHTYELLOW_EX)
coins_square = load_texture("textures/coins_square.txt", Fore.LIGHTYELLOW_EX)
coins_trap = load_texture("textures/coins_trap.txt", Fore.LIGHTYELLOW_EX)
door = load_texture("textures/door.txt", Fore.RED)
