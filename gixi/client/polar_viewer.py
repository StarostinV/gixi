import numpy as np
from PyQt5.QtCore import pyqtSlot

from .basic_widgets import Viewer2D
from .rois import Roi2DRect


class PolarViewer(Viewer2D):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._rois = []

    @pyqtSlot(object)
    def set_image(self, img):
        self.remove_rois()
        self.set_data(img)

    @pyqtSlot(object)
    def set_rois(self, boxes: np.ndarray):
        if self.image is None:
            return
        self.remove_rois()

        for box in boxes:
            self._rois.append(self._add_roi(box))

    def remove_rois(self):
        while self._rois:
            self.image_plot.removeItem(self._rois.pop())

    def _add_roi(self, box: np.ndarray):
        roi_widget = Roi2DRect()
        roi_widget.set_box(box, self.image.shape)
        self.image_plot.addItem(roi_widget)
        return roi_widget
