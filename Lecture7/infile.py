infile = open('params.txt','r')
intext = infile.read()

preamble = '#'+str(input('Cosa vuoi dire nella prima riga del file?\n'))

outfile = open('outfile.txt','w')
outfile.write(preamble+'\n')

#Per prendere il file di peso
outfile.write(intext)

#Per trascrivere il file riga per riga
intext.splitlines()
outfile.close()