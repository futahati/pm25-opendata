# 專案從遠端 git clone 下載，且無 .venv 環境參數

- 使用 VScode 透過 requirements.txt 重建 .venv（虛擬環境）

  1. 打開 `git clone` 下來的資料夾open folder
  2. `Ctrl + Shift + P`
  3. 輸入並選擇 `Python: Create Environment...`
  4. 選擇 Venv Creates a `.venv` virtual environment in the current workspace
  5. Python 版本，選推薦的即可
     - ❌Enter interpreter path...
     - ❌Use Python from `python.defaultInterpreterpath` setting C:\ProgramData\anaconda3\python.exe
     - ✔  **Python 3.11.9 ~\AppData\Local\Programs\Python|python311\python.exe**
  6. **如果偵測到有 requirements.txt，VScode會問要不要順便安裝，請勾選它**
     - 勾選 ✅requirements.txt
     - ok
     - 右下角有小視窗 Creating environment(Show logs): Installing packages...
     - The following environment is selected: ~\Desktop\django\mysql\pm25.py

  - 如何確認「啟動」
    1. VS Code 右下角，應該會顯示 (.venv): poetry 或 3.x.x ('.venv': venv) 之類的字樣
    2. 打開 VS Code 內建的終端機 (Ctrl + ~)，會發現路徑前面自動出現了 (.venv)
