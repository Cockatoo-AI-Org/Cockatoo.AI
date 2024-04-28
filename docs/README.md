# Preface

The docs/README file is a place intended to record folder structure, sphinx, model/IT/technical details,
while the root/READE me is more towards the whole picture of the project, its concept, and its roadmap.

# Folder Structure

The tree structre (excluding files and unimportant chache dirs) of the repo is displayed below:

Cockatoo.AI/
┣ .github/
┃ ┗ workflows/
┣ demo/
┣ docs/
┣ experiments/
┃ ┗ langchain_lab/
┃ ┗ model_a_eval/
┣ src/
┗ tests/

* `src/`: store source codes mainly .py files.
* `experiments/`: store experiment files. I created an empty .ipynb file to keep Git able to detect and upload the folder.
  - `experiments/langchain_lab/`: We put the sample codes of [`LangChain`](https://python.langchain.com/docs/get_started/introduction) here.
  - `experiments/model_a_eval/`: We put the code/framework to evaluate model A
    here.
* `demo/`: store any files related to demos in the future.
* `docs/`: store documentation files, eg. conf.py or some sphinx related html, css etc will be stored in the folder.
  - Note: `docs/conf.py` is intended to be used later for the configuration of sphinx for class/func documentation

* `tests/`: store testing .py files for code base unit/integration... testing.
* `.github/workflows`: store any workflow related to CI/CD.
