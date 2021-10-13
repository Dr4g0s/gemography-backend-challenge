from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONOpenAPIRenderer
from rest_framework.response import Response
import requests
from app.utils import (
    get_date, list_of_formated_repos, filter_by_language,
    list_of_unique_languages, list_of_formated_languages
)


@api_view(('GET',))
@renderer_classes([JSONOpenAPIRenderer])
def github_repos_list_api_view(request):
    '''
        fetch data from GitHub API in json format
    '''

    date = get_date()
    url = f'https://api.github.com/search/repositories?q=\
            created:>{date}&sort=stars&order=desc&per_page=100'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return Response(data)
    return Response('Server unreachable right now.')


@api_view(('GET',))
@renderer_classes([JSONOpenAPIRenderer])
def language_list_api_view(request):
    '''
        fetch data from GitHub API and return a list
        of format data that contain response data
    '''

    date = get_date()
    url = f'https://api.github.com/search/repositories?q=\
            created:>{date}&sort=stars&order=desc&per_page=100'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()['items']
        formated_repo_list = list_of_formated_repos(data)
        repo_list_without_none_language = filter_by_language(
            None, formated_repo_list
        )
        unique_languages = list_of_unique_languages(
            repo_list_without_none_language
        )
        languages_list = list_of_formated_languages(
            unique_languages,
            repo_list_without_none_language
        )
        return Response(languages_list)

    return Response('Server unreachable right now.')
