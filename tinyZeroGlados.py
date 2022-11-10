import json
import argparse
from datetime import datetime
import git

if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # parser.add_argument('--input_file', '-if', type=str, default='config.json',
    #                     help='Input file name',
    #                     required=True)
    # args = parser.parse_args()
    #
    # with open(args.config, 'r') as f:
    #     config = json.load(f)
    #
    # print(config)

    ex = dict()
    ex_paths = dict()
    ex_paths['global data'] = 'C:\work\inputs\global data'
    ex_paths['local data'] = 'C:\work\inputs\local data'
    ex_paths['output'] = 'C:\work\inputs\output data'
    ex['paths'] = ex_paths

    ex_metadata = dict()
    ex_metadata['UID'] = '123456789'
    ex_metadata['trigger time'] = datetime.timestamp(datetime.now())

    # Get the current commit hash
    repo = git.Repo(search_parent_directories=True)
    ex_metadata['commit hash'] = repo.head.object.hexsha
    ex_metadata['GIT Repo name'] = 1
