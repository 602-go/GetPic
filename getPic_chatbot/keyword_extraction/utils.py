from collections import Counter
from scipy.sparse import csr_matrix


def scan_vocabulary(sents, tokenize=None, min_count=2):
    """
    Arguments
    ---------
    sents : list of str
        Sentence list
    tokenize : callable
        tokenize(str) returns list of str
    min_count : int
        Minumum term frequency

    Returns
    -------
    idx_to_vocab : list of str
        Vocabulary list
    vocab_to_idx : dict
        Vocabulary to index mapper.
    """
    # counter = Counter(w for sent in sents for w in tokenize(sent))
    counter = Counter(w for sent in sents for w in tokenize.tokenizer(sent))    # sents는 문장 집합 리스트 
                                                                                # sent는 각 문장, 각 문장별로 토크나이징
    counter = {w: c for w, c in counter.items() if c >= min_count}              # min_count 미만으로 등장한 단어 제거
    idx_to_vocab = [w for w, _ in sorted(counter.items(), key=lambda x:-x[1])]  # 등장빈도 기준 내림차순 정렬 -> 단어 리스트
    vocab_to_idx = {vocab:idx for idx, vocab in enumerate(idx_to_vocab)}        # key: 단어, value:등장빈도
    return idx_to_vocab, vocab_to_idx   


def tokenize_sents(sents, tokenize):
    """
    Arguments
    ---------
    sents : list of str
        Sentence list
    tokenize : callable
        tokenize(sent) returns list of str (word sequence)

    Returns
    -------
    tokenized sentence list : list of list of str
    """
    return [tokenize.tokenizer(sent) for sent in sents]

def vectorize(tokens, vocab_to_idx):
    """
    Arguments
    ---------
    tokens : list of list of str
        Tokenzed sentence list
    vocab_to_idx : dict
        Vocabulary to index mapper

    Returns
    -------
    sentence bow : scipy.sparse.csr_matrix
        shape = (n_sents, n_terms)
    """
    rows, cols, data = [], [], []
    for i, tokens_i in enumerate(tokens):
        for t, c in Counter(tokens_i).items():
            j = vocab_to_idx.get(t, -1)
            if j == -1:
                continue
            rows.append(i)
            cols.append(j)
            data.append(c)
    n_sents = len(tokens)
    n_terms = len(vocab_to_idx)
    x = csr_matrix((data, (rows, cols)), shape=(n_sents, n_terms))
    return x
