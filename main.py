import sys
from pytube import YouTube, Playlist
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import *
from ytpd_beta import UiMainWindow
import os


def seconds_to_mmss(seconds):
    """Function:
    Returns a string in the format of mm:ss"""
    min = seconds // 60
    sec = seconds % 60
    if min < 10:
        min_str = '0' + str(min)
    else:
        min_str = str(min)
    if sec < 10:
        sec_str = '0' + str(sec)
    else:
        sec_str = str(sec)
    return min_str + ":" + sec_str


class DownloadingVideos(QThread):
    """ Download all videos from the videos_dict using the id, todo fix some bugs"""
    downloadCount = pyqtSignal(int, int, bool, str)  # downloaded, number_of_videos, finished

    def __init__(self, videos_dict, download_path, parent=None):
        QThread.__init__(self, parent)
        self.videos_dict = videos_dict
        self.download_path = download_path

    def run(self):
        """ Main function, downloads videos by their id while emitting progress data"""
        # Create download folder before downloading
        if not os.path.isdir(self.download_path):  # if path doesn't exist, create one.
            os.mkdir(self.download_path)
        # Download
        number_of_videos = len(self.videos_dict)
        failed_download = list()
        downloaded, now_downloading, finished = 0, "", False
        for key, value in self.videos_dict.items():
            try:
                stream = value["stream"]
                print(key, ": stream=", stream)
                _ = stream.download(output_path=self.download_path)
            except:
                failed_download.append(key)
                print("Unable to download: ", key)
            downloaded += 1
            now_downloading = key
            if downloaded == number_of_videos:
                finished = True
            self.downloadCount.emit(downloaded, number_of_videos, finished, now_downloading)
        if len(failed_download) == 0:
            print("Download was successful, all videos downloaded.")
        else:
            print("Download wasn't as successfull, these videos weren't downloaded: ")
            for title in failed_download:
                print(title)


class UrlLoading(QThread):
    """ Loads the videos data from playlist in another thread."""
    countChanged = pyqtSignal(dict, bool)

    def __init__(self, playlist_link, parent=None):
        QThread.__init__(self, parent)
        self.playlist_link = playlist_link

    def run(self):
        """ Main function, gets all the playlist videos data, emits the info dict"""
        videos_dict = dict()
        try:
            print("Parsing playlist successful, loading video data...")
            playlist = Playlist(self.playlist_link)
            for video in playlist.videos:
                print(video.title, "... loaded")
                try:
                    video.check_availability()
                except:  # If video is unavailable skip, print error to console
                    print("Unable to load: ", video.title)
                    continue
                videos_dict[video.title] = dict()
                # Save stream object to directly download
                videos_dict[video.title]["stream"] = video.streams.filter(only_audio=True, file_extension='mp4').first()
                videos_dict[video.title]["duration"] = seconds_to_mmss(video.length)
                # Send data dict after each song is loaded
                self.countChanged.emit(videos_dict, True)
        except:
            print("Exception(Playlist/Video Error)... Something went wrong with loading playlist or one of the videos.")
            self.countChanged.emit({}, False)


class MainPage(QMainWindow, UiMainWindow):
    def __init__(self, parent=None):
        super(MainPage, self).__init__(parent)
        self.setupUi(self)
        # Hide the fetching data label and the error label, shows up when its loading, invalid url
        self.url_fetching_data_label.hide()
        self.url_error_label.hide()
        # Seting the videos dict. and connecting the delete video button with the remove_selected_items fn.
        self.remove_from_list_button.clicked.connect(self.remove_selected_items)
        self.videos_dict = dict()
        # Hide progress bar, show it when it starts downloading
        self.progressBar.hide()
        # Buttons Connection with the appropriate functions
        self.url_load_button.clicked.connect(self.url_loading_button_click)
        self.download_button.clicked.connect(self.download_button_click)
        self.folder_name_button.clicked.connect(self.select_save_path)
        # Get the desktop path, set folder name, full download path, set label.
        self.current_path = os.path.dirname(os.path.abspath(__file__))
        self.download_folder_name = "YTPD_beta"
        self.download_full_path = self.current_path + "\\" + self.download_folder_name
        self.download_path_label.setText("Download path: {}".format(self.download_full_path))


