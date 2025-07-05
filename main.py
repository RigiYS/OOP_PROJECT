import tkinter as tk
from tkinter import messagebox
from datetime import date

from models.serve_training import ServeTraining
from models.passing_training import PassingTraining
from models.blocking_training import BlockingTraining
from models.spike_training import SpikeTraining
from models.training_log import TrainingLog
from data.data_manager import DataManager

# Mapping nama class untuk load data
CLASS_MAP = {
    "ServeTraining": ServeTraining,
    "PassingTraining": PassingTraining,
    "BlockingTraining": BlockingTraining,
    "SpikeTraining": SpikeTraining
}

class VolleyballApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🏐 Volleyball Training Tracker")
        self.root.geometry("450x500")
        self.root.configure(bg="#f0f9ff")

        self.today = str(date.today())
        self.log = TrainingLog()
        self.data_manager = DataManager()

        # Load data hari ini (jika ada)
        self.load_today_log()

        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.root, text="🏐 Volleyball Training Tracker", font=("Helvetica", 18, "bold"), bg="#f0f9ff", fg="#0d47a1").pack(pady=20)

        tk.Label(self.root, text="Jenis Latihan", bg="#f0f9ff").pack()
        self.training_var = tk.StringVar(value="Serve")
        tk.OptionMenu(self.root, self.training_var, "Serve", "Passing", "Blocking", "Spike").pack()

        tk.Label(self.root, text="Durasi (menit)", bg="#f0f9ff").pack(pady=(10, 0))
        self.duration_entry = tk.Entry(self.root)
        self.duration_entry.pack()

        tk.Label(self.root, text="Catatan (opsional)", bg="#f0f9ff").pack(pady=(10, 0))
        self.notes_entry = tk.Entry(self.root)
        self.notes_entry.pack()

        tk.Button(self.root, text="➕ Tambah Sesi", command=self.add_session, bg="#1565c0", fg="white").pack(pady=15)
        tk.Button(self.root, text="📆 Lihat Latihan Hari Ini", command=self.show_today_log, bg="#2e7d32", fg="white").pack(pady=5)
        tk.Button(self.root, text="🗂️ Lihat Semua Latihan", command=self.show_all_logs, bg="#6a1b9a", fg="white").pack(pady=5)

    def add_session(self):
        jenis = self.training_var.get()
        durasi = self.duration_entry.get()
        catatan = self.notes_entry.get()

        try:
            durasi = int(durasi)
        except ValueError:
            messagebox.showerror("Error", "Durasi harus berupa angka!")
            return

        # Buat objek latihan berdasarkan jenis
        if jenis == "Serve":
            session = ServeTraining(durasi, catatan)
        elif jenis == "Passing":
            session = PassingTraining(durasi, catatan)
        elif jenis == "Blocking":
            session = BlockingTraining(durasi, catatan)
        elif jenis == "Spike":
            session = SpikeTraining(durasi, catatan)
        else:
            messagebox.showerror("Error", "Jenis latihan tidak dikenal.")
            return

        self.log.add_session(session)
        self.data_manager.save(self.today, self.log.to_dict())

        self.duration_entry.delete(0, tk.END)
        self.notes_entry.delete(0, tk.END)
        messagebox.showinfo("Sukses", "Sesi latihan ditambahkan!")

    def show_today_log(self):
        entries = self.log.describe_all()
        if not entries:
            messagebox.showinfo("Log Hari Ini", "Belum ada latihan hari ini.")
            return

        msg = "\n".join(f"- {e}" for e in entries)
        messagebox.showinfo("Log Hari Ini", msg)

    def show_all_logs(self):
        all_data = self.data_manager.get_all()
        if not all_data:
            messagebox.showinfo("Log", "Belum ada data sama sekali.")
            return

        msg = ""
        for tanggal, session_list in all_data.items():
            msg += f"\n📅 {tanggal}:\n"
            for s in session_list:
                tipe = s['type']
                durasi = s['duration']
                notes = s.get('notes', '')
                msg += f"  - {tipe}: {durasi} menit. {notes}\n"

        messagebox.showinfo("Semua Log Latihan", msg)

    def load_today_log(self):
        today_data = self.data_manager.get_by_date(self.today)
        self.log.load_from_dict(today_data, CLASS_MAP)

if __name__ == "__main__":
    root = tk.Tk()
    app = VolleyballApp(root)
    root.mainloop()