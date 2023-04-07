from PySide.QtCore import Signal, QObject

class GuiSignals(QObject):
    materialsChanged = Signal(str)
    portsChanged = Signal(str)

    gridRenamed = Signal(str, str)
    materialRenamed = Signal(str, str)
    excitationRenamed = Signal(str, str)
    portRenamed = Signal(str, str)
    lumpedPartRenamed = Signal(str, str)

