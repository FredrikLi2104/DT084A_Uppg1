import cv2
import sys
import numpy as np

def initialize_camera(camera_index=0):
	cap = cv2.VideoCapture(camera_index)
    
	# Check if the cam is opened correctly
	if not cap.isOpened():
		print("Error: Could not open camera.")
		return None
        
	return cap

def process_frame(frame):
	# Add your processing code here
	# Convert BGR to HSV
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	# Define range of blue color in HSV
	lower_green = np.array([50,50,50])
	upper_green = np.array([70, 255, 255])
	
	# Threshold the HSV image to get only blue colors
	frame = cv2.inRange(hsv, lower_green, upper_green)
	return frame

def main():
	# Initialize the camera
	cap = initialize_camera()
	if cap is None:
		sys.exit(1)

	
	BLUE = [255,0,0]
	print("Camera feed started. Press 'q' to quit.")

	while True:
		# Capture frame-by-frame
		ret, frame = cap.read()
		

		# Check if frame is captured successfully
		if not ret:
			print("Error: Can't receive frame from camera.")
			break

		constant= cv2.copyMakeBorder(frame,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)

		# Process the frame with a chosen (set) of functions
		output_frame = process_frame(frame)
        
		# Display the original frame
		cv2.imshow('Original Frame', frame)

		# Display original frame with blue border
		cv2.imshow('Olle', constant)

		# Display the processed frame
		cv2.imshow('Processed Frame', output_frame)
        
		# Check for 'q' key press to quit the application
		# waitKey(1) returns -1 if no key is pressed
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	# Clean up
	cap.release()
	cv2.destroyAllWindows()

if __name__ == "__main__":
	main() 