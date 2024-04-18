import cv2
import numpy as np
import os

def is_game_frame(image, color_lower, color_upper, area_threshold):
    
    # Create a mask for the blue color of the billiards table
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)    
    mask = cv2.inRange(hsv, color_lower, color_upper)
    
    # Apply morphological operations to fill in the holes and find contours
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for cnt in contours:
        # Approximate the contour to see if it's close to a rectangle shape
        epsilon = 0.05 * cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, epsilon, True)
        if len(approx) == 4 and cv2.contourArea(approx) > area_threshold:
            return True
        
    return False

def process_directory(input_dir, output_dir, color_lower, color_upper, area_threshold):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for frame in os.listdir(input_dir):
        frame_path = os.path.join(input_dir, frame)
        image = cv2.imread(frame_path)
        if image is not None and is_game_frame(image, color_lower, color_upper, area_threshold):
            output_path = os.path.join(output_dir, frame)
            cv2.imwrite(output_path, image)

# HSV color range for blue color of the billiards table
color_lower = np.array([100, 150, 0])
color_upper = np.array([140, 255, 255])
area_threshold = 500000  

input_dir = r'C:\Users\prerk\OneDrive\Desktop\Prerana\PESU\Sem 6\IPCV\Mini Project 2\Frames'
output_dir = r'C:\Users\prerk\OneDrive\Desktop\Prerana\PESU\Sem 6\IPCV\Mini Project 2\Game_Frames'

# Process the directory
process_directory(input_dir, output_dir, color_lower, color_upper, area_threshold)





