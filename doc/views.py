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

def get_url(url, add_url = '', add_auth=True):
    if(add_auth):
        url += AUTH

    url += add_url

    req = requests.get(url)
    if(req.ok):
        return req
    else:
        return False

def category(request, category='.'):
    # GitHub API: https://api.github.com/repos/django/django/contents/(DIR_NAME|.)
    
    ## Get the last commit.
    last_commit_response = get_url("https://api.github.com/repos/%s/commits" % (CONFIG['github']['repository']), '&per_page=1')
    last_commit_api = json.loads(last_commit_response.text or last_commit_response.content)

    if(category == '.'):
        ## Get the index page.
        response = get_url("https://api.github.com/repos/%s/contents/Index.md" % (CONFIG['github']['repository']))
        api = json.loads(response.text or response.content)

        return render(request, 'categories.html', {
            'git_repo': 'https://github.com/%s' % (CONFIG['github']['repository']),
            'category': category,
            'Categories': api,
            'base_categories': get_categories(),

            # Last commit related stuff
            'last_commit_url': last_commit_api[0]['html_url'],
            'last_commit_sha': last_commit_api[0]['sha'][:8],

            # Git page related stuff
            'git_repo': CONFIG['github']['repository'],
            'git_url': api['_links']['html'],
            'git_size': api['size'],
            'git_sha1': api['sha'],
            'git_last_commit': api['sha'][:8],
            'git_last_commit_url': api['_links']['html'],
            'git_content': markdown.markdown(
                api['content'].decode(api['encoding']).decode('utf-8'),
                ['markdown.extensions.extra']
            )
        })
    else:
        response = get_url("https://api.github.com/repos/%s/contents/%s" % (CONFIG['github']['repository'], category))
        api = json.loads(response.text or response.content)
        return render(request, 'categories.html', {
            # Last commit related stuff
            'last_commit_url': last_commit_api[0]['html_url'],
            'last_commit_sha': last_commit_api[0]['sha'][:8],

            'git_repo': 'https://github.com/%s' % (CONFIG['github']['repository']),
            'category': category,
            'Categories': api,
            'base_categories': get_categories()
        })

def page(request, category, page_name=''):
    ## Get the last commit.
    last_commit_response = get_url("https://api.github.com/repos/%s/commits" % (CONFIG['github']['repository']), '&per_page=1')
    last_commit_api = json.loads(last_commit_response.text or last_commit_response.content)

    # GitHub API: https://api.github.com/repos/django/django/contents/CATEGORY/FILE_NAME.md
    if(category == '.'):
        url = "https://api.github.com/repos/%s/contents/Index.md" % (CONFIG['github']['repository'])
    else:
        url = "https://api.github.com/repos/%s/contents/%s/%s" % (CONFIG['github']['repository'], category, page_name)

    url = url + AUTH
    req = requests.get(url)

    print AUTH

    if(req.ok):
        api = json.loads(req.text or req.content)
        return render(request, 'wiki_page.html', {
            # Last commit related stuff
            'last_commit_url': last_commit_api[0]['html_url'],
            'last_commit_sha': last_commit_api[0]['sha'][:8],

            ## Page related stuff
            'name': api['name'],
            'path': api['path'].replace('.md', ''),
            'category': category,
            'git_repo': CONFIG['github']['repository'],
            'git_path': api['path'],
            'git_url': api['_links']['html'],
            'git_size': api['size'],
            'git_sha1': api['sha'],
            'git_last_commit': api['sha'][:8],
            'git_type': api['type'],
            'git_content': markdown.markdown(
                api['content'].decode(api['encoding']).decode('utf-8'),
                ['markdown.extensions.extra']
            )
        })

    # Return 404 error page.
    return render(request, '404.html')
