'''salt and peper'''
import os
import cv2
import numpy as np

# Define the directory path of your dataset
dataset_dir = '/home/aous/Desktop/MIPT/project/DATASET/new data2/image'

# Define the directory path to save the augmented dataset
augmented_dir = '/home/aous/Desktop/MIPT/project/DATASET/new data2/noisy/image'

# Create the augmented directory if it doesn't exist
if not os.path.exists(augmented_dir):
    os.makedirs(augmented_dir)


# Function to add salt and pepper noise to an image
def add_salt_and_pepper(image, salt_prob, pepper_prob):
    noisy_image = np.copy(image)
    salt_coords = np.random.rand(*image.shape[:2]) < salt_prob
    pepper_coords = np.random.rand(*image.shape[:2]) < pepper_prob
    noisy_image[salt_coords] = 255  # Add salt noise
    noisy_image[pepper_coords] = 0  # Add pepper noise
    return noisy_image


# Loop through each file in the dataset directory
for filename in os.listdir(dataset_dir):
    # Load the image
    img_path = os.path.join(dataset_dir, filename)
    image = cv2.imread(img_path)
    r = filename
    filename = filename[:-4]
    filename = int(filename)
    # filename += 325
    filename = str(filename)
    # Add salt and pepper noise to the image
    salt_prob = 0.02  # Adjust the probability based on the desired noise level
    pepper_prob = 0.02  # Adjust the probability based on the desired noise level
    noisy_image = add_salt_and_pepper(image, salt_prob, pepper_prob)

    # Save the augmented image
    # number = re.findall(r'\d+', filename)[0]
    # number = int(number)
    # number += 325
    # number = str(number)
    augmented_filename = f'{filename}.png'

    augmented_path = os.path.join(augmented_dir, augmented_filename)
    cv2.imwrite(augmented_path, noisy_image)
    print(f"noised  {r} to {augmented_filename}")