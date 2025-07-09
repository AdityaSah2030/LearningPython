"""
Challenge: Friendship Compatibility Calculator

Build a Python script that calculates a fun "compatibility score" between two friends based on their names.

Your program should:
1. Ask for two names (friend A and friend B).
2. Count shared letters, vowels, and character positions to create a compatibility score (0-100).
3. Display the percentage with a themed message like:
    "You're like chai and samosa — made for each other!" or 
    "Well... opposites attract, maybe?"

Bonus:
- Use emojis in the result
- Give playful advice based on the score range
- Capitalize and center the final output in a framed box
"""

def friendship_score(name1, name2):
    name1, name2 = name1.lower(), name2.lower()
    score = 0
    
    # Convert names to sets for efficient operations
    set1 = set(name1)
    set2 = set(name2)
    vowels = set('aeiou')
    
    # 1. Shared letters bonus (using set intersection)
    shared_letters = set1 & set2
    score += len(shared_letters) * 8
    
    # 2. Vowel compatibility (shared vowels get extra points)
    shared_vowels = shared_letters & vowels
    score += len(shared_vowels) * 12
    
    # 3. Name length similarity bonus
    len_diff = abs(len(name1) - len(name2))
    if len_diff == 0:
        score += 20  # Perfect length match
    elif len_diff <= 2:
        score += 10  # Close length match
    
    # 4. First and last letter connection
    if name1[0] == name2[0]:  # Same first letter
        score += 15
    if name1[-1] == name2[-1]:  # Same last letter
        score += 15
    
    # 5. Unique letters diversity bonus
    total_unique = len(set1 | set2)  # Union of both sets
    if total_unique >= 8:
        score += 10
    
    # 6. Special consonant pairs that sound good together
    special_pairs = {'b', 'p'}, {'d', 't'}, {'g', 'k'}, {'f', 'v'}, {'s', 'z'}
    for pair in special_pairs:
        if pair.issubset(set1 | set2):
            score += 5
    
    return min(score, 100)

def get_compatibility_message(score):
    """Return themed message based on score"""
    if score >= 90:
        return "🔥 You're like chai and samosa — made for each other! 🔥"
    elif score >= 75:
        return "✨ Like stars aligned perfectly in the sky! ✨"
    elif score >= 60:
        return "🌟 Great vibes! You two click really well! 🌟"
    elif score >= 45:
        return "😊 Pretty good match! Friendship goals ahead! 😊"
    elif score >= 30:
        return "🤔 Interesting dynamic... could work with effort! 🤔"
    else:
        return "😅 Well... opposites attract, maybe? 😅"

def run_friendship_calculator():
    print("❤️ Friendship Compatibility Calculator ❤️")
    name1 = input("Enter first name: ")
    name2 = input("Enter second name: ")

    score = friendship_score(name1, name2)
    message = get_compatibility_message(score)

    print(f"\n{name1.title()} & {name2.title()}: {score}%")
    print(message)

run_friendship_calculator()