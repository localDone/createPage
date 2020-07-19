import glob
import os

path = "/home/done/Documents/nginx/willy/"
read_files_path = path + "media/"
index_path = path + "index.html"

page_title = "McLaren Media"
page_top = '<!DOCTYPE html>\n' \
             '<html>\n' \
             '<head>\n' \
             '<title>{2}</title>\n' \
             '<style>\n' \
             '    body {0}\n' \
             '        width: 35em;\n' \
             '        margin: 0 auto;\n' \
             '        font-family: Tahoma, Verdana, Arial, sans-serif;\n' \
             '    {1}\n' \
             '</style>\n' \
             '</head>\n' \
             '<body>\n' \
             '<h1>Welcome to {2}!</h1>\n' \
             '<p>Have fun!</p>\n'
page_top = page_top.format("{", "}", page_title)

page_bottom = '<p><em>Yay.</em></p>\n' \
             '</body>\n' \
             '</html>\n'


def create_html_tag(file_path):
    try:
        f = open(index_path, 'a')
        # print(file_path)
        file_name = file_path.split("/media/")[1]
        if ".MOV" in file_name and "thumb" not in file_name:
            tag_string = '<div class=\"container\">\n' \
                         '	<div class=\"C-video\">\n' \
                         '		<a href=\"media/{0}\">{0}</a><br>\n' \
                         '	</div>\n' \
                         '</div>\n'.format(file_name)
            # print(tag_string)
            f.write(tag_string)
    except Exception as e:
        print("Error while creating tags", e)

    finally:
        print("end")
        f.close()


def create_page():
    try:
        # a = open(index_path, 'r')
        # a.readlines()

        f = open(index_path, 'w')
        f.write(page_top)
        f.close()
        for filename in glob.glob(os.path.join(read_files_path, '*')):
            create_html_tag(filename)
        f = open(index_path, 'a')
        f.write(page_bottom)

    except Exception as e:
        print("Error while creating page", e)

    finally:
        f.close()
        print("End of Create_Page")


create_page()
