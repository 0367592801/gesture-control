from detector import HandDetector

d = HandDetector()
cases = [
    ([False, True,  True,  False, False], "peace"),
    ([True,  True,  True,  False, False], "peace"),     # thumb up still V
    ([False, True,  False, False, False], "point_up"),
    ([True,  True,  False, False, False], "point_up"),  # thumb up still point
    ([True,  False, False, False, False], "thumb_up"),
    ([False, False, False, False, False], "fist"),
    ([True,  True,  True,  True,  True],  "open"),
    ([False, False, True,  False, False], "middle_up"),
    ([False, True,  True,  True,  False], "three_up"),
    ([False, False, False, False, True],  "pinky_up"),
    ([True,  False, False, False, True],  "shaka"),
]
all_ok = True
for fingers, expected in cases:
    got = d._classify(fingers)
    ok = got == expected
    print(f"{'OK' if ok else 'FAIL'} {expected:12} got={got}")
    if not ok:
        all_ok = False
print("ALL OK" if all_ok else "SOME FAILED")
