import os
from PIL import Image

def stretch_image(image_path, stretch_type, aspect_ratio):
    # Open the image
    image = Image.open(image_path)

    # Get the original width and height
    original_width, original_height = image.size

    # Convert the aspect ratio from a string to a decimal
    width_ratio, height_ratio = map(int, aspect_ratio.split(':'))
    aspect_ratio_decimal = width_ratio / height_ratio

    # Calculate the new width and height based on the aspect ratio
    if aspect_ratio == '1:1':
        new_size = max(original_width, original_height)
        stretched_image = image.resize((new_size, new_size))
    elif stretch_type == 'horizontal' or stretch_type == '1':
        new_width = int(original_width * aspect_ratio_decimal)
        new_height = original_height
        stretched_image = image.resize((new_width, new_height))
    elif stretch_type == 'vertical' or stretch_type == '2':
        new_width = original_width
        new_height = int(original_height * aspect_ratio_decimal)
        stretched_image = image.resize((new_width, new_height))
    else:
        raise ValueError("Invalid stretch type. Please choose 'horizontal' or 'vertical'.")

    # Get the file extension
    _, file_extension = os.path.splitext(image_path)

    # Save the stretched image with the same file extension
    stretched_image.save('stretched_image' + file_extension)

if __name__ == '__main__':
    image_path = input('Enter the image path: ')
    stretch_type = input('Enter the stretch type (horizontal(1) or vertical(2)): ')
    aspect_ratio = input('Enter the aspect ratio (for example, 4:3 or 16:9 or 1:1): ')

    stretch_image(image_path, stretch_type, aspect_ratio)