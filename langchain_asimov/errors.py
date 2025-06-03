# This is free and unencumbered software released into the public domain.

from __future__ import annotations # for Python 3.9

class AsimovModuleNotFound(Exception):
    """Exception raised when a module cannot be found or imported.

    Attributes:
        module_name: The name of the module that was not found
        message: Explanation of the error
    """

    def __init__(self, module_name: str, message: str | None = None) -> None:
        """Initializes the `AsimovModuleNotFound` exception.

        Args:
            module_name: The name of the module that was not found
            message: Optional custom error message. If not provided,
                    a default message will be generated.
        """
        self.module_name = module_name
        if message is None:
            message = f"Module '{module_name}' not found"
        self.message = message
        super().__init__(self.message)

    def __str__(self) -> str:
        """Returns a string representation of the exception."""
        return self.message

    def __repr__(self) -> str:
        """Returns a detailed string representation of the exception."""
        return f"{self.__class__.__name__}(module_name={self.module_name!r}, message={self.message!r})"
