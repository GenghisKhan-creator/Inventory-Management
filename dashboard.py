import sys
from datetime import datetime
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QPushButton, QLabel, QFrame, QGridLayout)
from PyQt6.QtGui import QFont, QIcon, QPixmap
from PyQt6.QtCore import Qt, QTimer, QDateTime, QSize


class InventorySystem(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BussiBee - Inventory Management System")
        self.setWindowIcon(QIcon("icons/inventory logo.png"))
        self.setMinimumSize(1200, 800)

        # Main layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QHBoxLayout(main_widget)

        # Sidebar
        sidebar = self.create_sidebar()
        layout.addWidget(sidebar)

        # Main content
        main_content = QWidget()
        main_content.setStyleSheet("background-color: #e5e7eb;")
        main_layout = QVBoxLayout(main_content)

        # Header
        header = self.create_header()
        main_layout.addWidget(header)

        # Dashboard content
        dashboard = self.create_dashboard()
        main_layout.addWidget(dashboard)

        layout.addWidget(main_content)

        # Start timer for updating date/time
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_datetime)
        self.timer.start(1000)

    from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
    from PyQt6.QtGui import QIcon, QPixmap
    from PyQt6.QtCore import Qt, QSize

    def create_sidebar(self):
        sidebar = QWidget()
        sidebar.setStyleSheet("background-color: white; min-width: 250px; max-width: 250px;")
        layout = QVBoxLayout(sidebar)

        # Logo as image
        logo_label = QLabel()
        logo_pixmap = QPixmap("icons/inventory logo.png")
        scaled_pixmap = logo_pixmap.scaled(300, 240, Qt.AspectRatioMode.KeepAspectRatio,
                                           Qt.TransformationMode.SmoothTransformation)
        logo_label.setPixmap(scaled_pixmap)
        logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        logo_label.setStyleSheet("padding: 10px 0; margin-right: 40px; margin-bottom: 20px;")
        layout.addWidget(logo_label)

        # Menu items with icons and click handlers
        menu_items = [
            ("Dashboard", "icons/use.png", self.handle_dashboard_click, "active"),
            ("Employees", "icons/employee.png", self.handle_employees_click, ""),
            ("Suppliers", "icons/supplier.png", self.handle_suppliers_click, ""),
            ("Category", "icons/category.png", self.handle_category_click, ""),
            ("Products", "icons/products.png", self.handle_products_click, ""),
            ("Sales", "icons/sales.png", self.handle_sales_click, ""),
            ("Reports", "icons/report.png", self.handle_reports_click, "")
        ]

        self.buttons = {}  # Store buttons to manage active state

        for text, icon_path, handler, state in menu_items:
            btn = QPushButton(text)
            btn.setIcon(QIcon(icon_path))
            btn.setIconSize(QSize(30, 30))

            base_style = """
                QPushButton {
                    text-align: left;
                    padding: 10px 10px 10px 35px;
                    border-top-left-radius: 17px;
                    border-bottom-left-radius: 17px;
                    border: none;
                    height: 20px;
                }
                QPushButton:hover {
                    background-color: #1b4d3e;
                    color: white;
                    height: 20px;
                }
                QPushButton::icon { margin-right: 10px;}
            """

            if state == "active":
                btn.setStyleSheet(base_style + """
                    QPushButton {
                        background-color: #1b4d3e;
                        color: white;
                    }
                """)
            else:
                btn.setStyleSheet(base_style + """
                    QPushButton {
                        background-color: white;
                        color: black;
                    }
                """)

            btn.clicked.connect(handler)
            self.buttons[text] = btn
            layout.addWidget(btn)

        layout.addStretch()

        # Logout button with icon
        logout_btn = QPushButton("Logout")
        logout_btn.setIcon(QIcon("icons/icons8-logout-96.png"))
        logout_btn.setIconSize(QSize(30, 30))
        logout_btn.setStyleSheet("""
            QPushButton {
                text-align: left;
                padding: 10px 10px 10px 35px;
                background-color: #1b4d3e;
                border-top-left-radius: 17px;
                border-bottom-left-radius: 17px;
                color: white;
                border: none;
                height: 20px;
            }
        """)
        logout_btn.clicked.connect(self.handle_logout_click)
        layout.addWidget(logout_btn)

        return sidebar

    def set_active_button(self, button_text):
        for text, btn in self.buttons.items():
            if text == button_text:
                btn.setStyleSheet(
                    btn.styleSheet().replace("background-color: white;", "background-color: #1b4d3e; color: white;"))
            else:
                btn.setStyleSheet(btn.styleSheet().replace("background-color: #1b4d3e; color: white;",
                                                           "background-color: white; color: black;"))

    def handle_dashboard_click(self):
        self.set_active_button("Dashboard")
        print("Dashboard clicked")
        # Add your dashboard logic here

    def handle_employees_click(self):
        self.set_active_button("Employees")
        print("Employees clicked")
        # Add your employees logic here

    def handle_suppliers_click(self):
        self.set_active_button("Suppliers")
        print("Suppliers clicked")
        # Add your suppliers logic here

    def handle_category_click(self):
        self.set_active_button("Category")
        print("Category clicked")
        # Add your category logic here

    def handle_products_click(self):
        self.set_active_button("Products")
        print("Products clicked")
        # Add your products logic here

    def handle_sales_click(self):
        self.set_active_button("Sales")
        print("Sales clicked")
        # Add your sales logic here

    def handle_reports_click(self):
        self.set_active_button("Reports")
        print("Reports clicked")
        # Add your reports logic here

    def handle_logout_click(self):
        print("Logout clicked")
        # Add your logout logic here

    def create_header(self):
        header = QWidget()
        header.setStyleSheet("background-color: white; padding: 10px; border-bottom-left-radius: 25px; border-top-right-radius: 25px;")
        layout = QHBoxLayout(header)

        # Left side - Title
        title_layout = QVBoxLayout()
        current_for_greeting = QDateTime.currentDateTime()
        time_day = current_for_greeting.toString("AP")
        if time_day == "AM":
            greeting = QLabel("Good Morning ⚡")
            greeting.setStyleSheet("font-size: 28px; font-weight: 800; color: #203e3a;")
            title_layout.addWidget(greeting)
        else:
            greeting = QLabel("Good Afternoon")
            greeting.setStyleSheet("font-size: 28px; font-weight: 800; color: #203e3a;")
            title_layout.addWidget(greeting)

        # Middle row with subtitle, date, and time
        middle_row = QHBoxLayout()
        subtitle = QLabel("BUSSI BEE INVENTORY MANAGEMENT SYSTEM")
        subtitle.setStyleSheet("font-size: 15px; color: #203e3a; font-weight: 700;")
        self.date_label = QLabel()
        self.date_label.setStyleSheet("font-size: 15px; color: #203e3a; font-weight: 700;")
        self.time_label = QLabel()
        self.time_label.setStyleSheet("font-size: 15px; color: #203e3a; font-weight: 700;")

        # Update time format to include AM/PM
        def update_datetime():
            current_datetime = QDateTime.currentDateTime()
            self.date_label.setText(f'DATE: {current_datetime.toString("MMM d, yyyy")}')
            self.time_label.setText(f'TIME: {current_datetime.toString("hh:mm:ss AP")}')  # AP adds AM/PM

        # Create timer to update every second
        timer = QTimer(self)
        timer.timeout.connect(update_datetime)
        timer.start(1000)  # Update every 1000ms (1 second)

        # Initial update
        update_datetime()

        middle_row.addWidget(subtitle)
        middle_row.addStretch()  # This pushes date/time to the right
        middle_row.addWidget(self.date_label)
        middle_row.addWidget(self.time_label)

        # Add middle row to title layout
        title_layout.addLayout(middle_row)

        # Right side - Admin only
        right_layout = QHBoxLayout()
        admin_label = QLabel("Admin")
        right_layout.addWidget(admin_label)

        # Add all layouts to main layout
        layout.addLayout(title_layout)
        layout.addStretch()
        layout.addLayout(right_layout)

        return header

    def create_dashboard(self):
        dashboard = QWidget()
        layout = QVBoxLayout(dashboard)

        # Stats grid using QGridLayout instead of QHBoxLayout
        stats_layout = QGridLayout()

        # Total Sales
        sales_card = self.create_stat_card(
            "₵500,000.00",
            "Total Sales",
            "background-color: #1b4d3e; color: white;"
        )

        # Total Employees
        employees_card = self.create_stat_card(
            "5000",
            "Total Employee",
            "background-color: white;"
        )

        # Total Categories
        categories_card = self.create_stat_card(
            "500",
            "Total Categories",
            "background-color: white;"
        )

        # Total Products
        products_card = self.create_stat_card(
            "59",
            "Total Products",
            "background-color: white;"
        )

        # Add widgets to grid layout
        # First row
        stats_layout.addWidget(sales_card, 0, 0)  # Row 0, Column 0
        stats_layout.addWidget(employees_card, 0, 1)  # Row 0, Column 1

        # Second row
        stats_layout.addWidget(categories_card, 1, 0)  # Row 1, Column 0
        stats_layout.addWidget(products_card, 1, 1)  # Row 1, Column 1

        # Set column and row stretch factors to ensure equal sizing
        stats_layout.setColumnStretch(0, 1)
        stats_layout.setColumnStretch(1, 1)
        stats_layout.setRowStretch(0, 1)
        stats_layout.setRowStretch(1, 1)

        # Add some spacing between cards
        stats_layout.setHorizontalSpacing(10)
        stats_layout.setVerticalSpacing(10)

        layout.addLayout(stats_layout)
        layout.addStretch()

        return dashboard

    def create_stat_card(self, number, label, style):
        card = QFrame()
        card.setStyleSheet(f"""
            QFrame {{
                border-radius: 10px;
                padding: 20px;
                height: 100px;
                {style}
            }}
        """)
        layout = QVBoxLayout(card)

        number_label = QLabel(number)
        number_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        label = QLabel(label)

        layout.addWidget(number_label)
        layout.addWidget(label)

        return card

    def update_datetime(self):
        current = datetime.now()
        self.date_label.setText(f"DATE: {current.strftime("MMM d, yyyy")}")
        self.time_label.setText(f"TIME: {current.strftime('%H:%M:%S AP')}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = InventorySystem()
    window.show()
    sys.exit(app.exec())