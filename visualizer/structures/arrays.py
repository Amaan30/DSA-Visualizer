# # visualizer/structures/arrays.py
# from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
#                               QPushButton, QLabel, QLineEdit, QComboBox, 
#                               QGridLayout, QFrame, QMessageBox)
# from PySide6.QtCore import Qt, QPropertyAnimation, QRect, QEasingCurve, QSequentialAnimationGroup
# from PySide6.QtGui import QFont, QColor

# class ArrayVisualizer(QMainWindow):
#     def __init__(self):
#         super().__init__()
        
#         # Configure window
#         self.setWindowTitle("Array Visualizer")
#         self.setMinimumSize(1000, 600)
        
#         # Create central widget and layout
#         central_widget = QWidget()
#         self.setCentralWidget(central_widget)
        
#         main_layout = QVBoxLayout(central_widget)
        
#         # Add title
#         title_label = QLabel("Array Visualization")
#         title_font = QFont("Arial", 18, QFont.Bold)
#         title_label.setFont(title_font)
#         title_label.setAlignment(Qt.AlignCenter)
#         main_layout.addWidget(title_label)
        
#         # Control panel
#         control_panel = QWidget()
#         control_layout = QHBoxLayout(control_panel)
        
#         # Array size input
#         size_layout = QHBoxLayout()

#         size_label = QLabel("Size:")
#         self.size_input = QLineEdit("10")
#         self.size_input.setFixedWidth(50)
#         create_button = QPushButton("Create Array")
#         create_button.clicked.connect(self.create_array)
        
#         size_layout.addWidget(size_label)
#         size_layout.addWidget(self.size_input)
#         size_layout.addWidget(create_button)
#         size_layout.addStretch()
        
#         # Operations
#         operations_layout = QHBoxLayout()
#         operations_label = QLabel("Operation:")
#         self.operation_combo = QComboBox()
#         self.operation_combo.addItems(["Access", "Insert", "Delete", "Search"])
#         self.index_input = QLineEdit()
#         self.index_input.setPlaceholderText("Index")
#         self.index_input.setFixedWidth(80)
#         self.value_input = QLineEdit()
#         self.value_input.setPlaceholderText("Value")
#         self.value_input.setFixedWidth(80)
#         execute_button = QPushButton("Execute")
#         execute_button.clicked.connect(self.execute_operation)
        
#         operations_layout.addWidget(operations_label)
#         operations_layout.addWidget(self.operation_combo)
#         operations_layout.addWidget(self.index_input)
#         operations_layout.addWidget(self.value_input)
#         operations_layout.addWidget(execute_button)
#         operations_layout.addStretch()
        
#         # Add layouts to control panel
#         control_layout.addLayout(size_layout)
#         control_layout.addLayout(operations_layout)
        
#         # Add control panel to main layout
#         main_layout.addWidget(control_panel)
        
#         # Add separator
#         separator = QFrame()
#         separator.setFrameShape(QFrame.HLine)
#         separator.setFrameShadow(QFrame.Sunken)
#         main_layout.addWidget(separator)
        
#         # Visualization area
#         self.visualization_widget = QWidget()
#         self.visualization_layout = QHBoxLayout(self.visualization_widget)
#         self.visualization_layout.setAlignment(Qt.AlignCenter)
#         self.visualization_layout.setSpacing(2)
        
#         main_layout.addWidget(self.visualization_widget)
        
#         # Status area
#         self.status_label = QLabel("Ready")
#         self.status_label.setAlignment(Qt.AlignCenter)
#         status_font = QFont("Arial", 12)
#         self.status_label.setFont(status_font)
#         main_layout.addWidget(self.status_label)
        
#         # Back button
#         back_button = QPushButton("Back to Main Menu")
#         back_button.clicked.connect(self.close)
#         main_layout.addWidget(back_button, alignment=Qt.AlignRight)
        
#         # Initialize array
#         self.array_cells = []
#         self.array_values = []
#         self.cell_size = 60
        
#     def create_array(self):
#         try:
#             size = int(self.size_input.text())
#             if size <= 0 or size > 20:
#                 QMessageBox.warning(self, "Invalid Size", "Array size should be between 1 and 20.")
#                 return
                
#             # Clear previous array
#             self.clear_visualization()
            
#             # Generate random values for array (for demonstration)
#             import random
#             self.array_values = [random.randint(1, 99) for _ in range(size)]
            
#             # Create visualization
#             self.visualize_array()
            
#             self.status_label.setText(f"Created array with {size} elements")
            
