
cat > fire_hybrid.py << 'ENDOFFILE'
import cv2
import numpy as np
from datetime import datetime
import time

print("🔥 Fire Detection System Starting...")

# Initialize camera
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 30)

if not cap.isOpened():
    print("❌ Error: Cannot open webcam")
    exit()

print("✅ System Ready!")
print("Press 'q' to quit, 's' to save screenshot\n")

last_alert = 0
frame_count = 0
start_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1

    # Convert to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    blur = cv2.GaussianBlur(hsv, (15, 15), 0)

    # Fire color detection - OPTIMIZED for lighter flame
    # Detecting bright yellow-orange colors
    lower1 = np.array([15, 120, 120])   # Yellow-orange fire
    upper1 = np.array([30, 255, 255])
    mask1 = cv2.inRange(blur, lower1, upper1)

    # Also detect more yellow fire (lighter flame tip)
    lower2 = np.array([5, 100, 180])    # Bright yellow
    upper2 = np.array([15, 255, 255])
    mask2 = cv2.inRange(blur, lower2, upper2)

    # Combine both masks
    mask = cv2.bitwise_or(mask1, mask2)

    # Smaller kernel for small flames
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    fire_detected = False
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 200:  # Small lighter flame threshold
            x, y, w, h = cv2.boundingRect(cnt)

            # Check brightness in the region
            roi = frame[y:y+h, x:x+w]
            if roi.size > 0:
                avg_brightness = np.mean(cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY))

                # More lenient for lighter flame
                if avg_brightness > 100:
                    fire_detected = True
                    # Draw THICK red bounding box
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 4)
                    cv2.putText(frame, f"FIRE! {int(area)}px", (x, y-10),
                               cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)

    # Display status
    if fire_detected:
        if time.time() - last_alert > 1:
            print(f"🚨 FIRE DETECTED at {datetime.now().strftime('%H:%M:%S')}")
            last_alert = time.time()

        cv2.putText(frame, "STATUS: FIRE DETECTED!", (10, 30),
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
    else:
        cv2.putText(frame, "STATUS: Monitoring...", (10, 30),
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Calculate and show FPS
    elapsed = time.time() - start_time
    fps = frame_count / elapsed if elapsed > 0 else 0
    cv2.putText(frame, f"FPS: {fps:.1f}", (10, 60),
               cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)

    cv2.imshow('Fire Detection', frame)
    cv2.imshow('Fire Mask', mask)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('s'):
        cv2.imwrite(f"fire_{datetime.now().strftime('%H%M%S')}.jpg", frame)
        print("📸 Screenshot saved!")

cap.release()
cv2.destroyAllWindows()
print("System stopped")
ENDOFFILE
