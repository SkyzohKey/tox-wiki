from django.shortcuts import render
import requests, json, markdown, config

# Yes this is fucking ugly. But it works. :)
CONFIG = config.get()
AUTH = "?client_id=%s&client_secret=%s" % (CONFIG['github']['client_id'], CONFIG['github']['client_key'])

def get_categories():
    url = "https://api.github.com/repos/%s/contents/" % (CONFIG['github']['repository'])
    url = url + AUTH
    req = requests.get(url)

    if(req.ok):
        return json.loads(req.text or req.content)

def category(request, category='.'):
    # GitHub API: https://api.github.com/repos/django/django/contents/(DIR_NAME|.)
    if(category == '.'):
        url = "https://api.github.com/repos/%s/contents/" % (CONFIG['github']['repository'])
    else:
        url = "https://api.github.com/repos/%s/contents/%s" % (CONFIG['github']['repository'], category)

    url = url + AUTH
    req = requests.get(url)

    if(req.ok):
        api = json.loads(req.text or req.content)
        return render(request, 'categories.html', {
            'git_repo': 'https://github.com/%s' % (CONFIG['github']['repository']),
            'api_url': url,
            'category': category,
            'Categories': api,
            'base_categories': get_categories()
        })


def page(request, category, page_name):
    # GitHub API: https://api.github.com/repos/django/django/contents/CATEGORY/FILE_NAME.md
    url = "https://api.github.com/repos/%s/contents/%s/%s" % (CONFIG['github']['repository'], category, page_name)
    url = url + AUTH
    req = requests.get(url)

    if(req.ok):
        api = json.loads(req.text or req.content)
        return render(request, 'wiki_page.html', {
            'name': api['name'],
            'path': api['path'].replace('.md', ''),
            'category': category,
            'git_path': api['path'],
            'git_url': api['_links']['html'],
            'git_size': api['size'],
            'git_sha1': api['sha'],
            'git_type': api['type'],
            'git_content': markdown.markdown(
                api['content'].decode(api['encoding']),
                ['markdown.extensions.extra']
            )
        })

    return render(request, 'page.html')
