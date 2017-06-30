$def with (data=None)

[this:author:name]:  # ($:(data['author_name']))
[this:author:email]: # ($:(data['author_email']))

__*I / II / III / IV*__

# A

__[a](#) | [b](#) | [c](#)__

$if data['toc']: $:render.partials.toc(data['permalink'], data['toc'])

$:render.pages.home()

## A.1

---

__[< PREV](#) | [NEXT >](#)__
