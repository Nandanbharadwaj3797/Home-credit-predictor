import os

# Go up from constant/ -> src/ -> project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

DATA_DIR = os.path.join(BASE_DIR, 'notebooks', 'data')

APPLICATION_TRAIN_PATH = os.path.join(DATA_DIR, 'application_train.csv')
APPLICATION_TEST_PATH = os.path.join(DATA_DIR, 'application_test.csv')

artifacts_folder = os.path.join(BASE_DIR, 'artifacts')

MODEL_FILE_NAME = 'model.pkl'
MODEL_FILE_EXTENSION = '.pkl'

TARGET_COLUMN = 'TARGET'