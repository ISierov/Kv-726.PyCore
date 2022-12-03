# Write a function taking in a string like
# WOW this is REALLY          amazing
# and returning
# Wow this is really amazing
# . String should be capitalized and properly spaced. Using re and string is not allowed.


def filter_words(st):
    st = st.lower()
    st = " ".join(st.split())
    st = st.capitalize()
    print(st)