✋ Finger Counter using OpenCV
📌 Overview

This project is a real-time hand gesture recognition system built with OpenCV and a custom hand tracking module. It detects a hand through the webcam, counts the number of fingers raised, and displays a corresponding image based on the detected number. It also shows FPS for performance monitoring.

🚀 Features
🎥 Real-time webcam capture
✋ Hand detection and landmark tracking
🔢 Accurate finger counting
🖼️ Dynamic image display based on finger count
⚡ FPS (Frames Per Second) display
🛠️ Requirements

Make sure you have the following installed:

pip install opencv-python

Additional requirements:

Python 3.x
Custom module: handtracking.py
📂 Project Structure
project/
│── main.py
│── handtracking.py
│── fingers/        # Folder containing images (0–5)
▶️ How to Run
Clone the repository:
git clone https://github.com/your-username/finger-counter.git
Navigate to the project folder:
cd finger-counter
Run the script:
python main.py
⚙️ How It Works
The webcam captures live video.
The hand tracking module detects hand landmarks.
The program checks fingertip positions.
Based on finger count, a specific image is displayed.
FPS is calculated and shown on screen.
📸 Demo

Show your hand in front of the camera, and the program will count your fingers and display the result visually.

📌 Future Improvements
Improve detection accuracy
Add support for both hands
Use deep learning models for better tracking
Create a GUI interface
🤝 Contributing

Contributions are welcome! Feel free to fork the repo and submit a pull request.

📄 License

This project is open-source and available under the MIT License.
