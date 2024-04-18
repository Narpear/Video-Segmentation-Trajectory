import cv2
import numpy as np
import os

frames_dir = r'C:\Users\prerk\OneDrive\Desktop\Prerana\PESU\Sem 6\IPCV\Mini Project 2\Game_Frames'
trajectory_frames_dir = r'C:\Users\prerk\OneDrive\Desktop\Prerana\PESU\Sem 6\IPCV\Mini Project 2\Trajectory_Frames'

# Create an empty list to store the trajectory points
trajectory_points = []
count = 0

# Loop over each frame in the directory
for filename in os.listdir(frames_dir):
    if filename.endswith('.png'):
        image = cv2.imread(os.path.join(frames_dir, filename))
        
        # Crop the image to the upper 80%
        height, width, _ = image.shape
        upper_80_height = int(height * 0.8)
        cropped_image = image[:upper_80_height, :]

        # Create a mask for the green color in the cropped image
        hsv = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2HSV)
        lower_green = np.array([60, 70, 150])
        upper_green = np.array([80, 255, 255])
        mask = cv2.inRange(hsv, lower_green, upper_green)

        # Find contours in the mask if any, and centroid of the largest contour
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if contours:
            largest_contour = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(largest_contour)
            centroid_x = x + w // 2
            centroid_y = y + h // 2
            trajectory_points.append((centroid_x, centroid_y))
            count = count+1

            # Draw lines between all trajectory points up to the current point
            if len(trajectory_points) > 1:
                trajectory_points_np = np.array(trajectory_points, dtype=np.int32)
                cv2.polylines(image, [trajectory_points_np], False, (0, 0, 255), 2)

            # Mark a large red spot on the original image
            cv2.circle(image, (centroid_x, centroid_y), 7, (0, 0, 255), -1)

            # Save the modified image to the Trajectory_Frames directory
            cv2.imwrite(os.path.join(trajectory_frames_dir, filename), image)

print("points: ", count)
print("trajectory points: ", trajectory_points)
