from typing import List
from collections import defaultdict
from heapq import nsmallest

class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.movie_mapping = defaultdict(dict)
        self.rented = []
        for (shop, movie, price) in entries:
            self.movie_mapping[movie][shop] = [price, shop, movie, False]

    def search(self, movie: int) -> List[int]:
        return [shop for _, shop, _, rented in
                nsmallest(10, self.movie_mapping[movie].values())
                if not rented][:5]

    def rent(self, shop: int, movie: int) -> None:
        self.movie_mapping[movie][shop][3] = True
        price = self.movie_mapping[movie][shop][0]
        self.rented.append([price, shop, movie])

    def drop(self, shop: int, movie: int) -> None:
        self.movie_mapping[movie][shop][3] = False
        price = self.movie_mapping[movie][shop][0]
        self.rented.remove([price, shop, movie])

    def report(self) -> List[List[int]]:
        return [[shop, movie] for _, shop, movie in nsmallest(5, self.rented)]


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()
