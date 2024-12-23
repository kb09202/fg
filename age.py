import cv2
from deepface import DeepFace


def main():
    # Ouvrir la webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Erreur : Impossible d'accéder à la webcam.")
        return

    print("Appuyez sur 'q' pour quitter.")

    while True:
        # Lire une image depuis la webcam
        ret, frame = cap.read()
        if not ret:
            print("Erreur : Impossible de lire depuis la webcam.")
            break

        # Afficher le flux vidéo
        cv2.imshow("Webcam - Analyse d'âge", frame)

        try:
            # Analyser l'image
            analysis = DeepFace.analyze(frame, actions=['age'], enforce_detection=False)
            age = analysis.get("age", "Inconnu")
            print(f"Âge estimé : {age}")

            # Ajouter l'âge sur l'image
            cv2.putText(frame, f"Age: {int(age)}", (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        except Exception as e:
            print(f"Erreur lors de l'analyse : {e}")

        # Afficher la vidéo avec l'âge estimé
        cv2.imshow("Webcam - Analyse d'âge", frame)

        # Quitter si 'q' est pressé
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Libérer les ressources
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
