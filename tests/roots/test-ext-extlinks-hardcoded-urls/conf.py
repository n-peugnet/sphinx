extensions = ['sphinx.ext.extlinks']
extlinks = {
    # links with printf style formatted caption
    'issue': ('https://github.com/sphinx-doc/sphinx/issues/%s', 'issue %s'),
    # links with non-formatted caption
    'wikipedia': ('https://en.wikipedia.org/wiki/%s', 'Wikipedia'),
}
extlinks_detect_hardcoded_links = True
