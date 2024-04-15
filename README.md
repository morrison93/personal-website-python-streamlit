## Major Iterations
* Added content regarding my personal experience and career.
* Added support for multiple languages taking the idea from Rsirp0c of using a constants file.
* Changed template visuals by changing the ./streamlit/config.toml 
* Added multi-page with streamlit sidebar and /pages.

## Future Ideas
* Creation of a blog space. 
* Some exercise of integration with a back-end firstly with a DB like postgresSQL and later with an API to separate the logic from the client-side
* I want to create a Posting area to present the books that I am reading maybe give an evaluation. 

## Requirements
```
streamlit_lottie==0.0.2
streamlit==1.33.0
requests==2.24.0
Pillow==8.4.0
protobuf~=3.19.0
watchdog==2.1.8
```

## Run the app
* Terminal
    ```
    # vanilla terminal
    streamlit run 1_Home.py

    # poetry
    poetry add `cat requirements.txt`
    poetry run streamlit run app.py

    # quit
    ctrl-c
    ```
* VSCode
  * Open the repo directory in VSCode
  * Open `app.py`
  * Start debugging with F5
  * Stop debugging with Shift-F5

## Author and References:
* Rodrigo forked from Sven's Bo repo (https://github.com/Sven-Bo/personal-website-streamlit)
* Template from Rsirp0c: (https://github.com/Rsirp0c/portfolio/blob/main/%F0%9F%8F%A0_Mainpage.py)

Please bear in mind that although I took these two projects as references I have iterated and will still iterate upon these solutions.


## Addendum
[@pythoninthegrass](https://github.com/pythoninthegrass) additions
* Setup [Poetry](https://python-poetry.org/docs/#installation), [reverted protobuf](https://discuss.streamlit.io/t/typeerror-descriptors-cannot-not-be-created-directly/25639/11)
* Added [watchdog](https://docs.streamlit.io/library/advanced-features/configuration) for performance
* VSCode [debugging](https://code.visualstudio.com/docs/python/debugging) with [launch.json](https://medium.com/geekculture/how-to-run-your-streamlit-apps-in-vscode-3417da669fc)
* Exclusions with `.gitignore`
* Linting via `.editorconfig`
