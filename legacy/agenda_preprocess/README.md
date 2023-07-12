Folder structure:
```
agenda_preprocess
    └── unprocessed
        ├── unprocessed.dev.json
        ├── unprocessed.test.json
        └── unprocessed.training.json
    └── preprocess
        └── generate_input_agenda.py
    └── processed
        ├── dev-src.txt
        ├── dev-tgt.txt
        ├── test-src.txt
        ├── test-tgt.txt
        ├── training-src.txt
        └── training-tgt.txt
    └── preprocess_AGENDA.sh
```
The unprocessed folder is empty, so download the https://github.com/rikdz/GraphWriter/blob/master/data/unprocessed.tar.gz, unzip it and copy the json files into unprocessed folder. Rename the unprocessed.train.json file to unprocessed.training.json!