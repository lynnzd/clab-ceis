class CeStage:

    _label = ""
    _id = ""
    _x = 0
    _y = 0

    def __init__(self, id, label, x, y) -> None:
        self._id = id
        self._label = label
        self._x = x
        self._y = y

    def to_cyto_elem(self) -> dict:
        return frozenset({
            "data": {"id": self._id, "label": self._label},
            "position": {"x": self._x, "y": self._y},
            "locked": True
        })
