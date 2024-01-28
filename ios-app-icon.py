import os
import zipfile
import shutil
from PIL import Image

def resize_image(input_image_path, output_image_path, size):
    with Image.open(input_image_path) as image:
        resized_image = image.resize(size)
        resized_image.save(output_image_path, 'PNG')

# Example usage
input_path = input('Enter the path for the source icon image: ')
target_sizes = [(20, 20),(29,29), (40, 40), (57, 57), (60, 60), (76, 76), (83.5,83.5), (1024,1024)]

zip_file_path = os.path.join(os.path.dirname(input_path), 'ios_app_icons.zip')

# Create a temporary directory to store resized images
temp_dir = os.path.join(os.path.dirname(input_path), 'temp')
os.makedirs(temp_dir, exist_ok=True)

# Resize and save the images
for i, targetSize in enumerate(target_sizes):
    if (i < 5) :
        for x in range(3):
            radius = int(targetSize[0]) * (x+1)
            size = (radius, radius)
            output_path = os.path.join(temp_dir, f"Icon-App-{int(targetSize[0])}x{int(targetSize[1])}@{x+1}x.png")
            resize_image(input_path, output_path, size)

    elif i == 5 :
        radius = int(targetSize[0]) * 2
        size = (radius, radius)
        output_path = os.path.join(temp_dir, f"Icon-App-{targetSize[0]}x{targetSize[1]}@{2}x.png")
        resize_image(input_path, output_path, size)

    else:
        radius = int(targetSize[0])
        size = (radius, radius)
        output_path = os.path.join(temp_dir, f"Icon-App-{int(targetSize[0])}x{int(targetSize[1])}@{1}x.png")
        resize_image(input_path, output_path, size)



# Create a ZIP file and add the resized images
with zipfile.ZipFile(zip_file_path, 'w') as zip_file:
    for root, _, files in os.walk(temp_dir):
        for file in files:
            file_path = os.path.join(root, file)
            zip_file.write(file_path, os.path.basename(file_path))

# Remove the temporary directory
shutil.rmtree(temp_dir)

print("iOS app icons generated successfully!")
