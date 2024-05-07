import os
from PIL import Image

def compress_jpeg(input_path, output_path, quality=85):
    """
    Compresses a JPEG image.
    
    Args:
        input_path (str): Path to the input JPEG image.
        output_path (str): Path to save the compressed JPEG image.
        quality (int): Compression quality (0-100), where 100 is the best quality.
    """
    try:
        # Open the input image
        with Image.open(input_path) as img:
            # Save the image with the specified quality
            img.save(output_path, quality=quality)
            print(f"Image compressed successfully to '{output_path}' with quality {quality}.")
    except Exception as e:
        print(f"Error: {e}")

def compress_jpeg_folder(input_folder, output_folder, quality=85):
    """
    Compresses all JPEG images in a folder.
    
    Args:
        input_folder (str): Path to the folder containing input JPEG images.
        output_folder (str): Path to save the compressed JPEG images.
        quality (int): Compression quality (0-100), where 100 is the best quality.
    """
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all files in the input folder
    files = os.listdir(input_folder)

    # Filter JPEG files
    jpeg_files = [f for f in files if f.lower().endswith('.png')]

    # Iterate over each JPEG file and compress
    for file in jpeg_files:
        input_path = os.path.join(input_folder, file)
        output_path = os.path.join(output_folder, file)
        compress_jpeg(input_path, output_path, quality)

# Example usage
input_folder = r"C:\Users\User\Desktop\airline_images\images"
output_folder = r"C:\Users\User\Desktop\airline_images\images_compressed"
compress_jpeg_folder(input_folder, output_folder, quality=65)
