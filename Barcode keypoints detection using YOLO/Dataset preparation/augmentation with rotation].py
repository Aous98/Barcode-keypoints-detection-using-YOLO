#rotation 30
import os
import cv2

# Set the path to the input directory containing the images
input_directory = "/home/aous/Desktop/MIPT/project/yolo data/3D"

# Set the path to the output directory to save the rotated images
output_directory = "/home/aous/Desktop/MIPT/project/yolo data/3D/rotated"

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Iterate over each image file in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith((".jpg", ".jpeg", ".png")):
        # Read the image
        image_path = os.path.join(input_directory, filename)
        image = cv2.imread(image_path)

        # Get the image dimensions
        height, width = image.shape[:2]

        # Calculate the rotation matrix
        rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), 30, 1)

        # Apply the rotation to the image
        rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

        # Generate the output file path
        output_path = os.path.join(output_directory, filename)

        # Save the rotated image
        cv2.imwrite(output_path, rotated_image)

        print(f"Rotated image saved: {output_path}")
