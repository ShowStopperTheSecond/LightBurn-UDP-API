# This Python file uses the following encoding: utf-8
import sys
import socket
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from PySide6.QtCore import QTimer
from ui_form import Ui_Widget  # Assuming you've generated this from form.ui

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        # Set default values
        self.ui.ip_txt.setText("127.0.0.1")
        self.ui.out_port_txt.setText("19840")
        self.ui.in_port_txt.setText("19841")

        # Initialize sockets
        self.outSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.inSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.inSock.settimeout(2.0)  # Set timeout for receiving

        # Connect signals
        self.ui.browse_file_btn.clicked.connect(self.browse_file)
        self.ui.bind_btn.clicked.connect(self.bind_socket)
        self.ui.load_file_btn.clicked.connect(self.send_load)
        self.ui.force_load_file_btn.clicked.connect(self.send_force_load)
        self.ui.close_btn.clicked.connect(self.send_close)
        self.ui.force_close_btn.clicked.connect(self.send_force_close)
        self.ui.start_btn.clicked.connect(self.send_start)
        self.ui.status_btn.clicked.connect(self.send_status)
        self.ui.ping_btn.clicked.connect(self.send_ping)

        self.bound = False  # Track binding status

    def browse_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Select a File", "", "All Files (*)")
        if filename:
            # Convert to Windows-style path if needed
            self.ui.lineEdit.setText(filename.replace("/", "\\"))

    def bind_socket(self):
        ip_address = self.ui.ip_txt.text()
        port = self.ui.in_port_txt.text()

        try:
            # Close existing socket if bound
            if self.bound:
                self.inSock.close()
                self.inSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                self.inSock.settimeout(2.0)

            self.inSock.bind((ip_address, int(port)))
            self.bound = True
            QMessageBox.information(self, "Success", f"Socket bound to {ip_address}:{port}")
        except socket.error as e:
            QMessageBox.critical(self, "Socket Error", f"Failed to bind socket: {e}")
            self.bound = False

    def send_command(self, command, expects_response=True):

        if not self.bound and expects_response:
            QMessageBox.warning(self, "Warning", "Receive socket not bound. Binding to default port.")
            try:
                self.inSock.bind(("127.0.0.1", 19841))
                self.bound = True
            except socket.error as e:
                QMessageBox.critical(self, "Error", f"Auto-bind failed: {e}")
                return

        ip_address = self.ui.ip_txt.text()
        out_port = int(self.ui.out_port_txt.text())

        try:
            # Send command
            self.outSock.sendto(command.encode(), (ip_address, out_port))

            # Receive response if expected
            if expects_response:
                try:
                    data, addr = self.inSock.recvfrom(1024)
                    self.ui.status_lbl.setText(f"Received from {addr[0]}:{addr[1]}:  {data.decode()}")
                    # QMessageBox.information(self, "Response",
                    #                        f"Received from {addr[0]}:{addr[1]}:\n{data.decode()}")
                except socket.timeout:
                    QMessageBox.warning(self, "Timeout", "No response received")
            else:
                QMessageBox.information(self, "Success", "Command sent successfully")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to send/receive: {e}")

    # Command-specific methods
    def send_load(self):
        file_path = self.ui.lineEdit.text()
        if not file_path:
            QMessageBox.warning(self, "Warning", "Please select a file first")
            return
        self.send_command(f"LOADFILE:{file_path}")

    def send_force_load(self):
        file_path = self.ui.lineEdit.text()
        if not file_path:
            QMessageBox.warning(self, "Warning", "Please select a file first")
            return
        self.send_command(f"FORCELOAD:{file_path}")

    def send_close(self):
        self.send_command("CLOSE")

    def send_force_close(self):
        self.send_command("FORCECLOSE")

    def send_start(self):
        self.send_command("START")

    def send_status(self):
        self.send_command("STATUS")

    def send_ping(self):
        self.send_command("PING")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
