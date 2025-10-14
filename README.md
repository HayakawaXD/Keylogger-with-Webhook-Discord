# Simple Keylogger for Discord

Simple Python keylogger to capture keystrokes and send them to a Discord webhook.

Repository contents

- `keylogger.py` - the main script with the keylogger logic and Discord integration.
- `README.md` - this file, providing documentation and setup instructions.
- `LICENSE` - MIT License file (if included).

Requirements

- Python 3.7+
- Dependencies listed in the code (pynput, requests).

Installation (Windows PowerShell)

```powershell
# Assuming you have the script in a folder
cd "path\to\your\project"
python -m venv .venv; .\.venv\Scripts\Activate.ps1
pip install pynput requests
```

Running the application

```powershell

python keylogger.py
```

The keylogger will start capturing keystrokes and sending data to the configured Discord webhook.

Key Features

- `on_press` function to handle keystrokes.
- Periodic sending of captured text via threading.
- Basic error handling for HTTP requests.

Tests

powershell

`# This project doesn't include automated tests, but you can add pytest for testing functions.
pip install pytest  # If you want to add tests`

License

This project is licensed under the MIT License — see the included `LICENSE` file for the full text.

---

## Table of Contents

- Overview
- Project structure
- How it works
- Installation and local run
- Running the application
- Configuration
- Security and best practices
- Contributing
- Troubleshooting / FAQ
- License

---

## Overview

This is a simple Python project that implements a basic keylogger. It captures keystrokes from the user's keyboard and sends the data periodically to a Discord webhook. The code was developed for educational purposes, demonstrating libraries like `pynput` for keyboard events and `requests` for HTTP communication. However, **it should not be used to monitor or spy on others without explicit consent**, as this could violate privacy laws.

Project goals:

- Show how to capture and process keyboard inputs.
- Integrate with external services like Discord for logging.
- Provide a starting point for learning about keyboard monitoring (ethically).

---

## Project structure

(This structure is based on the simple keylogger script)

- `keylogger.py` — the main file containing the keylogger logic, including functions for capturing keys and sending data.
- `README.md` — this documentation file.
- No additional packages or databases are used, keeping it lightweight.

---

## How it works

The keylogger uses the `pynput` library to listen for keyboard events and builds a string of captured text. It then sends this text to a Discord webhook using `requests`, with periodic scheduling via `threading`.

Key components:

`on_press(key)` — handles each keystroke, adding characters to a global string and ignoring certain keys like Shift.
`send_data()` — sends the accumulated text to Discord and schedules the next send.

---

### Installation and local run (Windows - PowerShell)

1 Clone or download the repository:

```powershell

git clone https://github.com/seu-usuario/keylogger-simples-discord.git
cd keylogger-simples-discord
```

2 Create a virtual environment (recommended):

```powershell

python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

*"If PowerShell blocks script execution, run `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` as administrator."*

3 Install dependencies:

```powershell

pip install pynput requests
```

4 Run the application:

```powershell

python keylogger.py
```

The keylogger will start immediately. Press Esc to stop it.

---

## Running the application

To run the keylogger:

```powershell

python keylogger.py
```

- The program will capture keystrokes in the background.
- Data is sent to Discord every 3 seconds by default.
- Access the output in your Discord channel via the webhook.

---

## Configuration

Main settings are in `keylogger.py`:

- webhook_url — replace with your Discord webhook URL.
- time_interval — change the interval (in seconds) for sending data.

Example:
```
webhook_url = "https://discord.com/api/webhooks/YOUR_WEBHOOK_ID/YOUR_WEBHOOK_TOKEN"
time_interval = 5  # Send every 5 seconds
```

---

## Security and best practices

Important notes:

- Ethical use: This tool can capture sensitive information. Always obtain consent and avoid illegal use.
- Validation: Ensure the webhook URL is secure and not exposed.
- Error handling: The code includes try-except for requests, but add more logging for production.
- Privacy: Do not run this on shared or public devices.

---

## Contributing
1 Fork the repository
2 Create a feature/bugfix branch: `git checkout -b feature/your-feature`
3 Make changes and include tests
4 Open a Pull Request

Suggested improvements:

- Add unit tests for key capture.
- Implement more key handling options.
- Enhance security with encryption for sent data.

---

## Troubleshooting / FAQ

Q: How do I stop the keylogger? 
A: Press the Esc key while the program is running. This will terminate the keyboard listener.

Q: What if the Discord webhook is invalid? 
A: You'll see an error in the console like "Erro ao enviar dados: 404" or similar. Check your webhook URL in the code and ensure it's correct. Also, verify that the Discord bot has the necessary permissions.

Q: Is this legal to use? 
A: Only if used ethically and with permission. Keyloggers can violate privacy laws (e.g., LGPD in Brazil). Use for educational purposes only and consult local regulations.

Q: The keylogger isn't capturing special keys like Shift or arrows. 
A: The code ignores keys like Shift by design to reduce noise, but you can modify the `on_press` function to handle them. For arrows or other specials, you may need to add more logic, as `pynput` captures them as objects.

Q: I get an error about missing modules when running the script. 
A: Ensure you have installed the dependencies with `pip install pynput requests`. If you're in a virtual environment, activate it first.

Q: How can I change the sending interval? 
A: Edit the `time_interval` variable in the code to a new value (e.g., 10 for every 10 seconds), then restart the script.
