"""
Mid semester part 1
Problem 1(b)

@author Mustapha Tidoo Yussif
"""

import math 
import sys 

class ClosestCities(object):
        """
        This finds the closest cities by using divide-and-conquer approach. It cannot also the closest 
        pair of 2-dimensional points. 

        :param points: list of 2-dimentional points of size more than 2. 
        :param x_cord_idx: the position of the x-cordinate. E.g 0 for (2, 1) and 1 for ('Tamale', 2, 1)
        :param y_cord_idx: the position of the y-cordinate. E.g 1 for (2, 4) and 2 for ('Accra', 2, 1)
        """
        def __init__(self, points, x_cord_idx = 0, y_cord_idx = 1):
            #Defaults the position of x cordinate and y cordinate in 2-dimensional 
            # geometry to 0 and 1 respectively
            self._P_points = points 
            self._Q_points = points 
            self._x_cord_idx = x_cord_idx
            self._y_cord_idx = y_cord_idx


        def findClosestCities(self):
            """
            Wrapper function (public function) for finding the closest cities by 
            calling the private closest pair method 
            """
            self._mergeSort(self._P_points, cord = 0) #sort by x cordinates
            self._mergeSort(self._Q_points, cord = 1) #sort by y cordinates
            return self._closestPair(self._P_points, self._Q_points)

        def _mergeSort(self, points, cord):
            """
            This sorts list of points by recursive _mergeSort

            :param: points: list of points to sort.
            :param: cord: the cordinate to sort the points by. 
            :return: A list sorted in nondecreasing order.
            """
            if len(points)>1:
                mid = len(points)//2
                lefthalf = points[:mid]
                righthalf = points[mid:]

                self._mergeSort(lefthalf, cord) #mergesort the left sub array by cord (eg. x or y)
                self._mergeSort(righthalf, cord) #mergesort the right sub array by cord (eg. x or y)
                self._merger(points, lefthalf, righthalf, cord)

        def _merger(self, points, lefthalf_points, righthalf_points, cord):
            """
            This merges two sorted arrays into one sorted array

            :param: points: list of points to sort.
            :param: lefthalf_points: sorted list to merge.
            :param: righthalf_points: sorted list to merge.
            :param: cord: the cordinate to sort the points by. 
            """
            i=0  #Initial index of the left half list.
            j=0  #Initial index of the left half list.
            k=0  #Initial index of the list being merged into.
            while i < len(lefthalf_points) and j < len(righthalf_points):
                if lefthalf_points[i][cord] < righthalf_points[j][cord]:
                    points[k]=lefthalf_points[i]
                    i=i+1
                else:
                    points[k]=righthalf_points[j]
                    j=j+1
                k=k+1

            # If there are remaining elements in the left half list, 
            # add them to the list being merged into. 
            while i < len(lefthalf_points):
                points[k]=lefthalf_points[i]
                i=i+1
                k=k+1

            # If there are remaining elements in the left half list, 
            # add them to the list being merged into. 
            while j < len(righthalf_points):
                points[k]=righthalf_points[j]
                j=j+1
                k=k+1 

        def _bruteForceClosestPair(self, P, x_cord_idx, y_cord_idx):
            """
            This solves the closes pair problem by brute-force

            :param P: list of points of size n>=2 
            :param x_cord_idx: the position of the x-cordinate
            :param y_cord_idx: the position of the y-cordinate
            :return : A tuple of closest distance, and the closest points. 
            """
            d = sys.maxsize #Set the minimum distance to a possibly large value. 

            if len(P) == 1:
                print('Error: require more than 1 point, but one was passed')
                exit(0)
            n = 0
            m = 0 
            for i in range(len(P)-1):
                for j in range(i+1, len(P)):
                    # Find the distance between points
                    # Find the two points with the minimum distance between them
                    euclidean_dist_sq = (P[j][x_cord_idx] - P[i][x_cord_idx])**2 \
                        + (P[j][y_cord_idx] - P[i][y_cord_idx])**2
                    if euclidean_dist_sq < d:
                        d = euclidean_dist_sq 
                        n = i
                        m = j 
            return (math.sqrt(d), P[n], P[m])

        def _closestPair(self, P, Q):
            """
            This solves the closest-pair problem by divide-and-conquer. 

            :param: P: points sorted in nondecreasing order of their x coordinates.
            :param: Q: points sorted in nondecreasing order of their y coordinates. 
            :return Euclidean distance between the closest pair of points.
            """
            if len(P) <= 3:
                return self._bruteForceClosestPair(P, self._x_cord_idx, self._y_cord_idx)
            else:
                midx = len(P)//2
                midy = len(Q)//2
                P_l = P[:midx] #copy the first n//2 points of P to array P_l
                P_r = P[midx:] #copy the same n//2 points from Q to array Q_l
                Q_l = Q[:midy] #copy the remaining (n//2) +1 points of P to array P_r
                Q_r = Q[midy:] #copy the remaining (n//2) +1 points of Q to array Q_r

                d_l, P_l, Q_l = self._closestPair(P_l, Q_l) #Find the closest pair in the left half. 
                d_r, P_r, Q_r = self._closestPair(P_r, Q_r) #Find the closest pair in the right half. 

                # Check if the lelf half or the right half contains the closest point
                # P_min is the first point and Q_min is the last point
                if d_l < d_r:
                    d = d_l 
                    P_min = P_l 
                    Q_min = Q_l
                else:
                    d =  d_r 
                    P_min = P_r
                    Q_min = Q_r

                #List of points within 2d boundary
                x_medean = P[midx][self._x_cord_idx]
                S = []
                for k in Q:
                    if abs(k[self._x_cord_idx] - x_medean) < d:
                        S.append(k)

                #Check if one pair of the closest points is found in the left half 
                # and the other pair of the closest points is found in the other half
                d_min_sq = d**2 
                for i in range(len(S)-2):
                    j = i + 1
                    while j < len(S) - 1:
                        euclidean_dist_sq = (S[j][self._x_cord_idx] - S[i][self._x_cord_idx])**2 +\
                             (S[j][self._y_cord_idx] - S[i][self._y_cord_idx])**2 
                        if euclidean_dist_sq < d_min_sq:
                            d_min_sq = euclidean_dist_sq 
                            P_min = S[i]
                            Q_min = S[j]
                        j = j + 1

            return (math.sqrt(d_min_sq), P_min, Q_min)

