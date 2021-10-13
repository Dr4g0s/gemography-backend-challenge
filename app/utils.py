import datetime


def get_date():
    '''
        get the current date and subtract 30 days from it,
        return well formated date
    '''

    current_date = datetime.datetime.now().date()
    date = current_date - datetime.timedelta(days=30)
    str_date = date.strftime('%Y-%m-%d')
    return str_date


def list_of_formated_repos(data):
    '''
        create a formated list of repositories
        with some fields
    '''

    new_list = []
    for item in data:
        repo_object = {
            'id': item['id'],
            'name': item['name'],
            'description': item['description'],
            'url': item['url'],
            'stars': item['stargazers_count'],
            'language': item['language']
        }
        new_list.append(repo_object)
    return new_list


def filter_by_language(lang, data):
    '''
        filter list of repositories by
        language name or language with null value
    '''

    if not lang:
        return [repo for repo in data if repo['language']]
    else:
        return [repo for repo in data if repo['language'] == lang]


def list_of_unique_languages(data):
    '''
        create a set of languages to be
        unique and return it as a list
    '''

    new_list = {repo['language'] for repo in data}
    return list(new_list)


def list_of_formated_languages(languages, data):
    '''
        filter formated repositories by
        unique languages and format them with
        new properties
    '''

    new_list = []
    for lang in languages:
        repo_list_by_language = filter_by_language(lang, data)
        obj = {
            'name': lang,
            'count': len(repo_list_by_language),
            'repo_list': repo_list_by_language
        }
        new_list.append(obj)
    return new_list
