"""Reject local-preview URLs in the actual GitHub Pages output, including redirects."""
from pathlib import Path
import re
import sys

BAD_URL=re.compile(r'https?://(?:localhost|127\.0\.0\.1|0\.0\.0\.0|\[::1\])(?=[:/])',re.I)
def check_publication(root):
    root=Path(root)
    assert (root/'index.html').is_file(), 'Missing published homepage'
    failures=[]
    for path in root.rglob('*'):
        if path.suffix in {'.html','.xml'}:
            text=path.read_text(encoding='utf-8')
            if BAD_URL.search(text) or '/livereload.js' in text:
                failures.append(str(path.relative_to(root)))
    assert not failures, 'Preview output must not be published: '+', '.join(failures[:20])
    print(f'Publication check passed: {root} has no loopback URLs or live-reload scripts.')
if __name__=='__main__':check_publication(sys.argv[1] if len(sys.argv)>1 else 'docs')
