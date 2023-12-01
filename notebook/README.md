
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

conda activate ag5

### Setup python environment
1. Create and activate a python virtual environment
```
python3 -m venv rag05

source rag/bin/activate

```
2. Install dependencies
```
pip install -r requirements05.txt 
```
### Jupyter 
3. _Run Jupyter_
```
jupyter lab --ip 0.0.0.0 --port 8888 --allow-root 

http://34.134.116.199:8888/lab?token=de2e7e6ab8f083e5d46e8fe2ca8a74a50633021da456c9d0

```  

# Confluence LLM RAG App  

## Amaç: 10 tane belgede aramak veya 10 farklı kişiye sormak yerine, bilginin kaynağına kolayca RAG yaparak Large Languange Model'e bu soruyu sormak. 


LLM modelleri başlangıçta cümledeki bir sonraki kelimeyi tahmin edecek şekilde eğitilir. ancak bu araçlar halisünasyon yaratma ve önyargılı cevaplar verme eğilimindedir. bu sorunu çözmek için RAG (Retrieval Augmented Generation ) tekniğpi kullanılır. 

RAG hangi adımlardan oluşur: 

1- Chunkların oluşturuması ( Topyekün metni veremeyiz, Dil modellerinin dayattığı boyut sınırı vardır.)
2- Embeddingleri oluşturuması (textlerin  vector denilen float değerli tek boyutlu diziler ) 
3- Vectorleri saklama
4- Semantic search ( anlamsal olarak en yakını arama)


[Markdown Header Text Splitter](https://python.langchain.com/docs/modules/data_connection/document_transformers/text_splitters/markdown_header_metadata) Markdown sayfanın başlıklarını ve alt başlıklarını tanımlayarak Confluence sayfamızı böler. Akıllı bölmeye ek olarak, parçaların meta verileri, bulunan başlıklar ve alt başlıklarla desteklenir.


### Run Docker file 

``` 
docker build -t wikiqna:1.0 .
docker run  --rm  -it -p 7860:7860 --name wikiqna  wikiqna:1.0

```

