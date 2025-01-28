from types import ModuleType

import cloudcoil.models.istio as istio


def test_has_modules():
    modules = list(filter(lambda x: isinstance(x, ModuleType), istio.__dict__.values()))
    assert modules, "No modules found in istio"
