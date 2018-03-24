"""L8ER: Documentation

Data format:
    path/to/sample.wav Transcription of the sample wave file.
"""

import os


DATA_PATH = '/home/marc/workspace/speech/data/timit/TIMIT/'     # Base path to the TIMIT data set.
TARGET_PATH = '/home/marc/workspace/speech/python/loader/'       # Where to generate the files.


def _gen_list(target):
    master_path = os.path.join(DATA_PATH, '{}_all.txt'.format(target))

    if not os.path.isfile(master_path):
        raise ValueError('"{}" is not a file.'.format(master_path))

    with open(master_path, 'r') as f:
        master_data = f.readlines()

    result = []

    for line in master_data:
        wav_path, txt_path, _, _ = line.split(',')
        txt_path = os.path.join(DATA_PATH, txt_path)

        with open(txt_path, 'r') as f:
            txt = f.readlines()
            assert len(txt) == 1, 'Text file contains to many lines.'
            txt = txt[0].strip()
            txt = txt.split(' ', 2)[2]

        output_line = '{} {}\n'.format(wav_path, txt)
        result.append(output_line)

    # Remove new line from last entry.
    result[-1] = result[-1].strip()

    target_path = os.path.join(TARGET_PATH, '{}.txt'.format(target))
    _delete_file_if_exists(target_path)

    with open(target_path, 'w') as f:
        print('Writing {} lines of {} files to {}'.format(len(result), target, target_path))
        f.writelines(result)


def _delete_file_if_exists(path):
    if os.path.exists(path) and os.path.isfile(path):
        os.remove(path)


if __name__ == '__main__':
    _gen_list('train')
    _gen_list('test')
    print('Training and evaluation file lists created.')
