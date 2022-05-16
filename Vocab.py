import numpy  as np
import pandas as pd
from  collections import Counter
class Vocab:
    def __init__(self,vocab_path=None):
        self.vocab_dict = []
        self.vocab_list = []
        if vocab_path==None:
            print("----------------tips--------------------")
            print("你没有传入vocab的路径，如果需要自己构建词表，请调用make_vocab(source,stoplist,special_list)方法")
            print("""
            :param source:path or strlist of the source text
            :param stop: path or strlist of the stop words
            :param special: path or strlist of the speical words""")
            print("----------------------------------------")
        else:
            df=pd.read_csv(vocab_path,names=["idx","word"],sep=" ")
            self.vocab_list=df["word"].tolist()
            self.vocab_dict = {word: self.vocab_list.index(word) for word in self.vocab_list}

    def make_vocab(self,source,stop_list=None,special_list=["<SOS>","<PAD>","<EOS>","<unfind>"]):
        '''
        :param source:path or strlist of the source text
        :param stop: path or strlist of the stop words
        :param special: path or strlist of the speical words
        '''
        assert isinstance(source,str),"param source should be str(path)"
        if(stop_list!=None):
            assert isinstance(stop_list,list),"param stop should be  strlist"
        if(special_list!=None):
            assert isinstance(special_list, list), "param special should be strlist"
        vocab=Counter()
        #加载vocab
        source_data=np.array(pd.read_csv(source)).squeeze(-1)
        slist=source_data.tolist()
        for sentence in slist:
            char_list=sentence.split(" ")
            # print(char_list)
            vocab+=Counter(char_list)

        #去除停用词
        if stop_list!=None:
            for s in stop_list:
                # print(s)
                del(vocab[s])

        #获取vocab_list,加载特殊字符并保存字典csv
        self.vocab_list=[i[0] for i in vocab.most_common()]
        #增加特殊词
        '''
        常用标识符如下
        <UNK>: 低频词或未在词表中的词
        <PAD>: 补全字符
        <GO>/<SOS>: 句子起始标识符
        <EOS>: 句子结束标识符
        [SEP]：两个句子之间的分隔符
        [MASK]：填充被掩盖掉的字符
        <CLS>：用在Bert中
        '''
        special_list.extend(self.vocab_list)

        self.vocab_list=special_list
        self.vocab_dict={word:self.vocab_list.index(word) for word in self.vocab_list}
        pd.DataFrame(self.vocab_list).to_csv("vocab.csv", sep=" ", header=None)

    def showVocab(self):
        # print(self.vocab)
        print(self.vocab_dict)

    def idx2word(self,idx):
        assert idx<len(self.vocab_list),"idx out of the vocab_list"
        return self.vocab_list[idx]

    def word2idx(self,word):
        return self.vocab_dict.get(word,self.vocab_dict["<unfind>"])

    def decode(self,idx_list):
        return [self.idx2word(idx) for idx in idx_list]

    def encode(self,word_list,padding_len=None):
        '''
        :param word_list:
        :param padding_len:the padding length,if None:no padding
        :return:
        '''
        result=[self.word2idx(word) for word in word_list]
        if padding_len!=None:
            return result+[self.word2idx("<PAD>")]*(padding_len-len(result))
        else:
            return [self.word2idx(word) for word in word_list]

