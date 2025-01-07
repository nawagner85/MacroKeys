# MacroKeys

MacroKeys is a Python-based application that allows users to map custom key combinations to specific applications. It provides a system tray application for easy access and a GUI for managing key mappings.

## Features

- Map custom key combinations to specific applications.
- System tray application for quick access.
- GUI for managing key mappings.
- Supports multiple applications with different key mappings.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd MacroKeys
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create an executable for the system tray application using PyInstaller:
   ```bash
   pyinstaller --onefile --windowed keypad_controller_tray.py
   ```

## Usage

1. Run the system tray application:
   - Navigate to the `dist` directory and run the `keypad_controller_tray.exe` file.

2. Right-click the system tray icon to open the Key Mappings GUI.

3. Use the GUI to add, update, or delete key mappings for different applications.

## Key Mappings

Key mappings are stored in a YAML file (`key_mappings.yaml`). Each application can have its own set of key mappings, which can be managed through the GUI.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.
