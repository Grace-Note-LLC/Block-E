import cv2
import pytesseract


def snapshot(frame):
    text = pytesseract.image_to_string(processed_frame, config='--psm 6')
    return text

def preprocess_image(frame):
    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply thresholding
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Optional: Apply blur to reduce noise (if necessary)
    # blur = cv2.GaussianBlur(thresh, (5,5), 0)

    return thresh

cap = cv2.VideoCapture('/dev/video2')

while True:
    ret, frame = cap.read()
    if not ret:
        break

    processed_frame = preprocess_image(frame)

    cv2.imshow('Processed Frame', processed_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if cv2.waitKey(1) & 0xFF == ord('s'):
        print({f"Text: {snapshot(processed_frame)}"})    

cap.release()
cv2.destroyAllWindows()