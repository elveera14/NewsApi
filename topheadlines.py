from newsapi import NewsApi

class TopHeadlines(NewsApi):


    def fetch_top_headlines(self, country='us', category=False, sources=False, pagesize=10, page=1):
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
