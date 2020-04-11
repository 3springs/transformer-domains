# -*- coding: utf-8 -*-
import click
from tqdm.auto import tqdm
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
from sklearn.model_selection import train_test_split


@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')
    input_filepath = Path(input_filepath)
    output_filepath = Path(output_filepath)
    domains(input_filepath/'../external'/'domains'/'data', output_filepath/'domains'/'data')

def domains(input_filepath, output_filepath):

    print(input_filepath, output_filepath)

    domain_files = sorted(input_filepath.glob('**/*.txt'))

    train_domains, test_domains = train_test_split(domain_files, random_state=42, train_size=0.8)
    test_domains, dev_domains = train_test_split(test_domains, random_state=42, train_size=0.5)

    output_filepath.mkdir(exist_ok=True, parents=True)
    # TEST, try with only 4 files
    splits = dict(test=test_domains[:4], train=train_domains[:44], dev=dev_domains[:4])
    for split, files in splits.items():
        outfile = output_filepath / f'{split}.txt'
        with outfile.open('w') as fo:
            for f in tqdm(files, desc=f"combining {split}"):
                fo.write(f.open().read())

    # TODO could pretokenize too


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
