---
layout: note
cdate: "Dec 10, 2020"
mdate: "Dec 10, 2020"
title: "Notes on RL"
category: NLP
index: 0
headline: 
picture: 
---

#### Tokenization

- **Stemming**: leave the root of the word.
Problems: overstemming ($universal,\;university \rightarrow univers$) and understamming ($data,\;datum \rightarrow dat,\;datu$)
    - nltk.stem.SnowballStemmer (most useful)
    - nltk.stem.PorterStemmer
    - nltk.stem.WordNetLemmatizer
    - nltk.corpus.stopwords

- **Lemmatization**: get a dictionary form of a word 

#### Bag of Words
How to improve BoW? - Use **collocations** (meaningful n-gramms) instead of words. 

Delete
- high frequency n-gramms
    - articles, prepositions
    - auxiliary verbs, 
    - general vocabulary

- low frequency n-gramms
    - typos
    - something extremely rare (1-2 occurrences)

#### TF-IDF (Term Frequency - Inverse Document Frequency)
- $tf$ gives us the frequency of the word $tT in each document $d$ in the corpus.
\\[
\begin{equation}
tf(t, d) =freq(t|d)
\end{equation}
\\]
- $idf$ is used to calculate the weight of rare words across all documents in the corpus.
\\[
\begin{equation}
idf(t, D) = \log{\frac{N}{\|d \in D \: t \in d\|}}
\end{equation}
\\]
where $N$ is the total number of documents in the corpus $D$, $\|d \in D \: t \in d\|$ is the number
of documents containing the term $t$. The terms that occur rarely in the corpus have high $idf$ value.

### Word embeddings

#### Pointwise Mutual Information + SVD

\\[
\begin{equation}
PMI = \log \frac{p(u, v)}{p(u) p(v)} = \log \frac{n_{uv}n}{n_u n_v}
\end{equation}
\\]
where $n_{uv}$ in the number of times the words $u$ and $v$ occur together in the window of fixed size.

We construct a **PMI Matrix** is a square matrix where each row represents word $u$ and each column represents word $v$.
Now we apply SVD to **PMI Matrix** that gives us vectorized representation of words.

#### Word2Vec


#### Word embeddings in different languages

- word embeddings for different languages are quite similar
- $\\{x_i, y_i\\}, \; i=1,..,N$ - is the set of word-translation pairs
- learn linear mapping between the source and the target spaces
\\[
\begin{equation}
W^{\ast} = argmin||WX - Y||
\end{equation}
\\]

- additional orthogonality constraint on matrix $W^{*}$ produces a better result
\\[
\begin{equation}
W^{\ast} = argmin||WX - Y|| = UV^T,\;\text{with}\;U\Sigma V^T = SVD(YX^T)
\end{equation}
\\]

The translation $\hat{y} = argmax(\cos(Wx_s, y_x))$. Cosine distance focuses on the angle between vectors.

<br>
## Links
- [Controlled Experiments for Word Embeddings](https://arxiv.org/pdf/1510.02675.pdf)
