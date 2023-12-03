from datetime import datetime
import pytz


def get_london_time():
    london_tz = pytz.timezone('Europe/London')
    london_time = datetime.now(london_tz)
    formatted_time = london_time.strftime('%d %B %Y %H:%M %Z')
    return formatted_time
