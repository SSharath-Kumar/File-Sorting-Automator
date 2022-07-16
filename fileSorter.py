from shutil import move
from os import scandir, rename
from os.path import splitext, exists, join, isdir

# DEFINING FILE EXTENSIONS
audio_extensions = [".m4a", ".flac", "mp3", ".wav", ".wma", ".aac"]
compressed_extensions = [".7z", ".pkg", ".rar", ".tar.gz", ".z", ".zip"]
code_extensions = [".c", ".cgi", ".pl", ".class", ".cpp", ".cs", ".h", ".java",
                   ".php", ".py", ".sh", ".swift", ".vb", ".ipynb"]
document_extensions = [".doc", ".docx", ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]
image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff",
                    ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw", ".k25", ".bmp", ".dib", ".heif",
                    ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm",
                    ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]
installation_extensions = [".exe", ".iso", ".bin"]
video_extensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg", ".mp4",
                    ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]

# DEFINING MODES
modes = ["AUDIO", "COMPRESSED", "CODE", "DOCUMENTS", "IMAGES", "INSTALLATIONS", "VIDEO"]

# DEFINING SOURCE AND DESTINATION PATHS
source_path = ""
dest_path_audio = ""
dest_path_compressed = ""
dest_path_code = ""
dest_path_documents = ""
dest_path_images = ""
dest_path_installations = ""
dest_path_video = ""


def make_unique(dest, name):
    filename, extension = splitext(name)
    counter = 1
    # * IF FILE EXISTS, ADDS NUMBER TO THE END OF THE FILENAME
    while exists(f"{dest}/{name}"):
        name = f"{filename}({str(counter)}){extension}"
        counter += 1

    return name


def move_file(dest, entry, name):
    if exists(f"{dest}/{name}"):
        unique_name = make_unique(dest, name)
        old_name = join(dest, name)
        new_name = join(dest, unique_name)
        rename(old_name, new_name)
    move(entry, dest)


def check_file(file, file_name, mode):
    """
    Method to check the file if it belongs to the defined categories

    Args:
    :param file: File object
    :param file_name: Name of the file
    :param mode: Category of the files

    Returns:
    :return: NONE
    """
    extensions = None
    destination_path = None

    if mode == "AUDIO":
        extensions = audio_extensions
        destination_path = dest_path_audio
    elif mode == "COMPRESSED":
        extensions = compressed_extensions
        destination_path = dest_path_compressed
    elif mode == "CODE":
        extensions = code_extensions
        destination_path = dest_path_code
    elif mode == "DOCUMENTS":
        extensions = document_extensions
        destination_path = dest_path_documents
    elif mode == "IMAGES":
        extensions = image_extensions
        destination_path = dest_path_images
    elif mode == "INSTALLATIONS":
        extensions = installation_extensions
        destination_path = dest_path_installations
    elif mode == "VIDEO":
        extensions = video_extensions
        destination_path = dest_path_video

    for extension in extensions:
        if file_name.endswith(extension) or file_name.endswith(extension.upper()):
            # print('Moving ', file_name, '--->', destination_path)
            move_file(destination_path, file, name)


with scandir(source_path) as files:
    for file in files:
        name = file.name
        if isdir(file):
            continue
        # print(name)
        for mode in modes:
            check_file(file, name, mode)
