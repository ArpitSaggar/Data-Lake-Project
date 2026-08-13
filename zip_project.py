import os
import zipfile

project_dir = r'c:\Users\LENOVO\DataLakeProject'
desktop_dir = r'c:\Users\LENOVO\OneDrive\Desktop'
zip_path = os.path.join(desktop_dir, 'DataLakeProject.zip')

# Write requirements.txt first
reqs = ['streamlit', 'babel', 'duckdb', 'pandas', 'plotly', 'pyspark', 'faker', 'kafka-python']
with open(os.path.join(project_dir, 'requirements.txt'), 'w') as f:
    f.write('\n'.join(reqs))

# Write run_dashboard.bat
bat_content = "@echo off\r\n"
bat_content += "echo =======================================\r\n"
bat_content += "echo Enterprise Clickstream Analytics Setup\r\n"
bat_content += "echo =======================================\r\n"
bat_content += "if not exist venv (\r\n"
bat_content += "    echo Creating virtual environment...\r\n"
bat_content += "    python -m venv venv\r\n"
bat_content += "    echo Installing dependencies...\r\n"
bat_content += "    venv\\Scripts\\python -m pip install --upgrade pip\r\n"
bat_content += "    venv\\Scripts\\pip install -r requirements.txt\r\n"
bat_content += ")\r\n"
bat_content += "echo Starting Dashboard...\r\n"
bat_content += "cd dashboard\r\n"
bat_content += "..\\venv\\Scripts\\streamlit run app.py\r\n"
bat_content += "pause\r\n"

with open(os.path.join(project_dir, 'run_dashboard.bat'), 'w') as f:
    f.write(bat_content)

# Folders and extensions to skip
skip_dirs = {'venv', '__pycache__', '.git', '.gemini'}

print('Creating ZIP file...')

with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(project_dir):
        # Remove skip dirs in-place so os.walk won't descend into them
        dirs[:] = [d for d in dirs if d not in skip_dirs]

        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.join('DataLakeProject', os.path.relpath(file_path, project_dir))
            zipf.write(file_path, arcname)

print(f'Done! ZIP saved to: {zip_path}')
