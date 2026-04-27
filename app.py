from src.parser import extract_followers, extract_following
from src.analyzer import analyze_follow_relationships
from src.exporter import export_list_to_csv


ZIP_PATH = "data/instagram_export.zip"


def main():
    followers = extract_followers(ZIP_PATH)
    following = extract_following(ZIP_PATH)

    results = analyze_follow_relationships(followers, following)

    print("\nInstagram Follow Analyzer")
    print("-------------------------")
    print(f"Followers: {results['followers_count']}")
    print(f"Following: {results['following_count']}")
    print(f"Mutuals: {results['mutuals_count']}")

    print("\nGente que NO te sigue pero que yo sigo:\n")

    for username in results["not_following_back"]:
        print(username)

    print(f"\nTotal: {len(results['not_following_back'])}")

    print("\nPeople who follow you but you do NOT follow back:")
    for username in results["you_dont_follow_back"]:
        print(username)

    export_list_to_csv(
        results["not_following_back"],
        "output/not_following_back.csv"
    )

    export_list_to_csv(
        results["you_dont_follow_back"],
        "output/you_dont_follow_back.csv"
    )

    print("\nCSV files created inside the output/ folder.")


if __name__ == "__main__":
    main()