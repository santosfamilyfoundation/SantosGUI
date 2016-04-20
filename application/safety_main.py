# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'safety_main.ui'
#
# Created: Wed Apr 20 12:49:37 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_TransportationSafety(object):
    def setupUi(self, TransportationSafety):
        TransportationSafety.setObjectName(_fromUtf8("TransportationSafety"))
        TransportationSafety.resize(1129, 808)
        self.centralWidget = QtGui.QWidget(TransportationSafety)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralWidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.main_tab_widget = QtGui.QTabWidget(self.centralWidget)
        self.main_tab_widget.setAcceptDrops(False)
        self.main_tab_widget.setAutoFillBackground(False)
        self.main_tab_widget.setTabShape(QtGui.QTabWidget.Rounded)
        self.main_tab_widget.setElideMode(QtCore.Qt.ElideNone)
        self.main_tab_widget.setTabsClosable(False)
        self.main_tab_widget.setObjectName(_fromUtf8("main_tab_widget"))
        self.tab_homography = QtGui.QWidget()
        self.tab_homography.setObjectName(_fromUtf8("tab_homography"))
        self.verticalLayout = QtGui.QVBoxLayout(self.tab_homography)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.control_box = QtGui.QFrame(self.tab_homography)
        self.control_box.setMinimumSize(QtCore.QSize(0, 40))
        self.control_box.setFrameShape(QtGui.QFrame.StyledPanel)
        self.control_box.setFrameShadow(QtGui.QFrame.Raised)
        self.control_box.setObjectName(_fromUtf8("control_box"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.control_box)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.open_buttons = QtGui.QHBoxLayout()
        self.open_buttons.setObjectName(_fromUtf8("open_buttons"))
        self.homography_button_open_camera_image = QtGui.QPushButton(self.control_box)
        self.homography_button_open_camera_image.setObjectName(_fromUtf8("homography_button_open_camera_image"))
        self.open_buttons.addWidget(self.homography_button_open_camera_image)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.open_buttons.addItem(spacerItem)
        self.homography_button_open_aerial_image = QtGui.QPushButton(self.control_box)
        self.homography_button_open_aerial_image.setObjectName(_fromUtf8("homography_button_open_aerial_image"))
        self.open_buttons.addWidget(self.homography_button_open_aerial_image)
        self.verticalLayout_4.addLayout(self.open_buttons)
        self.zoom_sliders = QtGui.QHBoxLayout()
        self.zoom_sliders.setObjectName(_fromUtf8("zoom_sliders"))
        self.homography_label_zoom_camera_image = QtGui.QLabel(self.control_box)
        self.homography_label_zoom_camera_image.setObjectName(_fromUtf8("homography_label_zoom_camera_image"))
        self.zoom_sliders.addWidget(self.homography_label_zoom_camera_image)
        self.homography_hslider_zoom_camera_image = ZoomSlider(self.control_box)
        self.homography_hslider_zoom_camera_image.setMinimum(10)
        self.homography_hslider_zoom_camera_image.setMaximum(400)
        self.homography_hslider_zoom_camera_image.setPageStep(25)
        self.homography_hslider_zoom_camera_image.setProperty("value", 100)
        self.homography_hslider_zoom_camera_image.setOrientation(QtCore.Qt.Horizontal)
        self.homography_hslider_zoom_camera_image.setTickPosition(QtGui.QSlider.NoTicks)
        self.homography_hslider_zoom_camera_image.setTickInterval(0)
        self.homography_hslider_zoom_camera_image.setObjectName(_fromUtf8("homography_hslider_zoom_camera_image"))
        self.zoom_sliders.addWidget(self.homography_hslider_zoom_camera_image)
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.zoom_sliders.addItem(spacerItem1)
        self.homography_label_zoom_computed_image = QtGui.QLabel(self.control_box)
        self.homography_label_zoom_computed_image.setObjectName(_fromUtf8("homography_label_zoom_computed_image"))
        self.zoom_sliders.addWidget(self.homography_label_zoom_computed_image)
        self.homography_hslider_zoom_computed_image = ZoomSlider(self.control_box)
        self.homography_hslider_zoom_computed_image.setMinimum(10)
        self.homography_hslider_zoom_computed_image.setMaximum(400)
        self.homography_hslider_zoom_computed_image.setPageStep(25)
        self.homography_hslider_zoom_computed_image.setProperty("value", 100)
        self.homography_hslider_zoom_computed_image.setOrientation(QtCore.Qt.Horizontal)
        self.homography_hslider_zoom_computed_image.setObjectName(_fromUtf8("homography_hslider_zoom_computed_image"))
        self.zoom_sliders.addWidget(self.homography_hslider_zoom_computed_image)
        spacerItem2 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.zoom_sliders.addItem(spacerItem2)
        self.homography_label_zoom_aerial_image = QtGui.QLabel(self.control_box)
        self.homography_label_zoom_aerial_image.setObjectName(_fromUtf8("homography_label_zoom_aerial_image"))
        self.zoom_sliders.addWidget(self.homography_label_zoom_aerial_image)
        self.homography_hslider_zoom_aerial_image = ZoomSlider(self.control_box)
        self.homography_hslider_zoom_aerial_image.setMinimum(10)
        self.homography_hslider_zoom_aerial_image.setMaximum(400)
        self.homography_hslider_zoom_aerial_image.setPageStep(25)
        self.homography_hslider_zoom_aerial_image.setProperty("value", 100)
        self.homography_hslider_zoom_aerial_image.setOrientation(QtCore.Qt.Horizontal)
        self.homography_hslider_zoom_aerial_image.setTickPosition(QtGui.QSlider.NoTicks)
        self.homography_hslider_zoom_aerial_image.setObjectName(_fromUtf8("homography_hslider_zoom_aerial_image"))
        self.zoom_sliders.addWidget(self.homography_hslider_zoom_aerial_image)
        self.verticalLayout_4.addLayout(self.zoom_sliders)
        self.homography_status_layout = QtGui.QHBoxLayout()
        self.homography_status_layout.setContentsMargins(-1, 0, -1, -1)
        self.homography_status_layout.setObjectName(_fromUtf8("homography_status_layout"))
        self.homography_camera_status_label = QtGui.QLabel(self.control_box)
        self.homography_camera_status_label.setText(_fromUtf8(""))
        self.homography_camera_status_label.setObjectName(_fromUtf8("homography_camera_status_label"))
        self.homography_status_layout.addWidget(self.homography_camera_status_label)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.homography_status_layout.addItem(spacerItem3)
        self.homography_aerial_status_label = QtGui.QLabel(self.control_box)
        self.homography_aerial_status_label.setText(_fromUtf8(""))
        self.homography_aerial_status_label.setObjectName(_fromUtf8("homography_aerial_status_label"))
        self.homography_status_layout.addWidget(self.homography_aerial_status_label)
        self.verticalLayout_4.addLayout(self.homography_status_layout)
        self.verticalLayout.addWidget(self.control_box)
        self.homography_layout = QtGui.QHBoxLayout()
        self.homography_layout.setObjectName(_fromUtf8("homography_layout"))
        self.homography_cameraview = HomographyView(self.tab_homography)
        self.homography_cameraview.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.homography_cameraview.setMouseTracking(True)
        self.homography_cameraview.setObjectName(_fromUtf8("homography_cameraview"))
        self.homography_layout.addWidget(self.homography_cameraview)
        self.homography_results = HomographyResultView(self.tab_homography)
        self.homography_results.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.homography_results.setResizeAnchor(QtGui.QGraphicsView.NoAnchor)
        self.homography_results.setObjectName(_fromUtf8("homography_results"))
        self.homography_layout.addWidget(self.homography_results)
        self.homography_aerialview = HomographyView(self.tab_homography)
        self.homography_aerialview.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.homography_aerialview.setMouseTracking(True)
        self.homography_aerialview.setObjectName(_fromUtf8("homography_aerialview"))
        self.homography_layout.addWidget(self.homography_aerialview)
        self.verticalLayout.addLayout(self.homography_layout)
        self.homography_flow_control = QtGui.QWidget(self.tab_homography)
        self.homography_flow_control.setMinimumSize(QtCore.QSize(0, 50))
        self.homography_flow_control.setObjectName(_fromUtf8("homography_flow_control"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.homography_flow_control)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.homography_label_notification = QtGui.QLabel(self.homography_flow_control)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.homography_label_notification.setFont(font)
        self.homography_label_notification.setText(_fromUtf8(""))
        self.homography_label_notification.setObjectName(_fromUtf8("homography_label_notification"))
        self.horizontalLayout_2.addWidget(self.homography_label_notification)
        self.unit_px_label = QtGui.QLabel(self.homography_flow_control)
        self.unit_px_label.setObjectName(_fromUtf8("unit_px_label"))
        self.horizontalLayout_2.addWidget(self.unit_px_label)
        self.unit_px_input = QtGui.QLineEdit(self.homography_flow_control)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.unit_px_input.sizePolicy().hasHeightForWidth())
        self.unit_px_input.setSizePolicy(sizePolicy)
        self.unit_px_input.setObjectName(_fromUtf8("unit_px_input"))
        self.horizontalLayout_2.addWidget(self.unit_px_input)
        self.unit_px_label2 = QtGui.QLabel(self.homography_flow_control)
        self.unit_px_label2.setObjectName(_fromUtf8("unit_px_label2"))
        self.horizontalLayout_2.addWidget(self.unit_px_label2)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.homography_compute_button = QtGui.QPushButton(self.homography_flow_control)
        self.homography_compute_button.setObjectName(_fromUtf8("homography_compute_button"))
        self.horizontalLayout_2.addWidget(self.homography_compute_button)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.homography_continue_button = QtGui.QPushButton(self.homography_flow_control)
        self.homography_continue_button.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.homography_continue_button.setObjectName(_fromUtf8("homography_continue_button"))
        self.horizontalLayout_2.addWidget(self.homography_continue_button)
        self.verticalLayout.addWidget(self.homography_flow_control)
        self.main_tab_widget.addTab(self.tab_homography, _fromUtf8(""))
        self.tab_features = QtGui.QWidget()
        self.tab_features.setObjectName(_fromUtf8("tab_features"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_features)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.feature_tracking_run_panel = QtGui.QWidget(self.tab_features)
        self.feature_tracking_run_panel.setObjectName(_fromUtf8("feature_tracking_run_panel"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.feature_tracking_run_panel)
        self.horizontalLayout_6.setMargin(0)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.feature_tracking_run_test_progress = QtGui.QProgressBar(self.feature_tracking_run_panel)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.feature_tracking_run_test_progress.sizePolicy().hasHeightForWidth())
        self.feature_tracking_run_test_progress.setSizePolicy(sizePolicy)
        self.feature_tracking_run_test_progress.setProperty("value", 0)
        self.feature_tracking_run_test_progress.setOrientation(QtCore.Qt.Horizontal)
        self.feature_tracking_run_test_progress.setInvertedAppearance(False)
        self.feature_tracking_run_test_progress.setObjectName(_fromUtf8("feature_tracking_run_test_progress"))
        self.horizontalLayout_6.addWidget(self.feature_tracking_run_test_progress)
        self.button_feature_tracking_test = QtGui.QPushButton(self.feature_tracking_run_panel)
        self.button_feature_tracking_test.setObjectName(_fromUtf8("button_feature_tracking_test"))
        self.horizontalLayout_6.addWidget(self.button_feature_tracking_test)
        self.gridLayout.addWidget(self.feature_tracking_run_panel, 1, 1, 1, 1)
        self.feature_tracking_parameter_area = QtGui.QScrollArea(self.tab_features)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.feature_tracking_parameter_area.sizePolicy().hasHeightForWidth())
        self.feature_tracking_parameter_area.setSizePolicy(sizePolicy)
        self.feature_tracking_parameter_area.setMinimumSize(QtCore.QSize(470, 0))
        self.feature_tracking_parameter_area.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.feature_tracking_parameter_area.setWidgetResizable(True)
        self.feature_tracking_parameter_area.setObjectName(_fromUtf8("feature_tracking_parameter_area"))
        self.feature_tracking_parameter_widget = QtGui.QWidget()
        self.feature_tracking_parameter_widget.setGeometry(QtCore.QRect(0, 0, 538, 568))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.feature_tracking_parameter_widget.sizePolicy().hasHeightForWidth())
        self.feature_tracking_parameter_widget.setSizePolicy(sizePolicy)
        self.feature_tracking_parameter_widget.setObjectName(_fromUtf8("feature_tracking_parameter_widget"))
        self.formLayout_2 = QtGui.QFormLayout(self.feature_tracking_parameter_widget)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.feature_tracking_parameter_layout = QtGui.QHBoxLayout()
        self.feature_tracking_parameter_layout.setObjectName(_fromUtf8("feature_tracking_parameter_layout"))
        self.formLayout_2.setLayout(0, QtGui.QFormLayout.LabelRole, self.feature_tracking_parameter_layout)
        self.feature_tracking_parameter_area.setWidget(self.feature_tracking_parameter_widget)
        self.gridLayout.addWidget(self.feature_tracking_parameter_area, 0, 1, 1, 1)
        self.feature_tracking_video_layout = QtGui.QVBoxLayout()
        self.feature_tracking_video_layout.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.feature_tracking_video_layout.setObjectName(_fromUtf8("feature_tracking_video_layout"))
        self.gridLayout.addLayout(self.feature_tracking_video_layout, 0, 0, 2, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.feature_tracking_flow_control = QtGui.QFrame(self.tab_features)
        self.feature_tracking_flow_control.setMinimumSize(QtCore.QSize(0, 50))
        self.feature_tracking_flow_control.setFrameShape(QtGui.QFrame.StyledPanel)
        self.feature_tracking_flow_control.setFrameShadow(QtGui.QFrame.Raised)
        self.feature_tracking_flow_control.setObjectName(_fromUtf8("feature_tracking_flow_control"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.feature_tracking_flow_control)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.feature_tracking_back_button = QtGui.QPushButton(self.feature_tracking_flow_control)
        self.feature_tracking_back_button.setObjectName(_fromUtf8("feature_tracking_back_button"))
        self.horizontalLayout_3.addWidget(self.feature_tracking_back_button)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.feature_tracking_continue_button = QtGui.QPushButton(self.feature_tracking_flow_control)
        self.feature_tracking_continue_button.setObjectName(_fromUtf8("feature_tracking_continue_button"))
        self.horizontalLayout_3.addWidget(self.feature_tracking_continue_button)
        self.gridLayout_3.addWidget(self.feature_tracking_flow_control, 1, 0, 1, 1)
        self.main_tab_widget.addTab(self.tab_features, _fromUtf8(""))
        self.roadusers_tab = QtGui.QWidget()
        self.roadusers_tab.setObjectName(_fromUtf8("roadusers_tab"))
        self.gridLayout_5 = QtGui.QGridLayout(self.roadusers_tab)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.gridLayout_14 = QtGui.QGridLayout()
        self.gridLayout_14.setObjectName(_fromUtf8("gridLayout_14"))
        self.roadusers_tracking_run_panel = QtGui.QWidget(self.roadusers_tab)
        self.roadusers_tracking_run_panel.setObjectName(_fromUtf8("roadusers_tracking_run_panel"))
        self.horizontalLayout_15 = QtGui.QHBoxLayout(self.roadusers_tracking_run_panel)
        self.horizontalLayout_15.setMargin(0)
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.roadusers_tracking_run_test_progress = QtGui.QProgressBar(self.roadusers_tracking_run_panel)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.roadusers_tracking_run_test_progress.sizePolicy().hasHeightForWidth())
        self.roadusers_tracking_run_test_progress.setSizePolicy(sizePolicy)
        self.roadusers_tracking_run_test_progress.setProperty("value", 0)
        self.roadusers_tracking_run_test_progress.setOrientation(QtCore.Qt.Horizontal)
        self.roadusers_tracking_run_test_progress.setInvertedAppearance(False)
        self.roadusers_tracking_run_test_progress.setObjectName(_fromUtf8("roadusers_tracking_run_test_progress"))
        self.horizontalLayout_15.addWidget(self.roadusers_tracking_run_test_progress)
        self.button_roadusers_tracking_test = QtGui.QPushButton(self.roadusers_tracking_run_panel)
        self.button_roadusers_tracking_test.setObjectName(_fromUtf8("button_roadusers_tracking_test"))
        self.horizontalLayout_15.addWidget(self.button_roadusers_tracking_test)
        self.button_roadusers_tracking_run = QtGui.QPushButton(self.roadusers_tracking_run_panel)
        self.button_roadusers_tracking_run.setObjectName(_fromUtf8("button_roadusers_tracking_run"))
        self.horizontalLayout_15.addWidget(self.button_roadusers_tracking_run)
        self.gridLayout_14.addWidget(self.roadusers_tracking_run_panel, 1, 1, 1, 1)
        self.roadusers_tracking_video_layout = QtGui.QVBoxLayout()
        self.roadusers_tracking_video_layout.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.roadusers_tracking_video_layout.setObjectName(_fromUtf8("roadusers_tracking_video_layout"))
        self.gridLayout_14.addLayout(self.roadusers_tracking_video_layout, 0, 0, 2, 1)
        self.roadusers_tracking_parameter_area = QtGui.QScrollArea(self.roadusers_tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.roadusers_tracking_parameter_area.sizePolicy().hasHeightForWidth())
        self.roadusers_tracking_parameter_area.setSizePolicy(sizePolicy)
        self.roadusers_tracking_parameter_area.setMinimumSize(QtCore.QSize(410, 0))
        self.roadusers_tracking_parameter_area.setWidgetResizable(True)
        self.roadusers_tracking_parameter_area.setObjectName(_fromUtf8("roadusers_tracking_parameter_area"))
        self.roadusers_tracking_parameter_widget = QtGui.QWidget()
        self.roadusers_tracking_parameter_widget.setGeometry(QtCore.QRect(0, 0, 538, 568))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.roadusers_tracking_parameter_widget.sizePolicy().hasHeightForWidth())
        self.roadusers_tracking_parameter_widget.setSizePolicy(sizePolicy)
        self.roadusers_tracking_parameter_widget.setObjectName(_fromUtf8("roadusers_tracking_parameter_widget"))
        self.formLayout_9 = QtGui.QFormLayout(self.roadusers_tracking_parameter_widget)
        self.formLayout_9.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_9.setObjectName(_fromUtf8("formLayout_9"))
        self.roadusers_tracking_parameter_layout = QtGui.QHBoxLayout()
        self.roadusers_tracking_parameter_layout.setObjectName(_fromUtf8("roadusers_tracking_parameter_layout"))
        self.formLayout_9.setLayout(0, QtGui.QFormLayout.LabelRole, self.roadusers_tracking_parameter_layout)
        self.roadusers_tracking_parameter_area.setWidget(self.roadusers_tracking_parameter_widget)
        self.gridLayout_14.addWidget(self.roadusers_tracking_parameter_area, 0, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_14, 0, 0, 1, 1)
        self.roadusers_tracking_flow_control = QtGui.QFrame(self.roadusers_tab)
        self.roadusers_tracking_flow_control.setMinimumSize(QtCore.QSize(0, 50))
        self.roadusers_tracking_flow_control.setFrameShape(QtGui.QFrame.StyledPanel)
        self.roadusers_tracking_flow_control.setFrameShadow(QtGui.QFrame.Raised)
        self.roadusers_tracking_flow_control.setObjectName(_fromUtf8("roadusers_tracking_flow_control"))
        self.horizontalLayout_16 = QtGui.QHBoxLayout(self.roadusers_tracking_flow_control)
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.roadusers_tracking_back_button = QtGui.QPushButton(self.roadusers_tracking_flow_control)
        self.roadusers_tracking_back_button.setObjectName(_fromUtf8("roadusers_tracking_back_button"))
        self.horizontalLayout_16.addWidget(self.roadusers_tracking_back_button)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem8)
        self.roadusers_tracking_continue_button = QtGui.QPushButton(self.roadusers_tracking_flow_control)
        self.roadusers_tracking_continue_button.setObjectName(_fromUtf8("roadusers_tracking_continue_button"))
        self.horizontalLayout_16.addWidget(self.roadusers_tracking_continue_button)
        self.gridLayout_5.addWidget(self.roadusers_tracking_flow_control, 1, 0, 1, 1)
        self.main_tab_widget.addTab(self.roadusers_tab, _fromUtf8(""))
        self.tab_results = QtGui.QWidget()
        self.tab_results.setObjectName(_fromUtf8("tab_results"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tab_results)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.results_grid = QtGui.QGridLayout()
        self.results_grid.setObjectName(_fromUtf8("results_grid"))
        self.results_plot2 = MatplotlibWidget(self.tab_results)
        self.results_plot2.setObjectName(_fromUtf8("results_plot2"))
        self.results_grid.addWidget(self.results_plot2, 1, 1, 1, 1)
        self.results_plot1 = MatplotlibWidget(self.tab_results)
        self.results_plot1.setObjectName(_fromUtf8("results_plot1"))
        self.results_grid.addWidget(self.results_plot1, 0, 1, 1, 1)
        self.results_plot0 = MatplotlibWidget(self.tab_results)
        self.results_plot0.setObjectName(_fromUtf8("results_plot0"))
        self.results_grid.addWidget(self.results_plot0, 0, 0, 1, 1)
        self.results_plot3 = MatplotlibWidget(self.tab_results)
        self.results_plot3.setObjectName(_fromUtf8("results_plot3"))
        self.results_grid.addWidget(self.results_plot3, 1, 0, 1, 1)
        self.verticalLayout_5.addLayout(self.results_grid)
        self.main_tab_widget.addTab(self.tab_results, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.main_tab_widget, 0, 0, 1, 1)
        TransportationSafety.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(TransportationSafety)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1129, 25))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuTraffic_Analysis = QtGui.QMenu(self.menuBar)
        self.menuTraffic_Analysis.setObjectName(_fromUtf8("menuTraffic_Analysis"))
        self.menuProject = QtGui.QMenu(self.menuBar)
        self.menuProject.setObjectName(_fromUtf8("menuProject"))
        self.menuHomography_2 = QtGui.QMenu(self.menuProject)
        self.menuHomography_2.setObjectName(_fromUtf8("menuHomography_2"))
        self.menuHelp = QtGui.QMenu(self.menuBar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        TransportationSafety.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(TransportationSafety)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        TransportationSafety.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(TransportationSafety)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        TransportationSafety.setStatusBar(self.statusBar)
        self.actionOpen_Project = QtGui.QAction(TransportationSafety)
        self.actionOpen_Project.setObjectName(_fromUtf8("actionOpen_Project"))
        self.actionAdd_Replace_Video = QtGui.QAction(TransportationSafety)
        self.actionAdd_Replace_Video.setObjectName(_fromUtf8("actionAdd_Replace_Video"))
        self.actionFeature_Tracking = QtGui.QAction(TransportationSafety)
        self.actionFeature_Tracking.setObjectName(_fromUtf8("actionFeature_Tracking"))
        self.actionRoad_User_Tracking = QtGui.QAction(TransportationSafety)
        self.actionRoad_User_Tracking.setObjectName(_fromUtf8("actionRoad_User_Tracking"))
        self.actionLoad_Image = QtGui.QAction(TransportationSafety)
        self.actionLoad_Image.setObjectName(_fromUtf8("actionLoad_Image"))
        self.actionAdd_Replace_Aerial_Image = QtGui.QAction(TransportationSafety)
        self.actionAdd_Replace_Aerial_Image.setObjectName(_fromUtf8("actionAdd_Replace_Aerial_Image"))
        self.actionAdd_Replace_Camera_Image = QtGui.QAction(TransportationSafety)
        self.actionAdd_Replace_Camera_Image.setObjectName(_fromUtf8("actionAdd_Replace_Camera_Image"))
        self.actionCompute_Homography_Performance = QtGui.QAction(TransportationSafety)
        self.actionCompute_Homography_Performance.setObjectName(_fromUtf8("actionCompute_Homography_Performance"))
        self.actionAcquire_Aerial_Image = QtGui.QAction(TransportationSafety)
        self.actionAcquire_Aerial_Image.setObjectName(_fromUtf8("actionAcquire_Aerial_Image"))
        self.actionUser_s_Guide = QtGui.QAction(TransportationSafety)
        self.actionUser_s_Guide.setObjectName(_fromUtf8("actionUser_s_Guide"))
        self.actionAbout = QtGui.QAction(TransportationSafety)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionOpen_Video = QtGui.QAction(TransportationSafety)
        self.actionOpen_Video.setObjectName(_fromUtf8("actionOpen_Video"))
        self.actionOpen_Config = QtGui.QAction(TransportationSafety)
        self.actionOpen_Config.setObjectName(_fromUtf8("actionOpen_Config"))
        self.actionNew_Project = QtGui.QAction(TransportationSafety)
        self.actionNew_Project.setObjectName(_fromUtf8("actionNew_Project"))
        self.menuTraffic_Analysis.addAction(self.actionNew_Project)
        self.menuTraffic_Analysis.addAction(self.actionOpen_Project)
        self.menuHomography_2.addAction(self.actionAdd_Replace_Aerial_Image)
        self.menuHomography_2.addAction(self.actionAdd_Replace_Camera_Image)
        self.menuHomography_2.addSeparator()
        self.menuHomography_2.addAction(self.actionCompute_Homography_Performance)
        self.menuHomography_2.addAction(self.actionAcquire_Aerial_Image)
        self.menuProject.addAction(self.menuHomography_2.menuAction())
        self.menuHelp.addAction(self.actionUser_s_Guide)
        self.menuHelp.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuTraffic_Analysis.menuAction())
        self.menuBar.addAction(self.menuProject.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(TransportationSafety)
        self.main_tab_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TransportationSafety)

    def retranslateUi(self, TransportationSafety):
        TransportationSafety.setWindowTitle(_translate("TransportationSafety", "Transportation Safety", None))
        self.homography_button_open_camera_image.setText(_translate("TransportationSafety", "Open Camera Image", None))
        self.homography_button_open_aerial_image.setText(_translate("TransportationSafety", "Open Aerial Image", None))
        self.homography_label_zoom_camera_image.setText(_translate("TransportationSafety", "Zoom:", None))
        self.homography_label_zoom_computed_image.setText(_translate("TransportationSafety", "Zoom:", None))
        self.homography_label_zoom_aerial_image.setText(_translate("TransportationSafety", "Zoom:", None))
        self.unit_px_label.setText(_translate("TransportationSafety", "Unit Pixel Ratio:", None))
        self.unit_px_label2.setText(_translate("TransportationSafety", "m/px", None))
        self.homography_compute_button.setText(_translate("TransportationSafety", "Compute Homography", None))
        self.homography_continue_button.setText(_translate("TransportationSafety", " Continue >", None))
        self.main_tab_widget.setTabText(self.main_tab_widget.indexOf(self.tab_homography), _translate("TransportationSafety", "Homography", None))
        self.feature_tracking_run_test_progress.setFormat(_translate("TransportationSafety", "%p%", None))
        self.button_feature_tracking_test.setText(_translate("TransportationSafety", "Test on Sample", None))
        self.feature_tracking_back_button.setText(_translate("TransportationSafety", "< Homography", None))
        self.feature_tracking_continue_button.setText(_translate("TransportationSafety", " Continue >", None))
        self.main_tab_widget.setTabText(self.main_tab_widget.indexOf(self.tab_features), _translate("TransportationSafety", "Track Features", None))
        self.roadusers_tracking_run_test_progress.setFormat(_translate("TransportationSafety", "%p%", None))
        self.button_roadusers_tracking_test.setText(_translate("TransportationSafety", "Test on Sample", None))
        self.button_roadusers_tracking_run.setText(_translate("TransportationSafety", "Run", None))
        self.roadusers_tracking_back_button.setText(_translate("TransportationSafety", "<Track Features", None))
        self.roadusers_tracking_continue_button.setText(_translate("TransportationSafety", " Continue >", None))
        self.main_tab_widget.setTabText(self.main_tab_widget.indexOf(self.roadusers_tab), _translate("TransportationSafety", "Track Road Users", None))
        self.main_tab_widget.setTabText(self.main_tab_widget.indexOf(self.tab_results), _translate("TransportationSafety", "Results", None))
        self.menuTraffic_Analysis.setTitle(_translate("TransportationSafety", "File", None))
        self.menuProject.setTitle(_translate("TransportationSafety", "Project", None))
        self.menuHomography_2.setTitle(_translate("TransportationSafety", "Homography", None))
        self.menuHelp.setTitle(_translate("TransportationSafety", "Help", None))
        self.actionOpen_Project.setText(_translate("TransportationSafety", "Open Project", None))
        self.actionOpen_Project.setShortcut(_translate("TransportationSafety", "Ctrl+O", None))
        self.actionAdd_Replace_Video.setText(_translate("TransportationSafety", "Video", None))
        self.actionFeature_Tracking.setText(_translate("TransportationSafety", "Feature Tracking", None))
        self.actionRoad_User_Tracking.setText(_translate("TransportationSafety", "Road-User Tracking", None))
        self.actionLoad_Image.setText(_translate("TransportationSafety", "Load Image", None))
        self.actionLoad_Image.setShortcut(_translate("TransportationSafety", "Ctrl+I", None))
        self.actionAdd_Replace_Aerial_Image.setText(_translate("TransportationSafety", "Add/Replace Aerial Image", None))
        self.actionAdd_Replace_Camera_Image.setText(_translate("TransportationSafety", "Add/Replace Camera Image", None))
        self.actionCompute_Homography_Performance.setText(_translate("TransportationSafety", "Compute Homography Performance", None))
        self.actionAcquire_Aerial_Image.setText(_translate("TransportationSafety", "Acquire Aerial Image", None))
        self.actionUser_s_Guide.setText(_translate("TransportationSafety", "User\'s Guide", None))
        self.actionAbout.setText(_translate("TransportationSafety", "About", None))
        self.actionOpen_Video.setText(_translate("TransportationSafety", "Open Video", None))
        self.actionOpen_Config.setText(_translate("TransportationSafety", "Open Config ", None))
        self.actionNew_Project.setText(_translate("TransportationSafety", "New Project", None))
        self.actionNew_Project.setShortcut(_translate("TransportationSafety", "Ctrl+N", None))

from custom.homography import HomographyResultView, HomographyView
from qt_plot import MatplotlibWidget
from custom.zoomslider import ZoomSlider
