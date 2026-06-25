import tkinter as tk
from tkinter import messagebox

BG = "#0F172A"
CARD = "#1E293B"
BLUE = "#2563EB"
GREEN = "#10B981"
RED = "#EF4444"
YELLOW = "#F59E0B"
TEXT = "#F8FAFC"
GRAY = "#94A3B8"

class EcoRouteAI:

    def __init__(self, root):
        self.root = root
        self.root.title("EcoRoute Logistic AI")
        self.root.geometry("1280x720")
        self.root.configure(bg=BG)

        self.estado = "En tránsito"
        self.ubicacion = "Santiago"
        self.clima = "Normal"

        self.conductores = [
            {"nombre": "Johaquin Fernandez", "disponible": True},
            {"nombre": "Goku Fernanfloo", "disponible": True}
        ]

        self.menu()


    def limpiar(self):
        for w in self.root.winfo_children():
            w.destroy()

    def titulo(self, texto):
        tk.Label(
            self.root,
            text=texto,
            bg=BG,
            fg=TEXT,
            font=("Segoe UI", 22, "bold")
        ).pack(pady=20)

    def boton(self, texto, color, comando):
        tk.Button(
            self.root,
            text=texto,
            bg=color,
            fg="white",
            width=25,
            height=2,
            relief="flat",
            font=("Segoe UI", 11, "bold"),
            command=comando
        ).pack(pady=8)

    def tarjeta(self, padre, titulo, valor):
        frame = tk.Frame(
            padre,
            bg=CARD,
            width=180,
            height=120
        )
        frame.pack_propagate(False)

        tk.Label(
            frame,
            text=titulo,
            bg=CARD,
            fg=GRAY,
            font=("Segoe UI", 10)
        ).pack(pady=10)

        tk.Label(
            frame,
            text=valor,
            bg=CARD,
            fg=TEXT,
            font=("Segoe UI", 15, "bold")
        ).pack()

        return frame

    def menu(self):
        self.limpiar()

        self.titulo("🚚 EcoRoute Logistic AI")

        tk.Label(
            self.root,
            text="Sistema Inteligente para la Ruta Austral",
            bg=BG,
            fg=GRAY,
            font=("Segoe UI", 11)
        ).pack()

        tk.Frame(self.root, bg=BG, height=40).pack()

        self.boton(
            "📦 Portal Cliente",
            BLUE,
            self.portal_cliente
        )

        self.boton(
            "🚛 App Conductor",
            GREEN,
            self.app_conductor
        )

        self.boton(
            "⚙️ Dashboard Administrador",
            "#0EA5E9",
            self.login_admin
        )

        tk.Label(
            self.root,
            text="ISO/IEC 25010 • Arquitectura 4+1 • EcoRoute AI v1.0",
            bg=BG,
            fg=GRAY
        ).pack(side="bottom", pady=20)

    def portal_cliente(self):
        self.limpiar()

        self.titulo("📦 Portal Cliente")

        card = tk.Frame(
            self.root,
            bg=CARD,
            padx=30,
            pady=30
        )
        card.pack(pady=20)

        tk.Label(
            card,
            text="Guía: TSA-2026-001",
            bg=CARD,
            fg=TEXT,
            font=("Segoe UI", 12)
        ).pack(pady=10)

        tk.Label(
            card,
            text=f"Estado: {self.estado}",
            bg=CARD,
            fg=GREEN,
            font=("Segoe UI", 15, "bold")
        ).pack()

        tk.Label(
            card,
            text=f"Ubicación: {self.ubicacion}",
            bg=CARD,
            fg=TEXT
        ).pack(pady=5)

        tk.Label(
            card,
            text=f"Clima: {self.clima}",
            bg=CARD,
            fg=TEXT
        ).pack()

        self.boton("⬅ Volver", "#475569", self.menu)

    # =========================
    # LOGIN ADMIN
    # =========================

    def login_admin(self):
        self.limpiar()

        self.titulo("🔐 Acceso Seguro 2FA")

        tk.Label(
            self.root,
            text="Código de verificación",
            bg=BG,
            fg=TEXT
        ).pack()

        codigo = tk.Entry(
            self.root,
            justify="center",
            font=("Segoe UI", 14)
        )
        codigo.pack(pady=20)

        def validar():
            if codigo.get() == "1234":
                self.dashboard_admin()
            else:
                messagebox.showerror(
                    "Acceso Denegado",
                    "Código 2FA incorrecto."
                )

        self.boton("Ingresar", BLUE, validar)
        self.boton("Cancelar", "#475569", self.menu)

    # =========================
    # DASHBOARD ADMIN
    # =========================

    def dashboard_admin(self):
        self.limpiar()

        self.titulo("⚙️ Dashboard Administrativo")

        fila = tk.Frame(self.root, bg=BG)
        fila.pack(pady=20)

        self.tarjeta(
            fila,
            "📦 Estado",
            self.estado
        ).grid(row=0, column=0, padx=10)

        self.tarjeta(
            fila,
            "📍 Ubicación",
            self.ubicacion
        ).grid(row=0, column=1, padx=10)

        self.tarjeta(
            fila,
            "🌨️ Clima",
            self.clima
        ).grid(row=0, column=2, padx=10)

        self.tarjeta(
            fila,
            "🚚 Conductores",
            str(len(self.conductores))
        ).grid(row=0, column=3, padx=10)

        # MAPA SIMULADO
        mapa = tk.Frame(
            self.root,
            bg=CARD,
            padx=30,
            pady=20
        )
        mapa.pack(pady=20)

        tk.Label(
            mapa,
            text="🗺️ GPS EN TIEMPO REAL",
            bg=CARD,
            fg=TEXT,
            font=("Segoe UI", 12, "bold")
        ).pack()

        tk.Label(
            mapa,
            text="Santiago -------- Balmaceda -------- Punta Arenas",
            bg=CARD,
            fg=GRAY
        ).pack(pady=5)

        tk.Label(
            mapa,
            text=f"🚚 Camión ubicado en: {self.ubicacion}",
            bg=CARD,
            fg=TEXT,
            font=("Segoe UI", 11)
        ).pack()

        botones = tk.Frame(self.root, bg=BG)
        botones.pack(pady=10)

        tk.Button(
            botones,
            text="Asignar Carga",
            bg=BLUE,
            fg="white",
            width=20,
            command=self.asignar_carga
        ).grid(row=0, column=0, padx=10)

        tk.Button(
            botones,
            text="Calcular Viáticos",
            bg=YELLOW,
            fg="white",
            width=20,
            command=self.calcular_viaticos
        ).grid(row=0, column=1, padx=10)

        tk.Button(
            botones,
            text="Emitir Alerta",
            bg=RED,
            fg="white",
            width=20,
            command=self.alerta_climatica
        ).grid(row=0, column=2, padx=10)

        self.boton("⬅ Volver", "#475569", self.menu)

    # =========================
    # FUNCIONALIDADES
    # =========================

    def asignar_carga(self):
        for c in self.conductores:
            if c["disponible"]:
                c["disponible"] = False

                messagebox.showinfo(
                    "Asignación",
                    f"Carga asignada a:\n{c['nombre']}"
                )
                return

        messagebox.showwarning(
            "Sistema",
            "No hay conductores disponibles."
        )

    def calcular_viaticos(self):
        messagebox.showinfo(
            "Viáticos",
            "Combustible: $845.000\n"
            "Peajes: $72.000\n\n"
            "Total: $917.000"
        )

    def alerta_climatica(self):
        self.clima = "Nieve en Ruta"

        messagebox.showwarning(
            "Alerta Climática",
            "Se detectó nieve extrema."
        )

        self.dashboard_admin()


    def app_conductor(self):
        self.limpiar()

        self.titulo("🚛 App del Conductor")

        if self.clima != "Normal":
            tk.Label(
                self.root,
                text="⚠️ ALERTA DE NIEVE ACTIVA",
                bg=RED,
                fg="white",
                width=40,
                height=2
            ).pack(pady=15)

        tk.Button(
            self.root,
            text="🛃 REGISTRAR ADUANA",
            bg=YELLOW,
            fg="white",
            width=30,
            height=3,
            font=("Segoe UI", 12, "bold"),
            command=self.registrar_aduana
        ).pack(pady=20)

        tk.Button(
            self.root,
            text="✅ CONFIRMAR ENTREGA",
            bg=GREEN,
            fg="white",
            width=30,
            height=3,
            font=("Segoe UI", 12, "bold"),
            command=self.confirmar_entrega
        ).pack(pady=20)

        self.boton("⬅ Volver", "#475569", self.menu)

    def registrar_aduana(self):
        self.estado = "En aduana"
        self.ubicacion = "Balmaceda"

        messagebox.showinfo(
            "Actualización",
            "Carga registrada en Aduana."
        )

    def confirmar_entrega(self):
        self.estado = "Entregado"
        self.ubicacion = "Punta Arenas"

        messagebox.showinfo(
            "Actualización",
            "Entrega confirmada."
        )

root = tk.Tk()
app = EcoRouteAI(root)
root.mainloop()