if __name__ == "__main__":
    locations_in_ghana =[
            ('Accra',	-0.10, 5.58),
            ('Asamankese',	-0.67, 5.83),
            ('Axim', -2.25, 4.85),
            ('Bawku',	-0.32, 11.05),
            ('Berekum',	-2.57, 7.48),
            ('Cape Coast', -1.25, 5.08),
            ('Koforidua',	-0.28, 6.05),
            ('Kumasi',	-1.47,	6.68),
            ('Obuasi',	-1.67,	6.28),
            ('Salaga',	-0.52, 8.52),
            ('Savelugu', -0.90,	9.63),
            ('Sekolndi Taoradi', -1.75,	4.97),
            ('Tamale',	-0.83,	9.37),
            ('Tema',	0.00, 5.68),
            ('Cape Three Points',	-3.00, 4.70),
            ('Tumu',	-1.93, 10.93),
            ('Volta',	0.68,	5.77),
            ('Wenchi',	-3.33,	7.77)
    ]

    #LOCATION, LATITUDE(X), LONGITUDE(Y)
    locations_in_SA = [
        ('Bloemfontei',	26.154898,	-29.087217),
        ('Port Elizabet',	25.619022,	-33.958252),
        ('Seboken',	27.844164,	-26.563404),
        ('Georg',	22.457581,	-33.977074),
        ('Roodepoor',	27.901464,	-26.120134),
        ('Emalahlen',	29.255323,	-25.872782),
        ('Carlton Centr',	28.046822,	-26.205681),
        ('Vrybur',	24.72986,	-26.958405),
        ('Robertsha',	28.01568,	-26.245167),
        ('Hermanu',	19.248734,	-34.414272)
    ]

    # Test finding the closest cities in Ghana.
    ghana = ClosestCities(locations_in_ghana, x_cord_idx = 1, y_cord_idx = 2)
    gh_c_cities = ghana.findClosestCities()
    print("TEST CASE 1: The closest cities in ghana : ", gh_c_cities[1][0], ' and ', gh_c_cities[2][0])

    # Test finding the closest cities in South Africa
    SA = ClosestCities(locations_in_SA, x_cord_idx = 1, y_cord_idx = 2)
    SA_c_cities = SA.findClosestCities()
    print("TEST CASE 2: The closest cities in SA : ", SA_c_cities[1][0], ' and ', SA_c_cities[2][0])

    # Test finding the closest pair of 2-dimensional points
    two_d_points = [(1,3), (0,2), (2, 1), (9, 5)]
    pairs = ClosestCities(two_d_points)
    c_pair = pairs.findClosestCities()
    print("TEST CASE 3: The closest pair :", c_pair[1], ' and ', c_pair[2], ' distance: ',c_pair[0])

    

    