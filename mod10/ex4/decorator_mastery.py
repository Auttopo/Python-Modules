
from typing import Callable, Any
import functools
import time
import os
import sys
import inspect
parentdir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(parentdir)


def check_signature(
        func: Callable[..., Any], *args: Any, **kwargs: Any
) -> None:
    try:
        inspect.signature(func).bind(*args, **kwargs)
    except TypeError as e:
        raise TypeError(e) from None


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    @functools.wraps(func)
    def mcdo_wrap_chicken(*args: Any, **kwargs: Any) -> Any:
        print("FUNC START | Casting", func.__name__)
        start = time.time()
        res = func(*args, **kwargs)
        print(end="FUNC END |")
        print("time execution:", time.time() - start)
        return res
    return mcdo_wrap_chicken


def power_validator(min_power: int) -> Callable[..., Any]:
    def power_checker(func: Callable[..., Any]) -> Any:
        @functools.wraps(func)
        def mcdo_wrap_chicken(*args: Any, **kwargs: Any) -> Any:
            check_signature(func, *args, **kwargs)
            first, *others = args
            try:
                if not first >= min_power:
                    return "Insufficient power for this spell"
            except Exception:
                if not others[1] >= min_power:
                    return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return mcdo_wrap_chicken
    return power_checker


def retry_spell(max_attempts: int) -> Callable[..., Any]:
    def retry_sequence(func: Callable[..., Any]) -> Any:
        @functools.wraps(func)
        def mcdo_wrap_chicken(*args: Any, **kwargs: Any) -> Any:
            check_signature(func, *args, **kwargs)
            res = None
            check = 0
            i = 0
            while check == 0 and i < max_attempts:
                try:
                    res = func()
                    check = 1
                except Exception:
                    print(
                        f"Spell failed, retrying... "
                        f"(attempt {i + 1}/{max_attempts})")
                i += 1
            return res
        return mcdo_wrap_chicken
    return retry_sequence


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) >= 3 and all(c.isalpha() or c.isspace() for c in name):
            return True
        return False

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@power_validator(150)
def attack(powa: int) -> int:
    return powa


@retry_spell(5)
def traitor() -> float | int:
    return 1 / 0


if __name__ == "__main__":
    print("\nspell_timer :")
    from ex1.higher_magic import heal
    pretty_heal = spell_timer(heal)
    print(pretty_heal())

    print("\npower_validator :")
    print(attack(120))
    print(attack(160))

    print("\nretry_spell :")
    print(traitor())

    print("\nMageGuild.validate_mage_name :")
    print(MageGuild.validate_mage_name("Agazr le mOdit"))

    print("\nMageGuild.cast_spell :")
    obj = MageGuild()
    print(obj.cast_spell("pls let me out", 8))
    print(obj.cast_spell("pleasssssse, let me free from pyt modules", 11))
