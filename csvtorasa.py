import pandas as pd


def create_rasa_files(path,create_files_path):
    """
    Converts an CSV file created with the specified format to RASA accepted nlu.md format
    :param path: path where the CSV file is present
    :param create_files_path: path where the nlu.md file needs to be created
    :return: return nothing. A file is created in the path specified via create_files_path
    """
    df = pd.read_csv(r"{}".format('C:\\Users\\saite\\OneDrive\\Desktop\\Dataset\\Dataset.csv'))
    file = open(r'{}\nlu.md'.format('C:\\Users\\saite\\OneDrive\Desktop\\Chatdata'), "w")
    intents = list(df.columns)
    for item in intents:
        file.write("## intent: {intent_name}\n".format(intent_name=item))
        for sent in df[item]:
            file.write("- {}\n".format(sent))
    file.close()
    file = open(r'{}\domain.yml'.format('C:\\Users\\saite\\OneDrive\Desktop\\Chatdata'), "w")
    file.write("intents:\n")
    for intent_name in intents:
        file.write("  - {}\n".format(intent_name))
    file.write("actions:\n")
    for intent_name in intents:
        file.write("  - utter_{}\n".format(intent_name))
    file.close()
    return None
create_rasa_files(path='C:\\Users\\saite\\OneDrive\\Desktop\\Dataset',create_files_path='C:\\Users\\saite\\OneDrive\Desktop\\Chatdata')