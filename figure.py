"""
figure 모듈은 직사각형, 타원, 직각삼각형의 넓이와 관련된
클래스와 함수를 제공합니다.
line이라는 이름의 클래스와
함수 area_rectangle, area_ellipse, area_right_triangle을 포함합니다.
"""
import math

class line():
    """
    line class는 선의 길이들에 대한 정보를 제공합니다.
    변수로는 외부에서 접근 불가능한 __width, __height가 있으며
    변수들을 수정하고 접근하기 위하여
    set_length, get_length 메소드를 제공합니다.
    """
    __width = 0
    __height = 0

    def __init__(self, width, height):
        """ 생성자 초기 width, height값을 받습니다.
        Args:
            width(int or float): 초기 선의 가로 길이
            height(int or float): 초기 선의 세로 길이
        """
        self.__width = width
        self.__height = height
    
    def set_length(self, width, height):
        """ 선의 길이를 수정합니다.
        Args:
            width(int or float): 선의 가로 길이 수정
            height(int or float): 선의 세로 길이 수정
        """
        self.__width = width
        self.__height = height
    
    def get_length(self):
        """ 객체가 저장하고 있는 선의 길이를 반환합니다.
        Returns:
            int or float: 저장하고 있는 선의 길이입니다.
        """
        return self.__width, self.__height
    
def area_rectangle(width, height):
    """ 길이를 입력받아 직사각형의 넓이를 구하는 함수입니다.
    Args:
        width(int or float): 밑변의 길이
        height(int or float): 높이의 길이
    Returns:
        int or float: 직사각형의 넓이를 반환합니다.
    """
    if width <= 0 or height <= 0: raise ValueError
    return width * height
    
def area_ellipse(width, height):
    """ 길이를 입력받아 타원의 넓이를 구하는 함수입니다.
    Args:
        width(int or float): 짧은쪽 반지름 길이
        height(int or float): 긴쪽 반지름 길이
    Returns:
        int or float: 타원의 넓이를 반환합니다.
    """
    if width <= 0 or height <= 0: raise ValueError
    return width * height * math.pi
    
def area_right_triangle(width, height):
    """ 길이를 입력받아 직각삼각형의 넓이를 구하는 함수입니다.
    Args:
         width(int or float): 밑변의 길이
        height(int or float): 높이의 길이
    Returns:
        int or float: 직각삼각형의 넓이를 반환합니다.
    """
    if width <= 0 or height <= 0: raise ValueError
    return width * height / 2