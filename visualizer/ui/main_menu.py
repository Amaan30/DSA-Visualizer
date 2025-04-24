# visualizer/ui/main_menu.py
import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                               QPushButton, QLabel, QFrame)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont, QColor

# Import visualizers
from visualizer.structures.arrays import ArrayVisualizer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Configure main window
        self.setWindowTitle("Advanced Data Structure Visualizer")
        self.setMinimumSize(800, 700)
        
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout(central_widget)
        main_layout.setAlignment(Qt.AlignCenter)
        main_layout.setSpacing(20)
        
        # Add title
        title_label = QLabel("Advanced Data Structure Visualizer")
        title_font = QFont("Arial", 24, QFont.Bold)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)
        
        # Add subtitle
        subtitle_label = QLabel("Visualize and learn data structures interactively")
        subtitle_font = QFont("Arial", 12)
        subtitle_label.setFont(subtitle_font)
        subtitle_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(subtitle_label)
        
        # Add separator
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        main_layout.addWidget(separator)
        
        # Create buttons for different data structures
        data_structures = [
            ("Arrays and Lists", self.open_array_visualizer),
            ("Linked Lists", lambda: self.open_visualization("Linked Lists")),
            ("Stacks and Queues", lambda: self.open_visualization("Stacks and Queues")),
            ("Trees", lambda: self.open_visualization("Trees")),
            ("Graphs", lambda: self.open_visualization("Graphs")),
            ("Hash Tables", lambda: self.open_visualization("Hash Tables"))
        ]
        
        # Style for buttons
        button_style = """
            QPushButton {
                background-color: #4a90e2;
                color: white;
                border-radius: 5px;
                padding: 10px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #357abd;
            }
            QPushButton:pressed {
                background-color: #2a5d8c;
            }
        """
        
        # Add buttons for each data structure
        for structure_name, callback in data_structures:
            button = QPushButton(structure_name)
            button.setMinimumSize(300, 50)
            button.setStyleSheet(button_style)
            button.clicked.connect(callback)
            main_layout.addWidget(button)
        
        # Add exit button
        exit_button = QPushButton("Exit")
        exit_button.setMinimumSize(300, 50)
        exit_button.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                border-radius: 5px;
                padding: 10px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
        """)
        exit_button.clicked.connect(self.close)
        main_layout.addWidget(exit_button)
    
    def open_array_visualizer(self):
        self.array_window = ArrayVisualizer()
        self.array_window.show()
    
    def open_visualization(self, structure_name):
        print(f"Opening visualization for: {structure_name}")
        # This is a placeholder for other visualizers that aren't implemented yet