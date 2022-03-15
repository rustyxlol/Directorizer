# Directorizer

## About <a name = "about"></a>

Super simple python script that moves files into categorized directories based on file names

## Usage <a name = "usage"></a>

Simply run the script and input source directory and categories that you want

```
> python3 directorize.py
```

Example:

```
.
└── source_directory/
    ├── docker fundamentals.pdf
    ├── python fundamentals.pdf
    └── machine learning with python.pdf
```

Running directory.py in `source_directory` with categories `docker,python` will create docker and python subdirectories and move files containing 'docker' and 'python' to their respective directories

```
.
└── source/
    ├── docker /
    │   └── dockerfundamentals.pdf
    └── python /
        ├── python fundamentals.pdf
        └── machine learning with python.pdf
```

## Extras <a name = "extras"></a>

Tree structures brought to you by: [nfriend's tree generator](https://tree.nathanfriend.io/)

Contributions are welcome!
