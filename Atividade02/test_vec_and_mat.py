import pytest
from vec2 import Vec2
from vec3 import Vec3
from vec4 import Vec4
from mat2 import Mat2
from mat3 import Mat3
from mat4 import Mat4

# Test vector addition for Vec2
def test_vec2_addition():
    v1 = Vec2(1, 2)
    v2 = Vec2(3, 4)
    result = v1 + v2
    assert result == Vec2(4, 6)

# Test vector addition for Vec3
def test_vec3_addition():
    v1 = Vec3(1, 2, 3)
    v2 = Vec3(4, 5, 6)
    result = v1 + v2
    assert result == Vec3(5, 7, 9)

# Test vector addition for Vec4
def test_vec4_addition():
    v1 = Vec4(1, 2, 3, 4)
    v2 = Vec4(5, 6, 7, 8)
    result = v1 + v2
    assert result == Vec4(6, 8, 10, 12)


def test_vec2_scalar_multiplication():
    v1 = Vec2(1, 2)
    scalar = 2
    result = v1 * scalar
    assert result == Vec2(2, 4)
    
def test_vec3_scalar_multiplication():
    v1 = Vec3(1, 2, 3)
    scalar = 2
    result = v1 * scalar
    assert result == Vec3(2, 4, 6)
    
def test_vec4_scalar_multiplication():
    v1 = Vec4(1, 2, 3, 4)
    scalar = 2
    result = v1 * scalar
    assert result == Vec4(2, 4, 6, 8)


# Test matrix multiplication for Mat2
def test_mat2_multiplication():
    m1 = Mat2(1, 2, 3, 4)
    m2 = Mat2(5, 6, 7, 8)
    result = m1.multiply(m2)
    assert result == Mat2(19, 22, 43, 50)

# Test matrix multiplication for Mat3
def test_mat3_multiplication():
    m1 = Mat3(1, 2, 3, 4, 5, 6, 7, 8, 9)
    m2 = Mat3(10, 11, 12, 13, 14, 15, 16, 17, 18)
    result = m1.multiply(m2)
    assert result == Mat3(84, 90, 96, 201, 216, 231, 318, 342, 366)

# Test matrix multiplication for Mat4
def test_mat4_multiplication():
    m1 = Mat4(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
    m2 = Mat4(17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32)
    result = m1.multiply(m2)
    expected_result = Mat4(
        250, 260, 270, 280,
        618, 644, 670, 696,
        986, 1028, 1070, 1112,
        1354, 1412, 1470, 1528
    )
    assert result == expected_result

if __name__ == '__main__':
    pytest.main()
