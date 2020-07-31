'''
===============================================================

    An interesting example of how greedy algorithms and sets simplify the solution of a problem.

    In this example we have some radio stations, information about city coverage and
    a task of making algorithm of maximize the coverage with costs minimum.

    The idea of using a greedy algorithm is in finding the best locally solutions on each iteration.
    It give us the best global result.

===============================================================
'''

class GreedyAlgorithmForSets:
    __the_best_radio_stations_set = set()

    def __init__(self, cities: set, radio_stations: dict):
        self.__dict_of_radio_stations = radio_stations
        self.__set_of_cities = cities.copy()

    def search_for_the_best_radio_stations_set(self):
        while self.__set_of_cities:
            locally_the_best_radio_station = None
            radio_stations_coverage = set()
            for radio_station, cities in self.__dict_of_radio_stations.items():
                coverage = self.__set_of_cities & cities
                if len(coverage) > len(radio_stations_coverage):
                    locally_the_best_radio_station = radio_station
                    radio_stations_coverage = coverage
            self.__set_of_cities -= radio_stations_coverage
            self.__the_best_radio_stations_set.add(locally_the_best_radio_station)

        return self.__the_best_radio_stations_set

################# example: #################
set_of_cities = set( [ "Moscow", "NY", "London", "Munich", "Yekaterinburg", "Dublin", "Amsterdam", "Paris"] )

dict_of_radio_stations = {}
dict_of_radio_stations["the_best_radio"] = set(["Munich", "Dublin", "Moscow"])
dict_of_radio_stations["math_radio"] = set(["Moscow", "NY", "Yekaterinburg"])
dict_of_radio_stations["classical_music_radio"] = set(["Paris", "Amsterdam"])
dict_of_radio_stations["animals_planet"] = set(["Amsterdam", "Dublin", "Paris"])
dict_of_radio_stations["all_news"] = set(["London", "NY"])
dict_of_radio_stations["the_world_today"] = set(["Paris", "London"])

print(GreedyAlgorithmForSets(set_of_cities, dict_of_radio_stations).search_for_the_best_radio_stations_set())
