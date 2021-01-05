with open('corpus_cima.txt', 'a') as newfile :
    with open('make_corpus/before_corpus_cima.txt', 'r') as oldfile :
        for line in oldfile :
            tab = line.find('<tab>')
            py = line[tab+5:-6]
            pj = line[5:tab]
            l = '<SOS>' + py + '<tab>' + pj + '<EOS>'
            newfile.write(l)
            newfile.write('\n')