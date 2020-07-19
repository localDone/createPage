
path = "/home/done/Documents/nginx/template.html"

def get_page_top():
    r = open(path, 'r')
    Lines = r.readlines()
    page_top = ''
    for line in Lines:
        page_top += line
        if 'page-top-end' in line:
            return page_top
            print(line.strip())

    return page_top


def get_page_bottom():
    r = open(path, 'r')
    Lines = r.readlines()
    page_bottom = ''
    read_bottom = False
    for line in Lines:
        # page_top += line
        if 'page-bottom' in line:
            read_bottom = True

        if read_bottom:
            page_bottom += line

    return page_bottom

