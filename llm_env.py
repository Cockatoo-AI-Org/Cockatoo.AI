import subprocess
import sys

def create_virtual_environment(name):
    # Step 1: 創建虛擬環境
    subprocess.run([sys.executable, "-m", "venv", name])

    # Step 2: 啟動虛擬環境
    activate_script = "Scripts\\activate" if sys.platform == "win32" else "bin/activate"
    activate_path = f"{name}/{activate_script}"
    subprocess.run([activate_path], shell=True)

    # Step 3: 安裝必要的套件
    subprocess.run(["pip", "install", "Flask"])

    # Step 4: 安装 Transformers 
    subprocess.run(["pip", "install", "transformers"])

    print(f"虛擬環境 {name} 創建成功！")

if __name__ == "__main__":
    venv_name = "llm"
    create_virtual_environment(venv_name)
