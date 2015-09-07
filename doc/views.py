from django.shortcuts import render
import requests, json, markdown

CLIENT_ID = "340769ec4bd82d0dc94a"
CLIENT_SECRET = "5d1cc67a14b004b635f943f14723f996883e90d0"
GIT_ORG = "ToxClient"
GIT_REPO = "wiki"

def index(request):
    """
    # GitHub API: https://api.github.com/repos/django/django/contents/(DIR_NAME|.)
    url = "https://api.github.com/repos/%s/%s/contents/" % (GIT_ORG, GIT_REPO)
    url = url + "?client_id=%s&client_secret=%s" % (CLIENT_ID, CLIENT_SECRET)
    req = requests.get(url)

    if(req.ok):
        api = json.loads(req.text or req.content)
        return render(request, 'categories.html', {
            'git_repo': 'https://github.com/%s/%s' % (GIT_ORG, GIT_REPO),
            'api_url': url,
            'Categories': api
        })

    return render(request, 'page.html')
    """
    category(request, '.')

def category(request, category='.'):
    # GitHub API: https://api.github.com/repos/django/django/contents/(DIR_NAME|.)
    if(category == '.'):
        url = "https://api.github.com/repos/%s/%s/contents/" % (GIT_ORG, GIT_REPO)
    else:
        url = "https://api.github.com/repos/%s/%s/contents/%s" % (GIT_ORG, GIT_REPO, category)

    url = url + "?client_id=%s&client_secret=%s" % (CLIENT_ID, CLIENT_SECRET)
    req = requests.get(url)

    if(req.ok):
        api = json.loads(req.text or req.content)
        return render(request, 'categories.html', {
            'git_repo': 'https://github.com/%s/%s' % (GIT_ORG, GIT_REPO),
            'api_url': url,
            'category': category,
            'Categories': api
        })


def page(request, category, page_name):
    page_name = page_name.replace('.md', '')

    # GitHub API: https://api.github.com/repos/django/django/contents/CATEGORY/FILE_NAME.md
    url = "https://api.github.com/repos/%s/%s/contents/%s/%s.md" % (GIT_ORG, GIT_REPO, category, page_name)
    url = url + "?client_id=%s&client_secret=%s" % (CLIENT_ID, CLIENT_SECRET)
    req = requests.get(url)

    if(req.ok):
        api = json.loads(req.text or req.content)
        return render(request, 'wiki_page.html', {
            'path': api['path'].replace('.md', ''),
            'category': category,
            'git_path': api['path'],
            'git_url': api['_links']['html'],
            'git_size': api['size'],
            'git_sha1': api['sha'],
            'git_type': api['type'],
            'git_content': markdown.markdown(api['content'].decode(api['encoding']))
        })

    return render(request, 'page.html')