# Input url threading

    def url_loading_button_click(self):
        """ Reads input data from url_input and creates an instance of the UrlLoading thread """
        self.listWidget.clear()  # Clear the widget
        self.videos_dict = dict()  # Clear the dict
        self.url_fetching_data_label.show()  # Show the loading label
        self.url_error_label.hide()          # Hide the error label if the input is a retry
        playlist_url = self.url_input.text()  # Get the input text
        self.calc = UrlLoading(playlist_url)  # Pass in the input text
        self.calc.countChanged.connect(self.url_loading_finished)  # connect with the changing variables
        self.calc.start()

    def url_loading_finished(self, videos_dict, executed):
        """ Retrieves data from thread at the end, updates the list"""
        self.url_fetching_data_label.hide()  # Hide the loading label as it has finished loading
        if executed:  # If it was executed successfully
            videos_list, counter = list(), 0
            for key, value in videos_dict.items():
                counter += 1
                line_str = str(counter) + ") " + key + "  " + videos_dict[key]["duration"]  # Display line
                videos_list.append(line_str)
            self.videos_dict = videos_dict
            self.listWidget.addItems(videos_list)  # Update the list with the strings
        else:
            self.url_error_label.show()  # Show the error label

# Downloading videos threading

    def download_button_click(self):
        """ Executes when the button is clicked """
        self.progressBar.show()
        self.download_button.setEnabled(False)
        self.down = DownloadingVideos(self.videos_dict, self.download_full_path)  # Pass in the dict
        self.down.downloadCount.connect(self.downloading_update)  # connect with the download function
        self.down.start()

    def downloading_update(self, downloaded, number_of_videos, finished, now_downloading):  # int, bool
        """ Executes as it receives signals from thread """
        # Update the progressBar, calculate the perc. here
        downloaded_percentages = int(round((downloaded / number_of_videos) * 100))
        self.progressBar.setProperty("value", downloaded_percentages)
        # Changing the downloaded label
        if finished:
            self.download_button.setEnabled(True)
            self.progressBar.hide()
            self.downloaded_label.setText("Finished. {} files saved to:\n {}".format(downloaded, self.download_full_path))
            self.progressBar.setProperty("value", 0)  # reset loading bar
        else:
            self.downloaded_label.setText("{}\nDownloaded {} out of {}.".format(now_downloading, downloaded,
                                                                                number_of_videos))

# Items videos from videos(of playlist) list

    def remove_selected_items(self):
        """ Removes the selected items from the self.videos_dict and self.list_of_titles
        Also refreshes the listWidget"""
        list_items = self.listWidget.selectedItems()  # list of the selected items (should not be a list but okay)
        selected_item_index = self.listWidget.currentRow()  # index of the selected item
        if not list_items:  # if nothing is selected
            return
        for item in list_items:  # iterate through the list and delete the items
            self.listWidget.takeItem(self.listWidget.row(item))

        if selected_item_index != -1:  # -1 means nothing was selected
            index, delete_key = 0, ''
            for key, value in self.videos_dict.items():
                if index == selected_item_index:
                    delete_key = key  # save the key of the deleted item in the videos_dict
                index += 1
            del self.videos_dict[delete_key]  # delete the actual key

# Getting input from the folder name folder_name_input, creating dir, changing labels

    def select_save_path(self):
        """ Sets the download path to the input one, auto set to YTPD_beta"""
        self.download_folder_name = self.folder_name_input.text()
        self.download_full_path = self.current_path + "\\" + self.download_folder_name
        self.download_path_label.setText("Download path: {}".format(self.download_full_path))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainPage()
    widget.show()
    sys.exit(app.exec_())
