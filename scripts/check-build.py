"""Build production and drafts in temporary folders, and verify archive routes/assets."""
import csv
import hashlib
from html.parser import HTMLParser
import io
from pathlib import Path
import subprocess
import tempfile
from urllib.parse import urlsplit, unquote
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
HUGO=str(ROOT/'scripts/hugo')
from check_publication import check_publication
class Page(HTMLParser):
    def __init__(self):super().__init__();self.assets=[];self.links=[];self.canonical=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag in ('img','script') and a.get('src'):self.assets.append(a['src'])
        if tag=='link' and a.get('rel')=='stylesheet':self.assets.append(a['href'])
        if tag=='link' and a.get('rel')=='canonical':self.canonical.append(a['href'])
        if tag=='a' and a.get('href'):self.links.append(a['href'])
def file_for(dest,url):
    path=unquote(urlsplit(url).path)
    return dest/path.lstrip('/')/('index.html' if path.endswith('/') else '')
def document(path):
    p=Page();p.feed(path.read_text());return p
with tempfile.TemporaryDirectory(prefix='hugo-blog-check-') as folder:
    base=Path(folder)
    for drafts in (False,True):
        dest=base/('drafts' if drafts else 'production')
        flags=['--buildDrafts'] if drafts else []
        subprocess.run([HUGO,*flags,'--destination',str(dest),'--cacheDir',str(base/'cache'),'--noBuildLock','--panicOnWarning'],check=True,cwd=ROOT)
        command=[HUGO,'list','all' if drafts else 'published']
        rows=list(csv.DictReader(io.StringIO(subprocess.check_output(command,cwd=ROOT,text=True))))
        for row in rows:
            if row['kind']!='page':continue
            path=file_for(dest,row['permalink'])
            assert path.is_file(),f'Missing content route: {row["permalink"]}'
        for route in ['/', '/post/', '/tags/', '/categories/', '/page/2/']:
            assert file_for(dest,route).is_file(),route
        for xml in ['index.xml','sitemap.xml']:ET.parse(dest/xml)
        if not drafts:check_publication(dest)
        all_rows=list(csv.DictReader(io.StringIO(subprocess.check_output([HUGO,'list','all'],cwd=ROOT,text=True))))
        for item in all_rows:
            if item['draft']=='true':
                assert file_for(dest,item['permalink']).exists()==drafts, item['path']
        article=next(r for r in all_rows if 'photo-revival' in r['path'])
        post_url=article['permalink']
        if drafts:
            page=document(file_for(dest,post_url))
            assert page.canonical==[post_url],page.canonical
            assert 'https://github.com/conoro/photo-revival' in page.links
            assert '/index.xml' in page.links, 'Footer must link to the site feed'
            for asset in page.assets:
                u=urlsplit(asset)
                if not u.netloc and not u.scheme:
                    assert file_for(dest,asset).is_file(),f'Missing post asset: {asset}'
            photos=[a for a in page.assets if '/photo-revival/' in a]
            assert len(photos)==4,photos
            for url in photos:
                original=ROOT/'static'/url.lstrip('/')
                assert hashlib.sha256(original.read_bytes()).digest()==hashlib.sha256(file_for(dest,url).read_bytes()).digest()
        print(f'{"Draft" if drafts else "Production"} build: {len(rows)} content routes checked; archives, feeds and assets passed.')
