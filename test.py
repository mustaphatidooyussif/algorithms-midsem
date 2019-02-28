"""
Problem 1(a)

@author Mustapha Tidoo Yussif
"""
import math 
import sys 

class ClosestPair(object):
        """
        This solves the closest-pair problem by divide-and-conquer

        :param points: list of 2-dimentional points of size more than 2. 
        """
        def __init__(self, points, x_cord_idx = 0, y_cord_idx = 1):
            self._P_points = points 
            self._Q_points = points 
            self._x_cord_idx = x_cord_idx
            self._y_cord_idx = y_cord_idx


        def findClosestCities(self):
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

                self._mergeSort(lefthalf, cord)
                self._mergeSort(righthalf, cord)
                self._merger(points, lefthalf, righthalf, cord)

        def _merger(self, points, lefthalf_points, righthalf_points, cord):
            """
            This merges two sorted arrays into one sorted array

            :param: points: list of points to sort.
            :param: lefthalf_points: sorted list to merge.
            :param: righthalf_points: sorted list to merge.
            :param: cord: the cordinate to sort the points by. 
            """
            i=0
            j=0
            k=0
            while i < len(lefthalf_points) and j < len(righthalf_points):
                if lefthalf_points[i][cord] < righthalf_points[j][cord]:
                    points[k]=lefthalf_points[i]
                    i=i+1
                else:
                    points[k]=righthalf_points[j]
                    j=j+1
                k=k+1

            while i < len(lefthalf_points):
                points[k]=lefthalf_points[i]
                i=i+1
                k=k+1

            while j < len(righthalf_points):
                points[k]=righthalf_points[j]
                j=j+1
                k=k+1 

        def _bruteForceClosestPair(self, P, x_cord_idx, y_cord_idx):
            d = sys.maxsize #Set the minimum distance to a possibly large value. 

            if len(P) == 1:
                print('Error: require more than 1 point, but one was passed')
                exit(0)
            n = 0
            m = 0 
            for i in range(len(P)-1):
                for j in range(i+1, len(P)):
                    euclidean_dist_sq = (P[j][x_cord_idx] - P[i][x_cord_idx])**2 + (P[j][y_cord_idx] - P[i][y_cord_idx])**2
                    if euclidean_dist_sq < d:
                        d = euclidean_dist_sq 
                        n = i
                        m = j 
                    # d = min(d, (P[j][0] - P[i][0])**2 + (P[j][1] - P[i][1])**2)
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
                P_l = P[:midx]
                P_r = P[midx:] 
                Q_l = Q[:midy]
                Q_r = Q[midy:]

                d_l, P_l, Q_l = self._closestPair(P_l, Q_l) #Find the closest pair in the left half. 
                d_r, P_r, Q_r = self._closestPair(P_r, Q_r) #Find the closest pair in the right half. 

                if d_l < d_r:
                    d = d_l 
                    P_min = P_l 
                    Q_min = Q_l
                else:
                    d =  d_r 
                    P_min = P_r
                    Q_min = Q_r

                # d = min(d_l, d_r)  

                #List of points within 2d boundary
                x_medean = P[midx][self._x_cord_idx]
                S = []
                for k in Q:
                    if abs(k[self._x_cord_idx] - x_medean) < d:
                        S.append(k)

                d_min_sq = d**2 
                for i in range(len(S)-2):
                    j = i + 1
                    while j < len(S) - 1:
                        euclidean_dist_sq = (S[j][self._x_cord_idx] - S[i][self._x_cord_idx])**2 + (S[j][self._y_cord_idx] - S[i][self._y_cord_idx])**2 
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

    points = [(1,3), (0,2), (2, 1), (9, 5)]
    pair =ClosestPair(locations_in_ghana, x_cord_idx = 1, y_cord_idx = 2)
    a, b, c = pair._bruteForceClosestPair(locations_in_ghana, x_cord_idx = 1, y_cord_idx = 2)
    # print(a)
    # print(b)
    # print(c)
    print(pair.findClosestCities())

    #Testing only positive integer cordinates
    # points1 = [(1,3), (0,2), (2, 1), (9, 5)]
    # pair1 =ClosestPair(points1)
    # c1 = pair1.findClosestPair()
    # print("TEST 1: Closest pair distance: ", c1)

    # #Testing only negative integer cordinates
    # points2 = [(-1,-5), (-7,-2), (-4, -2), (-9, -5), (-5, -2)]
    # pair2 =ClosestPair(points2)
    # c2 = pair2.findClosestPair()
    # print("TEST 2: Closest pair distance: ", c2)

    # #Testing negative and positve integer cordinates
    # points3 = [(3, -3), (0,-2), (-3, -1), (9, 5)]
    # pair3 =ClosestPair(points3)
    # c3 = pair3.findClosestPair()
    # print("TEST 3: Closest pair distance: ", c3)
  

    # #Testing negative and negative decimal point cordinates
    # points4 = [(1.3,0.2), (0.1,2.2), (2.7, 1), (0.9, 5.1)]
    # pair4 =ClosestPair(points4)
    # c4 = pair4.findClosestPair()
    # print("TEST 4: Closest pair distance: ", c4)

