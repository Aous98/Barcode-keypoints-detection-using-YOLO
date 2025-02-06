'''blured'''

import os
import cv2

source_directory = '/home/aous/Desktop/MIPT/project/yolo data/original 640'

# Define the directory path to save the augmented dataset
destination_directory = '/home/aous/Desktop/MIPT/project/yolo data/blured'
# Define the source directory path where your images are located
# source_directory = '/home/aous/Desktop/MIPT/project/DATASET/to augment/before'
y = 0
# # Define the destination directory path to save the blurred images
# destination_directory = '/home/aous/Desktop/MIPT/project/DATASET/to augment/blured'

# Specify the blur kernel size
kernel_size = (5, 5)

# Iterate over each file in the source directory
for filename in os.listdir(source_directory):
    if y == 7:
        break
    # y+=1
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # Read the image file
        image_path = os.path.join(source_directory, filename)
        image = cv2.imread(image_path)
        old = filename
        # Apply blur to the image
        blurred_image = cv2.blur(image, kernel_size)
        filename = filename[:-4]
        filename = int(filename)
        filename += 676
        filename = str(filename)

        # Create a new filename for the blurred image
        blurred_filename = f'{filename}.png'

        # Save the blurred image to the destination directory
        cv2.imwrite(os.path.join(destination_directory, blurred_filename), blurred_image)
        print(f'changed {old} to {blurred_filename}')