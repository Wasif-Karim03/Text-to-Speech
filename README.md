# Text-to-Speech Converter

This project is a simple Text-to-Speech (TTS) converter built using Python. It utilizes the Google Text-to-Speech (gTTS) library to convert input text to speech and the tkinter library to create a graphical user interface (GUI).

 Features
- Converts input text to speech
- Plays the converted speech as an audio file
- User-friendly GUI

 Installation

 Requirements
- Python 3.x
- `gTTS` library
- `tkinter` library (comes pre-installed with Python)

 Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/text-to-speech-converter.git
   cd text-to-speech-converter
   ```

2. Install the required packages:
   ```bash
   pip install gtts
   ```

 Usage

1. Run the Python script:
   ```bash
   python tts_converter.py
   ```

2. The GUI window will open. Enter the text you want to convert to speech in the text box.

3. Click the "Convert to Speech" button.

4. The application will convert the text to speech and play the audio file.

 Technical Details

 Libraries Used

- **os**: For interacting with the operating system, specifically to play the audio file.
- **gtts**: Google Text-to-Speech library to convert text to speech.
- **tkinter**: Standard Python interface to the Tk GUI toolkit.

 Script Breakdown

- **convert_to_speech()**: This function retrieves the text from the text entry widget, converts it to speech using gTTS, saves it as an MP3 file, and plays it using the default audio player on a Mac (`afplay`).
- **window**: The main application window created using tkinter.
- **text_entry**: A text widget where users can input the text to be converted.
- **convert_button**: A button that triggers the `convert_to_speech` function when clicked.

 Notes

- This script is designed to run on a MacOS system. For other operating systems, you may need to change the command used to play the audio file.
- Ensure you have an active internet connection, as gTTS requires access to Google’s Text-to-Speech API.

 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

