import os
import shutil
import datetime
import tkinter as tk


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
    try:
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

        label_confirm_organization.grid(padx=10, pady=10)

    # Error handling in case the specified directory cannot be found
    except FileNotFoundError:
        label_show_error.grid(padx=10, pady=10)


def organize_directory_by_date(folder_location):
    try:
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

        label_confirm_organization.grid(padx=10, pady=10)

    # Error handling in case the specified directory cannot be found
    except FileNotFoundError:
        label_show_error.grid(padx=10, pady=10)


def decide_between_criteria():
    # Getting the directory from the entry field
    directory_to_organize = entry_directory.get()

    # Deleting the widgets for selecting the criteria, after the user has chosen a criteria
    label_criteria.grid_forget()
    dropdown_menu_criteria.grid_forget()
    button_confirm_criteria.grid_forget()

    # Distinguishing between the possible options and execution of the respective function
    if options.get() == "file type":
        organize_directory_by_file_type(directory_to_organize)
    elif options.get() == "date":
        organize_directory_by_date(directory_to_organize)
    else:
        get_criteria_for_organisation()


def get_criteria_for_organisation():
    # Deleting the widgets for entering the directory, after the directory was entered by the user
    label_directory.grid_forget()
    entry_directory.grid_forget()
    button_confirm_directory.grid_forget()

    # Adding the widgets for selecting the criteria to the GUI root
    label_criteria.grid(row=0, column=0, padx=7, pady=10)
    dropdown_menu_criteria.grid(row=0, column=1, pady=10)
    button_confirm_criteria.grid(row=0, column=2, padx=7, pady=10)
    # if the button 'button_confirm_criteria' is pressed, then the function 'decide_between_criteria' is executed


def start_the_program():
    # Adding the widgets for entering the directory to the GUI root
    label_directory.grid(row=0, column=0, pady=10)
    entry_directory.grid(row=0, column=1, pady=10)
    button_confirm_directory.grid(row=0, column=2, padx=15, pady=10)

    # Execution of the mainloop from tkinter
    root.mainloop()
    # if the button 'button_confirm_directory' is pressed, then the function 'get_criteria_for_organisation' is executed


# GUI root configuration
root = tk.Tk()
root.title("DIRECTORY ORGANIZER")
root.geometry("510x50")
root.resizable(width=False, height=False)


# Creating the different widgets that will be used in the program

# Creating the widgets for entering the directory
label_directory = tk.Label(root, text="directory: ")
entry_directory = tk.Entry(root, width=50)
button_confirm_directory = tk.Button(root, text="CONFIRM", command=get_criteria_for_organisation)

# Creating the widgets for selecting the criteria by which the folder should be organized
label_criteria = tk.Label(root, text="Select a criterion by which the directory should be organized: ")
button_confirm_criteria = tk.Button(root, text="CONFIRM", command=decide_between_criteria)

# Creating a dropdown menu for selecting the different criteria
options = tk.StringVar()
options.set("SELECT")
dropdown_menu_criteria = tk.OptionMenu(root, options, "file type", "date")

# Creating a label for confirming that the directory was organized
label_confirm_organization = tk.Label(root, text="Your directory has successfully been organized.")

# Creating a label for informing the user that an error has occurred
label_show_error = tk.Label(root, text='Error: The system cannot find the specified directory!', fg="red")


# Running the function that starts the program
start_the_program()
