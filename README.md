

## Requirements
```
streamlit_lottie==0.0.2
streamlit==1.3.0
requests==2.24.0
Pillow==8.4.0
protobuf~=3.19.0
watchdog==2.1.8
```

## Run the app
* Terminal
    ```
    # vanilla terminal
    streamlit run app.py

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

## Author
* Sven from Coding Is Fun
* YouTube: https://youtube.com/c/CodingIsFun
* Website: https://pythonandvba.com

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/X7X47Q0EG)

## Feedback
#  If you have any feedback, please reach out to me at contact@pythonandvba.com
#  ![Logo](https://www.pythonandvba.com/banner-img)

## Addendum
[@pythoninthegrass](https://github.com/pythoninthegrass) additions
* Setup [Poetry](https://python-poetry.org/docs/#installation), [reverted protobuf](https://discuss.streamlit.io/t/typeerror-descriptors-cannot-not-be-created-directly/25639/11)
* Added [watchdog](https://docs.streamlit.io/library/advanced-features/configuration) for performance
* VSCode [debugging](https://code.visualstudio.com/docs/python/debugging) with [launch.json](https://medium.com/geekculture/how-to-run-your-streamlit-apps-in-vscode-3417da669fc)
* Exclusions with `.gitignore`
* Linting via `.editorconfig`
