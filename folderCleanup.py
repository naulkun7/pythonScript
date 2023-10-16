import os
import collections

EXT_AUDIO = ["mp3", "wav" "raw", "wma", "mid", "midi"]
EXT_MOVIES = ["mp4", "avi", "mov", "wmv", "flv", "mkv", "webm"]
EXT_IMAGE = [
    "jpg",
    "jpeg",
    "png",
    "gif",
    "bmp",
    "svg",
    "psd",
    "raw",
    "tif",
    "tiff",
    "ico",
    "heic",
]
EXT_DOCUMENT = [
    "doc",
    "docx",
    "pdf",
    "txt",
    "rtf",
    "tex",
    "wpd",
    "odt",
    "ppt",
    "pptx",
    "pps",
    "ppsx",
    "odp",
    "xls",
    "xlsx",
    "ods",
]
EXT_COMPRESSED = ["zip", "rar", "7z", "gz", "tar", "iso", "dmg", "pkg", "deb"]
EXT_INSTALL = ["exe", "msi", "iso", "dmg", "pkg", "deb"]

base_path = os.path.expanduser("~")
dest_path = ["Music", "Movies", "Pictures", "Documents", "Downloads", "random"]

for path in dest_path:
    dir_path = os.path.join(base_path, path)
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)

downloads_path = os.path.join(base_path, "Downloads")
file_mapping = collections.defaultdict(list)
file_list = os.listdir(downloads_path)

for file_name in file_list:
    file_ext = file_name.split(".")[-1]
    file_mapping[file_ext].append(file_name)


for f_ext, f_list in file_mapping.items():
    if f_ext in EXT_AUDIO:
        for file in f_list:
            os.rename(
                os.path.join(downloads_path, file),
                os.path.join(base_path, "Music", file),
            )
    elif f_ext in EXT_MOVIES:
        for file in f_list:
            os.rename(
                os.path.join(downloads_path, file),
                os.path.join(base_path, "Movies", file),
            )
    elif f_ext in EXT_IMAGE:
        for file in f_list:
            os.rename(
                os.path.join(downloads_path, file),
                os.path.join(base_path, "Pictures", file),
            )
    elif f_ext in EXT_DOCUMENT:
        for file in f_list:
            os.rename(
                os.path.join(downloads_path, file),
                os.path.join(base_path, "Documents", file),
            )
    else:
        for file in f_list:
            os.rename(
                os.path.join(downloads_path, file),
                os.path.join(base_path, "Downloads", file),
            )
