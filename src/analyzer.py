def analyze_follow_relationships(followers, following):
    not_following_back = following - followers
    you_dont_follow_back = followers - following
    mutuals = followers & following

    return {
        "not_following_back": sorted(not_following_back),
        "you_dont_follow_back": sorted(you_dont_follow_back),
        "mutuals": sorted(mutuals),
        "followers_count": len(followers),
        "following_count": len(following),
        "mutuals_count": len(mutuals),
    }