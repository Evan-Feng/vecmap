import pickle
import embeddings
import numpy as np

def main():
    for lang in ('en', 'es', 'ca', 'eu'):
        with open('emb/wiki.%s.vec' % lang, encoding='utf-8', errors='surrogateescape') as fin:
            with open('emb/%s.bin' % lang, 'wb') as fout:
                pickle.dump(embeddings.read(fin, dtype='float32'), fout)


if __name__ == '__main__':
    main()
