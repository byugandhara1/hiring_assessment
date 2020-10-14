
''' Program 1 : Check if the given point lies inside or outside a polygon? '''

from shapely.geometry import Point, Polygon
def check_point_position(polygon_coords, point_coords):	
	polygon = Polygon(polygon_coords)
	point = Point(point_coords)
	print(point.within(polygon))

polygon_coords = input('Enter polygon coordinates -')
point_coords = input('Enter point coordinates  -')
check_point_position(polygon_coords, point_coords)