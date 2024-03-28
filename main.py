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
    if stretch_type == 'horizontal':
        new_width = int(original_width * aspect_ratio_decimal)
        new_height = original_height
    elif stretch_type == 'vertical':
        new_width = original_width
        new_height = int(original_height * aspect_ratio_decimal)
    else:
        raise ValueError("Invalid stretch type. Please choose 'horizontal' or 'vertical'.")

    # Resize the image
    stretched_image = image.resize((new_width, new_height))

    # Save the stretched image
    stretched_image.save('stretched_image.jpg')

# Example usage
image_path = 'iexpdtlracpa1.png'
stretch_type = 'vertical'
aspect_ratio = '4:3'

stretch_image(image_path, stretch_type, aspect_ratio)