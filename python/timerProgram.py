import tkinter as tk
from tkinter import messagebox
from playsound import playsound
import threading

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("타이머 프로그램")

        # 타이머 변수
        self.running = False
        self.time_left = 0

        # UI 구성
        self.label = tk.Label(root, text="타이머 설정 (분:초)", font=("Helvetica", 14))
        self.label.pack(pady=10)

        self.time_entry = tk.Entry(root, width=10, font=("Helvetica", 14), justify="center")
        self.time_entry.insert(0, "00:00")
        self.time_entry.pack(pady=5)

        self.start_button = tk.Button(root, text="시작", command=self.start_timer, font=("Helvetica", 12))
        self.start_button.pack(side="left", padx=10, pady=10)

        self.stop_button = tk.Button(root, text="중지", command=self.stop_timer, font=("Helvetica", 12))
        self.stop_button.pack(side="left", padx=10, pady=10)

        self.reset_button = tk.Button(root, text="초기화", command=self.reset_timer, font=("Helvetica", 12))
        self.reset_button.pack(side="left", padx=10, pady=10)

        self.timer_label = tk.Label(root, text="00:00", font=("Helvetica", 36))
        self.timer_label.pack(pady=20)

    def start_timer(self):
        if not self.running:
            try:
                mins, secs = map(int, self.time_entry.get().split(":"))
                self.time_left = mins * 60 + secs
                if self.time_left <= 0:
                    raise ValueError
            except ValueError:
                messagebox.showerror("입력 오류", "올바른 형식으로 시간을 입력하세요 (예: 02:30)")
                return

            self.running = True
            self.update_timer()

    def stop_timer(self):
        self.running = False

    def reset_timer(self):
        self.running = False
        self.time_left = 0
        self.timer_label.config(text="00:00")
        self.time_entry.delete(0, tk.END)
        self.time_entry.insert(0, "00:00")

    def update_timer(self):
        if self.running and self.time_left > 0:
            mins, secs = divmod(self.time_left, 60)
            self.timer_label.config(text=f"{mins:02}:{secs:02}")
            self.time_left -= 1
            self.root.after(1000, self.update_timer)
        elif self.time_left == 0 and self.running:
            self.running = False
            self.timer_label.config(text="00:00")
            threading.Thread(target=self.play_alarm_sound).start()  # 소리 재생
            messagebox.showinfo("알림", "타이머가 종료되었습니다!")

    def play_alarm_sound(self):
        try:
            playsound("alarm.mp3")  # 알람 소리 파일 재생
        except Exception as e:
            print(f"소리 재생 오류: {e}")

# 실행
if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()
