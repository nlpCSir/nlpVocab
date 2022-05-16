from Vocab import Vocab


vocab=Vocab("vocab.csv")

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
