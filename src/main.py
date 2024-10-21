if __name__ == "__main__":
    import sys
    from schema import *

    filename = sys.argv[1]
    laws = Laws.from_json(filename)

    for law in laws:
        conditions = law.conditions
        conclusion = law.conclusion

        print(
            f"NẾU {", ".join(list(map(lambda condition: condition.value.lower(), conditions)))}, THÌ {conclusion.value.lower()}"
        )
