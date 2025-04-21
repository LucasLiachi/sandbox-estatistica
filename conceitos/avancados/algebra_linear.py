import numpy as np

class LinearAlgebra:
    def __init__(self):
        pass

    def linear_regression(self, X, y):
        """
        Calcula regressão linear usando álgebra matricial
        X: matriz de design (com coluna de 1s para o intercepto)
        y: vetor de respostas
        """
        # Calcular X transposta
        X_t = X.T
        
        # Calcular (X'X)^-1
        X_t_X_inv = np.linalg.inv(X_t @ X)
        
        # Calcular os coeficientes β = (X'X)^-1X'y
        beta = X_t_X_inv @ X_t @ y
        
        # Calcular y estimado
        y_est = X @ beta
        
        # Calcular R²
        SS_tot = np.sum((y - np.mean(y)) ** 2)
        SS_res = np.sum((y - y_est) ** 2)
        R2 = 1 - (SS_res / SS_tot)
        
        return {
            'coefficients': beta,
            'r_squared': R2,
            'y_predicted': y_est
        }

    def calculate_work(self, forces, angles, displacement):
        """
        Calcula o trabalho total realizado por forças em um sistema
        forces: lista com as magnitudes das forças [F1, F2, F3, F4, F5, F6]
        angles: lista com os ângulos em graus [θ1, θ2, θ3, θ4, θ5, θ6]
        displacement: deslocamento em metros
        """
        # Converter ângulos para radianos
        angles_rad = np.deg2rad(angles)
        
        # Calcular componentes x e y das forças
        Fx = np.sum([
            forces[0] * np.cos(angles_rad[0]),  # F1
            forces[1] * np.cos(angles_rad[1]),  # F2
            forces[2] * np.cos(angles_rad[2]),  # F3
            forces[3] * np.cos(angles_rad[3]),  # F4
            forces[4] * np.cos(angles_rad[4]),  # F5
            forces[5] * np.cos(angles_rad[5])   # F6
        ])
        
        Fy = np.sum([
            forces[0] * np.sin(angles_rad[0]),  # F1
            forces[1] * np.sin(angles_rad[1]),  # F2
            forces[2] * np.sin(angles_rad[2]),  # F3
            forces[3] * np.sin(angles_rad[3]),  # F4
            forces[4] * np.sin(angles_rad[4]),  # F5
            forces[5] * np.sin(angles_rad[5])   # F6
        ])
        
        # Calcular força resultante
        F_resultant = np.sqrt(Fx**2 + Fy**2)
        
        # Calcular ângulo resultante
        angle_resultant = np.arctan2(Fy, Fx)
        
        # Calcular trabalho
        work = F_resultant * displacement * np.cos(angle_resultant)
        
        return {
            'force_resultant': F_resultant,
            'angle_resultant_deg': np.rad2deg(angle_resultant),
            'work': work
        }

# Exemplo de uso - Regressão Linear
if __name__ == "__main__":
    algebra = LinearAlgebra()
    
    # Exemplo 1: Regressão Linear
    print("Exemplo 1: Regressão Linear")
    X = np.array([[1, 1], [1, 2], [1, 3], [1, 4]])
    y = np.array([2, 3, 4, 5])
    
    results = algebra.linear_regression(X, y)
    print(f"Coeficientes (β0, β1): {results['coefficients']}")
    print(f"R²: {results['r_squared']}")
    
    # Exemplo 2: Cálculo do Trabalho
    print("\nExemplo 2: Cálculo do Trabalho")
    forces = [20, 20, 30, 5, 10, 15]  # F1 a F6
    angles = [0, 30, 90, 150, 180, 270]  # ângulos em graus
    displacement = 10  # metros
    
    results = algebra.calculate_work(forces, angles, displacement)
    print(f"Força Resultante: {results['force_resultant']:.2f} N")
    print(f"Ângulo Resultante: {results['angle_resultant_deg']:.2f}°")
    print(f"Trabalho Total: {results['work']:.2f} J")