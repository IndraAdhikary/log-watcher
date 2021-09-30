from time import sleep
import logging
# logging.basicConfig(filemode='w', filename='log_generator.log')
logging.basicConfig(filename='app.log', filemode='w', level=0)
i = 0
while True:
    logging.info(f'New Entry Value: {i}')
    i +=1
    sleep(1)
