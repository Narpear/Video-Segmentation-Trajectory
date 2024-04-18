Through this document, we explain our adopted methodology for accomplishing three tasks: separating game frames from non-game frames, detecting the green ball, and obtaining its trajectory. 

1.	Separating Game Frames from Non-Game Frames

This is achieved by identifying frames that contain the game elements, specifically the billiards table, which is distinctively colored in blue. The methodology involves:

Color Space Conversion: Each frame is converted from the BGR color space to the HSV color space. The HSV color space is more effective for color-based detection because it separates the color information (Hue) from the brightness (Value) and saturation (Saturation), making it easier to isolate specific color.

Mask Creation: A mask is created for the blue color of the billiards table using the cv2.inRange function. This function creates a binary mask where the pixels within the specified color range are white, and the rest are black. This mask effectively isolates the table from the rest of the frame.

Morphological Operations: Morphological operations such as closing are applied to the mask to fill in any small holes and smooth the edges. This step is crucial for ensuring that the entire table is detected as a single contour.

Contour Detection: Contours are detected on the mask using cv2.findContours. The function identifies the boundaries of the table in the frame. The contours are then approximated to see if they closely resemble a rectangle shape, which is characteristic of the table.

Area Threshold: A threshold is set for the area of the contour. If the contour area exceeds this threshold, itis the table, indicating that the frame contains game content.


2.	Detecting the Green Ball

Detecting the green ball within the game frames involves identifying the ball's position in each frame. This is accomplished through:

Cropping the Frame: The upper 80% of each frame is cropped to focus on the area where the ball is likely to be. This step assumes that the ball will be in this region, reducing the search area and improving detection accuracy. This also excludes the green ball that is permanently at the bottom of the table.

Color Space Conversion: The cropped image is converted to the HSV color space for color-based detection. The HSV color space is chosen for its ability to isolate color information, making it easier to detect the green ball.

Mask Creation: A mask is created for the green color using cv2.inRange with predefined lower and upper bounds for the green color in HSV. This mask isolates the green ball from the rest of the frame.

Contour Detection: Contours are detected in the mask using cv2.findContours. The largest contour is assumed to be the green ball. The centroid of this contour is calculated, representing the ball's position in the frame.


3.	Obtaining the Ball's Trajectory

Tracking the green ball's movement across frames to obtain its trajectory involves:

Storing Centroid Coordinates: The centroid coordinates of the green ball in each frame are stored. This data is used to plot the ball's trajectory over time.

Drawing Lines Between Points: Lines are drawn between consecutive centroid points, using ‘cv2.polyline()’ to visualize the ball's trajectory. This visual representation allows for the analysis of the ball's movement direction and speed.

Marking the Current Position: The current position of the ball is marked with a red spot on the original image. This visual cue helps in tracking the ball's movement in real-time.
