import collections
Card = collections.namedtuple('Card', ['rank', 'suit'])
class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
        for rank in self.ranks]
    def __len__(self):
        return len(self._cards)
    def __getitem__(self, position):
        return self._cards[position]
if __name__ == '__main__':

    beer_card = Card('7', 'diamonds')
    print(beer_card)


def search(request):
    searchtype = request.POST.get("searchtype")
    keyword = request.POST.get("keyword")
    if searchtype == "all":
        # 多个字段模糊查询， 括号中的下划线是双下划线，双下划线前是字段名，双下划线后可以是icontains或contains,区别是是否大小写敏感，竖线是或的意思
        sciencenews = models.Sciencenews.objects.filter(Q(title__icontains=keyword) \
                                                        | Q(content__icontains=keyword) | Q(author__icontains=keyword))
    elif searchtype == "author":
        # 单个字段模糊查询
        sciencenews = models.Sciencenews.objects.filter(author__icontains=keyword)
    elif searchtype == "title":
        sciencenews = models.Sciencenews.objects.filter(title__icontains=keyword)
    elif searchtype == "content":
        sciencenews = models.Sciencenews.objects.filter(content__icontains=keyword)
    else:
        # 使用点连接的filter链表示and
        sciencenews = models.Sciencenews.objects.filter(author__icontains=keyword). \
            filter(title__icontains=keyword).filter(content__icontains=keyword)


    return render(request, "show/index.html", {"param": sciencenews, "searchtype": searchtype, "keyword": keyword})
