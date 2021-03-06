"""
Solve the Suffix Tree Construction Problem.
"""
import bio.io_utils
import bio.triee

def do_work(source):
    text = source.next()
    for s in source: pass # eat source
    t = bio.triee.suffix_trie()
    t.construct(text)
    tt = bio.triee.suffix_tree()
    tt.from_trie(t)
    return tt.emit_edges_as_text()

bio.io_utils.generate_input_output(do_work, True)
