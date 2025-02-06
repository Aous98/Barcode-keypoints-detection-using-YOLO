import cv2
import numpy as np
import os
import math

def calculate_distance(x1, y1, x2, y2):
    # print(x1,x2,y1,y2)
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    return distance


def click_event(event, x, y, flags, param):
    global keypoints, img, img_width, img_height

    if event == cv2.EVENT_LBUTTONDOWN:
        normalized_x = x
        normalized_y = y
        # print(x,y)
        keypoints.append((normalized_x, normalized_y))
        cv2.circle(img, (x, y), 7, (0, 0, 255), -1)
        cv2.imshow('Image', img)


# Directory path containing the images
image_dir = '/home/aous/Desktop/MIPT/project/yolo data/data splitted'

# Output folder path for the text files
output_folder = '/home/aous/Desktop/MIPT/project/yolo data/data splitted'
os.makedirs(output_folder, exist_ok=True)
c = 0
# Process each image in the directory
for filename in os.listdir(image_dir):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # Load the image
        image_path = os.path.join(image_dir, filename)
        img = cv2.imread(image_path)
        img_height, img_width, _ = img.shape

        # Create a window to display the image
        cv2.namedWindow('Image')
        cv2.imshow('Image', img)

        # Initialize the keypoints list
        keypoints = []

        # Set the callback function for mouse events
        cv2.setMouseCallback('Image', click_event)

        # Wait for the user to click on the keypoints
        cv2.waitKey(10000)
        cv2.destroyAllWindows()
        class_number = 0


        # Generate the text file
        output_file = f"{filename.split('.')[0]}.txt"
        output_path = os.path.join(output_folder, output_file)
        # print(keypoints)
        bbox = []
        points = np.array(keypoints)

        # Find the minimum and maximum x and y values
        min_x = np.min(points[:, 0])
        max_x = np.max(points[:, 0])
        min_y = np.min(points[:, 1])
        max_y = np.max(points[:, 1])

        # Find the four corner points of the bounding box
        top_left = (min_x, max_y)
        top_right = (max_x, max_y)
        bottom_left = (min_x, min_y)
        bottom_right = (max_x, min_y)

        # Calculate the center point
        center_x = (min_x + max_x) / 2
        center_y = (min_y + max_y) / 2
        center = (center_x, center_y)

        # Calculate the height and width of the bounding box
        height = max_y - min_y
        width = max_x - min_x
        bbox.append(center_x / 640)
        bbox.append(center_y / 640)
        bbox.append(width / 640)
        bbox.append(height / 640)

        with open(output_path, 'w') as file:
            file.write(f"{class_number} ")
            for i in bbox:
                file.write(f"{i} ")
            for x, y in keypoints:
                file.write(f"{x/640} {y/640} 2 ")
            remaining_values = 32 - len(bbox) - len(keypoints)*3 - 1
            for _ in range(remaining_values):
                file.write("0 ")
    c += 1
    print(c)