# NOVA – Next Gen Optimistic Virtual Assistance

This repository houses my Final Year Project: **NOVA**, a Python-based virtual assistant built with Object-Oriented Programming principles, integrated with Raspberry Pi and robotics to provide dynamic, music-responsive interactions. NOVA can not only dance to tunes via a robot speaker but also handle free-form queries using an NLP component—ensuring smooth responses even to unexpected inputs.

---

## ✨ Features

- **Python + OOP** architecture for modular and extensible functionality.  
- **Raspberry Pi integration**, enabling NOVA to operate on compact hardware.  
- **Robot-speaker interface** that can dance when music plays.  
- **Natural Language Processing (NLP)** enables responsive behavior to commands not hardcoded.  

---

## 📂 Project Structure

```
.
├── NOVAUi.py           # GUI controller for NOVA
├── NOVAUi.ui           # UI layout file for Raspberry Pi interface
├── NOVAWITHU.py        # Enhanced version with UI capabilities
├── nova.py             # Core logic of NOVA assistant
├── Recordings.py       # Audio capture and handling module
├── PhoneNumer.py       # Utility to process phone number inputs
├── state.py            # State management across interactions
├── Untitled-1.py       # Experimental/prototype module
├── requirements.txt    # Python dependencies used in the project
└── README.md           # Project overview (this file)
```

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/PranavhShetty/Final-Year-Project.git
   cd Final-Year-Project
   ```

2. **Install dependencies**
   Ensure you’re using Python 3.x:
   ```bash
   pip install -r requirements.txt
   ```

3. **Deploy on Raspberry Pi**
   - Load the project onto your Raspberry Pi.
   - Ensure required libraries (e.g., for audio processing and GUI) are installed.
   - Run `NOVAUi.py` or `NOVAWITHU.py` to launch the interface.

---

## ▶️ Usage

1. Launch the GUI:
   ```bash
   python NOVAUi.py
   ```

2. Play a song — NOVA will “dance” via the hardware.

3. Speak or type a query, and NOVA will attempt to understand and reply.

---

## 📊 Example Interactions

**1. Simple query**
```
User: What is the time now?
NOVA: The current time is 3:45 PM.
```

**2. Unexpected input**
```
User: Tell me a joke about robots.
NOVA: Why was the robot so bad at soccer? Because it kept kicking up sparks! 🤖⚡
```

**3. Music mode**
```
🎵 Playing a song on the robot speaker...
🤖 NOVA begins dancing in sync with the music.
```

---

## 🤝 Contributions

Feel free to fork and enhance NOVA! Whether optimizing the NLP, extending hardware support, or enriching interactivity, your contributions are welcome.

---

## 📜 License

This project is released for academic purposes. Please feel free to adapt or expand it with attribution.

---

✨ **NOVA** showcases a blend of software and hardware innovation—perfect for anyone exploring embedded AI, robotics, or conversational systems in real-world settings.  
