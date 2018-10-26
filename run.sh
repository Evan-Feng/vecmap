for i in `seq 1 3`
do
    for lang in es ca eu
    do
        python -u map_embeddings.py --verbose --pickle --batch_size 3000 --cuda --unsupervised emb/en.bin emb/$lang.bin checkpoints/en-$lang-vecmap-$i.bin
    done
done
