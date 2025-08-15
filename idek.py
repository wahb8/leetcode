##### TESTING PULLS FOR THE FIRST TIME IN MY LIFE
import numpy as np
from collections import deque, defaultdict, Counter

# 1. Burrows-Wheeler Transform (BWT)
def bwt_transform(block: bytes) -> (bytes, int):
    n = len(block)
    rotations = [block[i:] + block[:i] for i in range(n)]
    rotations_sorted = sorted(rotations)
    last_column = bytes(row[-1] for row in rotations_sorted)
    primary_index = rotations_sorted.index(block)
    return last_column, primary_index

# 2. Move-to-Front (MTF) encoding
def mtf_encode(data: bytes) -> list:
    symbols = list(range(256))
    output = []
    for b in data:
        idx = symbols.index(b)
        output.append(idx)
        symbols.pop(idx)
        symbols.insert(0, b)
    return output

# 3. LZ77 tokenization
def lz77_tokenize(data: list, window_size=65536, min_match=4, max_match=258):
    tokens = []
    n = len(data)
    pos = 0
    while pos < n:
        end = max(0, pos - window_size)
        best_len = 0
        best_off = 0
        for off in range(1, min(pos, window_size) + 1):
            length = 0
            while length < max_match and pos+length < n and data[pos+length] == data[pos-off+length]:
                length += 1
            if length > best_len:
                best_len, best_off = length, off
            if best_len >= max_match:
                break
        if best_len >= min_match:
            tokens.append(('MATCH', best_off, best_len))
            pos += best_len
        else:
            tokens.append(('LIT', data[pos]))
            pos += 1
    return tokens

# 4. Sequitur grammar inference
class Sequitur:
    def __init__(self):
        self.rules = {}  # nonterminal -> sequence
        self.digram_index = {}
        self.next_symbol = 256

    def process(self, tokens):
        output = []
        for t in tokens:
            output.append(t)
            self._check_rules(output)
        return output, self.rules

    def _check_rules(self, output):
        if len(output) < 2:
            return
        digram = tuple(output[-2:])
        if digram in self.digram_index:
            # found repeat — create or reuse rule
            prev_pos = self.digram_index[digram]
            nt = self.next_symbol
            self.next_symbol += 1
            self.rules[nt] = list(digram)
            # replace both occurrences
            output[-2:] = [('NT', nt)]
            # naive replacement for previous occurrence
            # (omitted for brevity)
        else:
            self.digram_index[digram] = len(output) - 2

# 5. Neural context mixer stub
def neural_predict(context):
    # stub: uniform probability
    return 0.5

# 6. ANS encoding stub
class ANSEncoder:
    def __init__(self):
        self.state = 0
        self.output = []

    def encode(self, symbol, prob):
        # stub: append (symbol,prob)
        self.output.append((symbol, prob))

    def finalize(self):
        return self.output

# 7. NeoComp compression pipeline
def neocomp_compress(data: bytes) -> dict:
    blocks = [data[i:i+65536] for i in range(0, len(data), 65536)]
    frames = []
    for block in blocks:
        bwt_block, primary_idx = bwt_transform(block)
        mtf_block = mtf_encode(bwt_block)
        tokens = lz77_tokenize(mtf_block)
        seq = Sequitur()
        tokens, grammar = seq.process(tokens)

        ans = ANSEncoder()
        for sym in tokens:
            # define contexts (stub)
            ctx = None
            p = neural_predict(ctx)
            ans.encode(sym, p)
        bitstream = ans.finalize()

        frames.append({
            'primary_idx': primary_idx,
            'grammar': grammar,
            'bitstream': bitstream
        })
    return {'frames': frames}

if __name__ == "__main__":
    sample = b"This is an example text to compress with NeoComp! \n"
    result = neocomp_compress(sample)
    print(result)  # demonstration of pipeline

