# Python Desktop Application Deployment

A practical project demonstrating how to package Python desktop applications into professional standalone Windows executables using PyInstaller.

## Features

* Convert Python scripts into EXE files
* Package PyQt5 / PyQt6 applications
* Add custom application icons
* Bundle images and assets
* Include external resources
* Generate standalone distributions
* Create deployment-ready builds
* Windows application packaging

## Technologies

* Python
* PyInstaller
* PyQt5
* PyQt6

## Build Command

```bash
pyinstaller -F -w --icon=app.ico main.py
```

## Resource Packaging

```bash
pyinstaller -F -w --add-data "assets;assets" main.py
```

## Project Structure

Python-Desktop-App-Deployment/

├── README.md

├── requirements.txt

├── src/

│   └── main.py

├── assets/

│   ├── logo.png

│   └── background.png

└── build/

## Skills Demonstrated

* Software Deployment
* Application Packaging
* Windows Desktop Development
* Executable Generation
* Resource Management
* Distribution Engineering
