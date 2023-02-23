import os
import shutil
import datetime


def move_file_into_folder(file, source, destination):
    shutil.move(source + '\\' + file, destination)


def create_new_folder(new_folder):
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)


def check_file_type(file):
    image_type = ['.png', '.jpg', '.jpeg']
    video_type = ['.mp4', '.avi', '.mkv']
    music_type = ['.mp3', '.wav']
    document_type = ['.pdf', '.txt', '.doc', '.docx', '.rtf']

    # Getting the file extension from the current file
    file_extension = os.path.splitext(file)[1].lower()

    if file_extension in image_type:
        ret = 'image'
    elif file_extension in video_type:
        ret = 'video'
    elif file_extension in music_type:
        ret = 'music'
    elif file_extension in document_type:
        ret = 'document'
    else:
        ret = 'other'

    return ret


def organize_directory_by_file_type(folder_location):
    os.chdir(folder_location)
    all_files = os.listdir(folder_location)

    create_new_folder('images')
    create_new_folder('videos')
    create_new_folder('music')
    create_new_folder('documents')
    create_new_folder('others')

    # Creation of the complete file paths of the folders
    images_folder = folder_location + '\\' + 'images'
    videos_folder = folder_location + '\\' + 'videos'
    music_folder = folder_location + '\\' + 'music'
    documents_folder = folder_location + '\\' + 'documents'
    others_folder = folder_location + '\\' + 'others'

    # Moving each file into the correct folder
    for current_file in all_files:
        # Skipping folders
        if os.path.isdir(current_file):
            pass
        else:
            if check_file_type(current_file) == 'image':
                move_file_into_folder(current_file, folder_location, images_folder)
            elif check_file_type(current_file) == 'video':
                move_file_into_folder(current_file, folder_location, videos_folder)
            elif check_file_type(current_file) == 'music':
                move_file_into_folder(current_file, folder_location, music_folder)
            elif check_file_type(current_file) == 'document':
                move_file_into_folder(current_file, folder_location, documents_folder)
            elif check_file_type(current_file) == 'other':
                move_file_into_folder(current_file, folder_location, others_folder)
            else:
                pass

    print("Your folder has successfully been organized.")


def organize_directory_by_date(folder_location):
    os.chdir(folder_location)
    all_files = os.listdir(folder_location)

    for current_file in all_files:
        if os.path.isdir(current_file):
            pass
        else:
            # Getting the creation time for current_file
            creation_timestamp = os.path.getmtime(current_file)
            # Extracting the information 'year' and 'month' from the modification time
            creation_date = datetime.datetime.fromtimestamp(creation_timestamp)
            year_month = creation_date.strftime('%Y_%m')

            # Creation and filling of a folder that is named after the associating year and month
            create_new_folder(year_month)
            move_file_into_folder(current_file, folder_location, year_month)

    print("Your folder has successfully been organized.")


def get_criteria_for_organisation():
    while True:
        print('\nAccording to which criteria should the directory be organized?')
        print('Press (1) for file type')
        print('Press (2) for date')
        criteria_selection = int(input('Selection: '))

        if criteria_selection == 1:
            organize_directory_by_file_type(directory_to_organize)
            break
        elif criteria_selection == 2:
            organize_directory_by_date(directory_to_organize)
            break
        else:
            print('\nError: Wrong input - Try again!')


try:
    directory_to_organize = input('Location of the directory you want to organize: ')
    get_criteria_for_organisation()

# Handle error case in case the specified folder cannot be found
except FileNotFoundError:
    print("Error! The system cannot find the specified directory.")
