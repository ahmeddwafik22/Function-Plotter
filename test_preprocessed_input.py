import pytest
import eval_system

@pytest.mark.parametrize("fun_x, expected_validation" ,[
    ("2","2"),
    ("2x","2*x"),
    ("2X","2*x"),
    ("2.x","2.0*x"),
    ("2,x","2.0*x"),
    ("2.5(x+2)","2.5*(x+2)"),
    ("2.+x","2.0+x"),
    ("2^x","2**x"),
    ("+2x","+2*x"),
    ("-2x","-2*x"),
    ("2x**2","2*x**2"),
    ("2x^2","2*x**2"),
    ("2x+++2","2*x+2"),
    ("2x---2","2*x-2"),
    ("x2","x*2"),
    ("(2+x)8","(2+x)*8"),
    ("[3x+3]2","(3*x+3)*2"),
    ("[3x*(2-1)]","(3*x*(2-1))"),
    ("{3x*(2-1)}","(3*x*(2-1))"),
    ("2x(4+8)","2*x*(4+8)"),
])

def test(fun_x, expected_validation):
    eval_sys=eval_system.eval_service()
    valid,s=eval_sys.preprocess_text(fun_x)
    assert s == expected_validation
