import cv2

# Initialize the camera
cap = cv2.VideoCapture('/dev/video2')  # 0 is typically the default camera

# Initialize the QR Code detector
detector = cv2.QRCodeDetector()

try:
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret:
            break

        # Detect and decode the QR code in the image
        data, bbox, _ = detector.detectAndDecode(frame)

        if bbox is not None and data:
            # Display the bounding box of the detected QR code in the frame
            n = len(bbox)
            for j in range(n):
                cv2.line(frame, tuple(bbox[j][0]), tuple(bbox[(j+1) % n][0]), (255, 0, 0), 3)

            # Display the decoded data
            print("QR Code detected:", data)

        # Display the resulting frame
        cv2.imshow('Frame', frame)

        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
