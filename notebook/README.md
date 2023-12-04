
# RAG
## Environment Setup
### Conda install 
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh

source ~/.bashrc

conda update conda

conda create -n rag python=3.9


conda activate rag

### Setup python environment
1. Create and activate a python virtual environment
```
python3 -m venv rag05

source rag/bin/activate

```
2. Install dependencies
```
pip install -r requirements.txt 
```
### Jupyter 
3. _Run Jupyter_
```
jupyter lab --ip 0.0.0.0 --port 8888 --allow-root 

http://127.0.0.1:8888/lab?token=de2e7e6ab8f083e5d46e8fe2ca8a74a50633021da456c9d0

```    
