import math


class Shape:
    """Base class for all shapes."""
    
    def area(self):
        """Calculate the area of the shape.
        
        This method should be overridden by derived classes.
        
        Raises:
            NotImplementedError: If the method is not overridden in a derived class.
        """
        raise NotImplementedError("Subclasses must override the area() method")


class Rectangle(Shape):
    """Rectangle shape that inherits from Shape."""
    
    def __init__(self, length, width):
        """Initialize a Rectangle with length and width.
        
        Args:
            length: The length of the rectangle.
            width: The width of the rectangle.
        """
        self.length = length
        self.width = width
    
    def area(self):
        """Calculate and return the area of the rectangle.
        
        Returns:
            The area of the rectangle (length × width).
        """
        return self.length * self.width


class Circle(Shape):
    """Circle shape that inherits from Shape."""
    
    def __init__(self, radius):
        """Initialize a Circle with a radius.
        
        Args:
            radius: The radius of the circle.
        """
        self.radius = radius
    
    def area(self):
        """Calculate and return the area of the circle.
        
        Returns:
            The area of the circle (π × radius²).
        """
        return math.pi * self.radius ** 2