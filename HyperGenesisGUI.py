import tkinter as tk
from tkinter import ttk
import math
import random

class GenesisMassCalculator:
    def __init__(self, master):
        self.master = master
        master.title("⚛️ Zero to Universe: Exponential Mass Generation")
        master.geometry("700x750")
        
        self.input_labels = [
            "1. Zero-Point Fluctuation (ZPF):",
            "2. Dark Energy Density ($\Lambda$):",
            "3. Gravitational Constant (G):",
            "4. Light Speed Squared ($c^2$):",
            "5. Initial Time Dilation Factor:",
            "6. Dark Matter (WIMP) Ratio:",
            "7. Pressurized Frequencies (Sound):",
            "8. Contraped Forces Threshold:",
            "9. Quantum Creation Unknowns ($\hbar$ factor):",
            "10. Vortex/Rotation Intensity ($\omega$):"
        ]
        
        self.initial_values = [
            1.054e-34, # Conceptual value based on Planck/h-bar
            1.3e-52,   # Conceptual Small Lambda
            6.67e-11,
            8.98e16,
            1.0,
            5.0,
            400.0,
            0.5,
            0.001,
            2.0
        ]
        
        self.inputs = []
        self.setup_gui(master)

    def setup_gui(self, master):
        # Header Frame
        header_frame = ttk.Frame(master, padding="10")
        header_frame.pack(fill='x')
        ttk.Label(header_frame, text="Input 10 Corresponding Physics Equivalents:", font=('Arial', 12, 'bold')).pack(pady=5)
        
        # Input Grid
        input_frame = ttk.Frame(master, padding="10")
        input_frame.pack(padx=10, pady=5)
        
        for i, label_text in enumerate(self.input_labels):
            row = i // 2
            col = (i % 2) * 2
            
            ttk.Label(input_frame, text=label_text).grid(row=row, column=col, sticky='w', padx=5, pady=5)
            entry = ttk.Entry(input_frame, width=20)
            entry.insert(0, f"{self.initial_values[i]:.2e}") # Pre-populate with scientific notation
            entry.grid(row=row, column=col + 1, padx=5, pady=5)
            self.inputs.append(entry)

        # Calculation Button
        ttk.Button(master, text="GENERATE COMPUTATIONAL MASS", command=self.calculate_mass, style='TButton', padding=10).pack(pady=20)
        
        # Output Display (The Final Mass)
        output_frame = ttk.Frame(master, padding="10")
        output_frame.pack(fill='x', padx=10)
        ttk.Label(output_frame, text="Calculated Exponential Mass ($M_c$):", font=('Arial', 12)).pack(side='left')
        self.mass_output = ttk.Label(output_frame, text="---", foreground='purple', font=('Consolas', 16, 'bold'))
        self.mass_output.pack(side='right')

        # Explanation Log
        ttk.Label(master, text="Evolution and Universe Log:", font=('Arial', 10, 'bold')).pack(fill='x', padx=10, pady=(10, 0))
        self.log = tk.Text(master, height=15, width=80, bg='#f0f0f0', font=('Consolas', 10))
        self.log.pack(padx=10, pady=5)
        self.initial_log()
    
    def initial_log(self):
        """Sets the initial state and explanation."""
        self.log.insert(tk.END, "--- ABSOLUTE ZERO: START OF CALCULATION ---\n")
        self.log.insert(tk.END, "0 Mass, 0 Force, 0 Absolute.\n\n")
        self.log.insert(tk.END, "The equation models the transition from ZPF (Zero-Point Fluctuation) to macro-scale mass generation.\n")
        self.log.insert(tk.END, "Input parameters determine the 'Exponential Components of Gaining More Mass'.\n")
        self.log.insert(tk.END, "---------------------------------------------------\n")

    def calculate_mass(self):
        self.log.delete(1.0, tk.END) # Clear previous log
        self.initial_log()
        
        try:
            # 1. Gather all 10 inputs (C1 through C10)
            C = []
            for entry in self.inputs:
                C.append(float(entry.get()))
            
            C1, C2, C3, C4, C5, C6, C7, C8, C9, C10 = C
            
            # --- The Mathematical Make-up of the Universe (Conceptual) ---
            
            # Term 1: Initial symmetry break (ZPF / Dark Energy)
            term1 = C1 / C2
            self.log.insert(tk.END, f"Phase I: Symmetry Break (C1/C2) -> {term1:.4e}\n", 'bold')

            # Term 2: Spacetime Curvature/Relativity (G*c^2 / T-Dilation)
            term2 = math.sqrt((C3 * C4) / C5)
            self.log.insert(tk.END, f"Phase II: Spacetime Curvature (sqrt(C3*C4/C5)) -> {term2:.4e}\n")

            # Term 3: Dark Matter/Invisible Energy interaction (WIMP * Frequencies / Contraped Forces)
            term3 = (C6 * C7) / C8
            self.log.insert(tk.END, f"Phase III: Dark Matter Interaction (C6*C7/C8) -> {term3:.4e}\n")

            # Term 4 & 5: Quantum Seeds and Macro-structure (Quantum Unknowns + Rotation)
            term4_5 = C9 + C10
            self.log.insert(tk.END, f"Phase IV: Macro-Seeding (C9 + C10) -> {term4_5:.4e}\n")
            
            # Total Exponent (The Exponential Growth Factor)
            total_exponent = term1 + term2 + term3 + term4_5
            self.log.insert(tk.END, "---------------------------------------------------\n")
            self.log.insert(tk.END, f"TOTAL EXPONENTIAL GROWTH FACTOR (X): {total_exponent:+.6e}\n")
            
            # Final Mass Calculation (M_c = 1 * e^X)
            # The '1' represents the initial unity potential of Absolute Zero.
            computational_mass = 1.0 * math.exp(total_exponent)
            
            # --- Output Final Result ---
            self.mass_output.config(text=f"{computational_mass:+.8E}")
            self.log.insert(tk.END, "\n✨ RESULT: GENERATING FROM NOTHING TO MASS ✨\n", 'result')
            self.log.insert(tk.END, f"Computational Mass ($M_c$) = e^X = {computational_mass:+.8E}\n")
            
        except ValueError:
            self.mass_output.config(text="INPUT ERROR", foreground='red')
            self.log.insert(tk.END, "ERROR: Please enter valid numerical solutions for all 10 fields.\n", 'error')
        except ZeroDivisionError:
            self.mass_output.config(text="ZERO DIVISION ERROR", foreground='red')
            self.log.insert(tk.END, "ERROR: Division by Zero detected (C2, C5, or C8 is zero).\n", 'error')

if __name__ == "__main__":
    root = tk.Tk()
    
    # Custom styles for highlighting
    style = ttk.Style()
    style.configure('TButton', font=('Arial', 10, 'bold'), foreground='darkgreen')
    
    # Custom tags for the log window
    GenesisMassCalculator.log_tags = {
        'bold': {'font': ('Consolas', 10, 'bold')},
        'result': {'font': ('Consolas', 10, 'bold'), 'foreground': 'blue'},
        'error': {'foreground': 'red'}
    }
    
    app = GenesisMassCalculator(root)
    root.mainloop()
