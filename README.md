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
Model prompt >>> three
=== GENERATED SEQUENCE 1 ===
threeflorianopolis.com.br!!!!!!!!!!!!!
=== GENERATED SEQUENCE 2 ===
three-pink-makes.blogspot.com.br!!!!!!!!!
=== GENERATED SEQUENCE 3 ===
threeoncomicon.com.br!!!!!!!!!!!!!
=== GENERATED SEQUENCE 4 ===
three-urls-co.blogspot.com.br!!!!!!!!!
=== GENERATED SEQUENCE 5 ===
three-five.blogspot.com.br!!!!!!!!!!!!
=== GENERATED SEQUENCE 6 ===
threeizestes.com.br!!!!!!!!!!!!!
=== GENERATED SEQUENCE 7 ===
threeteenchallenges.blogspot.no!!!!!!!!!!!!!
=== GENERATED SEQUENCE 8 ===
threeesizes.blogspot.com.br!!!!!!!!!!!!
=== GENERATED SEQUENCE 9 ===
threefulmaker.blogspot.com.br!!!!!!!!!!!!
=== GENERATED SEQUENCE 10 ===
threedolfatto.com.br!!!!!!!!!!!!!
=== GENERATED SEQUENCE 11 ===
three.altosoft.no!!!!!!!!!!!!!!
=== GENERATED SEQUENCE 12 ===
threeseven.com.br!!!!!!!!!!!!!!!
=== GENERATED SEQUENCE 13 ===
threeblogisbrasil.blogspot.com.br!!!!!!!!!
=== GENERATED SEQUENCE 14 ===
three-day-registre.blogspot.com.br!!!!!!!!
=== GENERATED SEQUENCE 15 ===
threeyuki.shop!!!!!!!!!!!!!!!!
=== GENERATED SEQUENCE 16 ===
three-rolands.no!!!!!!!!!!!!!!!
=== GENERATED SEQUENCE 17 ===
threehashelen.blogspot.com.br!!!!!!!!!!!
=== GENERATED SEQUENCE 18 ===
threedudajeh.blogspot.com.br!!!!!!!!!!
=== GENERATED SEQUENCE 19 ===
threesskjell.no!!!!!!!!!!!!!!!
=== GENERATED SEQUENCE 20 ===
three.no!!!!!!!!!!!!!!!!!!
```

```
Model prompt >>> buy
04/11/2020 08:12:51 - WARNING - transformers.modeling_utils -   Setting `pad_token_id` to 50256 (first `eos_token_id`) to generate sequence
=== GENERATED SEQUENCE 1 ===
buybybeer.shop!!!!!!!!!!!!!!!!
=== GENERATED SEQUENCE 2 ===
buy-tour-inside-la-bela-des.ibooked.com.br!
=== GENERATED SEQUENCE 3 ===
buyasul.com.br!!!!!!!!!!!!!!
=== GENERATED SEQUENCE 4 ===
buy-inn-at-ice-inn-askibdering.ibooked.no!!
=== GENERATED SEQUENCE 5 ===
buy.no!!!!!!!!!!!!!!!!!!
=== GENERATED SEQUENCE 6 ===
buyout.com.br!!!!!!!!!!!!!!!
=== GENERATED SEQUENCE 7 ===
buylistingshow.no!!!!!!!!!!!!!!!
=== GENERATED SEQUENCE 8 ===
buylycritor.blogspot.com.br!!!!!!!!!!!
=== GENERATED SEQUENCE 9 ===
buyingsplace.no!!!!!!!!!!!!!!!!
=== GENERATED SEQUENCE 10 ===
buytinaonline.com.br!!!!!!!!!!!!!
=== GENERATED SEQUENCE 11 ===
buygavegada.blogspot.com.br!!!!!!!!!!
=== GENERATED SEQUENCE 12 ===
buycrystal.com.br!!!!!!!!!!!!!!
=== GENERATED SEQUENCE 13 ===
buymadeinenglish.blogspot.no!!!!!!!!!!!!!
=== GENERATED SEQUENCE 14 ===
buy-and-soft.shop!!!!!!!!!!!!!!
=== GENERATED SEQUENCE 15 ===
buyingindustria.com.br!!!!!!!!!!!!!
=== GENERATED SEQUENCE 16 ===
buy.unifesp.br!!!!!!!!!!!!!!
=== GENERATED SEQUENCE 17 ===
buycosmeticos.com.br!!!!!!!!!!!!!
=== GENERATED SEQUENCE 18 ===
buys.no!!!!!!!!!!!!!!!!!
=== GENERATED SEQUENCE 19 ===
buyaventure.com.br!!!!!!!!!!!!!!
=== GENERATED SEQUENCE 20 ===
buycites.com.br!!!!!!!!!!!!!!
```

```
Model prompt >>>arx
04/11/2020 08:13:35 - WARNING - transformers.modeling_utils -   Setting `pad_token_id` to 50256 (first `eos_token_id`) to generate sequence
=== GENERATED SEQUENCE 1 ===
arxisecasamento.com.br!!!!!!!!!!!!
=== GENERATED SEQUENCE 2 ===
arx-lumatessen.no!!!!!!!!!!!!!
=== GENERATED SEQUENCE 3 ===
arxivocafm.com.br!!!!!!!!!!!!
=== GENERATED SEQUENCE 4 ===
arx.pro.br!!!!!!!!!!!!!!!!
=== GENERATED SEQUENCE 5 ===
arximports.com.br!!!!!!!!!!!!!!
=== GENERATED SEQUENCE 6 ===
arxivocasamento.blogspot.com.br!!!!!!!!!
=== GENERATED SEQUENCE 7 ===
arxoreslagante.com.br!!!!!!!!!!!!!
=== GENERATED SEQUENCE 8 ===
arxivarcissoes.jusbrasil.com.br!!!!!
=== GENERATED SEQUENCE 9 ===
arxivazadornacontador.com.br!!!!!!!!!
=== GENERATED SEQUENCE 10 ===
arxivarenda.com.br!!!!!!!!!!!!!
=== GENERATED SEQUENCE 11 ===
arxandrisoluz.blogspot.com.br!!!!!!!!!!
=== GENERATED SEQUENCE 12 ===
arxujuregos.com.br!!!!!!!!!!!!
=== GENERATED SEQUENCE 13 ===
arximaisasp.blogspot.com.br!!!!!!!!!!!
=== GENERATED SEQUENCE 14 ===
arx.unirio.br!!!!!!!!!!!!!!
=== GENERATED SEQUENCE 15 ===
arxivaoquintal.ufes.br!!!!!!!!!!
=== GENERATED SEQUENCE 16 ===
arxis.com.br!!!!!!!!!!!!!!!
=== GENERATED SEQUENCE 17 ===
arxvillecriativa.com.br!!!!!!!!!!!
=== GENERATED SEQUENCE 18 ===
arxies.no!!!!!!!!!!!!!!!!!
=== GENERATED SEQUENCE 19 ===
arxivademocracia.blogspot.com.br!!!!!!!!!!
=== GENERATED SEQUENCE 20 ===
arxacaju.blogspot.com.br!!!!!!!!!!!
```

# See also

- transformers+lightning
  - https://github.com/ricardorei/lightning-text-classification
  - https://github.com/sobamchan/pytorch-lightning-transformers/blob/master/mrpc.py
- transformers + gen
  - https://github.com/huggingface/transformers/blob/master/examples/run_generation.py

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

