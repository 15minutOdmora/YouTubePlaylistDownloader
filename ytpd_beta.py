from PyQt5 import QtCore, QtGui, QtWidgets


class UiMainWindow(object):
    """ GUI Design class """
    def setupUi(self, MainWindow):
        """ GUI style and display settings"""
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(827, 498)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # Main title
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(10, 0, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        # Video title list display
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(520, 40, 281, 301))
        self.listWidget.setObjectName("listWidget")
        # URL input label
        self.enter_playlist_url_label = QtWidgets.QLabel(self.centralwidget)
        self.enter_playlist_url_label.setGeometry(QtCore.QRect(10, 70, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.enter_playlist_url_label.setFont(font)
        self.enter_playlist_url_label.setObjectName("enter_playlist_url_label")
        # URL input box
        self.url_input = QtWidgets.QLineEdit(self.centralwidget)
        self.url_input.setGeometry(QtCore.QRect(140, 70, 301, 20))
        self.url_input.setObjectName("url_input")
        # URL load button
        self.url_load_button = QtWidgets.QPushButton(self.centralwidget)
        self.url_load_button.setGeometry(QtCore.QRect(370, 100, 71, 23))
        self.url_load_button.setObjectName("url_load_button")
        # Remove from QList buton
        self.remove_from_list_button = QtWidgets.QPushButton(self.centralwidget)
        self.remove_from_list_button.setGeometry(QtCore.QRect(670, 350, 131, 23))
        self.remove_from_list_button.setObjectName("remove_from_list_button")
        # Loading bar
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 390, 481, 16))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        # Error label
        self.url_error_label = QtWidgets.QLabel(self.centralwidget)
        self.url_error_label.setGeometry(QtCore.QRect(140, 50, 350, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.url_error_label.setFont(font)
        self.url_error_label.setObjectName("url_error_label")
        # Loading data label
        self.url_fetching_data_label = QtWidgets.QLabel(self.centralwidget)
        self.url_fetching_data_label.setGeometry(QtCore.QRect(140, 100, 231, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.url_fetching_data_label.setFont(font)
        self.url_fetching_data_label.setObjectName("url_fetching_data_label")
        # Download folder label
        self.download_folder_name_label = QtWidgets.QLabel(self.centralwidget)
        self.download_folder_name_label.setGeometry(QtCore.QRect(10, 280, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.download_folder_name_label.setFont(font)
        self.download_folder_name_label.setObjectName("download_folder_name_label")
        # Folder name input box
        self.folder_name_input = QtWidgets.QLineEdit(self.centralwidget)
        self.folder_name_input.setGeometry(QtCore.QRect(170, 280, 211, 20))
        self.folder_name_input.setObjectName("folder_name_input")
        # Folder name load button
        self.folder_name_button = QtWidgets.QPushButton(self.centralwidget)
        self.folder_name_button.setGeometry(QtCore.QRect(390, 280, 61, 23))
        self.folder_name_button.setObjectName("folder_name_button")
        # Download folder name input box
        self.download_path_label = QtWidgets.QLabel(self.centralwidget)
        self.download_path_label.setGeometry(QtCore.QRect(10, 320, 450, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.download_path_label.setFont(font)
        self.download_path_label.setObjectName("download_path_label")
        # Description label
        self.guide_label = QtWidgets.QLabel(self.centralwidget)
        self.guide_label.setGeometry(QtCore.QRect(10, 130, 451, 111))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.guide_label.setFont(font)
        self.guide_label.setObjectName("guide_label")
        # Lists widget label
        self.listWidget_label = QtWidgets.QLabel(self.centralwidget)
        self.listWidget_label.setGeometry(QtCore.QRect(520, 20, 201, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.listWidget_label.setFont(font)
        self.listWidget_label.setObjectName("listWidget_label")
        # Download button
        self.download_button = QtWidgets.QPushButton(self.centralwidget)
        self.download_button.setGeometry(QtCore.QRect(10, 350, 91, 23))
        self.download_button.setObjectName("download_button")
        # Donload label
        self.downloaded_label = QtWidgets.QLabel(self.centralwidget)
        self.downloaded_label.setGeometry(QtCore.QRect(520, 390, 350, 30))
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.downloaded_label.setFont(font)
        self.downloaded_label.setObjectName("downloaded_label")
        # Bottom credits label
        self.credits_label = QtWidgets.QLabel(self.centralwidget)
        self.credits_label.setGeometry(QtCore.QRect(10, 460, 581, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.credits_label.setFont(font)
        self.credits_label.setObjectName("credits_label")
        # Bottom credits hyperlink
        self.link_label = QtWidgets.QLabel(self.centralwidget)
        self.link_label.setGeometry(QtCore.QRect(220, 460, 300, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.link_label.setFont(font)
        self.link_label.setOpenExternalLinks(True)
        self.link_label.setObjectName("link_label")
        #  Main menu bar, not used
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 827, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        # Trainslations
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        """ Set the text and translations """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YTPD.Beta"))
        self.title_label.setText(_translate("MainWindow", "YouTube Playlist Downloader"))
        self.enter_playlist_url_label.setText(_translate("MainWindow", "Enter playlist url:"))
        self.url_load_button.setText(_translate("MainWindow", "Load"))
        self.remove_from_list_button.setText(_translate("MainWindow", "Remove from list"))
        self.url_error_label.setText(_translate("MainWindow", "Could not retrieve data from url." +
                                                " Check the link and try again?"))
        self.url_fetching_data_label.setText(_translate("MainWindow", "Fetching data ... This might take a while."))
        self.download_folder_name_label.setText(_translate("MainWindow", "Download folder name:"))
        self.folder_name_button.setText(_translate("MainWindow", "Apply"))
        self.download_path_label.setText(_translate("MainWindow", "Download path: "))
        self.guide_label.setText(_translate("MainWindow", "Guide:\n" +
                                            "- Once the data from the url is loaded, video titles will be displayed" +
                                            " in the box to the right.\n" +
                                            "- By selecting a video title and pressing the Remove from list" +
                                            " button you can remove\n" +
                                            "  the video from the download list.\n" +
                                            "- Then type in the folder name in which the files will be saved.\n" +
                                            "- The download path is set to the current path and" +
                                            " can not be changed.\n" +
                                            "- To download the files click Download. \n" +
                                            "- All video files are saved in a .mp4(only audio) format."))
        self.listWidget_label.setText(_translate("MainWindow", "Playlist videos:"))
        self.download_button.setText(_translate("MainWindow", "Download"))
        self.downloaded_label.setText(_translate("MainWindow", "Waiting for download :)"))
        self.credits_label.setText(_translate("MainWindow", "Created by: L.M.," +
                                              " source files available at: "))
        self.link_label.setText("<a href=\"https://github.com/15minutOdmora/YouTubePlaylistDownloader\">'github.com/15minutOdmora/YouTubePlaylistDownloader'</a>")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
