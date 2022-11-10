from gladosZero import GladosZero
import time
from tqdm import tqdm

if __name__ == '__main__':
    gladosZero = GladosZero()
    inpfile, outfile, logger = gladosZero.start()
    print = logger.info
    parameters = inpfile['parameters']

    steps = 20
    print("String is: {}".format(parameters['string to print']))
    for i in tqdm(range(steps), desc='Progress'):
        print("Hello World! {}".format(i))
        time.sleep(0.5)

    gladosZero.terminate()
