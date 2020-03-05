from mrjob.job import MRJob
import re

WORD_RE = re.compile(r"[\w']+")
class MRFIndMeanValue(MRJob):
    def mapper(self, _, line):
        lines = line.split('\n')
        for word in WORD_RE.findall(line):
            yield word, lines

    def reducer(self, word, lines):
        temp = list()
        for i in lines:
            temp.extend(i)
        yield word, temp

if __name__ == '__main__':
    MRFIndMeanValue.run()