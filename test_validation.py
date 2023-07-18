import pytest
import eval_system

@pytest.mark.parametrize("fun_x, expected_validation" ,[
    ("2",True),
    ("2x",True),
    ("2X",True),
    ("",False),
    ("   ",False),
    ("2.x",True),
    ("2,x",True),
    ("2.5(x+2)",True),
    ("2.5(x+2).",False),
    ("2.5(x+2)#",False),
    ("2.5!(x+2)",False),
    ("2.+x",True),
    ("+2x",True),
    ("-2x",True),
    ("*2x",False),
    ("/2x",False),
    ("2x//2",False),
    ("2x**2",True),
    ("2x^2",True),
    ("2x***2",False),
    ("2x+++2",True),
    ("2x---2",True),
    ("2x++*2",False),
    ("2x^^2",False),
    ("+",False),
    ("2y",False),
    ("x2",True),
    ("(2+x)8",True),
    ("(2x+8",False),
    ("{2+x)8",False),
    ("[3x+3]2",True),
    ("[3x*(2-1)]",True),
    ("2x(4+8)",True),
    ("()",False),
    ("{}",False),
    ("2x(2+)",False),

])


def test(fun_x, expected_validation):
    eval_sys=eval_system.eval_service()
    valid,s=eval_sys.preprocess_text(fun_x)
    assert valid == expected_validation

