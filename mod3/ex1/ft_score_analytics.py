
import sys

if __name__ == "__main__":

    scores = []
    i = 0
    print("=== Player Score Analytics ===")
    for arg in sys.argv[1:]:
        if arg.isdigit():
            scores.append(int(arg))
            i += 1
        else:
            print(f"\"{arg}\" ignored cos not a digit or negative")
    if i < 1:
        print("no score provided")
        raise SystemExit
    print("total player:", i)
    print("total score:", sum(scores))
    av = 0
    if i > 0 and sum(scores) > 0:
        av = int(sum(scores) / i)
    print(f"average score: {av:.1f}")
    print("high score:", max(scores))
    print("low score:", min(scores))
    print("scores range:", max(scores) - min(scores))
