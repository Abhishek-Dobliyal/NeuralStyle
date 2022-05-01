# NeuralStyle
Style your snaps with the power of Deep Learning. Deployed [Here](https://neural-style.netlify.app/)

![](neural_style_demo.gif)

## Installations and Dependencies

- [Python](https://www.python.org) Installed.
- [NodeJS](https://nodejs.org/en/) Installed.
- [VGG19 NoTop](https://github.com/fchollet/deep-learning-models/releases/tag/v0.1) Weights File.
- [VueJS](https://vuejs.org/) Installed.

## Usage

### Backend

- Open Terminal/ Command Prompt and type in:

> Windows Users

```bash
pip install -r /path/to/requirements.txt
```

> MacOS/Linux Users

```bash
pip3 install -r /path/to/requirements.txt
```

- Inside the Repository's directory, Open Terminal/ Command Prompt and type in:

> Windows Users

```bash
python app.py
```

> MacOS/Linux Users

```bash
python3 app.py
```

- The above command should result in something like this:
```bash
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [16864] using statreload
INFO:     Started server process [16874] 
INFO:     Waiting for application startup. 
```

### Frontend

- Open Terminal/ Command Prompt, then navigate to the `frontend` directory and type in:

```bash
npm run serve
```

- The above command should result in something like this:
```bash
> frontend@0.1.0 serve
> vue-cli-service serve

 INFO  Starting development server...


 DONE  Compiled successfully in 7988ms                                                                     16:50:41


  App running at:
  - Local:   http://localhost:8080/ 
  - Network: http://192.168.134.61:8080/
```

## Note

- Kindly do not move, delete, rename or modify any files (unless you know what you are doing).

- The stylization process depends on your system's specifications (GPU is recommended).

## Todo

- [ ] Improve Styling
- [ ] Work on issues (if any)
