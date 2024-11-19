import numpy as np
import matplotlib.pyplot as plt

# 함수와 도함수 정의
def f(x):
    return x**3 - 3*x**2 + 2

def f_prime(x):
    return 3*x**2 - 6*x

# 뉴턴랩슨법 함수 정의
def newton_method(x0, tol=1e-6, max_iter=100):
    x_vals = [x0]  # x 값들을 저장할 리스트
    for i in range(max_iter):
        # 접선의 기울기
        slope = f_prime(x_vals[-1])
        
        # 접선의 x절편 구하기
        x_next = x_vals[-1] - f(x_vals[-1]) / slope
        x_vals.append(x_next)
        
        # 근에 충분히 가까워지면 종료
        if abs(f(x_next)) < tol:
            break
    return x_vals

# 초기 추정값
x0 = 5

# 뉴턴-랩슨법 실행
x_vals = newton_method(x0)

x = np.linspace(-10, 10, 1000)
y = f(x)

# 함수의 그래프 그리기
plt.plot(x, y, label=r'$f(x) = x^3 - 3x^2 + 2$', color='blue')

# 접선을 점선으로 그리기
for i in range(1, len(x_vals)):
    x_current = x_vals[i-1]
    y_current = f(x_current)
    slope = f_prime(x_current)
    
    # 접선의 방정식
    x_tangent = np.linspace(x_current - 3, x_current + 3, 10)
    y_tangent = slope * (x_tangent - x_current) + y_current
    
    # 점선으로 접선 그리기
    plt.plot(x_tangent, y_tangent, 'r--', alpha=0.6)

# x,y축
plt.axhline(0, color='black',linewidth=1)
plt.axvline(0, color='black',linewidth=1)

plt.xlim(2,6)
plt.ylim(-5,70)
plt.scatter(x_vals, f(np.array(x_vals)), color='red', zorder=5)

final_x = x_vals[-1]
plt.text(final_x, f(final_x) + 3, f'{final_x:.2f}', color='red', fontsize=12, ha='left')

plt.title('Newton-Raphson Method')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
