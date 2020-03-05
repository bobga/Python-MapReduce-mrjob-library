from mrjob.job import MRJob
from mrjob.step import MRStep
import re

WORD_RE = re.compile(r"[\w']+")
class MRFindMaxValue(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_values,
                   combiner=self.combiner_max_values,
                   reducer=self.reducer_max_values),
            MRStep(reducer=self.reducer_find_max_value)
        ]
    def mapper_get_values(self, _, line):
        for value in WORD_RE.findall(line):
            yield (value, int(value))

    def combiner_max_values(self, word, values):
        yield (word, max(values))

    def reducer_max_values(self, word, values):
        yield None, ('max', max(values))

    def reducer_find_max_value(self, _, value_max_pairs):
        yield max(value_max_pairs)
if __name__ == '__main__':
    MRFindMaxValue.run()