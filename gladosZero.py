import json
import argparse
from datetime import datetime
import git
import logging
import os
import sys


class GladosZero(object):
    def __init__(self):
        self.logger = None
        self.outfile = None
        self.log_path = None
        self.outfile_path = None
        self.inpfile = None

    def start(self, print_run_info=True):
        parser = argparse.ArgumentParser()
        parser.add_argument('--input_file', '-if', type=str, default='config.json',
                            help='Input file name',
                            required=True)
        inpfile = parser.parse_args().input_file

        with open(inpfile, 'r') as f:
            inpfile = json.load(f)

        # Set up log file
        outpath = inpfile['paths']['output']
        self.log_path = os.path.join(outpath, 'log.log')
        self.outfile_path = os.path.join(outpath, 'output.json')
        if not os.path.exists(outpath):
            os.makedirs(outpath)
        if os.path.exists(self.log_path):
            os.remove(self.log_path)

        # Set up logging to console and file
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(levelname)-8s %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S',
                            filename=self.log_path,
                            filemode='w')
        console = logging.StreamHandler(sys.stdout)
        console.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
        console.setFormatter(formatter)
        logging.getLogger(__name__).addHandler(console)

        logger = logging.getLogger(__name__)
        # logger.addHandler(logging.StreamHandler(sys.stdout))
        print = logger.info

        # Add time stamp to log file
        run_cmd = ' '.join(sys.argv)

        outfile = dict()
        outfile['input file'] = inpfile.copy()

        out_meta = dict()
        out_meta['CMD'] = run_cmd
        out_meta['start time'] = datetime.now().timestamp()
        outfile['metadata'] = out_meta
        outfile['files'] = dict()

        if print_run_info:
            print("<>" * 30)
            print("Run command: {}".format(run_cmd))
            print("Run metadata")
            print('Run started at: {}'.format(datetime.fromtimestamp(out_meta['start time'])))
            print('Input file:')
            print('\n' + json.dumps(inpfile, indent=4))

            print('Output path: {}'.format(outpath))
            print('Log file: {}'.format(self.log_path))
            print("<>" * 30)
            print('\n' * 2)

        self.inpfile = inpfile
        self.outfile = outfile
        self.logger = logger

        return inpfile, outfile, logger

    def terminate(self, outfile=None, print_run_info=True):
        if outfile is None:
            outfile = self.outfile

        outfile['metadata']['end time'] = datetime.now().timestamp()
        outfile['files']['log'] = self.log_path
        outfile['files']['output metadata'] = self.outfile_path

        print = self.logger.info
        if print_run_info:
            print("\n" * 2)
            print("<>" * 30)
            print("Run TERMINATED.")
            print('Run finished at: {}'.format(datetime.now()))
            print('Output file:')
            print('\n' + json.dumps(outfile, indent=4))
            print("<>" * 30)

        with open(self.outfile_path, 'w') as f:
            json.dump(outfile, f, indent=4)


if __name__ == '__main__':
    gladosZero = GladosZero()
    inpfile, outfile, logger = gladosZero.start()
    print("Hello World!")

    print = logger.info

    gladosZero.terminate()
