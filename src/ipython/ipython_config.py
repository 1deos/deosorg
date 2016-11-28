c = get_config()
c.StoreMagics.autorestore = True
c.InteractiveShell.editor = 'vim'
c.AliasManager.user_aliases = [
    ('git', 'git'),
    ('vi', 'vim'),
    ('screen', 'screen'),
    ('make', 'make'),
    ('pip', 'pip'),
    ('node', 'node'),
    ('npm', 'npm')
]
