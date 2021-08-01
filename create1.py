import glob
import os

import copy_files
import readfile
import readhtml
#test
path = "/home/done/Documents/nginx/"
read_files_path = path

page_title = "Anime WebPage"

# '		<video class=\"video\" src=\"{0}\" controls></video>\n' \ test
# '		<a href=\"{0}\"><img src =\"{0}.thumb\">{0}</a><br>\n' \
def create_html_tag(index_path, raw_file_name):
    try:
        f = open(index_path, 'a')
        # print(file_path)

        if (".mov" in raw_file_name.lower() or ".mp4" in raw_file_name.lower()) and "thumb" not in raw_file_name.lower():
            file_name = raw_file_name.split("/")[len(raw_file_name.split("/")) - 1]
            # file_name = raw_file_name.split("/media/")[1]

            tag_string = '<div class=\"container\">\n' \
                         '	<div class=\"C-video\">\n' \
                         '		<div>{0}</div><video class=\"video\" src=\"{0}\" controls></video>\n' \
                         '	</div>\n' \
                         '</div>\n'.format(file_name)
            f.write(tag_string)

        if (".jpg" in raw_file_name.lower()
            or ".jpeg" in raw_file_name.lower()
            or ".heic" in raw_file_name.lower()
            or ".png" in raw_file_name.lower()) \
                and "thumb" not in raw_file_name.lower():
            file_name = raw_file_name.split("/")[len(raw_file_name.split("/")) - 1]
            # file_name = raw_file_name.split("/media/")[1]
            tag_string = '<div class=\"gallery\"> \n' \
                         '		<a href=\"{0}\"><img src =\"{0}\"></a><br> \n' \
                         '		<div class=\"desc\"> {0}</div> \n' \
                         '</div>\n'.format(file_name, raw_file_name)
            f.write(tag_string)

        # If it is a folder, enters the folder and creates a new page
        if "." not in raw_file_name:
            file_name = raw_file_name.split("/")[len(raw_file_name.split("/")) - 1]
            tag_string = '      <a href=\"{0}/\">{0}</a>\n'.format(file_name)
            print("Created folder {0}".format(raw_file_name))

            if '/v' not in raw_file_name or '/v/' in raw_file_name:
                f.write(tag_string)

            f.close()
            create_page(raw_file_name + "/")


    except Exception as e:
        print("Error while creating tags", e)

    finally:
        # print("end")
        f.close()


def create_page(file_path):
    try:
        # Gets page top from template
        page_top = readhtml.get_page_top()

        # Creates HTML file inside folder and adds header
        index_path = file_path + "index.html"
        f = open(index_path, 'w')
        page_name = index_path.split('/')[len(index_path.split('/'))-2]
        f.write(page_top.format("{", "}", page_name))

        # Creates 'Back' Button on HTML file
        if len(index_path) > 37:
            tag_string = '<a href=\"{0}\"><<---</a><br>\n'.format('..\\')
            f.write(tag_string)
        else:
            print(index_path)

        # TODO - Check if there is no folder inside. If there isn't any, jump next step. (Close the file above first)

        tag_string = '<div class="dropdown"> \n' \
                     '  <button onclick="myFunction()" class="dropbtn">Dropdown</button>\n' \
                     '  <div id="myDropdown" class="dropdown-content">\n'.format('..\\')
        f.write(tag_string)

        f.close()

        arr = []

        # Create Folder links
        for raw_file_name in glob.glob(os.path.join(file_path, '*')):
            if '.' not in raw_file_name and 'page-content' not in raw_file_name:
                arr.append(raw_file_name)

        arr.sort()

        for folder_name in arr:
            create_html_tag(index_path, folder_name)

        f = open(index_path, 'a')
        tag_string = '  </div>\n' \
                     '</div>\n'
        f.write(tag_string)
        f.close()

        # TODO - Implement one line code for below

        add_file(index_path, file_path, '*.HEIC')

        add_file(index_path, file_path, '*.heic')

        add_file(index_path, file_path, '*.png')

        add_file(index_path, file_path, '*.PNG')

        add_file(index_path, file_path, '*.jpg')

        add_file(index_path, file_path, '*.jpeg')

        add_file(index_path, file_path, '*.mp4')

        add_file(index_path, file_path, '*.MP4')

        add_file(index_path, file_path, '*.MOV')

        add_file(index_path, file_path, '*.mov')

        # Gets page bottom from template
        page_bottom = readhtml.get_page_bottom()

        # Closes the HTML file
        f = open(index_path, 'a')
        f.write(page_bottom)
        f.close()

    except Exception as e:
        print("Error while creating page", e)

    finally:
        f.close()
        # print("End of Create_Page")


def add_file(index_path, file_path, extention):
    arr = []

    # Sorts file names
    for raw_file_name in glob.glob(os.path.join(file_path, extention)):
        arr.append(raw_file_name)
    arr.sort()

    # Iterates folder, append files to html file and looks for extra folder to do the same inside it
    for raw_file_name in arr:
        create_html_tag(index_path, raw_file_name)

copy_files.copy_ufw()

create_page(path)

readfile.create_page()
