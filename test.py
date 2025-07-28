from feruca import collate

strings = ["zebra", "éléonore", "grok"]
print(f"Input:  {strings}")

# Tailoring options are "default", "ArabicScript", and "ArabicInterleaved"
strings_sorted = collate(strings, tailoring="default")

print(f"Output: {strings_sorted}")
assert strings_sorted == ["éléonore", "grok", "zebra"]
