## Major Iterations
* Achieved language choice consistency throughout the pages.
* Added content regarding my personal experience and career.
* Added support for multiple languages taking the idea from Rsirp0c of using a constants file.
* Changed template visuals by changing the ./streamlit/config.toml 
* Added multi-page with streamlit sidebar and /pages.

## Future Ideas
1 - Creation of a blog/posting space. 
  1.1 - I want to create a posting area to present books that I'm reading or I have read and maybe debate about them. 

2 - Creation of a back-end to interact with the client side. 
  2.2 - As a first instance I can try just to connect a postgreSQL database and maybe recover sentences(or wtv!) from it via a button.
  2.3 - But ideally I want to create a small API that we'll hide the business logic from the client connecting to the database and returning the response.

## Snapshots
Here are some snapshots of this whole project:

Home page snapshot:

![TO BE ADDED](/images/snapshot_contact.png)

Projects page snapshot:

![TO BE ADDED](/images/snapshot_contact.png)

Resume page snapshot:

![TO BE ADDED](/images/snapshot_contact.png)

Contact page snapshot:

![Alt text](/images/snapshot_contact.png)

And you can check this project live over here:

* To Be Added

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
* morrison93 forked from Sven's Bo repo (https://github.com/Sven-Bo/personal-website-streamlit)
* Template from Rsirp0c: (https://github.com/Rsirp0c/portfolio/blob/main/%F0%9F%8F%A0_Mainpage.py)

Please bear in mind that although I took these two projects as references I have iterated and will still iterate upon these solutions.

## Addendum
[@pythoninthegrass](https://github.com/pythoninthegrass) additions
* Setup [Poetry](https://python-poetry.org/docs/#installation), [reverted protobuf](https://discuss.streamlit.io/t/typeerror-descriptors-cannot-not-be-created-directly/25639/11)
* Added [watchdog](https://docs.streamlit.io/library/advanced-features/configuration) for performance
* VSCode [debugging](https://code.visualstudio.com/docs/python/debugging) with [launch.json](https://medium.com/geekculture/how-to-run-your-streamlit-apps-in-vscode-3417da669fc)
* Exclusions with `.gitignore`
* Linting via `.editorconfig`
