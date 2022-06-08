from dataclasses import dataclass

@dataclass
class ColorParameter:
    img: bytes
    h_min: int
    h_max: int
    s_min: int
    v_min: int
    h_red_min: int
    h_red_max: int
    check_red: bool
    