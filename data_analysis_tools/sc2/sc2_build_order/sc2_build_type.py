class BuildType:
    """
    A base class representing a generic build type in a game, characterized by economic and non-economic
    resource allocation ranges.

    Attributes:
        - min_econ (int): The minimum economic resources required for this build.
        - max_econ (int): The maximum economic resources allocated for this build.
        - min_non_econ (int): The minimum non-economic (likely military or development) resources required.
        - max_non_econ (int): The maximum non-economic resources allocated.
        - name (str): The name of the build type.
    """

    def __init__(self, name, min_econ, max_econ, min_non_econ, max_non_econ) -> None:
        """
        Initializes a new instance of BuildType with the given parameters.

        Parameters:
            name (str): The name of the build type.
            min_econ (int): Minimum economic resources for the build.
            max_econ (int): Maximum economic resources for the build.
            min_non_econ (int): Minimum non-economic resources for the build.
            max_non_econ (int): Maximum non-economic resources for the build.
        """

        # Error handling checking that min values are not greater than max values
        if (min_econ > max_econ):
            raise ValueError(f"min values cannot be greater than max values: min_econ == {min_econ} > max_econ == {max_econ}")
        elif (min_non_econ > max_non_econ):
            raise ValueError(f"min values cannot be greater than max values: min_non_econ == {min_non_econ} > max_non_econ == {max_non_econ}")
        
        self.min_econ = min_econ
        self.max_econ = max_econ
        self.min_non_econ = min_non_econ
        self.max_non_econ = max_non_econ
        self.name = name

    def __str__(self) -> str:
        """
        Returns a string representation of the build type, which is its name.
        """
        return self.name


class Standard(BuildType):
    """
    Represents a Standard build type, indicating a balanced approach between economic and non-economic
    investments. Inherits from BuildType.
    """

    def __init__(self, min_econ, max_econ, min_non_econ, max_non_econ) -> None:
        """
        Initializes a Standard build type with specified resource allocation ranges.
        """
        name = "Standard"
        super().__init__(name, min_econ, max_econ, min_non_econ, max_non_econ)


class Aggressive(BuildType):
    """
    Represents an Aggressive build type, likely indicating a focus on military or non-economic
    resources over economy. Inherits from BuildType.
    """

    def __init__(self, min_econ, max_econ, min_non_econ, max_non_econ) -> None:
        """
        Initializes an Aggressive build type with specified resource allocation ranges.
        """
        name = "Aggressive"
        super().__init__(name, min_econ, max_econ, min_non_econ, max_non_econ)


class Economic(BuildType):
    """
    Represents an Economic build type, emphasizing investment in economic resources over non-economic
    ones. Inherits from BuildType.
    """

    def __init__(self, min_econ, max_econ, min_non_econ, max_non_econ) -> None:
        """
        Initializes an Economic build type with specified resource allocation ranges.
        """
        name = "Economic"
        super().__init__(name, min_econ, max_econ, min_non_econ, max_non_econ)
