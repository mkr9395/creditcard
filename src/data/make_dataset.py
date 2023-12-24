import pathlib
from pathlib import Path
import yaml
import sys
import pandas as pd

from sklearn.model_selection import train_test_split


# loading the dataset
def load_data(data_path):
    df = pd.read_csv(data_path)
    return df

# splitting into train and test
def split_data(df,test_split,seed):
    train,test = train_test_split(df,test_size=test_split,random_state=seed)
    return train, test

# save the train and test splits
def save_data(train,test,output_path):
    pathlib.Path(output_path).mkdir(parents=True,exist_ok=True) 
    train.to_csv(output_path + '/train.csv', index=False)
    test.to_csv(output_path + '/test.csv', index=False)
    
    
def main():
    curr_dir = pathlib.Path(__file__)
    home_dir = curr_dir.parent.parent.parent
    params_file = (home_dir / 'params.yaml').as_posix()
    params = yaml.safe_load(open(params_file))["make_dataset"]
    
    #input_file = pathlib.Path(home_dir / 'data/raw/credit_card.csv').as_posix()
    #print(input_file)
    
    input_file = sys.argv[1]
    
    data_path = home_dir.as_posix() + input_file
    
    #data_path = Path(home_dir / 'data/raw/creditcard.csv').as_posix()
    output_path = (home_dir / 'data/processed').as_posix()
    
    data = load_data(data_path)
    train_data, test_data = split_data(data,params['test_split'],params['seed'])
    save_data(train_data, test_data, output_path)
    
if __name__ == "__main__":
    main()