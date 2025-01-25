import pandas as pd
import json
import logging
import os

# handling the logging
# Ensure the "logs" directory exists
log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)

# logging configuration
logger = logging.getLogger('PreProcess')
logger.setLevel('DEBUG')

console_handler = logging.StreamHandler()
console_handler.setLevel('DEBUG')

log_file_path = os.path.join(log_dir, 'PreProcess.log')
file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel('DEBUG')

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

class preprocess:
    def generate_embedding_data(self,path):
        df = pd.read_csv(path)
        logger.debug("Completed Reading the Data csv")
        clms = list(df.columns)
        no_of_rows = len(df.iloc[:,0:1])
        logger.debug("Started The emebeding_data generation process")

        embedding_data = []
        for i in range(no_of_rows):
            data = list(df.iloc[i,:])
            s = ""
            for j in range(len(clms)):
                s+=" "+str(clms[j])+" "+str(data[j])
            embedding_data.append(s)
            if i>=1:
                break

        data = [{"id": f"item-{i+1}", "text": embedding_data[i]} for i in range(len(embedding_data))]
        logger.debug("Completed The emebeding_data generation process")
        # for i in data:
        #     print(i)
        return data

    