from PIL import Image

# Input dimensions in mm
board_game_width_mm = 914.4  # 65 cm
board_game_height_mm = 609.6 # 96.5 cm

# Convert dimensions to pixels using the TV's pixel density
# For the given TV size and resolution, the pixel density is about 3.2 px/mm
board_game_width_px = int(board_game_width_mm * 3.2)
board_game_height_px = int(board_game_height_mm * 3.2)

# Load the board game image
board_game = Image.open('../Dune/Regular-Dune-Mat-2-x-3.jpg')

# If the image is in webp format, convert it to png
if board_game.format == 'WEBP':
    board_game = board_game.convert('RGB')
    board_game.save('board_game_map.png')
    board_game = Image.open('board_game_map.png')

board_game = board_game.rotate(90, resample=Image.BICUBIC, expand=True)

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
tv_image.save('../Dune/Dune_Board.png')

