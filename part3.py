from mrjob.job import MRJob
import re

WORD_RE = re.compile(r"[\w']+")
class MRFIndMeanValue(MRJob):
    def mapper(self, _, line):
        for value in WORD_RE.findall(line):
            yield None, value

    def reducer(self, key, values):
        t1 = list()
        t2 = list()
        c = 0
        for i in values:
            if c % 2 == 0:
                t1.append(i)
            else:
                t2.append(i)
            c += 1
        j = 0
        while j < len(t2):

            k = 0
            while k < len(t1):
                if t2[j] == t1[k]:
                    yield "(u, v, w)", (t1[j], t2[j], t2[k])
                k += 1
            j += 1

if __name__ == '__main__':
    MRFIndMeanValue.run()