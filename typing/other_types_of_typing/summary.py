import pandas as pd

data = {
    "Type Keyword": [
        "List[int]", "Tuple[str, int]", "Dict[str, int]", "Optional[str]", "Union[int, str]",
        "Any", "Callable", "Literal", "Final", "TypedDict"
    ],
    "Description": [
        "List of integers", "Tuple of string and int", "Dictionary with str keys and int values",
        "Can be string or None", "Can be int or string", "Any type",
        "A function as argument", "Only specific allowed values",
        "Constants (cannot be changed)", "Dict with structured keys and types"
    ]
}

df = pd.DataFrame(data)
df.to_excel("summary_of_python_typing.xlsx", index=False)

print("Excel file 'python_typing.xlsx' created!")
