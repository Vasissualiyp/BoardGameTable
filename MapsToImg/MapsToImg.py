from PIL import Image

# Input dimensions in mm
board_game_width_mm = 920  # 65 cm
board_game_height_mm = 920 # 96.5 cm

#input_file_name = '../TI4/twilight-imperium-playmat(85x85).jpg'
#output_file_name = '../TI4/TI_Mat1.png'
#map_scaling_factor = 0.5/0.47* 100/98

#input_file_name = '../Eclipse/Mat1(92x92).jpg'
#output_file_name = '../Eclipse/Eclipse_Mat1.png'
#map_scaling_factor = 80/83.5 * 80/80.2

input_file_name = '../Eclipse/Mat2(92x92).webp'
output_file_name = '../Eclipse/Eclipse_Mat2.png'
map_scaling_factor = 80/80.45
#map_scaling_factor = 80/83.5 * 80/80.2

rotation_angle = 270

# ---- Source code starts here -----

# Convert dimensions to pixels using the TV's pixel density
# For the given TV size and resolution, the pixel density is about 3.2 px/mm
board_game_width_px = int(board_game_width_mm * 3.2 * map_scaling_factor)
board_game_height_px = int(board_game_height_mm * 3.2 * map_scaling_factor)

# Load the board game image
board_game = Image.open(input_file_name)

# If the image is in webp format, convert it to png
if board_game.format == 'WEBP':
    board_game = board_game.convert('RGB')
    board_game.save('board_game_map.png')
    board_game = Image.open('board_game_map.png')

board_game = board_game.rotate(rotation_angle, resample=Image.BICUBIC, expand=True)

# Resize the board game map to fit the desired space on the TV
resized_board_game = board_game.resize((board_game_width_px, board_game_height_px))

# Create a new black image with the dimensions of the TV
tv_image = Image.new('RGB', (4096, 2160))

# Calculate the position to place the board game map
x = (tv_image.width - resized_board_game.width) // 2
y = (tv_image.height - resized_board_game.height) // 2

# Paste the board game image onto the TV image
tv_image.paste(resized_board_game, (x, y))

# Save the new image
tv_image.save(output_file_name)

