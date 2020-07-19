import shutil

def copy_ufw():
    try:
        original = r'/var/log/ufw.log'
        target = r'/home/done/Documents/nginx/logs/ufw/ufw.log'

        shutil.copyfile(original, target)
    except:
        print("File was not copied")

    finally:
        print("End of Copy_Files")
