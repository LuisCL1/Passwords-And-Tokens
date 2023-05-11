def splitCsv(inputFile,outputName,lines):
    with open(inputFile,'r') as file:
        header = file.readline().strip()
        outputFile=None
        linecount=0
        for line in file:
            if linecount % lines ==0:
                if outputFile is not None:
                    outputFile.close()
                outputFile=open(f"{outputName}_{linecount//lines}.csv",'w')
                outputFile.write(header+'\n')
            outputFile.write(line)
            linecount+=1
    if outputFile is not None:
        outputFile.close()




if __name__ =="__main__":
    splitCsv('usuarios.csv','output',1000)