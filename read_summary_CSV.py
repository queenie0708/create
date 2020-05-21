import csv

def _main():
    text = open("all_summary.csv", "r")
    text = ''.join([i for i in text]) \
        .replace(" ANR", ",ANR") \
        .replace(" App_crash",",App_crash") \
        .replace(" Tombstone",",Tombstone")
    x = open("new.csv","w")
    x.writelines(text)
    x.close()
    with open("new.csv",'rt') as myFile:
        lines=csv.reader(myFile)
        for line in lines:     #line[1] error type,  line[0] error count, line[2] packagename
            if int(line[0]) > 5:
                print('python3 read_error_CSV.py -f all_new.csv -e ' + line[1] + ' -p ' + line[2] + ' -b V0.170') 

if __name__ == '__main__':
    _main()