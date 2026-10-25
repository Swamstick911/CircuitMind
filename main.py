import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QPainter
from PySide6.QtWidgets import (
    QApplication,
    QDockWidget,
    QGraphicsScene,
    QGraphicsView,
    QLabel,
    QMainWindow,
    QToolBar,
)

class CircuitMindWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CircuitMind")
        self.resize(1200, 780)

        self.scene = QGraphicsScene(self)
        self.scene.setSceneRect(-2000, -2000, 4000, 4000)
        self.scene.setBackgroundBrush(Qt.GlobalColor.white)

        self.view = QGraphicsView(self.scene)
        self.view.setRenderHint(QPainter.RenderHint.Antialising)
        self.view.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)
        self.setCentralWidget(self.view)

        self.create_toolbar()
        self.create_feedback_panel()

        self.scene.addText("Welcome to CircuitMind! your circuit workspace").setPos(
            -160, -30
        )
        self.view.centerOn(0, 0)

        self.statusBar().showMessage(
            "Workspace ready. Drag the canvas to pan"
        )

    def create_toolbar(self):
        toolbar = QToolBar("Circuit Tools", self)
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        for name in ("Battery", "Resistor", "LED", "Switch"):
            action = QAction(f"+ {name}", self)
            action.triggered.connect(
                lambda checked=False, component=name:
                self.show_component_placeholder(component)
            )
            toolbar.addAction(action)

        toolbar.addSeparator()

        run_action = QAction("Run Check", self)
        run_action.triggered.connect(self.run_check)
        toolbar.addAction(run_action)

    def create_feedback_panel(self):
        dock = QDockWidget("Circuit Feedback", self)
        dock.setAllowedAreas(Qt.DockWidgetArea.LeftDockWidgetArea | Qt.DockWdigetArea.RightDockWidgetArea)

        self.feedback = QLabel(
            "Welcome to CircuitMind!\n\n" 
            "This first build checks that the desktop interface works\n\n"
        )
        self.feedback.setWordWrap(True)
        self.feedback.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        self.feedback.setMargin(16)
        self.feedback.setMinimumWidth(260)

        dock.setWidget(self.feedback)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, dock)

    def show_component_placeholder(self, component):
        self.feedback.setText(
            f"{component} tool selected.\n\n"
            "Component placement is not yet implemented in this build"
        )
        self.statusBar().showMessage(f"Selected: {component}")

    def run_check(self):
        self.feedback.setText(
            "Circuit checking is not implemented yet.\n\n"
            "First we will add components and wires, then connect "
            "the editor to the diagnostic engine"
        )

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("CircuitMind")
    app.setStyle("Fusion")

    window = CircuitMindWindow()
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()