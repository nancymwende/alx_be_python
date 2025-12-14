class Calculator:
    """A calculator class demonstrating static and class methods."""
    
    # Class attribute
    calculation_type = "Arithmetic Operations"
    
    @staticmethod
    def add(a, b):
        """Add two numbers using a static method.
        
        Static methods don't have access to class or instance attributes.
        They behave like regular functions but are namespaced within the class.
        
        Args:
            a: First number to add.
            b: Second number to add.
            
        Returns:
            The sum of a and b.
        """
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        """Multiply two numbers using a class method.
        
        Class methods receive the class as the first argument (cls) and can
        access class attributes and other class methods.
        
        Args:
            cls: The class itself (automatically passed).
            a: First number to multiply.
            b: Second number to multiply.
            
        Returns:
            The product of a and b.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b