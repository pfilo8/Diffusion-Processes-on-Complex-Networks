import os
import time

from api_downloader import download_friends, clean_data

START_USERNAME = 'valerois'
DEPTH = 3
OUTPUT_DIR = 'outputs'
OUTPUT_FILENAME = 'livejournal.csv'


def generate_friends(start_username, depth=1):
    print(f'Current username: {start_username}')
    response = download_friends(start_username)
    list_of_friends = clean_data(response)

    for friend in list_of_friends:
        yield start_username, friend
    if depth != 1:
        for friend in list_of_friends:
            print(friend)
            time.sleep(1 / 4)
            yield from generate_friends(friend, depth - 1)


if __name__ == '__main__':
    with open(os.path.join(OUTPUT_DIR, OUTPUT_FILENAME), 'w+') as f:
        f.write('source,target')
        f.write('\n')
        for u, v in generate_friends(START_USERNAME, depth=DEPTH):
            line = '{u},{v}'.format(u=u, v=v)
            f.write(line)
            f.write('\n')