#         except ValueError:
#             QMessageBox.warning(self, "Invalid Input", "Please enter a valid integer for array size.")
    
#     def visualize_array(self):
#         # Clear any existing visualization
#         self.clear_visualization()
        
#         # Create a cell for each array element
#         for i, value in enumerate(self.array_values):
#             cell_frame = QFrame()
#             cell_frame.setFrameShape(QFrame.Box)
#             cell_frame.setLineWidth(2)
#             cell_frame.setFixedSize(self.cell_size, self.cell_size)
#             cell_frame.setStyleSheet("background-color: #4a90e2; color: white; border-radius: 5px;")
            
#             cell_layout = QVBoxLayout(cell_frame)
            
#             # Value label
#             value_label = QLabel(str(value))
#             value_label.setAlignment(Qt.AlignCenter)
#             value_label.setFont(QFont("Arial", 14, QFont.Bold))
#             cell_layout.addWidget(value_label)
            
#             # Index label
#             index_label = QLabel(str(i))
#             index_label.setAlignment(Qt.AlignCenter)
#             index_label.setStyleSheet("color: rgba(255, 255, 255, 0.7);")
#             cell_layout.addWidget(index_label)
            
#             self.visualization_layout.addWidget(cell_frame)
#             self.array_cells.append((cell_frame, value_label, index_label))
    
#     def clear_visualization(self):
#         # Remove all cells from layout
#         while self.visualization_layout.count():
#             item = self.visualization_layout.takeAt(0)
#             widget = item.widget()
#             if widget:
#                 widget.deleteLater()
        
#         self.array_cells = []
    
#     def execute_operation(self):
#         operation = self.operation_combo.currentText()
        
#         try:
#             index = int(self.index_input.text()) if self.index_input.text() else -1
            
#             if operation != "Search" and (index < 0 or index >= len(self.array_values)):
#                 QMessageBox.warning(self, "Invalid Index", f"Index should be between 0 and {len(self.array_values)-1}.")
#                 return
                
#             if operation == "Access":
#                 self.access_element(index)
#             elif operation == "Insert":
#                 if not self.value_input.text():
#                     QMessageBox.warning(self, "Missing Value", "Please enter a value to insert.")
#                     return
#                 value = int(self.value_input.text())
#                 self.insert_element(index, value)
#             elif operation == "Delete":
#                 self.delete_element(index)
#             elif operation == "Search":
#                 if not self.value_input.text():
#                     QMessageBox.warning(self, "Missing Value", "Please enter a value to search.")
#                     return
#                 value = int(self.value_input.text())
#                 self.search_element(value)
                
#         except ValueError:
#             QMessageBox.warning(self, "Invalid Input", "Please enter valid integers for index and value.")
    
#     def access_element(self, index):
#         # Highlight the accessed element
#         cell_frame, _, _ = self.array_cells[index]
#         original_style = cell_frame.styleSheet()
        
#         # Create highlight animation
#         cell_frame.setStyleSheet("background-color: #4caf50; color: white; border-radius: 5px; border: 2px solid yellow;")
#         self.status_label.setText(f"Accessed element at index {index}: {self.array_values[index]}")
        
#         # Reset after a delay using a QTimer
#         from PySide6.QtCore import QTimer
#         QTimer.singleShot(1500, lambda: cell_frame.setStyleSheet(original_style))
    
#     def insert_element(self, index, value):
#         # Insert value into the array
#         self.array_values.insert(index, value)
        
#         # Recreate visualization
#         self.visualize_array()
        
#         # Highlight the inserted element
#         cell_frame, _, _ = self.array_cells[index]
#         cell_frame.setStyleSheet("background-color: #4caf50; color: white; border-radius: 5px; border: 2px solid yellow;")
        
#         self.status_label.setText(f"Inserted {value} at index {index}")
        
#         # Reset after a delay
#         from PySide6.QtCore import QTimer
#         QTimer.singleShot(1500, lambda: cell_frame.setStyleSheet("background-color: #4a90e2; color: white; border-radius: 5px;"))
    
#     def delete_element(self, index):
#         # Highlight the element to be deleted
#         cell_frame, _, _ = self.array_cells[index]
#         cell_frame.setStyleSheet("background-color: #e74c3c; color: white; border-radius: 5px;")
        
#         deleted_value = self.array_values[index]
        
#         # Update after a delay
#         from PySide6.QtCore import QTimer
#         QTimer.singleShot(1000, lambda: self._complete_deletion(index, deleted_value))
    
#     def _complete_deletion(self, index, deleted_value):
#         # Remove the element
#         self.array_values.pop(index)
        
