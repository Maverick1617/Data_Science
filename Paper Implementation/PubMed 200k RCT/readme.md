# PubMed 200k RCT
link - https://arxiv.org/abs/1710.06071

## Description - 
This notebook is a replica model of the research PubMed 200k RCT.
The model summarizes a large document into five categorical classes (Background, Methods, Objectives, Conclusion, and Result) making the document easier to read.

`For further details or research work read` https://arxiv.org/pdf/1710.06071.pdf

## Contents - 

**There are four models trained for each separate part of the model and one combined (complete replica) model-**

* Model 0 - This model is a baseline model for comparing other model progress.
* Model 1 - This model replicates the token embedding model from the research paper.
* Model 2  - This is again the model as "Model 2" but with transfer learning for token vectorization (tfh model - https://tfhub.dev/google/universal-sentence-encoder/4)
* Model 3  - This model replicates the character embedding model from the research paper.
* Model 4 - This model concatenate model 3 and 2  and trains upon them ( the lower part of the model).
* Model 5 - The complete replica of the model architecture ( https://arxiv.org/pdf/1612.05251.pdf ).


## Credits-
`Thanks to-` 
* Franck Dernoncour MIT francky@mit.edu 
* Ji Young Lee MIT jjylee@mit.edu
* Peter Szolovits MIT psz@mit.edu
for the `dataset and neural network model architecture :)`
