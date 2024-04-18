import os
import cv2

# This function extracts frames from video
# Input parameters: video path : Path of the video to be converted into frames
#                   output_directory : The directory into which the frames will be stored upon execution
def split_video_into_frames(video_path, output_directory):
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Get the video's frames per second (fps)
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    frame_count = 0

    while True:
        # Read a frame from the video
        ret, frame = cap.read()

        # If there are no more frames, break from the loop
        if not ret:
            break
        
        # Save the frame as an image in the output directory
        frame_count += 1


        frame_filename = os.path.join(output_directory, f"frame_{frame_count:04d}.png")
        cv2.imwrite(frame_filename, frame)

    # Release the video capture object
    cap.release()

# This function merges all the frames in a particular Folder into a video
# Input parameters: input_frames_directory : Path of the directory containing the fra,es to be combined
#                   output_video_path : the path where the output video should be saved
#                   fps : the number of frames that have to be combined per second
def frames_to_video(input_frames_directory, output_video_path, fps):
    # Get the list of frame files in the input directory
    frame_files = sorted([f for f in os.listdir(input_frames_directory) if f.startswith("frame_")])

    # Read the first frame to get its size
    first_frame = cv2.imread(os.path.join(input_frames_directory, frame_files[0]))
    height, width, _ = first_frame.shape

    # Create a VideoWriter object to save the output video
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height), isColor=True)

    for frame_file in frame_files:
        # Read each frame and write it to the output video
        # print("In for loop")
        frame_path = os.path.join(input_frames_directory, frame_file)
        frame = cv2.imread(frame_path)
        out.write(frame)

    # Release the VideoWriter object
    out.release()

if __name__ == "__main__":

    # video_path = r"C:\Users\prerk\OneDrive\Desktop\Prerana\PESU\Sem 6\IPCV\Mini Project 2\input_video.mp4"
    # output_dir = r"C:\Users\prerk\OneDrive\Desktop\Prerana\PESU\Sem 6\IPCV\Mini Project 2\Frames"
    
    # split_video_into_frames(video_path, output_dir)
    # print("==================================== Video has been splitted into its corresponding frames ====================================")

    input_frames_directory = r"C:\Users\prerk\OneDrive\Desktop\Prerana\PESU\Sem 6\IPCV\Mini Project 2\Trajectory_Frames"
    output_video_path = r"C:\Users\prerk\OneDrive\Desktop\Prerana\PESU\Sem 6\IPCV\Mini Project 2\output_video.mp4"
    fps = 60  # Adjust the frames per second as needed

    frames_to_video(input_frames_directory, output_video_path, fps)
    print("==================================== Video has been formed from its corresponding frames ====================================")