#         # Update visualization
#         self.visualize_array()
        
#         self.status_label.setText(f"Deleted element {deleted_value} from index {index}")
    
#     def search_element(self, value):
#         found = False
        
#         # Sequential search animation
#         for i, (cell_frame, _, _) in enumerate(self.array_cells):
#             # Skip animation for simplicity, but in a real app you'd want to
#             # animate this to show the search process
#             if self.array_values[i] == value:
#                 cell_frame.setStyleSheet("background-color: #4caf50; color: white; border-radius: 5px; border: 2px solid yellow;")
#                 self.status_label.setText(f"Found {value} at index {i}")
#                 found = True
#                 break
        
#         if not found:
#             self.status_label.setText(f"Value {value} not found in the array")


# visualizer/structures/arrays.py
from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                              QPushButton, QLabel, QLineEdit, QComboBox, 
                              QGridLayout, QFrame, QMessageBox)
from PySide6.QtCore import Qt, QPropertyAnimation, QRect, QEasingCurve, QSequentialAnimationGroup, QTimer
from PySide6.QtGui import QFont
import random
import time

class ArrayVisualizer(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Configure window
        self.setWindowTitle("Array Visualizer")
        self.setMinimumSize(1000, 600)
        
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout(central_widget)
        
        # Add title
        title_label = QLabel("Array Visualization")
        title_font = QFont("Arial", 18, QFont.Bold)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)
        
        # Control panel
        control_panel = QWidget()
        control_layout = QHBoxLayout(control_panel)
        
        # Array size input
        size_layout = QHBoxLayout()
        size_label = QLabel("Size:")
        self.size_input = QLineEdit("10")
        self.size_input.setFixedWidth(50)
        create_button = QPushButton("Create Array")
        create_button.clicked.connect(self.create_array)
        
        size_layout.addWidget(size_label)
        size_layout.addWidget(self.size_input)
        size_layout.addWidget(create_button)
        size_layout.addStretch()
        
        # Operations
        operations_layout = QHBoxLayout()
        operations_label = QLabel("Operation:")
        self.operation_combo = QComboBox()
        self.operation_combo.addItems(["Access", "Insert", "Delete", "Search"])
        self.index_input = QLineEdit()
        self.index_input.setPlaceholderText("Index")
        self.index_input.setFixedWidth(80)
        self.value_input = QLineEdit()
        self.value_input.setPlaceholderText("Value")
        self.value_input.setFixedWidth(80)
        execute_button = QPushButton("Execute")
        execute_button.clicked.connect(self.execute_operation)
        
        operations_layout.addWidget(operations_label)
        operations_layout.addWidget(self.operation_combo)
        operations_layout.addWidget(self.index_input)
        operations_layout.addWidget(self.value_input)
        operations_layout.addWidget(execute_button)
        operations_layout.addStretch()
        
        # Add layouts to control panel
        control_layout.addLayout(size_layout)
        control_layout.addLayout(operations_layout)
        
        # Add control panel to main layout
        main_layout.addWidget(control_panel)
        
        # Add sorting panel
        sorting_panel = QWidget()
        sorting_layout = QHBoxLayout(sorting_panel)
        
        sorting_label = QLabel("Sorting:")
        self.sorting_combo = QComboBox()
        self.sorting_combo.addItems([
            "Bubble Sort", 
            "Selection Sort", 
            "Insertion Sort", 
            "Quick Sort", 
            "Merge Sort"
        ])
        
        sort_button = QPushButton("Sort Array")
        sort_button.clicked.connect(self.sort_array)
        
        self.speed_label = QLabel("Animation Speed:")
        self.speed_combo = QComboBox()
        self.speed_combo.addItems(["Slow", "Medium", "Fast"])
        self.speed_combo.setCurrentIndex(1)  # Default to Medium
        
        sorting_layout.addWidget(sorting_label)
        sorting_layout.addWidget(self.sorting_combo)
        sorting_layout.addWidget(sort_button)
        sorting_layout.addWidget(self.speed_label)
        sorting_layout.addWidget(self.speed_combo)
        sorting_layout.addStretch()
        
        main_layout.addWidget(sorting_panel)
        
        # Add separator
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        main_layout.addWidget(separator)
        
        # Visualization area
        self.visualization_widget = QWidget()
        self.visualization_layout = QHBoxLayout(self.visualization_widget)
        self.visualization_layout.setAlignment(Qt.AlignCenter)
        self.visualization_layout.setSpacing(2)
        
        main_layout.addWidget(self.visualization_widget)
        
        # Status area
        self.status_label = QLabel("Ready")
        self.status_label.setAlignment(Qt.AlignCenter)
        status_font = QFont("Arial", 12)
        self.status_label.setFont(status_font)
        main_layout.addWidget(self.status_label)
        
        # Algorithm explanation area
        self.explanation_label = QLabel("")
        self.explanation_label.setAlignment(Qt.AlignLeft)
        self.explanation_label.setWordWrap(True)
        main_layout.addWidget(self.explanation_label)
        
        # Back button
        back_button = QPushButton("Back to Main Menu")
        back_button.clicked.connect(self.close)
        main_layout.addWidget(back_button, alignment=Qt.AlignRight)
        
        # Initialize array
        self.array_cells = []
        self.array_values = []
        self.cell_size = 60
        self.is_sorting = False
        
    def create_array(self):
        try:
            size = int(self.size_input.text())
            if size <= 0 or size > 20:
                QMessageBox.warning(self, "Invalid Size", "Array size should be between 1 and 20.")
                return
                
            # Clear previous array
            self.clear_visualization()
            
            # Generate random values for array
            self.array_values = [random.randint(1, 99) for _ in range(size)]
            
            # Create visualization
            self.visualize_array()
            
            self.status_label.setText(f"Created array with {size} elements")
            self.explanation_label.setText("")
            
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Please enter a valid integer for array size.")
    
    def visualize_array(self):
        # Clear any existing visualization
        self.clear_visualization()
        
        # Create a cell for each array element
        for i, value in enumerate(self.array_values):
            cell_frame = QFrame()
            cell_frame.setFrameShape(QFrame.Box)
            cell_frame.setLineWidth(2)
            cell_frame.setFixedSize(self.cell_size, self.cell_size)
            cell_frame.setStyleSheet("background-color: #4a90e2; color: white; border-radius: 5px;")
            
            cell_layout = QVBoxLayout(cell_frame)
            
            # Value label
            value_label = QLabel(str(value))
            value_label.setAlignment(Qt.AlignCenter)
            value_label.setFont(QFont("Arial", 14, QFont.Bold))
            cell_layout.addWidget(value_label)
            
            # Index label
            index_label = QLabel(str(i))
            index_label.setAlignment(Qt.AlignCenter)
            index_label.setStyleSheet("color: rgba(255, 255, 255, 0.7);")
            cell_layout.addWidget(index_label)
            
            self.visualization_layout.addWidget(cell_frame)
            self.array_cells.append((cell_frame, value_label, index_label))
    
    def clear_visualization(self):
        # Remove all cells from layout
        while self.visualization_layout.count():
            item = self.visualization_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
        
        self.array_cells = []
    
    def execute_operation(self):
        if self.is_sorting:
            QMessageBox.warning(self, "Operation in Progress", "Please wait for the current sorting operation to finish.")
            return
            
        operation = self.operation_combo.currentText()
        
        try:
            index = int(self.index_input.text()) if self.index_input.text() else -1
            
            if operation != "Search" and (index < 0 or index >= len(self.array_values)):
                QMessageBox.warning(self, "Invalid Index", f"Index should be between 0 and {len(self.array_values)-1}.")
                return
                
            if operation == "Access":
                self.access_element(index)
            elif operation == "Insert":
                if not self.value_input.text():
                    QMessageBox.warning(self, "Missing Value", "Please enter a value to insert.")
                    return
                value = int(self.value_input.text())
                self.insert_element(index, value)
            elif operation == "Delete":
                self.delete_element(index)
            elif operation == "Search":
                if not self.value_input.text():
                    QMessageBox.warning(self, "Missing Value", "Please enter a value to search.")
                    return
                value = int(self.value_input.text())
                self.search_element(value)
                
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Please enter valid integers for index and value.")
    
    def access_element(self, index):
        # Highlight the accessed element
        cell_frame, _, _ = self.array_cells[index]
        original_style = cell_frame.styleSheet()
        
        # Create highlight animation
        cell_frame.setStyleSheet("background-color: #4caf50; color: white; border-radius: 5px; border: 2px solid yellow;")
        self.status_label.setText(f"Accessed element at index {index}: {self.array_values[index]}")
        
        # Reset after a delay using a QTimer
        QTimer.singleShot(1500, lambda: cell_frame.setStyleSheet(original_style))
    
    def insert_element(self, index, value):
        # Insert value into the array
        self.array_values.insert(index, value)
        
        # Recreate visualization
        self.visualize_array()
        
        # Highlight the inserted element
        cell_frame, _, _ = self.array_cells[index]
        cell_frame.setStyleSheet("background-color: #4caf50; color: white; border-radius: 5px; border: 2px solid yellow;")
        
        self.status_label.setText(f"Inserted {value} at index {index}")
        
        # Reset after a delay
        QTimer.singleShot(1500, lambda: cell_frame.setStyleSheet("background-color: #4a90e2; color: white; border-radius: 5px;"))
    
    def delete_element(self, index):
        # Highlight the element to be deleted
        cell_frame, _, _ = self.array_cells[index]
        cell_frame.setStyleSheet("background-color: #e74c3c; color: white; border-radius: 5px;")
        
        deleted_value = self.array_values[index]
        
        # Update after a delay
        QTimer.singleShot(1000, lambda: self._complete_deletion(index, deleted_value))
    
    def _complete_deletion(self, index, deleted_value):
        # Remove the element
        self.array_values.pop(index)
        
        # Update visualization
        self.visualize_array()
        
        self.status_label.setText(f"Deleted element {deleted_value} from index {index}")
    
    def search_element(self, value):
        found = False
        
        # Sequential search animation
        for i, (cell_frame, _, _) in enumerate(self.array_cells):
            # Skip animation for simplicity, but in a real app you'd want to
            # animate this to show the search process
            if self.array_values[i] == value:
                cell_frame.setStyleSheet("background-color: #4caf50; color: white; border-radius: 5px; border: 2px solid yellow;")
                self.status_label.setText(f"Found {value} at index {i}")
                found = True
                break
        
        if not found:
            self.status_label.setText(f"Value {value} not found in the array")
            
    def sort_array(self):
        if self.is_sorting:
            QMessageBox.warning(self, "Sorting in Progress", "Please wait for the current sorting operation to finish.")
            return
            
        if len(self.array_values) <= 1:
            QMessageBox.information(self, "Array Too Small", "Array needs at least 2 elements to sort.")
            return
            
        self.is_sorting = True
        self.status_label.setText("Sorting...")
        
        # Get the sorting algorithm and speed
        algorithm = self.sorting_combo.currentText()
        speed = self.speed_combo.currentText()
        
        # Set animation delay based on speed
        if speed == "Slow":
            delay = 1000  # 1 second
        elif speed == "Medium":
            delay = 500   # 0.5 seconds
        else:  # Fast
            delay = 200   # 0.2 seconds
            
        # Display algorithm description
        self.show_algorithm_explanation(algorithm)
        
        # Start sorting with a small delay
        QTimer.singleShot(500, lambda: self.start_sorting_algorithm(algorithm, delay))
        
    def start_sorting_algorithm(self, algorithm, delay):
        # Make a copy of the array for animation
        array_copy = self.array_values.copy()
        
        if algorithm == "Bubble Sort":
            self.animate_bubble_sort(array_copy, delay)
        elif algorithm == "Selection Sort":
            self.animate_selection_sort(array_copy, delay)
        elif algorithm == "Insertion Sort":
            self.animate_insertion_sort(array_copy, delay)
        elif algorithm == "Quick Sort":
            # For Quick Sort, we need to keep track of the original array for visualization
            self.animate_quick_sort(0, len(array_copy) - 1, array_copy, delay)
        elif algorithm == "Merge Sort":
            # For Merge Sort, we'll use a different approach
            self.animate_merge_sort(array_copy, 0, len(array_copy) - 1, delay)
            
    def show_algorithm_explanation(self, algorithm):
        explanations = {
            "Bubble Sort": "Bubble Sort: A simple comparison sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they're in the wrong order. The pass through the list is repeated until the list is sorted. Time complexity: O(n²) in worst and average case.",
            "Selection Sort": "Selection Sort: The algorithm divides the input list into two parts: a sorted sublist and an unsorted sublist. It repeatedly finds the minimum element from the unsorted sublist and puts it at the end of the sorted sublist. Time complexity: O(n²) in all cases.",
            "Insertion Sort": "Insertion Sort: Builds the final sorted array one item at a time. It takes one element from the input data in each iteration and finds the location it belongs to in the sorted list and inserts it there. Time complexity: O(n²) worst/average case, but efficient for small data sets.",
            "Quick Sort": "Quick Sort: A divide-and-conquer algorithm that picks an element as a pivot and partitions the array around the pivot. Different versions pick the pivot in different ways. Time complexity: O(n log n) on average, O(n²) worst case.",
            "Merge Sort": "Merge Sort: A divide-and-conquer algorithm that divides the input array into two halves, recursively sorts them, and finally merges the two sorted halves. Time complexity: O(n log n) in all cases, but requires additional O(n) space."
        }
        
        self.explanation_label.setText(explanations.get(algorithm, ""))
        
    def animate_bubble_sort(self, arr, delay):
        n = len(arr)
        
        # Function to perform one step of bubble sort and update visualization
        def bubble_step(i, j, swapped):
            if j < n - i - 1:
                # Highlight elements being compared
                self.highlight_cells([j, j+1], "#ff9800")  # Orange for comparison
                
                if arr[j] > arr[j+1]:
                    # Swap elements
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    # Update values in array_values
                    self.array_values[j], self.array_values[j+1] = self.array_values[j+1], self.array_values[j]
                    # Update cell labels
                    self.update_cell_values()
                    
                    # Highlight swapped elements
                    self.highlight_cells([j, j+1], "#e91e63")  # Pink for swap
                    swapped = True
                
                # Continue with next comparison
                QTimer.singleShot(delay, lambda: bubble_step(i, j+1, swapped))
            elif i < n - 1:
                # Highlight settled element
                self.highlight_cells([n-i-1], "#4caf50")  # Green for settled
                
                # Move to next pass if swapped occurred
                if swapped:
                    QTimer.singleShot(delay, lambda: bubble_step(i+1, 0, False))
                else:
                    # Array is sorted
                    self.finalize_sorting()
            else:
                # Sorting completed
                self.finalize_sorting()
        
        # Start the first step
        bubble_step(0, 0, False)
        
    def animate_selection_sort(self, arr, delay):
        n = len(arr)
        
        def selection_step(i):
            if i < n - 1:
                # Find the minimum element in unsorted array
                min_idx = i
                
                def find_min(j, min_idx):
                    if j < n:
                        # Highlight current element being examined
                        self.highlight_cells([j], "#ff9800")  # Orange for comparison
                        
                        if arr[j] < arr[min_idx]:
                            # Update min_idx if smaller element found
                            if min_idx != i:  # Reset previous min
                                self.highlight_cells([min_idx], "#4a90e2")  # Back to blue
                            min_idx = j
                            # Highlight new minimum
                            self.highlight_cells([min_idx], "#e91e63")  # Pink for current min
                        
                        # Continue searching for minimum
                        QTimer.singleShot(delay, lambda: find_min(j+1, min_idx))
                    else:
                        # Found minimum, perform swap
                        if min_idx != i:
                            # Swap the found minimum element with the first element
                            arr[i], arr[min_idx] = arr[min_idx], arr[i]
                            self.array_values[i], self.array_values[min_idx] = self.array_values[min_idx], self.array_values[i]
                            self.update_cell_values()
                            
                            # Highlight the swap
                            self.highlight_cells([i, min_idx], "#e91e63")  # Pink for swap
                        
                        # Mark current position as sorted
                        QTimer.singleShot(delay, lambda: self.highlight_cells([i], "#4caf50"))  # Green for sorted
                        
                        # Move to next position
                        QTimer.singleShot(delay * 2, lambda: selection_step(i+1))
                
                # Start finding minimum
                find_min(i+1, min_idx)
            else:
                # Mark last element as sorted
                self.highlight_cells([n-1], "#4caf50")  # Green for sorted
                # Sorting completed
                self.finalize_sorting()
        
        # Start the first step
        selection_step(0)
        
    def animate_insertion_sort(self, arr, delay):
        n = len(arr)
        
        def insertion_step(i):
            if i < n:
                # Highlight current element to be inserted
                self.highlight_cells([i], "#ff9800")  # Orange for current key
                key = arr[i]
                j = i - 1
                
                def insert_key(j, key):
                    if j >= 0 and arr[j] > key:
                        # Highlight element being compared
                        self.highlight_cells([j], "#e91e63")  # Pink for comparison
                        
                        # Move elements greater than key to one position ahead
                        arr[j+1] = arr[j]
                        self.array_values[j+1] = self.array_values[j]
                        self.update_cell_values()
                        
                        # Continue moving back
                        QTimer.singleShot(delay, lambda: insert_key(j-1, key))
                    else:
                        # Found insertion point, insert key
                        arr[j+1] = key
                        self.array_values[j+1] = key
                        self.update_cell_values()
                        
                        # Highlight sorted portion
                        sorted_indices = list(range(i+1))
                        self.highlight_cells(sorted_indices, "#4caf50")  # Green for sorted portion
                        
                        # Move to next element
                        QTimer.singleShot(delay, lambda: insertion_step(i+1))
                
                # Start inserting key
                QTimer.singleShot(delay, lambda: insert_key(j, key))
            else:
                # Sorting completed
                self.finalize_sorting()
        
        # Start the first step
        insertion_step(1)  # Start from second element
        
    def animate_quick_sort(self, low, high, arr, delay):
        # Use a class-level variable to track if this is the initial call
        if not hasattr(self, '_quicksort_initial_bounds'):
            self._quicksort_initial_bounds = (low, high)
            self._quicksort_active_regions = set()
            print(f"Initial quicksort call: {low}-{high}")
        
        # Register this region
        region_id = f"{low}-{high}"
        self._quicksort_active_regions.add(region_id)
        print(f"Added region {region_id}, active regions: {self._quicksort_active_regions}")
        
        def partition_and_continue():
            # If no elements to sort
            if low >= high:
                print(f"Base case for region {region_id}")
                # Remove this region
                self._quicksort_active_regions.discard(region_id)
                check_if_complete()
                return
            
            # Highlight the pivot
            self.highlight_cells([high], "#ff9800")  # Orange for pivot
            
            # Partition the array
            pivot = arr[high]
            i = low - 1
            
            def run_partition(j):
                nonlocal i
                
                if j <= high - 1:
                    # Highlight current element being compared
                    self.highlight_cells([j], "#e91e63")  # Pink for comparison
                    
                    if arr[j] <= pivot:
                        # Increment index of smaller element
                        i += 1
                        
                        # Swap if needed
                        if i != j:
                            arr[i], arr[j] = arr[j], arr[i]
                            self.array_values[i], self.array_values[j] = self.array_values[j], self.array_values[i]
                            self.update_cell_values()
                            
                            # Highlight swapped elements
                            self.highlight_cells([i, j], "#9c27b0")  # Purple for swap
                    
                    # Continue to next element
                    QTimer.singleShot(delay, lambda: run_partition(j+1))
                else:
                    # Place pivot in correct position
                    if i + 1 != high:
                        arr[i+1], arr[high] = arr[high], arr[i+1]
                        self.array_values[i+1], self.array_values[high] = self.array_values[high], self.array_values[i+1]
                        self.update_cell_values()
                        
                        # Highlight final pivot position
                        self.highlight_cells([i+1], "#4caf50")  # Green for final pivot position
                    
                    pivot_index = i + 1
                    
                    # Remove current region from active list
                    self._quicksort_active_regions.discard(region_id)
                    print(f"Completed region {region_id}")
                    
                    # Schedule left subarray if needed
                    if low < pivot_index - 1:
                        QTimer.singleShot(delay, lambda: self.animate_quick_sort(low, pivot_index - 1, arr, delay))
                    
                    # Schedule right subarray if needed
                    if pivot_index + 1 < high:
                        QTimer.singleShot(delay, lambda: self.animate_quick_sort(pivot_index + 1, high, arr, delay))
                    
                    # Check if we're done - in case no new regions were scheduled
                    if low >= pivot_index - 1 and pivot_index + 1 >= high:
                        check_if_complete()
            
            # Start partition
            run_partition(low)
        
        def check_if_complete():
            print(f"Checking if complete. Initial bounds: {self._quicksort_initial_bounds}")
            print(f"Active regions: {self._quicksort_active_regions}")
            
            # If no more regions to process, we're done!
            if not self._quicksort_active_regions:
                print("All sorting completed!")
                # Clean up tracking variables
                initial_bounds = self._quicksort_initial_bounds
                delattr(self, '_quicksort_initial_bounds')
                delattr(self, '_quicksort_active_regions')
                
                # Call finalize_sorting with a small delay to ensure UI updates are complete
                QTimer.singleShot(10, self.finalize_sorting)
        
        # Start the sorting process
        partition_and_continue()

    def animate_merge_sort(self, arr, left, right, delay):
        # For the initial call, set up tracking
        if not hasattr(self, '_merge_sort_initial'):
            self._merge_sort_initial = True
            self._merge_temp = arr.copy()
            self._merge_active_operations = 0
            print(f"Starting merge sort on range {left}-{right}")
        
        # Increment active operations counter
        self._merge_active_operations += 1
        
        def merge_sort_step():
            # Base case: Single element is already sorted
            if left >= right:
                self._merge_active_operations -= 1
                check_if_complete()
                return
            
            # Find the middle point
            mid = (left + right) // 2
            
            # Highlight current range being processed
            indices = list(range(left, right + 1))
            self.highlight_cells(indices, "#ff9800")  # Orange for current range
            
            # Schedule left and right subarrays with a delay
            QTimer.singleShot(delay, lambda: self.animate_merge_sort(arr, left, mid, delay))
            QTimer.singleShot(delay * 2, lambda: self.animate_merge_sort(arr, mid + 1, right, delay))
            
            # Schedule the merge operation to happen after both subarrays are sorted
            QTimer.singleShot(delay * 3, lambda: merge_subarrays())
        
        def merge_subarrays():
            mid = (left + right) // 2
            
            # Copy data to temp array
            for i in range(left, right + 1):
                self._merge_temp[i] = arr[i]
            
            # Set up initial indices
            i = left      # Initial index of first subarray
            j = mid + 1   # Initial index of second subarray
            k = left      # Initial index of merged subarray
            
            def merge_step():
                nonlocal i, j, k
                
                if i <= mid and j <= right:
                    # Highlight elements being compared
                    self.highlight_cells([i, j], "#e91e63")  # Pink for comparison
                    
                    if self._merge_temp[i] <= self._merge_temp[j]:
                        arr[k] = self._merge_temp[i]
                        self.array_values[k] = self._merge_temp[i]
                        i += 1
                    else:
                        arr[k] = self._merge_temp[j]
                        self.array_values[k] = self._merge_temp[j]
                        j += 1
                    
                    # Update visualization
                    self.update_cell_values()
                    self.highlight_cells([k], "#4caf50")  # Green for merged position
                    
                    k += 1
                    # Continue merging
                    QTimer.singleShot(delay // 2, merge_step)
                    
                elif i <= mid:
                    # Copy remaining elements of left subarray
                    arr[k] = self._merge_temp[i]
                    self.array_values[k] = self._merge_temp[i]
                    self.update_cell_values()
                    self.highlight_cells([k], "#4caf50")
                    
                    i += 1
                    k += 1
                    
                    # Continue copying
                    QTimer.singleShot(delay // 2, merge_step)
                    
                elif j <= right:
                    # Copy remaining elements of right subarray
                    arr[k] = self._merge_temp[j]
                    self.array_values[k] = self._merge_temp[j]
                    self.update_cell_values()
                    self.highlight_cells([k], "#4caf50")
                    
                    j += 1
                    k += 1
                    
                    # Continue copying
                    QTimer.singleShot(delay // 2, merge_step)
                    
                else:
                    # This merge is complete
                    self._merge_active_operations -= 1
                    check_if_complete()
            
            # Start the merge process
            merge_step()
        
        def check_if_complete():
            if hasattr(self, '_merge_active_operations') and self._merge_active_operations == 0:
                # We're done! The entire array is sorted
                if hasattr(self, '_merge_sort_initial'):
                    print("Merge sort completed!")
                    # Clean up tracking variables
                    delattr(self, '_merge_sort_initial')
                    delattr(self, '_merge_temp')
                    delattr(self, '_merge_active_operations')
                    
                    # Call finalize_sorting with a delay
                    QTimer.singleShot(delay, self.finalize_sorting)
        
        # Start the merge sort process
        merge_sort_step()


    def highlight_cells(self, indices, color):
        # Reset all cells to default color
        for cell_frame, _, _ in self.array_cells:
            cell_frame.setStyleSheet("background-color: #4a90e2; color: white; border-radius: 5px;")
        
        # Highlight specified cells
        for idx in indices:
            if 0 <= idx < len(self.array_cells):
                cell_frame, _, _ = self.array_cells[idx]
                cell_frame.setStyleSheet(f"background-color: {color}; color: white; border-radius: 5px;")
     
    def update_cell_values(self):
        # Update the displayed values in cells
        for i, (_, value_label, _) in enumerate(self.array_cells):
            if i < len(self.array_values):
                value_label.setText(str(self.array_values[i]))
    
    def finalize_sorting(self):

        print("finalize_sorting called")
        # Mark all cells as sorted
        for cell_frame, _, _ in self.array_cells:
            cell_frame.setStyleSheet("background-color: #4caf50; color: white; border-radius: 5px;")
        
        self.status_label.setText("Sorting completed!")
        self.is_sorting = False
        
        # Reset all cells to default after a delay
        QTimer.singleShot(2000, lambda: self.reset_cell_styles())
    
    def reset_cell_styles(self):
        for cell_frame, _, _ in self.array_cells:
            cell_frame.setStyleSheet("background-color: #4a90e2; color: white; border-radius: 5px;")