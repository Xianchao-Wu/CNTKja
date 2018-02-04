import glob
import codecs
import json

def update_cell(cell, d):
    if cell['cell_type'] == 'markdown':
        k = ''.join(cell['source'])
        cell['metadata']['original_source'] = cell['source']
        cell['source'] = d[k]

for fname in glob.glob('./Tutorials/CNTK_*.ipynb'):
    outfname = fname.replace('./Tutorials/', './Tutorials_ja/').replace('.ipynb', '_ja.ipynb')
    print('Cleaning %s' % (outfname,))
    with codecs.open(outfname, 'r', 'utf-8') as f:
        doc = json.load(f)
    d = {
        ''.join(x['metadata']['original_source']): x['source']
        for x in doc['cells']
        if x['cell_type'] == 'markdown' and 'original_source' in x['metadata'] 
    }
    with codecs.open(fname, 'r', 'utf-8') as f:
        doc = json.load(f)
    for cell in doc['cells']:
        update_cell(cell, d)
    with codecs.open(outfname, 'w', 'utf-8') as f:
        json.dump(doc, f, indent=1, ensure_ascii=False, sort_keys=True)
