# 这是一个用来自建词表并完成encode的工具类，使用说明如下：
#### 1.构建词表格式如下
```text
    0 <SOS>
    1 <PAD>
    2 <EOS>
    3 <unfind>
    ………………
```
#### 2.How to build a vocab
```python
    from Vocab import Vocab
    vocab=Vocab()
    stop_list=["the","a","","(",")"]
    vocab.make_vocab(source="./test.csv",stop_list=stop_list)
    '''
        :param source:path or strlist of the source text
        :param stop: path or strlist of the stop words
        :param special: path or strlist of the speical words
    '''
```

#### 3.load a local vocab
```python
    vocab=Vocab("./vocab.csv")
```

#### 3.How to usr vocab
```python
    #showvocab
    vocab.showVocab()
    #word2idx
    print(vocab.word2idx("love"))
    #idx2word
    print(vocab.idx2word(1))
    #encode
    print(vocab.encode(["i","love","you"]))
    print(vocab.encode(["i","love","you"],padding_len=5))
    #decode
    print(vocab.decode([55, 71, 23]))
```