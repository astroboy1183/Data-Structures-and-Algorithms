# Dunder / magic methods: special __methods__ that hook into Python's
# built-in behavior (printing, ==, sorting, len, +, indexing, calling).


# 1. __init__ + __str__ + __repr__
print("\n--- 1. __init__, __str__, __repr__ ---")


class Book:
    """A book with a title; demonstrates init/str/repr."""

    def __init__(self, title, pages):
        self.title = title  # __init__ runs at construction time
        self.pages = pages

    def __str__(self):
        # Human-friendly text, used by print() and str().
        return f"'{self.title}' ({self.pages} pages)"

    def __repr__(self):
        # Unambiguous, dev-facing; ideally recreates the object.
        return f"Book(title={self.title!r}, pages={self.pages!r})"


book = Book("Python 101", 320)
print("print(obj) uses __str__:", book)  # calls __str__
print("repr(obj) uses __repr__:", repr(book))  # calls __repr__


# 2. __eq__ : define == for your objects
print("\n--- 2. __eq__ (equality) ---")


class Point:
    """A 2D point that knows how to compare itself for equality."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        if not isinstance(other, Point):  # guard against odd comparisons
            return NotImplemented
        return self.x == other.x and self.y == other.y


p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(5, 9)
print("p1 == p2 (same coords):", p1 == p2)  # True via __eq__
print("p1 == p3 (different):", p1 == p3)  # False via __eq__


# 3. __lt__ : ordering so sorted() works (also __gt__/__le__/__ge__ exist)
print("\n--- 3. __lt__ (ordering / sortable) ---")


class Vector:
    """A vector compared by magnitude; supports +, indexing, ordering."""

    def __init__(self, *components):
        self.components = list(components)

    def __repr__(self):
        return f"Vector{tuple(self.components)}"

    def magnitude(self):
        return sum(c * c for c in self.components) ** 0.5

    def __lt__(self, other):
        # Defining __lt__ alone is enough for sorted() to order objects.
        return self.magnitude() < other.magnitude()

    def __add__(self, other):
        # Component-wise addition: Vector + Vector -> Vector.
        paired = zip(self.components, other.components, strict=True)
        return Vector(*(a + b for a, b in paired))

    def __getitem__(self, index):
        # Enables v[i] indexing into the components.
        return self.components[index]


vectors = [Vector(3, 4), Vector(1, 1), Vector(6, 8)]
print("unsorted:", vectors)
print("sorted by magnitude:", sorted(vectors))  # uses __lt__


# 4. __len__ : make len(obj) work
print("\n--- 4. __len__ (len support) ---")


class Playlist:
    """A simple container wrapping a list of song titles."""

    def __init__(self, songs):
        self.songs = list(songs)

    def __len__(self):
        # len(obj) calls __len__.
        return len(self.songs)

    def __getitem__(self, index):
        # len() pairs nicely with indexing.
        return self.songs[index]


playlist = Playlist(["Intro", "Verse", "Chorus"])
print("len(playlist):", len(playlist))  # calls __len__


# 5. __add__ : operator overloading (obj1 + obj2)
print("\n--- 5. __add__ (operator overloading) ---")
v1 = Vector(1, 2)
v2 = Vector(3, 4)
print("v1 + v2 (component-wise):", v1 + v2)  # calls Vector.__add__


# 6. __getitem__ : make obj[i] indexing work
print("\n--- 6. __getitem__ (indexing) ---")
print("playlist[0]:", playlist[0])  # calls Playlist.__getitem__
print("v2[1]:", v2[1])  # calls Vector.__getitem__


# 7. __call__ : make an instance callable like a function
print("\n--- 7. __call__ (callable instance) ---")


class Multiplier:
    """Stores a factor and acts like a function when called."""

    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        # obj(value) triggers __call__.
        return value * self.factor


triple = Multiplier(3)
print("triple(10) via __call__:", triple(10))  # calls Multiplier.__call__
print("callable(triple):", callable(triple))  # True: it defines __call__
