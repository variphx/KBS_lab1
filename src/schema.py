import typing


class Condition:
    def __init__(self, value: str):
        self.value = value

    @staticmethod
    def parse(unparsed: str):
        self = Condition(unparsed)
        return self

    def __repr__(self):
        return f"Condition({self.value})"

    def __eq__(self, other):
        assert isinstance(other, Condition)
        return self.value == other

    def __hash__(self):
        return hash(self.value)


class Conclusion:
    def __init__(self, value: str):
        self.value = value

    @staticmethod
    def parse(unparsed: str):
        self = Conclusion(unparsed)
        return self

    def __repr__(self):
        return f"Conclusion({self.value})"


class Law:
    def __init__(self, conditions: list[Condition], conclusion: Conclusion):
        self.conditions = conditions
        self.conclusion = conclusion

    def __repr__(self):
        return f"Law(conditions: {self.conditions}, conclusion: {self.conclusion})"


class Laws:
    @staticmethod
    def from_list(data: list[dict]) -> list[Law]:
        def parse(data):
            conditions = list(map(Condition.parse, data["conditions"]))
            conclusion = Conclusion.parse(unparsed=data["conclusion"])
            return Law(conditions=conditions, conclusion=conclusion)

        return list(map(parse, data))

    @staticmethod
    def from_json(path: str) -> list[Law]:
        import json

        with open(path, "r") as f:
            data = json.load(f)

        return Laws.from_list(data=data["laws"])


class Deductor:
    def __init__(self, laws: list[Law]):
        self.laws = laws

    def deduct(self, conditions: list[Condition]) -> None | Conclusion:
        conditions = set(conditions)

        for law in self.laws:
            if conditions == set(law.conditions):
                return law.conclusion

        return None
