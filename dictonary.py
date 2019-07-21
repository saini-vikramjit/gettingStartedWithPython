monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    1: "One",
    33: "Thirty three"
}

print(monthConversions["Apr"])

print(monthConversions.get(331,"Not a valid key"))