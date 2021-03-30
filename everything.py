from newsapi import NewsApi

class Everything(NewsApi):


    def fetch_everything(self, kw_to_search_in_title=False, kw_to_serch_in_both=False, sources=False, 
                pagesize=10, page=1):
        params = {}
        if kw_to_search_in_title:
            params.update({'qInTitle' : kw_to_search_in_title})
        if kw_to_serch_in_both:
            params.update({'q': kw_to_serch_in_both})
        if sources:
            params.update({'sources': sources})

        response = self.connect(endpoint='everything', params=params, pagesize=pagesize, page=page)
        return response

    def show_everything(self, kw_to_search_in_title='us', kw_to_serch_in_both=False, sources=False, pagesize=10,
                                      page=1, display_items=['name', 'title']):
        result = self.fetch_everything(kw_to_search_in_title, kw_to_serch_in_both, sources, pagesize, page)
        articles = result.get('articles')
        for count, article in enumerate(articles):
            print('Article {}'.format(count))
            for display_item in display_items:
                values = '{0} : {1}'.format(display_item, article.get(display_item))
                print(values)
            print('\n\n')
        else:
            return 'Could not fetch headlines!!'
