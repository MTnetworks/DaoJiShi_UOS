DARK_THEME = """
QWidget#CentralWidget {
    background-color: #2b2b2b;
    color: #ffffff;
    font-family: "Segoe UI", Arial, sans-serif;
}
QWidget#TimeContainer {
    background-color: transparent;
    border-radius: 10px;
}
QLabel#TimeLabelPart {
    font-weight: bold;
    color: #00ff00;
    background-color: transparent;
    padding: 0px;
}
QLabel#PresetLabel {
    font-size: 16px;
    color: #aaaaaa;
    background-color: transparent;
}
QProgressBar {
    border: 1px solid #555;
    border-radius: 5px;
    text-align: center;
    background-color: #333;
    color: white;
}
QProgressBar::chunk {
    background-color: #00ff00;
    border-radius: 4px;
}
QPushButton {
    background-color: #444;
    border: none;
    padding: 8px 15px;
    border-radius: 4px;
    color: white;
}
QPushButton:hover {
    background-color: #555;
}
QPushButton:pressed {
    background-color: #333;
}
QPushButton#TitleButton {
    background-color: transparent;
    border: none;
    font-size: 18px;
    font-weight: normal;
    padding: 0px;
    color: #aaaaaa;
}
QPushButton#TitleButton:hover {
    background-color: rgba(255, 255, 255, 0.15);
    border-radius: 4px;
}
QPushButton#TitleButtonClose {
    background-color: transparent;
    border: none;
    font-size: 20px;
    font-weight: normal;
    padding: 0px;
    color: #aaaaaa;
}
QPushButton#TitleButtonClose:hover {
    background-color: #e81123;
    color: white;
    border-radius: 4px;
}
"""

LIGHT_THEME = """
QWidget#CentralWidget {
    background-color: #f0f0f0;
    color: #000000;
    font-family: "Segoe UI", Arial, sans-serif;
}
QWidget#TimeContainer {
    background-color: transparent;
    border-radius: 10px;
}
QLabel#TimeLabelPart {
    font-weight: bold;
    color: #008800;
    background-color: transparent;
    padding: 0px;
}
QLabel#PresetLabel {
    font-size: 16px;
    color: #666666;
    background-color: transparent;
}
QProgressBar {
    border: 1px solid #bbb;
    border-radius: 5px;
    text-align: center;
    background-color: #e0e0e0;
    color: black;
}
QProgressBar::chunk {
    background-color: #00cc00;
    border-radius: 4px;
}
QPushButton {
    background-color: #ddd;
    border: none;
    padding: 8px 15px;
    border-radius: 4px;
    color: black;
}
QPushButton:hover {
    background-color: #ccc;
}
QPushButton:pressed {
    background-color: #bbb;
}
QPushButton#TitleButton {
    background-color: transparent;
    border: none;
    font-size: 18px;
    font-weight: normal;
    padding: 0px;
    color: #666666;
}
QPushButton#TitleButton:hover {
    background-color: rgba(0, 0, 0, 0.08);
    border-radius: 4px;
}
QPushButton#TitleButtonClose {
    background-color: transparent;
    border: none;
    font-size: 20px;
    font-weight: normal;
    padding: 0px;
    color: #666666;
}
QPushButton#TitleButtonClose:hover {
    background-color: #e81123;
    color: white;
    border-radius: 4px;
}
"""
