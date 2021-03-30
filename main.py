from newsapi import NewsApi
from topheadlines import TopHeadlines
from sources import Sources
from everything import Everything

def main():
    newsapi_obj = NewsApi()
    newsapi_obj._key = '0eacfb62485f4a4cacf8b62680452532'
    
    #possible display_items - ['name', 'author', 'title', 'description', 'publishedAt']
    TopHeadlines().show_top_headlines(display_items=['name', 'author', 'title', 'description', 'publishedAt'])
    
    #possible display_items - ['name', 'description', 'url', 'category', 'language', 'country']
    Sources().show_sources(display_items=['name', 'description', 'url', 'category', 'language', 'country'])

    #possible display_items - ['name', 'author', 'title', 'description', 'publishedAt']
    Everything().show_everything(kw_to_search_in_title='narendra modi', kw_to_serch_in_both=False, display_items=['name', 'author', 'title', 'description', 'publishedAt'])

main()