
# Confluence LLM RAG App  - WikiQnA

## Amaç: 10 tane belgede aramak veya 10 farklı kişiye sormak yerine, bilgi kaynağına kolayca RAG yaparak Large Languange Model'e bu soruyu sormak. 


LLM modelleri başlangıçta cümledeki bir sonraki kelimeyi tahmin edecek şekilde eğitilir. ancak bu araçlar halisünasyon yaratma ve önyargılı cevaplar verme eğilimindedir. bu sorunu çözmek için RAG (Retrieval Augmented Generation ) tekniği kullanılır. 

RAG hangi adımlardan oluşur: 

1- Chunkların oluşturuması ( Topyekün metni veremeyiz, Dil modellerinin dayattığı boyut sınırı vardır.)
2- Embeddingleri oluşturuması (textlerin  vector denilen float değerli tek boyutlu diziler ) 
3- Vectorleri saklama
4- Semantic search ( anlamsal olarak en yakını arama)
 
![image](https://github.com/devops-alierdogan/wikiqna/assets/132436988/3abb1f80-8a3e-4f49-98d2-8fc2ba9aa955)


## TODOs
- [X]  load pre-defined collection 
- [ ]  upload file for DocumentQnA
- [ ]  Allow open-source LLMs
- [ ]  Streaming response
- [X]  Add docker/docker compose


### Run Docker file 

``` 
docker build -t wikiqna:1.0 .
docker run  --rm  -it -p 7860:7860 --name wikiqna  wikiqna:1.0

```
