from newsapi import NewsApi

class TopHeadlines(NewsApi):
    '''This class handles request and response with the newsapi on 'top-headlines' endpoint.'''


    def fetch_top_headlines(self, country='us', category=False, sources=False, pagesize=10, page=1):
        '''This method fetches data as per the given parameters from the 'top-headlines' endpoint of 
        the newsapi.'''
        params = {}
        if country:
            params.update({'country' : country})
        if category:
            params.update({'category': category})
        if sources:
            params.update({'sources': sources})

        response = self.connect(endpoint='top-headlines', params=params, pagesize=pagesize, page=page)
        return response

    def show_top_headlines(self, country='us', category=False, sources=False, pagesize=10,
                                      page=1, display_items=['name', 'title']):
        '''This method prints data fetched from 'top-headlines' endpoint of the newsapi in a visually
        appealing manner.'''
        result = self.fetch_top_headlines(country, category, sources, pagesize, page)
        articles = result.get('articles')
        for count, article in enumerate(articles):
            print('Article {}'.format(count))
            for display_item in display_items:
                values = '{0} : {1}'.format(display_item, article.get(display_item))
                print(values)
            print('\n\n')
        else:
            return 'Could not fetch headlines!!'
