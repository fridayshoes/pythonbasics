# Example 1: Subscription Overlaps

# Find common subscribers

# Objective: Analyze subscription overlaps
# Outcome: Shows intersections/differences between sets



news_sub = {"alice@mail.com", "bob@mail.com", "charlie@mail.com"}
blog_sub = {"bob@mail.com", "diana@mail.com", "alice@mail.com"}

common = news_sub.intersection(blog_sub)
only_news = news_sub - blog_sub
all_subs = news_sub.union(blog_sub)

print(f"Common subscribers: {common}")
print(f"News-only subscribers: {only_news}")
print(f"All subscribers: {all_subs}")


# Common subscribers: {'bob@mail.com', 'alice@mail.com'}
# News-only subscribers: {'charlie@mail.com'}
# All subscribers: {'alice@mail.com', 'diana@mail.com', 'bob@mail.com', 'charlie@mail.com'}






# Example 2: Unique Entry Filter

# Filter duplicate sensor readings

# Objective: Identify unique and duplicate values
# Outcome: Unique: {22.1,22.5,23.0}, Duplicates: {22.1,22.5}


readings = [22.1, 22.5, 22.1, 23.0, 22.5, 22.1]
unique = set()
duplicates = set()

for value in readings:
    if value in unique:
        duplicates.add(value)
    else:
        unique.add(value)

print(f"Original: {len(readings)} readings")
print(f"Unique values: {unique}")
print(f"Duplicate values: {duplicates}")


# Original: 6 readings
# Unique values: {23.0, 22.1, 22.5}
# Duplicate values: {22.1, 22.5}
