from newsapi import NewsApi

class Sources(NewsApi):
    '''This class handles request and response with the newsapi on 'sources' endpoint.'''


    def fetch_sources(self, country='us', category=False, language=False, pagesize=10, page=1):
        '''This method fetches data as per the given parameters from the 'sources' endpoint of the
        newsapi.'''
        params = {}
        if country:
            params.update({'country' : country})
        if category:
            params.update({'category': category})
        if language:
            params.update({'language': language})

        response = self.connect(endpoint='sources', params=params, pagesize=pagesize, page=page)
        return response

    def show_sources(self, country='us', category=False, language=False, pagesize=10,
                                      page=1, display_items=['name', 'category']):
        '''This method prints data fetched from 'sources' endpoint of the newsapi in a visually
        appealing manner.'''
        result = self.fetch_sources(country, category, language, pagesize, page)
        sources = result.get('sources')
        for count, article in enumerate(sources):
            print('Source {}'.format(count))
            for display_item in display_items:
                values = '{0} : {1}'.format(display_item, article.get(display_item))
                print(values)
            print('\n\n')
        else:
            return 'Could not fetch Sources!!'
