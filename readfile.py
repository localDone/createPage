

page_title = "Log WebPage"

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
           '<a href=\"/var/log/ufw.log\">Logs</a>' \
           '<p>Have fun!</p>\n'
page_top = page_top.format("{", "}", page_title)


def create_page():
    page_bottom = '<p><em>Yay.</em></p>\n' \
                  '</body>\n' \
                  '</html>\n'
    try:
        index_path = '/home/done/Documents/nginx/logs/ufw/index.html'
        f = open(index_path, 'w')
        f.write(page_top)
        tag_string = '<div class=\"container\">\n' \
                     '	<div class=\"return-button\">\n' \
                     '		<a href=\"{0}\"><<---</a><br>\n' \
                     '	</div>\n' \
                     '</div>\n'.format('..\\')
        f.write(tag_string)
        f.close()
        path = "/home/done/Documents/nginx/logs/ufw/ufw.log"
        r = open(path, 'r')
        Lines = r.readlines()
        f = open(index_path, 'a')
        for line in Lines:
            f.write('<p>{0}</p>\n'.format(line.strip()))
            # print(line.strip())

        f.write(page_bottom)
        f.close()

    except Exception as e:
        print("Error while creating page", e)
        f.close()

    finally:
        r.close()
        print("End of readFile")

