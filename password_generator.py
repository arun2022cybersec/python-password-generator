import random
import string
from typing import List

class PasswordGenerator:
    """
    A class to generate random passwords based on specified length, complexity, and periodicity.
    
    Attributes:
    -----------
    length : int
        The length of the generated password (between 8 and 32).
    complexity : str
        The complexity of the generated password ('easy', 'medium', 'hard', 'extreme').
    periodicity : bool
        If True, the password will contain repeated substrings. If False, the password will not have any repeated substrings.
    """
    
    def __init__(self, length: int, complexity: str, periodicity: bool):
        if not 8 <= length <= 32:
            raise ValueError("Length must be between 8 and 32 characters.")
        if complexity not in ('easy', 'medium', 'hard', 'extreme'):
            raise ValueError("Complexity must be 'easy', 'medium', 'hard', or 'extreme'.")
        
        self.length = length
        self.complexity = complexity
        self.periodicity = periodicity
    
    def generate(self) -> str:
        """
        Generate a random password based on the specified length, complexity, and periodicity.
        
        Returns:
        --------
        str
            The generated password.
        """
        char_sets = {
            'easy': string.ascii_lowercase,
            'medium': string.ascii_letters,
            'hard': string.ascii_letters + string.digits,
            'extreme': string.ascii_letters + string.digits + string.punctuation
        }
        
        chars = char_sets[self.complexity]
        
        if self.periodicity:
            password = self._generate_with_periodicity(chars)
        else:
            password = self._generate_without_periodicity(chars)
        
        return password
    
    def _generate_with_periodicity(self, chars: str) -> str:
        """
        Generate a password with repeated substrings.
        
        Parameters:
        -----------
        chars : str
            The characters to use for generating the password.
        
        Returns:
        --------
        str
            The generated password with repeated substrings.
        """
        repeat_length = random.randint(2, max(2, self.length // 4))
        repeat_segment = ''.join(random.choice(chars) for _ in range(repeat_length))
        repeats = self.length // repeat_length
        remainder = self.length % repeat_length
        
        password = repeat_segment * repeats + ''.join(random.choice(chars) for _ in range(remainder))
        return ''.join(random.sample(password, len(password)))  # Shuffle to mix the pattern
    
    def _generate_without_periodicity(self, chars: str) -> str:
        """
        Generate a password without repeated substrings.
        
        Parameters:
        -----------
        chars : str
            The characters to use for generating the password.
        
        Returns:
        --------
        str
            The generated password without repeated substrings.
        """
        password = ''.join(random.choice(chars) for _ in range(self.length))
        while self._has_repeated_substring(password):
            password = ''.join(random.choice(chars) for _ in range(self.length))
        return password
    
    def _has_repeated_substring(self, s: str) -> bool:
        """
        Check if a string contains repeated substrings.
        
        Parameters:
        -----------
        s : str
            The string to check for repeated substrings.
        
        Returns:
        --------
        bool
            True if the string contains repeated substrings, False otherwise.
        """
        n = len(s)
        for i in range(1, n // 2 + 1):
            seen = set()
            for j in range(n - i + 1):
                substring = s[j:j + i]
                if substring in seen:
                    return True
                seen.add(substring)
        return False

if __name__ == "__main__":
    # Generating Password
    pg = PasswordGenerator(16, 'hard', False)
    print("Generated Password:", pg.generate())