from geopy.distance import geodesic


class Distance:

    def get_lat_long(self, city):
        city_data = city.split(',')
        final_city_data = (float(city_data[0][:7]), float(city_data[1][:7]))
        return final_city_data


if __name__ == '__main__':
    City_1 = '51.5074 N , 0.1278 W'
    City_2 = '48.8566 N,  2.3522 E'
    distance = Distance()
    city_1_lat_long = distance.get_lat_long(City_1)
    city_2_lat_long = distance.get_lat_long(City_2)
    distance_between_cities = geodesic(city_1_lat_long, city_2_lat_long).km
    print('City 1 and City 2 are {:.2f} km apart'.format(distance_between_cities))
