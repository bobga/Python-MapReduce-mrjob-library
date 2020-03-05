from mrjob.job import MRJob
import re

WORD_RE = re.compile(r"[\w']+")
class MRFIndMeanValue(MRJob):
    def mapper(self, _, line):
        for value in WORD_RE.findall(line):
            yield None, int(value)

    def reducer(self, key, values):
        i, totalL, totalW = 0, 0, 0
        for i in values:
            totalL += 1
            totalW += i
        yield "mean", totalW / totalL

if __name__ == '__main__':
    MRFIndMeanValue.run()