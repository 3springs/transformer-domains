transformer-domains
==============================

Using transformers to generate domain names

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


# Setup

This project uses git lfs



```sh
# clone
git clone git@github.com:3springs/transformer-domains.git

# unpack domain data
cd data/external/domains/data
./unpack.sh
cd ../../../..

make data
make run_language_modeling name=1
make run_generation name=1
```

# Example output

```
Model prompt >>> .com
=== GENERATED SEQUENCE 1 ===
www.pestbomsb.com
=== GENERATED SEQUENCE 2 ===
chos-gfg.g4.com
=== GENERATED SEQUENCE 3 ===
www.bloggeerte.com
=== GENERATED SEQUENCE 4 ===
www.upprasvic.com
=== GENERATED SEQUENCE 5 ===
2bhaspao.com
=== GENERATED SEQUENCE 6 ===
vimittico.com
=== GENERATED SEQUENCE 7 ===
www.listharkkman.com
=== GENERATED SEQUENCE 8 ===
goanargente.com
=== GENERATED SEQUENCE 9 ===
www.matesarapsk.com
=== GENERATED SEQUENCE 10 ===
www.litvoni.com
=== GENERATED SEQUENCE 11 ===
tsdingpraclioct.com
=== GENERATED SEQUENCE 12 ===
chorjosudeconmeurolamr.blogspot.com
=== GENERATED SEQUENCE 13 ===
www.superdokkeroisavaels.com
=== GENERATED SEQUENCE 14 ===
calayndoettch.conweb.com
=== GENERATED SEQUENCE 15 ===
www.frecnamato.com
=== GENERATED SEQUENCE 16 ===
www.carofowm.bloggetich.com
=== GENERATED SEQUENCE 17 ===
babrimeros.larpop.com
=== GENERATED SEQUENCE 18 ===
www.claseperlivroy.com
=== GENERATED SEQUENCE 19 ===
www.munoxos.com
=== GENERATED SEQUENCE 20 ===
www.radiulsongaicos.com
=== GENERATED SEQUENCE 1 ===
www.pestbomsb.com
=== GENERATED SEQUENCE 2 ===
chos-gfg.g4.com
=== GENERATED SEQUENCE 3 ===
www.bloggeerte.com
=== GENERATED SEQUENCE 4 ===
www.upprasvic.com
=== GENERATED SEQUENCE 5 ===
2bhaspao.com
=== GENERATED SEQUENCE 6 ===
vimittico.com
=== GENERATED SEQUENCE 7 ===
www.listharkkman.com
=== GENERATED SEQUENCE 8 ===
goanargente.com
=== GENERATED SEQUENCE 9 ===
www.matesarapsk.com
=== GENERATED SEQUENCE 10 ===
www.litvoni.com
=== GENERATED SEQUENCE 11 ===
tsdingpraclioct.com
=== GENERATED SEQUENCE 12 ===
chorjosudeconmeurolamr.blogspot.com
=== GENERATED SEQUENCE 13 ===
www.superdokkeroisavaels.com
=== GENERATED SEQUENCE 14 ===
calayndoettch.conweb.com
=== GENERATED SEQUENCE 15 ===
www.frecnamato.com
=== GENERATED SEQUENCE 16 ===
www.carofowm.bloggetich.com
=== GENERATED SEQUENCE 17 ===
babrimeros.larpop.com
=== GENERATED SEQUENCE 18 ===
www.claseperlivroy.com
=== GENERATED SEQUENCE 19 ===
www.munoxos.com
=== GENERATED SEQUENCE 20 ===
www.radiulsongaicos.com
```

# See also

- transformers+lightning
  - https://github.com/ricardorei/lightning-text-classification
  - https://github.com/sobamchan/pytorch-lightning-transformers/blob/master/mrpc.py
- transformers + gen
  - https://github.com/huggingface/transformers/blob/master/examples/run_generation.py

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

