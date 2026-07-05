import cv2
from ultralytics import YOLO

# Load the YOLOv8 segmentation model
model = YOLO(r"C:\Users\ASUS\Downloads\yolov8n-seg.pt")  # load a pretrained model (recommended for training)

# Initialize the video capture object
cap = cv2.VideoCapture(r"C:\Users\ASUS\Downloads\video1.mp4")

if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    # Perform inference on the frame
    results = model(frame)

    # Annotate the frame
    annotated_frame = results[0].plot()

    # Display the annotated frame
    cv2.imshow('YOLOv8 Segmentation', annotated_frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()