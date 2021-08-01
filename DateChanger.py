integrationId = '4a916a1c-c8e7-4edf-9a8e-b2370ea67a9b'
month = '05'

day = '12'

hour = 17

minute = 10

def int_to_string(time):
    time_string = ''
    if time < 10:
        time_string = '0' + str(time)
    else:
        time_string = str(time)
    return time_string


open_hour = int_to_string(hour)

open_minute = int_to_string(minute)

close_hour = int_to_string(hour)

close_minute = int_to_string(minute + 5)

post_hour = int_to_string(hour)

post_minute = int_to_string(minute + 6)



print('\"integrationId\" : \"{8}\",\n\n'

      '\"openDate\": \"2021-{0}-{1}T{2}:{3}:00+0000\",\n\n'

      '\"closeDate\": \"2021-{0}-{1}T{4}:{5}:00+0000\",\n\n'

      '\"postDate\": \"2021-{0}-{1}T{6}:{7}:00+0000\"\n\n'.format(month, day, open_hour, open_minute, close_hour,
                                                                  close_minute, post_hour, post_minute, integrationId))