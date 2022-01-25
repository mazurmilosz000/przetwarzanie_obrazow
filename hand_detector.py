import cv2
from cvzone.HandTrackingModule import HandDetector

camera_port = 0
cap = cv2.VideoCapture(camera_port)

detector = HandDetector(detectionCon=0.8)

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:

    # przechwytywanie obrazu
    ret, frame = cap.read()
    # wykrywanie dloni
    hands, frame = detector.findHands(frame)

    if hands:
        hand1 = hands[0]  # tworzenie 1 dloni

        if hand1:
            fingers = detector.fingersUp(hand1)         # detektor palcow w dloni 1
            fingerscount = fingers.count(1)             # licznik palcow w 1 dloni
            # wypisanie liczby palcow w 1 dloni
            cv2.putText(frame, f'Hand 1 fingers: {fingerscount}', (20, 50), cv2.FONT_HERSHEY_PLAIN, 2,
                        (255, 0, 0), 2)

    if len(hands) == 2:
        hand2 = hands[1]  # tworzenie 2 dloni

        if hand2:
            fingers = detector.fingersUp(hand2)     # detektor palcow w dloni 2
            fingerscount = fingers.count(1)         # licznik palcow w 2 dloni
            # wypisanie liczby palcow w 2 dloni
            cv2.putText(frame, f'Hand 2 fingers: {fingerscount}', (320, 50), cv2.FONT_HERSHEY_PLAIN, 2,
                        (0, 0, 255), 2)

    # jesli frame jest wczytany poprawnie ret = True
    if not ret:
        print("Can't receive frame")
        break

    # Opracje na frame
    # wyswietlanie rezultatu na frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

# Koniec programu, zwolnienie przechwytywania
cap.release()
cv2.destroyAllWindows()
