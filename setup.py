# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages

setup(name="automl-x",
        version="0.3.0",
        description="automl tools",
        author="caihengxing",
        author_email="caihengxing@4paradigm.com",
        url='https://github.com/4paradigm/autox',
        install_requires=[
            'lightgbm',
            'xgboost',
            # 'pytorch-tabnet',
            'torch',
            'numpy',
            'pandas',
            'sklearn',
            'tqdm',
            'optuna',
            'img2vec_pytorch',
            'pypinyin',
            'keras',
            'tensorflow',
            'gensim',
            # 'glove-python-binary',
            'transformers',
            # 'datasets',
            'pyarrow>=6.0.0',
        ],
        python_requires='>=3.6',
        packages=find_packages(exclude=['data', 'demo', 'img', 'sub', 'test',
                                        'run.py', 'run_oneclick.py', 'submit.py']),
        include_package_data=True,
        zip_safe=False
        )
# python setup.py sdist build
# twine upload dist/*
