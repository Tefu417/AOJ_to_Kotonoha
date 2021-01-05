with open('make_corpus/before_corpus_cima.txt', 'a') as newfile :
    with open('make_corpus/cleaned_cima.txt', 'r') as oldfile :
        for line in oldfile :
            if line[0] == '#' :
                l = line[2:-1]
                newfile.write('<SOS>' + l + '<tab>')
            else :
                l = line[:-1]
                newfile.write(l + '<EOS>')
                newfile.write('\n')
