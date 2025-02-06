# contrast and brightness

import os
import cv2

source_directory = '/home/aous/Desktop/MIPT/project/DATASET/new data2/temp'

# Define the directory path to save the augmented dataset
destination_directory = '/home/aous/Desktop/MIPT/project/DATASET/new data2/noisy'
if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)
# Specify the brightness and contrast adjustment values
brightness_factor = 1.2  # Increase brightness by 20%
contrast_factor = 1.5  # Increase contrast by 50%
y = 0


# Iterate over each file in the source directory
for filename in os.listdir(source_directory):
    if y == 7:
        break
    # y+=1
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # Read the image file
        image_path = os.path.join(source_directory, filename)
        image = cv2.imread(image_path)

        # Apply brightness and contrast adjustment
        adjusted_image = cv2.convertScaleAbs(image, alpha=brightness_factor, beta=0)
        adjusted_image = cv2.convertScaleAbs(adjusted_image, alpha=contrast_factor, beta=0)

        # Create a new filename for the augmented image
        augmented_filename = filename

        # Save the augmented image to the destination directory
        cv2.imwrite(os.path.join(destination_directory, augmented_filename), adjusted_image)
