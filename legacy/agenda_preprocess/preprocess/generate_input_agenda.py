"""
Leonardo Ribeiro
ribeiro@aiphes.tu-darmstadt.de
"""
import sys
import json
import os, re

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

def check_weird(rel, entities_list):
    h = None
    t = None
    r = None
    for entity in entities_list:
        if " -- " in entity and entity in rel:
            try:
                if rel.startswith(entity):
                    h = entity
                    rel = re.sub(entity, '', rel)
                elif rel.endswith(entity):
                    t = entity
                    rel = re.sub(entity, '', rel)
                else:
                    print("IN THE MIDDLE?: ", rel)
                    exit()
            except:
                print("ERROR: ", rel)
                print([x for x in re.sub(entity, '', rel).split(' -- ') if x != '' and x != ' '])
    res = [x for x in rel.split(' -- ') if x != '' and x != ' ']
    try:
        counter = 0
        if h == None:
            h = res[counter]
            counter += 1
        r = res[counter]
        counter += 1
        if t == None:
            t = res[counter]
    except:
        print("ERROR: ", rel, res, re.sub(entity, '', rel).split(' -- '), h,r,t, counter)
    return h,r,t

def process_data(relations_list, entities_list):
    relations = []
    for rel in relations_list:
        h,r,t = check_weird(rel, entities_list)

        relations.append('<H> {} <R> {} <T> {}'.format(h,r,t))
    return ' '.join(relations)


def read_dataset(file_, part):
    print(file_)
    with open(file_, 'r', encoding="utf-8") as dataset_file:
        data = json.load(dataset_file)

    sources = []
    targets = []

    for point in data:

        title = '<TITLE> ' + point['title'].lower().strip()

        targets.append(point['abstract_og'].strip())

        relations = process_data(point['relations'], point['entities'])
        
        sources.append(title + ' ' + relations)
    return sources, targets

def create_files(sources, targets, part, path, bpe=None):
    with open(path + '/' + part + '-src.txt', 'w', encoding='utf8') as f:
        f.write('\n'.join(sources))
    with open(path + '/' + part + '-tgt.txt', 'w', encoding='utf8') as f:
        f.write('\n'.join(targets))


def input_files(path_dataset, processed_data_folder):
    """
    Read the corpus, write train and dev files.
    :param path: directory with the AMR json files
    :return:
    """

    parts = ['training', 'dev', 'test']

    for part in parts:
        file_ = path_dataset + '/unprocessed.' + part + '.json'

        print('Processing files...')
        sources, targets = read_dataset(file_, part)
        print('Done')

        print('Creating opennmt files...')
        create_files(sources, targets, part, processed_data_folder)
        print('Done')
    """
    num_operations = 20000
    os.system('cat ' + processed_data_folder + '/training-src.txt ' + processed_data_folder + '/training-tgt.txt > ' +
              processed_data_folder + '/training_source.txt')
    
    print('criating bpe codes...')
    os.system('subword-nmt learn-bpe -s ' + str(num_operations) + ' < ' +
                    processed_data_folder + '/training_source.txt > ' + processed_data_folder + '/codes-bpe.txt')
    print('done')
    
    print('converting files to bpe...')
    for part in parts:
        print(part)
        file_pre = processed_data_folder + '/' + part + '-src.txt'
        file_ = processed_data_folder + '/' + part + '-src-bpe.txt'
        os.system('subword-nmt apply-bpe -c ' + processed_data_folder +
                  '/codes-bpe.txt < ' + file_pre + ' > ' + file_)

        file_pre = processed_data_folder + '/' + part + '-tgt.txt'
        file_ = processed_data_folder + '/' + part + '-tgt-bpe.txt'
        os.system('subword-nmt apply-bpe -c ' + processed_data_folder +
                  '/codes-bpe.txt < ' + file_pre + ' > ' + file_)

    print('done')
    
    for part in parts:
        file_ = path_dataset + '/unprocessed.' + part + '.json'

        print('Processing files bpe...')
        data = read_dataset_bpe(file_, processed_data_folder, part)
        print('Done')

        print('Creating opennmt bpe files...')
        create_files(data, part, processed_data_folder, bpe=True)
        print('Done')
    """
    print('Files necessary for training/evaluating/test are written on disc.')


def main(path_dataset, processed_data_folder):

    input_files(path_dataset, processed_data_folder)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
