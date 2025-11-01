import os
from tinytag import TinyTag

def seconds_to_mmssff(total_seconds, fps=75):
    """
    Converts a total number of seconds into mm:ss:ff format.

    Args:
        total_seconds (float or int): The total number of seconds.
        fps (int): The frames per second. Defaults to 24.

    Returns:
        str: The time in mm:ss:ff format.
    """
    minutes = int(total_seconds // 60)
    remaining_seconds = total_seconds % 60
    seconds = int(remaining_seconds)
    frames = int((remaining_seconds - seconds) * fps)

    return f"{minutes:02}:{seconds:02}:{frames:02}"


def get_folder_list(directory_path):
    """
    Returns a list of folder names within the specified directory.
    """
    folders = []
    for entry in os.listdir(directory_path):
        full_path = os.path.join(directory_path, entry)
        if os.path.isdir(full_path):
            folders.append(entry)
    return folders

def get_files_os_listdir(directory_path):
    """
    Returns a list of files in the specified directory using os.listdir().
    """
    file_list = []
    for entry in os.listdir(directory_path):
        full_path = os.path.join(directory_path, entry)
        if os.path.isfile(full_path):
            file_list.append(entry)
    return file_list

def get_song_metadata(audio_file):
    try:
        tag = TinyTag.get(audio_file)
        title = tag.title
        artist = tag.artist
        duration = tag.duration
    except FileNotFoundError:
        print(f"Error: Audio file not found at {audio_file}")
    except Exception as e:
        print(f"Error extracting audio metadata: {e}")
    return title, artist, duration

def get_album_metadata(album_path):
    folder_dir = get_files_os_listdir(album_path)
    audio_file = album_path + "\\" + folder_dir[3]
    try:
        tag = TinyTag.get(audio_file)
        album = tag.album
        artist = tag.artist
        genre = tag.genre
        year = tag.year
    except FileNotFoundError:
        print(f"Error: Audio file not found at {audio_file}")
    except Exception as e:
        print(f"Error extracting audio metadata: {e}")
    return album, artist, genre, year

def get_tracklist(album_path):
    folder_dir = get_files_os_listdir(album_path)
    file_type = folder_dir[4][-4:]
    # for ind, val in enumerate(folder_dir)
    tracklist = []
    for ind, val in enumerate(folder_dir):
        if val[-4:] == file_type:
            tracklist.append(val)
    return tracklist

def get_tracklist_metadata(folder_path):
    tracklist = get_tracklist(folder_path)
    tracklist_metadata = [0]*len(tracklist)
    for ind, track in enumerate(tracklist):
        track_path = folder_path + "//" + track
        tracklist_metadata[ind] = get_song_metadata(track_path)
    return tracklist_metadata

def check_for_multidisk(folder_path):
    files = get_files_os_listdir(folder_path)
    if files[0] == "Disk 1":
        return True
    else:
        return False

def check_for_cue(folder_path):
    files = get_files_os_listdir(folder_path)
    cue = False
    for ind, val in enumerate(files):
        if val[-4:] == ".cue":
            cue = True
    return cue

def write_cue(album_path):
    album, artist, genre, year = get_album_metadata(album_path)
    tracklist_metadata = get_tracklist_metadata(album_path)
    

path = "C:\\Users\srs19\slsk_sharing"



folders = get_folder_list(path)

folder = path + "\\" + folders[0]

dir_1 = get_files_os_listdir(folder)
song = folder + "\\" + dir_1[0]

file_type = song[-4:]

tracklist = get_tracklist(folder)
metadata = get_tracklist_metadata(folder)

alb_metadata = get_album_metadata(folder)

print(alb_metadata)
# print(file_type)

# print(tracklist)
# print(metadata)

#get_song_metadata(song)


# print(dir_1)
# print(song)