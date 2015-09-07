from django.shortcuts import render
import requests, json, markdown

CLIENT_ID = "340769ec4bd82d0dc94a"
CLIENT_SECRET = "5d1cc67a14b004b635f943f14723f996883e90d0"

def index(request):
    # GitHub API: https://api.github.com/repos/django/django/contents/(DIR_NAME|.)
    url = "https://api.github.com/repos/ToxClient/wiki/contents/"
    url = url + "?client_id=%s&client_secret=%s" % (CLIENT_ID, CLIENT_SECRET)
    req = requests.get(url)

    if(req.ok):
        api = json.loads(req.text or req.content)
        return render(request, 'categories.html', {'Categories': api})

    return render(request, 'page.html')

def page(request, category, page_name):
    # GitHub API: https://api.github.com/repos/django/django/contents/CATEGORY/FILE_NAME.md
    url = "https://api.github.com/repos/ToxClient/wiki/contents/%s/%s.md" % (category, page_name)
    url = url + "?client_id=%s&client_secret=%s" % (CLIENT_ID, CLIENT_SECRET)
    req = requests.get(url)

    if(req.ok):
        api = json.loads(req.text or req.content)
        return render(request, 'wiki_page.html', {
            'path': api['path'].replace('.md', ''),
            'git_path': api['path'],
            'git_url': api['_links']['html'],
            'git_size': api['size'],
            'git_sha1': api['sha'],
            'git_type': api['type'],
            'git_content': markdown.markdown(api['content'].decode(api['encoding']))
        })

    return render(request, 'page.html')
