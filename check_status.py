import codecs
import glob
import json

def is_markdown(cell):
    return cell['cell_type'] == 'markdown'

def is_unchecked(cell):
    source = cell['source']
    if isinstance(source, list):
        source = ''.join(source)
    return '_unchecked_' in source

fnames = list(glob.glob('./Tutorials_ja/CNTK_*_ja.ipynb'))
fnames = sorted(fnames)

for fname in fnames:
    with codecs.open(fname, 'r', 'utf-8') as f:
        doc = json.load(f)
    x = [int(is_unchecked(cell)) for cell in doc['cells'] if is_markdown(cell)]        
    progress = (1 - sum(x) / len(x))
    stem = fname.split('/')[-1]
    print("%d%%\t%s" % (progress * 100, stem))
