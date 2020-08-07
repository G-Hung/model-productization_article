# My Medium article for model productization


# Objective
This repo is the code for [my article in Medium](https://medium.com/@geoffreyhung/from-jupyter-notebook-to-sc-582978d3c0c) that demonstrates how to convert Jupyter Notebook to scripts together with some engineering practices, we only surfaced with the basics and want to show the benefits quickly!


# High level topics

    a. Why scripts instead of Jupyter notebook
    b. Conversion from ipynb to .py
    c. Make the scripts configurable [Click]
    d. Include logging [logging]
    e. Make sure the local environment is the same [Conda env]
    f. Include unit test and basic CI [pytest, GitHub Action]
    g. Autoformat the script style [black, isort]

Code structure tree, hope this can help you to understand how the codes evolve
```
.
├── README.md
├── __init__.py
├── .github/workflows         [f]
├── autoformat.sh             [g]
├── data
│   ├── predict.csv           [b]
│   ├── test.csv              [b]
│   ├── train.csv             [b]
│   └── winequality.csv
├── log
│   ├── etl.log               [d]
│   ├── predict.log           [d]
│   └── train.log             [d]
├── model
│   └── model.pkl             [b]
├── notebook
│   └── prediction-of-quality-of-wine.ipynb [a]
├── requirement.txt           [e]
└── scripts
    ├── config.yml            [c]
    ├── etl.py                [b, c]
    ├── predict.py            [b, c]
    ├── test_train.py         [f]
    ├── test_utility.py       [f]
    ├── train.py              [b, c]
    └── utility.py
```

# Setup

1. Git Clone the repo
```
git clone https://github.com/G-Hung/model-productization_article.git
```

2. Go to project root folder
```
cd model-productization_article
```

3. Setup conda env in terminal
```
conda create - name YOU_CHANGE_THIS python=3.7 -y

conda activate YOU_CHANGE_THIS

pip install –r requirements.txt
```

4. Run the code in terminal
```
python3 ./scripts/etl.py
python3 ./scripts/train.py
python3 ./scripts/predict.py
```

We should expect nothing popup except files inside log/ and model/ are updated! In few seconds, the scripts finish the processes of ETL, training, evaluation and prediction!

5. To run unit test in terminal
```
pytest
```

6. To run autoformat.sh in terminal
```
# If you get permission error, you can try
# chmod +rx autoformat.sh

./autoformat.sh
```

6. After usage
```
conda deactivate
conda remove –name YOU_CHANGE_THIS –all
```
